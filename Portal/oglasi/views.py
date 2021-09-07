from django.shortcuts import render
from django.views.generic.base import TemplateView
from diskutovanje.models import Diskusija
from oglasi.models import Oglas

class PortalTemplateView(TemplateView):
    def get_context_data(self, **kwargs):
        broj_diskusija = Diskusija.objects.count()
        diskusije = Diskusija.objects.all()
        oglasi = Oglas.objects.all()
        context = {
            'broj_diskusija': broj_diskusija,
            'diskusije': diskusije,
            'oglasi': oglasi,
        }
        return context


