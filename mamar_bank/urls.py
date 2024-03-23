
from django.contrib import admin
from django.urls import path,include
from core.views import HomeView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # new


urlpatterns = [
    path('', HomeView.as_view(),name= 'home'),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('transactions/',include('transaction.urls')),
]
urlpatterns += staticfiles_urlpatterns() # new