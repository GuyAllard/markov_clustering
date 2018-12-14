import pytest
from markov_clustering.utils import MessagePrinter


def test_message_printer_enabled(capfd):
    mp = MessagePrinter(enabled=True)
    msg = "hello universe"
    mp.print(msg)
    out, err = capfd.readouterr()
    assert out == msg + "\n"


def test_message_printer_disabled(capfd):
    mp = MessagePrinter(enabled=False)
    msg = "hello universe"
    mp.print(msg)
    out, err = capfd.readouterr()
    assert out == ""


def test_message_printer_enable(capfd):
    mp = MessagePrinter(enabled=False)
    msg = "hello universe"
    mp.enable()
    mp.print(msg)
    out, err = capfd.readouterr()
    assert out == msg + "\n"


def test_message_printer_disable(capfd):
    mp = MessagePrinter(enabled=True)
    msg = "hello universe"
    mp.disable()
    mp.print(msg)
    out, err = capfd.readouterr()
    assert out == ""
