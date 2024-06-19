from django.contrib import admin
from django.urls import path
from AlgoVisual import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bubbleSort/', views.viewBubble, name='viewBubble'),
    path('insertionSort/', views.viewInsertion, name='viewInsertion'),
    path('selectionSort/', views.viewSelection, name='viewSelection'),
    path('mergeSort/', views.viewMerge, name='viewMerge'),
    path('quickSort/', views.viewQuick, name='viewQuick'),
    path('compareAlgorithms/', views.viewCompare, name='viewCompare'),
]