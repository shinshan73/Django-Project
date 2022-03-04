from django.contrib import admin
from django.urls import path, include 

def home(request):
    return HttpResponse('Product Page')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('app.urls'))
]
