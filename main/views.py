from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import RepertoirePiece

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
    return render(request, 'main/servicios.html')

def videos(request):
    return render(request, 'main/videos.html')

def repertorio_list(request):
    # This will be empty for now, until we load the data in Step 4
    pieces = RepertoirePiece.objects.all().order_by('nombre')
    return render(request, 'main/repertorio_list.html', {'pieces': pieces})

def repertorio_detail(request, pk):
    piece = get_object_or_404(RepertoirePiece, pk=pk)
    return render(request, 'main/repertorio_detail.html', {'piece': piece})

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
    return render(request, 'main/sitemap_template.xml', {'pages': pages}, content_type='application/xml')