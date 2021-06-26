from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('common.urls')),  # include app's urls here.
    path('pets/', include('pets.urls'))
]
