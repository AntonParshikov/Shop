from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from statistic.models import Statistic


class StatisticCreateView(CreateView):
    model = Statistic
    fields = ('title', 'content', 'publication_feature',)
    success_url = reverse_lazy('statistic:list')

    def form_valid(self, form):
        if form.is_valid():
            new_stat = form.save()
            new_stat.slug = slugify(new_stat.title)
            new_stat.save()
        return super().form_valid(form)


class StatisticUpdateView(UpdateView):
    model = Statistic
    fields = ('title', 'content', 'publication_feature',)

    # success_url = reverse_lazy('statistic:list')

    def form_valid(self, form):
        if form.is_valid():
            new_stat = form.save()
            new_stat.slug = slugify(new_stat.title)
            new_stat.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('statistic:view', args=[self.kwargs.get('pk')])


class StatisticDeleteView(DeleteView):
    model = Statistic
    success_url = reverse_lazy('statistic:list')


class StatisticListView(ListView):
    model = Statistic

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication_feature=True)
        return queryset


class StatisticDetailView(DetailView):
    model = Statistic

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()

        return self.object
