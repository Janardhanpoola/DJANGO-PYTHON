from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

from .resources import StudentResource

from .models import Student

from tablib import Dataset



def export(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response


def upload(request):
    if request.method == 'POST':
        student = Student()
        dataset = Dataset()
        file = request.FILES['myfile']

        imported_data = dataset.load(file.read(),format='xlsx')
        print(imported_data)
        for data in imported_data:
        	value = Student(
               data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[11],
        		)
        	value.save()       
        

    return render(request, 'upload.html')


def success(request):
    context={}
    return render(request,'success.html',context)