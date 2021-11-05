import json

from django.core.management.base import BaseCommand
from django.conf import settings
from kafka import KafkaConsumer

from popug_auth.models import User


class Command(BaseCommand):
    help = "Start kafka consumer"

    def handle(self, *args, **options):
        consumer = KafkaConsumer(bootstrap_servers=settings.KAFKA_SERVER)
        consumer.subscribe(["user_stream"])
        self.stdout.write("Consumer is started...\n")
        for event in consumer:
            self.stdout.write(f"Incoming message:\n {event} \n")
            data = json.loads(event.value.decode(encoding='utf-8'))
            self.stdout.write(f"Data:\n {data} \n")

            if data["event_type"] == "user.created":
                user = User(username=data["username"], uuid=data["uuid"])
                user.save()
                self.stdout.write(f"New user: {data}")

