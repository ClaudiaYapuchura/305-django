from django.shortcuts import render

# Create your views here.

def mostrar_index(request):
    return render(request, 'index.html')

def mostrar_pombos(request):
    return render(request,'pombos.html')

def mostrar_rolezinho(request):
    roles = ['bailão', 'Sopping União', 'Quermesse da Paróquia de São Jõao', 'Calçadão de Osasco', 'SESC', 'Risca Faca']
    bairro = 'Rochdale'
    return render(request, 'rolezinho.html', {'roles':roles, 'bairro':bairro})

def mostrar_cachorroquente(request):
    
    
