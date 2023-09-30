from django.shortcuts import render, HttpResponse, redirect
import csv
from .models import Product
from django.db import connection
# Create your views here.
def add_product(request):
    if request.method == "GET":
        return render(request, 'form.html')
    
    elif request.method == "POST":
        data = request.POST
        print(data)
        name = data.get('name')
        price = data.get('prc')
        qty = data.get('qty')
        print(name, price, qty)
        Product.objects.create(name = name, price = price, qty = qty)
    return redirect('show_pro')

    
def upload_csv(request):
    file = request.FILES['csv_file']
    file_obj = file.read().decode('utf-8').splitlines()
    cur = csv.reader(file_obj)
    for x in cur:
        print(x)
        if x[0] == "Name":
            continue
        try:
            name = x[0]
            print(name)
            price = x[1]
            print(price)
            qty = x[2]
            print(qty)
            if name is None or price is None:
                raise ValueError
        except ValueError:
             return HttpResponse("Name or price Not Null be null")
        else:
            Product.objects.create(name = name, price = price, qty = qty)
            pass
    return redirect('show_pro')


def get_data(request):
    obj = Product.objects.all()  
    return render(request, 'show.html', {'obj' : obj})


def create_csv(request):
    print('Hello')
    responsed = HttpResponse(content_type = "sample/csv")   
    responsed['Content-Disposition'] = 'attachment; filename = "sample.csv"'
    cur = csv.writer(responsed)
    cur.writerow(["id", "Name", "Price", "Qty"])
    obj = Product.objects.all()  
    conn = connection.cursor()
    conn.execute("select * from prodcut")
    data = conn.fetchall()
    for x in data:
        cur.writerow(x)
    return responsed



    
    