from django.conf.urls import url
from basic_app import views
from django.urls import path

# Template Tagging
app_name = 'basic_app' # look under the basic app and find the url that matches

# if you come to project page and you see "basic app" / then you go to basic_app.urls and you want the "relative"= it gives you the relative view
# if you want the "others" it gives you the 'other' view
urlpatterns = [
    path('relative/', views.relative, name = 'relative'),
    path('other/', views.other, name ='other'),
]


# urlpatterns = [
#     path(r'^relative/$', views.relative, name = 'relative'),
#     path(r'^other/$', views.other, name ='other'),
# ]
