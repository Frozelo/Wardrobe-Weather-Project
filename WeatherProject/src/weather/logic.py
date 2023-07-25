from src.client.models import Client


def get_city_for_client(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        user_instance = request.user

        try:
            client = Client.objects.get(user=user_instance)
            client.city = city
            client.save()
        except:
            client = Client(user=user_instance, city=city)
            client.save()
