"""
URL configuration for social_media_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from django.http import HttpResponseRedirect
from django.urls import reverse
from drf_yasg import openapi
# def redirect_to_swagger(request):
#     return HttpResponseRedirect(reverse('schema-swagger-ui'))
# schema_view = get_schema_view(
#     openapi.Info(
#         title="Social Media API",
#         default_version='v1',
#         description="Test description",
#         terms_of_service="https://www.example.com/terms/",
#         contact=openapi.Contact(email="contact@example.com"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
    path('secret-admin/', admin.site.urls),
    path('account/',include('accounts.urls')),
    path('api/',include('posts.urls')),
    path('user/',include('notifications.urls')),
    # path('', redirect_to_swagger),

    # drf-yasg endpoints for swagger and redoc
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]