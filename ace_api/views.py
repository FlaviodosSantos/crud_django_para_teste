from django.shortcuts import render
from .models import Indice, Ace
from .forms import IndiceForm
from django.views.generic.list import ListView
import folium

# Create your views here.


class AceList(ListView):
    model = Ace
    fields = '__all__'
    template_name = 'index.html'


def indice(request, ciclo):
    template_name = 'indice.html'
    # ciclo = get_object_or_404(Indice, ciclo=ciclo)
    c = ciclo
    indices = Indice.objects.filter(ciclo=ciclo)
    new_indice = None  # indice postado
    if request.method == 'POST':
        indice_form = IndiceForm(data=request.POST)
        if indice_form.is_valid():
            # cria o indice mas não o salva no bd ainda
            new_indice = indice_form.save(commit=False)
            # actrinui o atual indice ao ciclo
            new_indice.ciclo = c
            # agora salva no bd
            new_indice.save()

    else:
        indice_form = IndiceForm()
    
    context = {
        'ciclo': c,
        'indices': indices,
        'new_indice': new_indice,
        'indice_form': indice_form,
    }

    return render(request, template_name, context)


def mapa_dengue_caico(request, ciclo):
    # carregando os dados

    geojson_arquivo = "data/malha_bairro_caico.json"
    

    # filtrando os dados pelo ciclo
    indices = Indice.objects.filter(ciclo=ciclo)
    siglas = []
    indice = []
    # pegando as siglas e os indices
    for i in indices:
        siglas.append(i.bairro_nome.sigla)

    for i in indices:
        indice.append(float(i.indice_bairro))
    # juntando as duas listas
    dados = list(zip(siglas, indice))

    # centralizando o mapa
    mapa_caico = folium.Map([-6.4648, -37.0853],
                            zoom_start=14, control_scale=True)

    # um tipo de tiles
    folium.TileLayer(tiles='https://{s}.tile.jawg.io/jawg-sunny/{z}/{x}/{y}{r}.png?access-token={accessToken}',
                     attr='<a href="http://jawg.io" title="Tiles Courtesy of Jawg Maps" target="_blank">&copy; <b>Jawg</b>Maps</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
                     name='Sunny',
                     subdomains='abcd',
                     accessToken='M3WEKah99yGyp261TH3WrLRbMw82fe4LJuPqbtfwTyozuBmz67OzlNPOEwAjnW8c').add_to(mapa_caico)

    # colorir o mapa
    folium.Choropleth(
        geo_data=geojson_arquivo,
        data=dados,
        columns=["id", "Indice"],
        key_on="feature.id",
        # fill_color="GnBu",
        fill_color="YlOrRd",
        nan_fill_color="green",
        nan_fill_opacity=0.4,
        bins=[0, 1.0, 2.0, 4.0, 6.0, 8.0, 10.0, 100],
        legend_name='Indice de Infestação',
        highlight=True,
    ).add_to(mapa_caico)

    # Adicionando a fronteira dos bairros
    def estilo(x): return {"color": "black", "fillOpacity": 0, "weight": 3}

    # desenhando os bairros e add legendas
    folium.GeoJson(geojson_arquivo, style_function=estilo, tooltip=folium.GeoJsonTooltip(
        fields=["name"]), name="Caicó").add_to(mapa_caico)
    # Controle de camadas
    folium.LayerControl(position="topleft").add_to(mapa_caico)
    mapa_caico.add_child(folium.LatLngPopup())

    mapa_caico.save("mapas/mapa_do_ciclo_"+str(ciclo)+".html")

    context = {'map': mapa_caico._repr_html_(), 'ciclo': ciclo}
    return render(request, 'mapcaico.html', context)
