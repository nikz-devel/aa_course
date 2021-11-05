import json
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, Protocol

from django.conf import settings
from kafka import KafkaProducer

from .models import User


class EventTransport(Protocol):
    def send(self,  data: bytes, topic: str):
        pass


class KafkaEventTransport:
    def __init__(self, producer: KafkaProducer):
        self.producer = producer

    def send(self, data: bytes, topic: str):
        self.producer.send(topic, data)


producer = KafkaProducer(bootstrap_servers=settings.KAFKA_SERVER)
default_transport = KafkaEventTransport(producer)


class Event(ABC):
    topic: str = "default"
    event_type: Optional[str] = None

    def __init__(self, transport: EventTransport = default_transport) -> None:
        self.transport = transport

    @abstractmethod
    def make_event_data(self) -> Dict[str, Any]:
        pass

    def send(self) -> None:
        if not self.event_type:
            raise RuntimeError()

        data = self.make_event_data()
        data.update({"event_type": self.event_type})
        raw_data = json.dumps(data).encode(encoding="utf-8")
        self.transport.send(raw_data, self.topic)


class UserCreatedEvent(Event):
    topic = "user_stream"
    event_type = "user.created"

    def __init__(self, user: User, *args, **kwargs) -> None:
        self.user = user
        super().__init__(*args, **kwargs)

    def make_event_data(self) -> Dict[str, Any]:
        return {
            "username": self.user.username,
            "email": self.user.email,
            "uuid": str(self.user.uuid),
        }

