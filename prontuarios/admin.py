from django.contrib import admin
from django.utils.html import format_html
from .models import Prontuario, ImagemProntuario


class ImagemProntuarioInline(admin.TabularInline):
    model = ImagemProntuario
    extra = 1
    readonly_fields = ['imagem_preview']
    
    def imagem_preview(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" width="150" height="auto" />', obj.imagem.url)
        return "Sem imagem"
    
    imagem_preview.short_description = 'Visualização'


@admin.register(Prontuario)
class ProntuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'paciente', 'dentista', 'data', 'qtd_imagens']
    list_filter = ['dentista', 'data']
    search_fields = ['paciente__nome', 'dentista__nome', 'anotacoes']
    date_hierarchy = 'data'
    inlines = [ImagemProntuarioInline]
    
    def qtd_imagens(self, obj):
        return obj.imagens.count()
    
    qtd_imagens.short_description = 'Imagens'


@admin.register(ImagemProntuario)
class ImagemProntuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'prontuario', 'descricao', 'data_upload', 'imagem_thumbnail']
    list_filter = ['data_upload']
    search_fields = ['prontuario__paciente__nome', 'descricao']
    
    def imagem_thumbnail(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" width="100" height="auto" />', obj.imagem.url)
        return "Sem imagem"
    
    imagem_thumbnail.short_description = 'Imagem'
