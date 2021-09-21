from django.shortcuts import render
from django.views.generic.base import TemplateView
from diskutovanje.models import Diskusija
from oglasi.models import Oglas
from .forms import Forma_postavljanja_oglasa
from django.shortcuts import redirect

class PortalTemplateView(TemplateView):
    def get_context_data(self):
        broj_diskusija = Diskusija.objects.count()
        diskusije = Diskusija.objects.all()
        oglasi = Oglas.objects.all()
        oglasi_javni = Oglas.objects.filter(vidljivost = 1)
        context = {
            'broj_diskusija': broj_diskusija,
            'diskusije': diskusije,
            'oglasi': oglasi,
            'oglasi_javni': oglasi_javni,
        }
        return context

def detaljiOglasa(request, id):
    oglasi = Oglas.objects.get(pk=id)
    context = {
      'oglasi': oglasi
    }
    return render(request, 'oglasi/detail.html', context)

def postavljanjeOglasa(request):
    form = Forma_postavljanja_oglasa()
    if (request.method == "POST"):
        form = Forma_postavljanja_oglasa(request.POST);
    if (form.is_valid()):
        oglas = form.save();
        oglas.autor = request.user;
        oglas.save();
        return redirect("index");

    context = {
        "form": form
    };

    return render(request, "oglasi/kreiranje_oglasa.html", context);


# def create ( request ):
# form = ThreadCreateForm ( );
#
#  if (request.method == "POST"):
# form = ThreadCreateForm ( request.POST );
# if (form.is_valid ( )):
# thread = form.save ( );
# thread.author = request.user;
# thread.save ( );
# return redirect ( "index" );
#
#  context = {
# "form": form
# };
#
#  return render ( request, "thread/create.html", context );
