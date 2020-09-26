from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, ListView

from webapp.models import Product
from webapp.forms import ProductForm, Review
from .base_views import SearchView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class IndexView(ListView):
    template_name = 'prouct/index.html'
    context_object_name = 'product'
    paginate_by = 5
    paginate_orphans = 0
    model = Product
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductView(TemplateView):
    template_name = 'product/product_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pk = self.kwargs.get('pk')
        product = get_object_or_404(Product, pk=pk)

        context['product'] = product
        return context



class ProductCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'product/product_create.html'
    form_class = ProductForm
    permission_required = 'webapp.add_product'

    def form_valid(self, form):
        self.product = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.product.pk})


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'product/product_update.html'
    form_class = ProductForm
    model = Product
    permission_required = 'webapp.change_product'


    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'product/product_delete.html'
    model = Product
    success_url = reverse_lazy('index')
    permission_required = 'webapp.delete_product'





