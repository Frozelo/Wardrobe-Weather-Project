class ExtractUserMiddleware:
    def __init__(self, get_response):
        self.response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            request.custom_user = request.user
        else:
            request.custom_user = None
        return self.response(request)