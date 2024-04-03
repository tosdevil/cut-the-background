from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
		path('',views.index, name='home'),
		path('cut',views.cut, name='cut'),
		path('cuttt/<int:pk>/', views.cut_detail_view, name='cut_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
