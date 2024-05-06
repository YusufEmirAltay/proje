from datetime import date
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Tur
data = {
    "Yurt Dışı":"Yurt dışı kategorisine ait turlar",
    "Yurt İçi":"Yurt içi kategorisine ait turlar",
}

db = {
    "turlar": [
        {
            "title":"İstanbul Turu",
            "description":"İstanbul Turu Açıklaması",
            "imageUrl":"3.jpg",
            "slug":"istanbul-turu",
            "date": date(2025,10,10),
            "isActive": True
        },
        {
            "title":"Atina Turu",
            "description":"Atina Turu Açıklaması",
            "imageUrl":"1.jpg",
            "slug":"atina-turu",
            "date": date(2025,7,15),
            "isActive": True

        },
        {
            "title":"Paris Turu",
            "description":"Paris Turu Açıklaması",
            "imageUrl":"2.jpg",
            "slug":"paris-turu",
            "date": date(2025,5,26),
            "isActive": True
 
        }
    ],
    "categories": [
        {"id":1,"name":"Yurt Dışı","slug":"Yurt Dışı"},
        {"id":2,"name":"Yurt İçi","slug":"Yurt İçi"},
        
        ]
}



def index(request):
    turlar = Tur.objects.all()
    kategoriler = db["categories"]

    

    return render(request, 'turlar/index.html',{
        'categories': kategoriler,
        'turlar':turlar 
    })
    
    
def details(request, tur_adi):
    return HttpResponse(f'{tur_adi} detay Sayfası')

def getTurlarByCategory(request, category_name):
    try:
        category_text = data[category_name];
        return render(request, 'turlar/turlar.html', {
            'category': category_name,
            'category_text': category_text
        })
    except:
        return HttpResponseNotFound("Yanlış Kategori Seçimi")

def getTurlarByCategoryId(request, category_id):
    category_list = list(data.keys())
    if(category_id > len(category_list)):
        return HttpResponse("Yanlış Kategori Seçimi")
    
    
    category_name = category_list[category_id - 1]

    redirect_url = reverse('turlar_by_category', args=[category_name])
    
    return redirect(redirect_url)
