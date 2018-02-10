import logging
import socket
class Debug(object):        
    def __init__(self, logName, logFile, level = logging.INFO):
        self.hostname = socket.gethostname()
        self._logger = logging.getLogger(self.hostname + ' '+ logName)
        handler = logging.FileHandler(logFile)
        formatter = logging.Formatter('%(asctime)s %(name)-s %(levelname)s:  %(message)s')
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)
        self._logger.setLevel(level)
        
    def debug(self, msg):
        if self._logger is not None:
            self._logger.debug(msg)

    def info(self, msg):
        if self._logger is not None:
            self._logger.info(msg)

    def warning(self, msg):
        if self._logger is not None:
            self._logger.warning(msg)