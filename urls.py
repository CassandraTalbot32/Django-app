from django.contrib import admin
from django.urls import include, path
from .views import home_view, contact_view, about_view, projects_view, directory_view, prices_view, quoteView, successView, updates_View, reasons_View
from django.conf import settings
from django.urls import re_path
from django.views.static import serve

# ... the rest of your URLconf goes here ...



urlpatterns = [
	path('blog/', include('blog.urls')),
	path('challenges/', include('challenges.urls')),
	path('products/', include('products.urls')),
	path('admin/', admin.site.urls),
   	path('', home_view, name='home'),
	path('contact/', contact_view),
	path('projects/', projects_view),
	path('directory/', directory_view),
	path('prices/', prices_view),
	path('about/', about_view),
	path('quote/', quoteView, name='contact'),
    path('success/', successView, name='success'),
    path('updates/', updates_View), 
    path('reasons/', reasons_View),
	]
