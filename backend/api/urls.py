from django.urls import path, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('api/users/', views.users, name='users'),
    path('api/create_user/', views.create_user, name='create_user'),
    # path("listar-clientes/", views.listar_clientes, name='listar_clientes'),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('clients/', views.ClientList.as_view()),
]


