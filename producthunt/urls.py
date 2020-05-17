
from django.contrib import admin
from django.urls import path,include
from products import views #Debo importar los views de las app que este llamando
from django.conf.urls.static import static
from django.conf import settings

#Son las direcciones a las que se admiten en la pag web
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), #Nos lleva al homepage
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),  
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
