from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.models import Category, Product


class CategoryListView(ListView):
    model = Category


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        else:
            return Product.objects.all()


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class CategoryProductDetailView(DetailView):
    model = Category
    template_name = 'catalog/product.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_item = self.object
        context['title'] = 'Товары'
        context['object_list'] = category_item.product_set.all()
        return context


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'category', 'image', 'description')
    success_url = reverse_lazy('catalog:product')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'category', 'purchase_price', 'image', 'description',)
    success_url = reverse_lazy('catalog:product')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}) {message}')
    return render(request, 'catalog/contacts.html')


def in_stock(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    if product_item.in_stock:
        product_item.in_stock = False
    else:
        product_item.in_stock = True

    product_item.save()

    return redirect(reverse('catalog:product'))
