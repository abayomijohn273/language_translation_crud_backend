from translatorcrud import serialize
from translatorcrud.models import TranslationsModel
from translatorcrud.serialize import TranslationsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class TranslationsTable(APIView):
    # Get all translation data
    def get(self, request):
        translationsObject=TranslationsModel.objects.all()
        translationsSerializeObject=TranslationsSerializer(translationsObject,many=True)
        return Response(translationsSerializeObject.data)

    # Create new translation
    def post(self, request):
        serializeObject=TranslationsSerializer(data=request.data)
        if serializeObject.is_valid():
            serializeObject.save()
            return Response(serializeObject.data, status=200)
        return Response(serializeObject.errors, status=400)

class TranslationsDetails(APIView):
    # Get single translation
    def get(self, request, pk):
        try:
            translationSingleObject=TranslationsModel.objects.get(pk=pk)
        except:
            return Response("Not Found in Database", status=400)

        serializeObject=TranslationsSerializer(translationSingleObject)
        return Response(serializeObject.data, status=200)

class TranslationsUpdate(APIView):
    # Update translation
    def put(self, request, pk):
        try:
            translationsObject=TranslationsModel.objects.get(pk=pk)
        except:
            return Response("Not Found in Database", status=400)
            
        serializeObject=TranslationsSerializer(translationsObject, data=request.data)
        if serializeObject.is_valid():
            serializeObject.save()
            return Response(serializeObject.data, status=200)
        return Response(serializeObject.errors)

class TranslationsDelete(APIView):
    # Delete translation
    def delete(self, request, pk):
        try:
            translationsObject=TranslationsModel.objects.get(pk=pk)
        except:
            return Response("Not Found in Database", status=400)
            
        translationsObject.delete()
        return Response("Traslation Deleted Successfully", status=200)