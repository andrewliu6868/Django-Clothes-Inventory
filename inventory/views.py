from django.shortcuts import render
from .models import ProductModel, CategoryModel, TagModel
from django.db.models import Q

# Create your views here.
def product_list(request):
    # fetch the query params from given request URL
    q = request.GET.get("query", "").strip()
    cat_id = request.GET.get("category", "").strip()
    tag_ids = request.GET.getlist("tags")  

    # fetch base queryset, using select_related since category is foreign key
    qs = ( ProductModel.objects.all() )
    
    # apply filtering if necessary
    if q:
        # filter based on search, Q works similar to LIKE in SQL
        qs = qs.filter(Q(name__icontains=q) | Q(description__icontains=q))
    if cat_id:
        # filter based on category
        qs = qs.filter(category_id=cat_id)
        
    for t_id in tag_ids:
        # filter based on tag
        qs = qs.filter(tags=t_id)

    # render html template
    return render(request, "inventory/product_list.html", {
        "products": qs,
        "categories": CategoryModel.objects.order_by('name'),
        "tags": TagModel.objects.order_by('name'),
        "query": q,
        "selected_category": cat_id,
        "selected_tags": [int(t) for t in tag_ids],
    })
        
        
    