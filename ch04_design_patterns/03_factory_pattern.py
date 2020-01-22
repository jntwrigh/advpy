"""
    03_factory_pattern -
    Defines concrete classes made from an abstract base,
    but all overriding the get_output method from the base
"""
import abc


class Message(abc.ABC):
    def __init__(self, msg=''):
        self.msg = msg

    @abc.abstractmethod
    def get_output(self):
        pass


class Text(Message):
    def __init__(self, msg):
        super().__init__(msg)

    def get_output(self):
        return self.msg


class Html(Message):
    def __init__(self, msg):
        super().__init__(msg)

    def get_output(self):
        return f'<span>{self.msg}</span>'


class Json(Message):
    def __init__(self, msg):
        super().__init__(msg)

    def get_output(self):
        return f'{{ "msg": "{self.msg}" }}'


class MessageFactory:
    message_formats = {'text': Text, 'html': Html, 'json': Json}

    @classmethod
    def create_msg(cls, msg_type, msg):
        return cls.message_formats[msg_type](msg)


msgs = {'html': 'Sample HTML msg.', 'json': 'This message is JSON-Based.', 'text': 'A simple text msg.'}
for typ, message in msgs.items():
    print(MessageFactory.create_msg(typ, message).get_output())
