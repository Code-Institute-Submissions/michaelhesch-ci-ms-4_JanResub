from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import ListView
from product.models import Product, Category


class HomeView(ListView):
    model = Product
    template_name='index.html'


def products_store(request):
    products = Product.objects.all()
    # Variables for searching and filtering store page
    query = None
    category = None
    page_obj = None

    if request.GET:
        # Logic to filter the store page by GPU type (category)
        if 'category' in request.GET:
            category = request.GET['category'].split(',')
            products = products.filter(category__category_name__in=category)
            category = Category.objects.get(category_name__in=category)
            if len(list(products)) > 8:
                # Configure pagination for store page
                paginator = Paginator(products, 8)
                # Retrieve current page number from GET request, default to pg 1
                page_number = request.GET.get('page', 1)
                # Generate pagination page_obj to return in context
                page_obj = paginator.get_page(page_number)
                # Update paginated object to return in context
                products = paginator.page(page_number)

        # Logic to search the store items on product name, description and category name fields
        elif 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter criteria to search by!")
                return redirect(reverse('home:store'))
            
            queries = Q(product_name__product_name__icontains=query) | Q(description__icontains=query) | Q(category__category_name__icontains=query)
            products = products.filter(queries)
            if len(list(products)) > 8:
                paginator = Paginator(products, 8)
                page_number = request.GET.get('page', 1)
                page_obj = paginator.get_page(page_number)
                products = paginator.page(page_number)

    # Set current_category value to return in context for menu bar dynamic styling
    if category:
        current_category = category.category_name
    else:
        current_category = None
    if len(list(products)) > 8:
        paginator = Paginator(products, 8)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        products = paginator.page(page_number)

    context = {
        'products': products,
        'search_term': query,
        'current_category': current_category,
        'page_obj': page_obj
    }
    return render(request, 'home/store.html', context)
