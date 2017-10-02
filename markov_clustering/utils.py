"""
Simple togglable printer class
"""


class MessagePrinter(object):
    def __init__(self, enabled):
        self._enabled = enabled

    def enable(self):
        self._enabled = True

    def disable(self):
        self._enabled = False

    def print(self, string):
        if self._enabled:
            print(string)
