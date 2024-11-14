# dtos.py
from .entities import Message
from .models import MessageModel

class MessageDTO:
    def __init__(self, content: str, user_id: int):
        self.content = content
        self.user_id = user_id

    @classmethod
    def from_entity(cls, message: Message):
        return cls(content=message.content, user_id=message.user_id)

    def to_entity(self) -> Message:
        return Message(content=self.content, user_id=self.user_id)

    @classmethod
    def from_model(cls, message_model: MessageModel):
        return cls(content=message_model.content, user_id=message_model.user.id)

    def to_model(self) -> MessageModel:
        return MessageModel(content=self.content, user_id=self.user_id)