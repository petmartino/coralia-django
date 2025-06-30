# main/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import RepertoirePiece
from quotes.models import EventType

def index(request):
    return render(request, 'main/index.html')

def acerca(request):
    return render(request, 'main/acerca.html')

def contacto(request):
    return render(request, 'main/contacto.html')

def encuesta(request):
    return redirect("https://forms.gle/GmxMzKhDXjFHPFp68")

def politica(request):
    return render(request, 'main/politica.html')

def servicios(request):
    # Fetch data for the template
    event_types = EventType.objects.all().order_by('order')
    popular_pieces = RepertoirePiece.objects.filter(tags__name__icontains='popular').order_by('nombre')[:10]

    context = {
        'event_types': event_types,
        'popular_pieces': popular_pieces,
    }
    return render(request, 'main/servicios.html', context)

def videos(request):
    return render(request, 'main/videos.html')

# --- UPDATED VIEW ---
def repertorio_list(request):
    # This query gets all pieces and pre-fetches their related tags to avoid extra DB hits.
    pieces = RepertoirePiece.objects.prefetch_related('tags').all().order_by('nombre')
    context = {
        'pieces': pieces
    }
    return render(request, 'main/repertorio_list.html', context)

# --- VERIFY THIS VIEW ---
def repertorio_detail(request, pk):
    # This gets a single piece using the primary key (pk) from the URL.
    piece = get_object_or_404(RepertoirePiece, pk=pk)
    # The context dictionary MUST use the key 'piece' to match your template.
    context = {
        'piece': piece
    }
    return render(request, 'main/repertorio_detail.html', context)

def sitemap_view(request):
    """Generates a dynamic sitemap.xml."""
    pages = [
        {'loc': request.build_absolute_uri(reverse('main:index'))},
        {'loc': request.build_absolute_uri(reverse('main:servicios'))},
        {'loc': request.build_absolute_uri(reverse('main:videos'))},
        {'loc': request.build_absolute_uri(reverse('main:repertorio_list'))},
        {'loc': request.build_absolute_uri(reverse('main:contacto'))},
        {'loc': request.build_absolute_uri(reverse('main:politica'))},
        {'loc': request.build_absolute_uri(reverse('main:acerca'))},
    ]
    pieces = RepertoirePiece.objects.all()
    for piece in pieces:
        pages.append({
            'loc': request.build_absolute_uri(reverse('main:repertorio_detail', args=[piece.id]))
        })
    # Note: Ensure you have a 'main/sitemap_template.xml' file or this will error.
    return render(request, 'main/sitemap_template.xml', {'pages': pages}, content_type='application/xml')