from django.urls import path

from first.views import *

urlpatterns = [
    path('', index, name = 'home'),
    path('about/', about, name='about'),
    path('addpage', addpage, name='add_page'),
    path('threads/<int:post_id>/', show_post, name='post'),

]