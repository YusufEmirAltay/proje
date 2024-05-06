from django.contrib import admin
from django.urls import  path, include



urlpatterns = [
    path('', include('pages.urls')),
    path('turlar/', include('turlar.urls')),
    path('admin/', admin.site.urls),
]

# site
# turlar
# pages








