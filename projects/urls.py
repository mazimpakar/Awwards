from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^projects/(\d+)',views.projects,name ='projects'),
    url(r'^$',views.projects_today,name='projectsToday'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^new/image$', views.new_projects, name='new-projects')
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
