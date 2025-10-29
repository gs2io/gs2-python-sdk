# encoding: utf-8
#
# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

from __future__ import annotations

import os
import sys
import threading
from typing import Any, Optional, Callable


class timeout:
    def __init__(
            self,
            seconds: int = 1,
            error_message: str = 'Timeout'
    ):
        self.seconds = int(seconds)
        self.error_message = error_message

        self._use_signal = False

        self._timer: Optional[threading.Timer] = None
        self._timed_out = False
        self._prev_trace: Optional[Callable] = None

    def _raise_timeout(self, *_: Any) -> None:
        from multiprocessing import TimeoutError
        raise TimeoutError(self.error_message)
    def handle_timeout(self, _: Any, __: Any):
        from multiprocessing import TimeoutError
        raise TimeoutError(self.error_message)

    def _tracer(self, frame, event, arg):
        if self._timed_out:
            from multiprocessing import TimeoutError
            raise TimeoutError(self.error_message)
        return self._tracer

    def __enter__(self) -> None:
        try:
            import signal
            if hasattr(signal, "SIGALRM") and os.name != "nt" and threading.current_thread() is threading.main_thread():
                self._use_signal = True
                signal.signal(signal.SIGALRM, self._raise_timeout)
                signal.alarm(self.seconds)
                return
        except Exception:
            self._use_signal = False

        self._use_signal = False
        self._timed_out = False
        self._prev_trace = sys.gettrace()
        sys.settrace(self._tracer)
        self._timer = threading.Timer(self.seconds, self._set_timed_out)
        self._timer.daemon = True
        self._timer.start()

    def _set_timed_out(self) -> None:
        self._timed_out = True

    def __exit__(self, _type, value, traceback) -> None:
        if self._use_signal:
            import signal
            try:
                signal.alarm(0)
            finally:
                self._use_signal = False
            return

        try:
            if self._timer is not None:
                self._timer.cancel()
        finally:
            self._timer = None
            self._timed_out = False
            sys.settrace(self._prev_trace)
            self._prev_trace = None
