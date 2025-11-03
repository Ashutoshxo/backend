
from django.urls import path
from .views import TodoSerializer,TodoUpdateDelete,TodoGetCreate
urlpatterns = [
    path('', TodoGetCreate.as_view()),
    path('<int:pk>', TodoUpdateDelete.as_view())
   
]
