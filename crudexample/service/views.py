from django.shortcuts import render, redirect  
from service.forms import ServiceForm  
from service.models import Service  
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = ServiceForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = ServiceForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    services = Service.objects.all()  
    return render(request,"show.html",{'services':services})  
def edit(request, id):  
    service = Service.objects.get(id=id)  
    return render(request,'edit.html', {'service':service})  
def update(request, id):  
    service = Service.objects.get(id=id)  
    form = ServiceForm(request.POST, instance = service)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'service': service})  
def destroy(request, id):  
    service = Service.objects.get(id=id)  
    service.delete()  
    return redirect("/show")  