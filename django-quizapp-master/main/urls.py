from django.urls import path
from .views import (
    base,
    quiz_view,
    quiz_data_view,
    save_quiz_view,
)


urlpatterns = [
    path('', base, name='base'),
    path('<pk>/', quiz_view, name='view'),
    path('<pk>/save/', save_quiz_view, name='save'),
    path('<pk>/data/', quiz_data_view, name='data'),
]
