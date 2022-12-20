from django.contrib import admin
from django.urls import path
from .views import admission,admissionReport
from .views import admission,Vendor,deleteStudent,updateStudent,Firstclassbasedview,TeacherRead
from .views import admission,GetTeacher
from .views import admission,AddTeacher
from .views import admission,UpdateTeacher
from .views import admission,DeleteTeacher
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('admin/', admin.site.urls),
    path('newadm/',admission),
    path('admReport/',admissionReport),
    path('newvndr/',Vendor),
    path('delete/<int:id>',deleteStudent),
    path('update/<int:id>',updateStudent),
    path('firstcbv/',login_required(Firstclassbasedview.as_view())),
    path('teacherslist/',login_required(TeacherRead.as_view()),name='listteachers'),
    path('getteachersdetails/<int:pk>/',login_required(GetTeacher.as_view())),
    path('insertteacher/',login_required(AddTeacher.as_view())),
    path('updateteacher/<int:pk>/',login_required(UpdateTeacher.as_view())),
    path('deleteteacher/<int:pk>/',login_required(DeleteTeacher.as_view()))

]