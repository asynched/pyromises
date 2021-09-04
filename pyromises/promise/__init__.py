from typing import Callable
from threading import Thread as _Thread
from concurrent.futures import ThreadPoolExecutor as _ThreadPoolExecutor


class Promise:
    """Base promise class"""

    def __init__(self, callback: Callable, *args, **kwargs):
        # Main callback
        self.callback = callback
        self.args = args
        self.kwargs = kwargs

        # Promise result
        self.result = None

        # Promise handlers (.then and .catch)
        self.success_handler = None
        self.error_handler = None

        self._start_process()

    def then(self, callback: Callable):
        """Register a callback to run in the case the promise is fullfilled

        Args:
            callback (Callable): Callback to run after the promise is fullfilled
        """
        self.success_handler = callback

    def catch(self, callback: Callable):
        """Registers a callback to handle in the promise is rejected

        Args:
            callback (Callable): Callback to run after the promise is rejected
        """
        self.error_handler = callback

    def _start_process(self):
        """Starts the thread"""
        process = _Thread(target=self._execute)
        process.start()

    def _execute(self):
        """Executes the callback with the thread pool executor and passes the result (or error) to it's handler"""

        with _ThreadPoolExecutor() as executor:
            try:
                future = executor.submit(self.callback, *self.args, **self.kwargs)

                if self.success_handler:
                    self.success_handler(future.result())
            except Exception as exception:
                if self.error_handler:
                    self.error_handler(exception)
