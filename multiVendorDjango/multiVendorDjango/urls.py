from django.contrib import admin
from django.urls import include, path

# from quickstart import urls
from quickstart import views



# urlpatterns = [
#     # path('admin/', admin.site.urls),
#     # path('api/', include(router.urls)),    
#     # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     path('', include(urls)),
# ]

urlpatterns = [
    path('api/', include('quickstart.urls')),
    path('', views.Reactapp ),
    path('<path:resource>', views.Reactapp),
]