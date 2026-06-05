from django.urls import path
from .views import (
    home,
    buy,
    sale,
    add_stock,
    sale_stack,
    total_stack,
    predict_data,
    predict_page
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),

    path('buy', buy, name="buy"),

    path('sale', sale, name="sale"),

    path('predict', predict_data, name='predict_data'),

    path('predict-page', predict_page, name='predict_page'),

    path('total_stack', total_stack, name="total_stack"),

    path('add_stack', add_stock, name='add_stock'),

    path('sale_stack', sale_stack, name='sale_stack'),
]

urlpatterns += static(
    settings.STATIC_URL,
    document_root='ration_shop_stock/static'
)