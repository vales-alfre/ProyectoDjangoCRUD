from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/items/', permanent=False)),
    path('items/', include('crud.urls')),
]
