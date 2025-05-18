import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Nomina
from .serializers import NominaSerializer
from rest_framework import status, generics
from drf_spectacular.utils import extend_schema
from django.http import HttpResponse

# Create your views here.
class NominaListView(APIView):
    def get(self, request):
        nominas = Nomina.objects.all()
        serializer = NominaSerializer(nominas, many=True)
        return Response(serializer.data)


# Post to create a new Nomina register
class NominaCreateView(APIView):
    @extend_schema(request=NominaSerializer, responses=NominaSerializer)
    def post(self, request):
        serializer = NominaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create nomina file to send to the bank
class NominaDetailedFile(APIView):
    def get(self, request):
        try:
            nomina = Nomina.objects.all()

            # Armar el contenido como lineas de texto
            lines = ["\t"]
            separator = "|"
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            for item in nomina:
                row = [
                    item.rnc_empresa.strip(),
                    date,
                    item.codigo_cliente.strip(),
                    item.moneda.strip(),
                    item.cuenta_bancaria_empresa.strip(),
                    item.cuenta_bancaria_empleado.strip(),
                    item.cedula_empleado.strip(),
                    item.monto_pagar.strip(),
                    item.referencia.strip() if item.referencia else "Null"
                ]
                #Concatena todos los elementos del array row en una sola cadena (string) separando cada elemento con el separador
                lines.append(separator.join(row))
            
            Nomina.objects.all().update(fecha_proceso=date)
            file_content = "\n".join(lines)
            
            response = HttpResponse(file_content, content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename="nomina.txt"'
            return response
            
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# Frontend view to render the HTML page
def nomina_frontend(request):
    return render(request, 'nomina/nomina_frontend.html')