from django.urls import path
from .views import PlotView, PlotDetailView

urlpatterns = [
    path('', PlotView.as_view()),
    path('<int:pk>', PlotDetailView.as_view())
]
