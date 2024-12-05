from django.shortcuts import render

def inicio(request):
    # Esta lista es para guardar cuántos días tiene cada mes (No consideramos años bisiestos)
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Aquí están los nombres de los meses, para que no se vean solo números en la gráfica
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
             'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    
    # Esto junta los datos para mandarlos al HTML y usarlos en las gráficas
    contexto = {
        'dias_por_mes': dias_por_mes,
        'meses': meses,
    }
    # Esto carga la página HTML con los datos de arriba
    return render(request, 'vistas_html/inicio.html', contexto)
