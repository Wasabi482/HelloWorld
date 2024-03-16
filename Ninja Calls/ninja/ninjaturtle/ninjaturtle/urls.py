"""
URL configuration for ninjaturtle project.

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
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI



api= NinjaAPI()
@api.get("/name")
def name(request):
    return {"name": "John Wick"}

@api.get("/add/{a}/{b}")
def add(request, a: float, b: float):
    return {"result": a + b}

@api.get("/subtract/{a}/{b}")
def subtract(request, a: float, b: float):
    return {"result": a - b}

@api.get("/multiply/{a}/{b}")
def multiply(request, a: float, b: float):
    return {"result": a * b}

@api.get("/divide/{a}/{b}")
def divide(request, a: float, b: float):
    if b == 0:
        return {"error": "Cannot divide by zero"}
    return {"result": a / b}


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
    path("api/add", api.urls),
    path("api/subtract", api.urls),
    path("api/multiply", api.urls),
    path("api/divide", api.urls),
]

