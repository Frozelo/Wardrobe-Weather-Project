from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from src.client.models import Client


def get_client(user):
    return get_object_or_404(Client, user=user)


def fetch_client_info(user):
    try:
        client = get_client(user)
        region = client.region
        city = client.city
        return region, city

    except Exception as e:
        raise ValueError(f"An unexpected error occurred: {str(e)}")
