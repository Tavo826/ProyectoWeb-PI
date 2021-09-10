#Creando la variable global
def importe_total_carro(request):
    total = 0
    #if request.user.is_authenticated: (Aún no se crea autenticación)
    for key, value in request.session['carro'].items():
        total += float(value['precio'])
    
    return {'Importe_total_carro': total}