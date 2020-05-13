from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',
        views.product_list,
        name='product_list_by_category'),
    url(r'about/', views.pageabout, name='about'),
    url(r'contact/', views.pagecontact, name='contact'),
    url(r'delivery/', views.pagedelivery, name='delivery'),
    url(r'^(?P<manufacture_slug>[-\w]+)/$',
        views.product_list,
        name='product_list_by_manufacture'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),
]