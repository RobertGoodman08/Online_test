from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/', include('quiz.urls')),
    path('', include('main.urls')),
    path('questions/', include('questions.urls')),
    path('result/', include('results.urls')),
    path('url/', include('user.urls'))
]
