from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView

from webapp.forms import ReviewForm
from webapp.models import Review, Product


class ReviewView(TemplateView):
    template_name = 'review/review_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        review = get_object_or_404(Review, pk=pk)
        context['review'] = review
        return context


class ReviewCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    template_name = 'review/review_create.html'
    form_class = ReviewForm
    model = Review
    permission_required = 'webapp.add_review'

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        review = form.save(commit=False)
        review.product = product
        review.save()
        return redirect('webapp:product_view', pk=product.pk)



class ReviewUpdateView(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = Review
    template_name = 'review/review_update.html'
    form_class = ReviewForm
    permission_required = 'webapp.change_review'

    def get_success_url(self):
        return reverse('webapp:review_view', kwargs={'pk': self.object.pk})

    def has_permission(self):
        return super().has_permission() and self.get_object().author == self.request.user

class ReviewDeleteView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = Review
    template_name = 'review/review_delete.html'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_review'

    def has_permission(self):
        return super().has_permission() and self.get_object().author == self.request.user


