from src.apps.client.models import Client
from src.core.services import get_objects


def get_city_for_client(request):
    region = request.POST.get('region')
    city = request.POST.get('city')
    user_instance = request.user

    try:
        client = get_objects(obj=Client.objects.only('region', 'city'),
                             user=user_instance
                             )
        client.region = region
        client.city = city
        client.save()

    except Exception as e:
        print(e)
        client = Client(user=user_instance, region=region, city=city)
        client.save()
