from django.urls import path
from .import views

app_name='MetaModel'
urlpatterns = [
    
    path('home',views.home,name='home'),
    path('',views.home,name='home'),

    path('general/',views.general,name='general'),      
    path('metahealth/',views.metahealth,name='metahealth'),
    path('marketing/',views.marketing,name='marketing'),

    path('object/',views.object,name='object'),

    path('nft_a/',views.nft_a,name='nft_a'),
    path('nft_b/',views.nft_b,name='nft_b'),
    path('nft_c/',views.nft_c,name='nft_c'),

    path('map/',views.map,name='map'),
    path('3d/',views.three_d,name='three_d'),
    path('meta/',views.meta,name='meta'),

    path('chart_a/',views.chart_a,name='chart_a'),
    path('chart_b/',views.chart_b,name='chart_b'),
    path('chart_c/',views.chart_c,name='chart_c'),
    
     path('white paper/',views.white_paper,name='white_paper'),
]


