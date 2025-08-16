from django.contrib import admin
from django.urls import path
from django.http import HttpRequest, HttpResponse

def health_check(request: HttpRequest) -> HttpResponse:
    return HttpResponse("DJANGO IS ALIVE", content_type="text/plain")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health_check),
] 