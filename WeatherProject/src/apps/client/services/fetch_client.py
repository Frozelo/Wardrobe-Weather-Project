from django.shortcuts import get_object_or_404

from src.apps.client.models import Client


def get_client(user):
    return get_object_or_404(Client, user=user)


def fetch_client_info(client):
    try:
        region = client.region
        city = client.city
        return region, city

    except Exception as e:
        raise ValueError(f"An unexpected error occurred: {str(e)}")
