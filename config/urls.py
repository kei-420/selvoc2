from django.contrib import admin
from django.urls import path, include
from .settings import develop

urlpatterns = [
    path('admin/', admin.site.urls),
    path('selvoc/accounts/', include('accounts.urls')),
    path('selvoc/', include('wordbook.urls')),
]

if develop.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns



