from django.shortcuts import render

from admissions.models import Student
from admissions.forms import StudentModelForm
from admissions.forms import VendorForm
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from admissions.models import Teacher
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.
@login_required
def homepage(request):
    return render(request, 'index.html')
def logoutUser(request):
    return render(request,'logout.html')

@login_required
def admission(request):
    form = StudentModelForm
    studentform = {'form': form}

    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
        return homepage(request)
    return render(request, 'admissions/admission.html', studentform)
    # return HttpResponse("<h1>this is add admission view<h1><h2>welcome to school app<h2>")

@login_required
@permission_required('admissions.view_student')
def admissionReport(request):
    result = Student.objects.all()
    Students = {'allstudents': result}
    return render(request, 'admissions/admissionReport.html', Students)
    # return HttpResponse("this is admissions report view")

@login_required
def Vendor(request):
    form = VendorForm
    vform = {'form': form}

    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            a = form.cleaned_data['address']
            c = form.cleaned_data['contact']
            i = form.cleaned_data['item']
            response = render(request,'index.html')
            # response.set_cookie('name',n)
            # response.set_cookie('address',a)
            # response.set_cookie('contact',c)
            # response.set_cookie('item',i)
            request.session['name']=n
            request.session['address']=a
            request.session['contact']=c
            request.session['item']=i

        return response
    return render(request, 'admissions/Vendor.html', vform)

@login_required
@permission_required('admissions.delete_student')
def deleteStudent(request, id):
    s = Student.objects.get(id=id)
    s.delete()
    return admissionReport(request)

@login_required
@permission_required('admissions.change_student')#add delete change view
def updateStudent(request, id):
    s = Student.objects.get(id=id)
    form = StudentModelForm(instance=s)
    dict = {'form':form}
    if request.method == 'POST':
        form = StudentModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
        return admissionReport(request)
    return render(request, 'admissions/update.admission.html/', dict)
# class based view

class Firstclassbasedview(View):
    def get(self,request):
        return HttpResponse("<h1>Hello....CHEVURU Penchalakumar<h1>")

class TeacherRead(ListView):
    model=Teacher

class GetTeacher(DetailView):
    model=Teacher

class AddTeacher(CreateView):
    model = Teacher
    fields = ('Name','subject','exp','contact')

class UpdateTeacher(UpdateView):
    model=Teacher
    fields=('Name','contact')

class DeleteTeacher(DeleteView):
    model=Teacher
    success_url = reverse_lazy('listteachers')



