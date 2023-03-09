from django.urls import path
from . import views
from home.models import Order 
from django.views.generic import ListView, DetailView

urlpatterns = [
    path(
        '', 
        views.OrderListView.as_view(), 
        name='name_pos',
    ),
    # path(
    #     '<int:pk>', 
    #     DetailView.as_view(
    #         model = Order,
    #         template_name = 'html/pos_id.html',
    #     ), 
    #     name='name_pos_id'
    # ),
    path(
        '<int:pk>', 
        views.load_id,
        name='name_pos_id',
    ),
]