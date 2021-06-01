from django.urls import path
from mobile.views import create_brands,list_all_brands,get_brandindex,delete_brands,update_brands

urlpatterns=[
    path("index",get_brandindex,name="index"),
    path("createbrands",create_brands,name="create"),
    path("brands",list_all_brands,name="list"),
    path("remove/<int:id>",delete_brands,name="delete"),
    path("update/<int:id>",update_brands,name="update"),
]