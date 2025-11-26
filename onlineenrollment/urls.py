from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include your app URLs
    path('', include('accounts.urls')),  # change 'schoolapp' to your actual app name


]
