from django.urls import path
from .views import CartList,CartAdd,CartDelete,CartUpdate

urlpatterns = [
   path('',CartList.as_view(),name='cart_list'),
   path('add/',CartAdd.as_view(),name='cart_add'),
   path('delete/',CartDelete.as_view(),name='cart_delete'),
   path('update/',CartUpdate.as_view(),name='cart_update'),

]