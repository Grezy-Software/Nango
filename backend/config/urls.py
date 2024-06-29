"""URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/

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

from django.htttp import HttpResponse
from django.urls import path


def health_check(request) -> HttpResponse:  # noqa: ANN001, ARG001
    """Return a simple 'OK' status."""
    return HttpResponse("OK", status=200)


urlpatterns = [
    path("health_check/", health_check, name="health_check"),
]
