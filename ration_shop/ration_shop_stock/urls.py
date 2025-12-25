from django.urls import path
from .views import home,buy,sale,add_stock,sale_stack,total_stack
from .db import db_con
urlpatterns=[
    path('',home, name="home"),
    path('buy',buy,name="bye"),
    path('sale',sale,name="sale"),
    path('total_stack',total_stack , name="total_stack"),
    #=----
    #add tha itmes
    path('add_stack',add_stock,name='add_stock'),
    
    
    # sale the items 
    path('sale_stack',sale_stack,name='sale_stack'),
     
    # totla stack is 
   
]