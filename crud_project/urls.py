from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.http import HttpResponse

def health(request):
    return HttpResponse("OK")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',health, name='health'),
    path('', RedirectView.as_view(url='/items/', permanent=False)),
    path('items/', include('crud.urls')),
]
