from django.shortcuts import render,redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

#Vista Contacto para el Formulario
def contacto(request):
    formulario_contacto=FormularioContacto()
    
    if request.method=="POST":
        formulario_contacto=FormularioContacto(request.POST)
                        
        if formulario_contacto.is_valid():
            
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            
            email=EmailMessage(subject="Mensaje desde Pagina Con Django"
                            ,body="El ususario con nombre {} con correo : {} escribe lo siguiente : \n\n {}".format(nombre,email,contenido)
                            ,from_email=''
                            ,to=['ale.astudillo.1989@gmail.com']
                            ,reply_to=[email])
            
            try:
                email.send()
                
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")


       
    return render(request, "contacto/contacto.html", {'miFormulario':formulario_contacto})