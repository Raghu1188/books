from django.shortcuts import render
from .forms import Student
from .models import User
# Create your views here.
def Show_All(request):
  if request.method == 'POST':
    fm = Student(request.POST)
    if fm.is_valid():
      fm.save()
    fm = Student()  
  else:
    fm = Student()
  stud = User.objects.all()    
  return render(request , 'question/showquestion.html',{'form':fm ,'stu':stud})

def update_data(request, id):
 if request.method == 'POST':
  pi = User.objects.get(pk=id)
  fm = Student(request.POST, instance=pi)
  if fm.is_valid():
   fm.save()
 else:
  pi = User.objects.get(pk=id)
  fm = Student(instance=pi)
 return render(request, 'question/updatestudent.html', {'form':fm})
