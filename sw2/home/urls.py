from home.views import(bookslistview,registration,search,users,booksDetailview,DeletebookView)
from django.urls import path
urlpatterns=[
    path('',bookslistview.as_view(),name="books"),
    path('signup/',registration.as_view(),name='signup'),
    path('search/',search,name='search'),
    path('users/',users.as_view(),name='user'),
    path('show/<int:pk>',booksDetailview.as_view(),name='book.show'),
    path('<int:pk>',DeletebookView.as_view(),name='book.delete')
]
