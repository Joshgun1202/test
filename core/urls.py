from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('analytics', views.analytics, name='analytics'),
    path('cloud_forensic', views.cloud_forensic, name='cloud_forensic'),
    path('computer_forensic', views.computer_forensic, name='computer_forensic'),
    path('db_forensic', views.db_forensic, name='db_forensic'),
    path('index2', views.index2, name='index2'),
    path('index', views.index, name='index'),
    path('iot_forensic', views.iot_forensic, name='iot_forensic'),
    path('main', views.main, name='main'),
    path('mobil_forensic', views.mobil_forensic, name='mobil_forensic'),
    path('network_forensic', views.network_forensic, name='network_forensic'),
    path('page_404_error', views.page_404_error, name='page_404_error'),
    path('page_coming_soon', views.page_coming_soon, name='page_coming_soon'),
    path('page_login', views.page_login, name='page_login'),
    path('page_register', views.page_register, name='page_register'),
    path('pos_customer_order', views.pos_customer_order, name='pos_customer_order'),
    path('pos_menu_stock', views.pos_menu_stock, name='pos_menu_stock'),
    path('settings', views.settings, name='settings'),
    path('ui_icons', views.ui_icons, name='ui_icons'),
    path('items/<int:id>',views.items, name='item' ),
]