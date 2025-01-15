from django.urls import path, include
from django.views.generic import TemplateView

from mysite.books import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # Hapus ^$
    path('books/', views.book_list, name='book_list'),  # Hapus ^ dan $
    path('books/create/', views.book_create, name='book_create'),  # Hapus ^ dan $
    path('books/<int:pk>/update/', views.book_update, name='book_update'),  # Ganti regex dengan <int:pk>
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),  # Ganti regex dengan <int:pk>
]
