from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns =[
    path("", views.index, name="index"),
    #path("login",LoginView.as_view(template_name='FireCheck/login.html') , name="login"),
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path("devicelist", views.device_list, name="devicelist"),
    path("site/<int:did>", views.device_details, name="devicedetails"),
    path("zone/<int:zid>", views.zone_details, name="zonedetails"),
    path("panel/<int:pid>", views.panel_details, name="paneldetails"),
    path("building/<int:bid>", views.building_details, name="buildingdetails"),
    path("reddevicelist", views.red_device_list, name="reddevicelist"),
    path("yellowdevicelist", views.yellow_device_list, name="yellowdevicelist"),
    path("greendevicelist", views.green_device_list, name="greendevicelist"),
    path("buildinglist", views.building_list, name="buildinglist"),
    path("zonelist", views.zone_list, name="zonelist"),
    path("accounts/", include('django.contrib.auth.urls')),
    path("create", views.create, name="create"),
    #path("panellist", views.panel_list, name="panellist"),
]
