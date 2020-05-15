
from django.contrib import admin
from django.urls import path,include
from products import views #Debo importar los views de las app que este llamando

#Son las direcciones a las que se admiten en la pag web
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), #Nos lleva al homepage
    path('accounts/', include('accounts.urls')),  
]
