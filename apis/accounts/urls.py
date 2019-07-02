from django.urls import path
from apis.accounts.views import CreateUserView, UpdateUserView

urlpatterns = [ 
    path('', CreateUserView.as_view()),
    path('<int:id>/', UpdateUserView.as_view())
] 