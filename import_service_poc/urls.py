"""
URL configuration for import_service_poc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import_shipment:  from my_app import_shipment views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import_shipment:  from other_app.views import_shipment Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import_shipment include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from import_shipment.views import import_fast_pro_xml_v1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shipment/fast-pro/xml/v1', import_fast_pro_xml_v1, name="import_shipment")
]
