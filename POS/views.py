from django.shortcuts import render
from home.models import Order 
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from home.models import Comment
from home.forms import CommentForm
from django.http import HttpResponseRedirect


# Create your views here.

# def list_order(request):
#     Data = {'Order_data': Order.objects.all().order_by('-date')}
#     return render(request, 'html/pos.html', Data)
# class thay the cho fuction o tren
class OrderListView(ListView):
    queryset = Order.objects.all().order_by('-date')
    template_name = 'html/pos.html'
    context_object_name = 'Order_data'
    paginate_by = 2

# def load_id(request, id):
#     order = Order.objects.get(id=id)
#     return render(request, 'html/pos_id.html', {'order' : order})
class OrderDetailView(DetailView):
    model = Order
    template_name = 'html/pos_id.html'

def load_id(request, pk):
    order = get_object_or_404(Order, pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST, author=request.user, order=order)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, 'html/pos_id.html', {'order':order, 'form':form})