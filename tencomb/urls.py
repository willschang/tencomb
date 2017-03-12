from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from tencomb.views import homepage

admin.autodiscover()

urlpatterns = [
    url(r'^$', homepage),
    url(r'^api/v1/', include('initdata.api_urls')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
] 


# DEBUG为TRUE时指定static文件
if not settings.DEBUG:
    urlpatterns += [url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})]

