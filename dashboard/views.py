import datetime

from django.http import JsonResponse

# Create your views here.


def ping(request):
    return JsonResponse({"time": datetime.datetime.utcnow().isoformat()})
