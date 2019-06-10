from django.contrib import admin
from django.urls import path,include
import datablog.views
import blogapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', datablog.views.home, name='home'),
    path('new/', datablog.views.new, name='new'),
    path('result/',datablog.views.result, name='result'),
    path('about/',datablog.views.about, name='about'),

    
    path('blog/', include('blogapp.urls')),

]
