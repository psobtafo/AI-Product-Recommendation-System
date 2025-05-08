from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recommendations/<int:user_id>/', views.get_recommendations, name='recommendations'),
    path('myapp/', include('myapp.urls')),  # Needed to reach /myapp/api/recommend
    path('', include('myapp.urls')),  # Optional if you want root-level routes
    path('myapp/', include('myapp.urls')),  # Only if you use myapp/ URLs separately
    path('blog/', include('blog.urls')),    # Optional
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # Home view
]



