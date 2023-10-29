from src.client.models import Client


def get_city_for_client(request):
    region = request.POST.get('region')
    city = request.POST.get('city')
    user_instance = request.user

    try:
        client = Client.objects.get(user=user_instance)
        client.region = region
        client.city = city
        client.save()

    except:
        client = Client(user=user_instance, region=region, city=city)
        client.save()
