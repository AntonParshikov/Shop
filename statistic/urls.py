from django.urls import path
from statistic.apps import StatisticConfig
from statistic.views import StatisticCreateView

app_name = StatisticConfig.name

urlpatterns = [
    path('create/', StatisticCreateView.as_view(), name='create'),
    # path('', ..., name='list'),
    # path('view/<int:pk>/', ..., name='view'),
    # path('edit/<int:pk>/', ..., name='edit'),
    # path('delete/<int:pk>/', ..., name='delete'),
]
