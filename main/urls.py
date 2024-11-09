from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework import permissions , re_path
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Your API Title",
#         default_version='v1',
#         description="API documentation",
#         terms_of_service="###",
#         contact=openapi.Contact(email="contact@yourapi.com"),
#         license=openapi.License(name="DATA UNION"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    # path('api-auth/', include('rest_framework.urls')),
    # path('api/', include('api.urls')),
    # # path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('account', include('allauth.urls')),
    # # path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)