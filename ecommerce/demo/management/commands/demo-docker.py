from typing import Any, Optional

from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        call_command("docker-compose up -d")

        # https://docs.docker.com/compose/profiles/
        # docker-compose --profile frontend --profile debug up
