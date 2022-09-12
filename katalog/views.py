from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    data_barang_catalog = CatalogItem.objects.all()
    context = {
    'list_barang': data_barang_catalog,
    'nama'      : 'Carissa Almira',
    'studentid' : '2106751676',
}
    return render(request, "katalog.html", context)