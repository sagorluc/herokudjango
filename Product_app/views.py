from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Category, ProductType, Product, Warranty, Brand
from django.db.models import Q, Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request ): 
    cate_obj         = Category.objects.all()
    product_type_obj = ProductType.objects.all()
    warranty_obj     = Warranty.objects.all()
    brand_obj        = Brand.objects.all()   
    product_filter   = Product.objects.all().filter(is_available=True)
   
    min_price          = request.GET.get('min-price-keyword')
    max_price          = request.GET.get('max-price-keyword')
    search_input       = request.GET.get('keyword')
    
    
    # Searching Product
    if search_input != "" and search_input is not None:
        product_filter = product_filter.filter(Q(category__category_name__icontains=search_input) 
                                               | Q(product_type__product_type__icontains=search_input)
                                               | Q(brand__brand_name__icontains=search_input)
                                               | Q(product_name__icontains=search_input)
                                               | Q(product_title__icontains=search_input)
                                               )
        
        
    # Filtering Product by Price range
    if min_price and max_price and int(min_price) <= int(max_price):
        product_filter =  product_filter.filter(Q(price__gte=min_price) & Q(price__lte=max_price))


    # Set paginator
    paginator = Paginator(product_filter, 3) # 2 product per page
    page = request.GET.get('page')
    page_products = paginator.get_page(page)
    
    product_count = product_filter.count()

    
    context = {
        'cate_objs' : cate_obj,
        'product_type_objs' : product_type_obj,
        'warranty_objs' : warranty_obj,
        'brand_objs' : brand_obj,
        'filter_products' : product_filter,   # it will show all the product
        'product_count' : product_count,
        'products' : page_products,           # paginated product

    }
    
    return render(request, 'store.html', context)



def filter_data(request):
    categories    = request.GET.getlist('category[]')
    product_types = request.GET.getlist('product_type[]')
    brands        = request.GET.getlist('brand[]')
    warrantys     = request.GET.getlist('warranty[]')
    # print(categories, 'line 79')

    filter_products = Product.objects.all().order_by('id').distinct()
    
    # Real time filtering by AjaxJs
    if len(categories) > 0:
        filter_products = filter_products.filter(category__category_name__in=categories).distinct()
        
    if len(product_types) > 0:
        filter_products = filter_products.filter(product_type__product_type__in=product_types).distinct()

    if len(brands) > 0:
        filter_products = filter_products.filter(brand__brand_name__in=brands).distinct()
        
    if len(warrantys) > 0:
        filter_products = filter_products.filter(warranty__warranty_duration__in=warrantys).distinct()
 
    paginator = Paginator(filter_products, 2) # 2 product per page
    page = request.GET.get('page')
    page_products = paginator.get_page(page)       
    product_cnt = filter_products.count()

    context = {
        
            'datas': filter_products, 
            'product_cnt': product_cnt,
            'page_products' : page_products,  
        }

    template = render_to_string('filter_product.html', context)

    return JsonResponse({'datas': template})