import abc


# Python 3.4+
class AbstractBase1(abc.ABC):

    def __init__(self, item):
        self.item = item
        self.do_action()

    @abc.abstractmethod
    def do_action(self):                # subclass will define this work
        pass


# Python 3.0 - 3.3
class AbstractBase2(metaclass=abc.ABCMeta):

    def __init__(self, item):
        self.item = item
        self.do_action()

    @abc.abstractmethod
    def do_action(self):
        pass


# Python 2
class AbstractBase3:
    __metaclass__ = abc.ABCMeta

    def __init__(self, item):
        self.item = item
        self.do_action()

    @abc.abstractmethod
    def do_action(self):
        pass


class TextMessage(abc.ABC):
    def __init__(self, msg):
        self.msg = msg

    @abc.abstractmethod
    def get_text(self):
        pass


class JsonMessage(TextMessage):
    def __init__(self, msg):
        super().__init__(msg)

    def get_text(self):
        return f'{{ "text": "{self.msg}" }}'


class HtmlMessage(TextMessage):
    def __init__(self, msg):
        super().__init__(msg)

    def get_text(self):
        return f'<span>{self.msg}</span>'


msg1 = HtmlMessage('Your meeting is at 3pm.')
msg2 = JsonMessage('Your meeting is at 3pm.')
print(msg1.get_text())
print(msg2.get_text())
msg3 = TextMessage('Meeting cancelled.')       # generates an error
