
from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models import Q




def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'films/mp2.html', {'movie': movie})


# def index(request):
#     return render(request, 'index.html')

# def mp2(request):
#     return render(request, 'mp2.html')






# index sayfası için view fonksiyonu.
def movie_list(request):
    # Tüm filmleri al
    film_listesi = Movie.objects.all()
    sayfa_sayisi = 16  # Her sayfada 6 film göstermek istiyoruz
    paginator = Paginator(film_listesi, sayfa_sayisi)

    # Geçerli sayfa numarasını URL'den alıyoruz. Varsayılan olarak sayfa 1.
    sayfa_numarasi = request.GET.get('sayfa', 1)
    sayfa_objesi = paginator.get_page(sayfa_numarasi)

    # Sayfa numaralarını belirleyelim
    mevcut_sayfa = sayfa_objesi.number
    toplam_sayfa = paginator.num_pages
    sayfa_numaralari = []

    # "İlk" sayfa
    if mevcut_sayfa > 3:
        sayfa_numaralari.append(1)

    # 2 önceki, 1 önceki, mevcut, 1 sonraki, 2 sonraki
    sayfa_numaralari.extend(
        numara for numara in range(mevcut_sayfa - 2, mevcut_sayfa + 3)
        if 1 <= numara <= toplam_sayfa
    )

    # "Son" sayfa
    if mevcut_sayfa < toplam_sayfa - 2:
        sayfa_numaralari.append(toplam_sayfa)

    return render(request, 'films/index.html', {
        'sayfa_objesi': sayfa_objesi,
        'sayfa_numaralari': sayfa_numaralari
    })

def search_movies(request):
    query = request.GET.get('query', '')
    if query:
        # Filter movies based on title, original title, or description
        filmler = Movie.objects.filter(
            Q(title__icontains=query) | 
            Q(original_title__icontains=query) | 
            Q(description__icontains=query)
        )[:5]  # Get only the first 8 matches
    else:
        filmler = Movie.objects.none()  # Return an empty QuerySet

    # Convert movies to JSON format, including `poster_url`
    film_verileri = list(filmler.values(
        'id', 'title', 'original_title', 'imdb_score', 
        'release_year', 'image', 'poster_url'
    ))
    return JsonResponse({'filmler': film_verileri})


# Arama sonuçlarını JSON formatında döndüren view fonksiyonu
# def search_movies(request):
#     query = request.GET.get('query', '')
#     if query:
#         # Filmleri isme, açıklamaya veya diğer alanlara göre filtrele
#         filmler = Movie.objects.filter(
#             Q(title__icontains=query) | 
#             Q(original_title__icontains=query) | 
#             Q(description__icontains=query)
#         )[:8]
#     else:
#         filmler = Movie.objects.none()  # Boş bir QuerySet döner

#     # Filmleri JSON formatında döndür
#     film_verileri = list(filmler.values('id', 'title', 'original_title', 'imdb_score', 'release_year', 'image'))
#     return JsonResponse({'filmler': film_verileri})




