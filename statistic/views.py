from django.shortcuts import render
from django.views.generic import CreateView
from statistic.models import Statistic


class StatisticCreateView(CreateView):
    model = Statistic
    fields = ('title', 'slug', 'publication_feature', 'views_count',)
    # success_url =
