from rest_framework import serializers
from .models import Prontuario, ImagemProntuario


class ImagemProntuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagemProntuario
        fields = ['id', 'imagem', 'descricao', 'data_upload']


class ProntuarioSerializer(serializers.ModelSerializer):
    paciente_nome = serializers.CharField(source='paciente.nome', read_only=True)
    dentista_nome = serializers.CharField(source='dentista.nome', read_only=True)
    imagens = ImagemProntuarioSerializer(many=True, read_only=True)
    imagens_upload = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )
    
    class Meta:
        model = Prontuario
        fields = ['id', 'paciente', 'dentista', 'data', 'anotacoes', 
                  'paciente_nome', 'dentista_nome', 'imagens', 'imagens_upload']
    
    def create(self, validated_data):
        imagens_data = validated_data.pop('imagens_upload', None)
        prontuario = Prontuario.objects.create(**validated_data)
        
        if imagens_data:
            for imagem in imagens_data:
                ImagemProntuario.objects.create(
                    prontuario=prontuario,
                    imagem=imagem
                )
        
        return prontuario
    
    def update(self, instance, validated_data):
        imagens_data = validated_data.pop('imagens_upload', None)
        
        #atualiza campos do prontuário
        instance.paciente = validated_data.get('paciente', instance.paciente)
        instance.dentista = validated_data.get('dentista', instance.dentista)
        instance.anotacoes = validated_data.get('anotacoes', instance.anotacoes)
        instance.save()
        
        #adiciona novas imagens, se fornecidas
        if imagens_data:
            for imagem in imagens_data:
                ImagemProntuario.objects.create(
                    prontuario=instance,
                    imagem=imagem
                )
        
        return instance