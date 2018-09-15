#_*_coding:utf-8_*_

from django.conf.urls import url, include
from rest_framework import routers
from cmdbinfo import rest_views as views
from cmdbinfo import views as asset_views
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'assets', views.AssetViewSet)
router.register(r'servers', views.ServerViewSet)
router.register(r'ram', views.RamViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #访问 api/的时候返回的主页在这里显示
    url(r'^', include(router.urls)),
    url(r'asset_list/$',views.AssetList ),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #get_dashboard_data
    url(r'^dashboard_data/',asset_views.get_dashboard_data,name="get_dashboard_data")
]