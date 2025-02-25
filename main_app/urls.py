from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",home_view,name="home"),
    path("new/",create_portfolio,name="new_porfolio"),
    path("portfolio/<int:id>",view_portfolio,name="view_portfolio")
]


if settings.DEBUG:  # Serve media only in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)