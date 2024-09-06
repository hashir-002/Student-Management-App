from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import *


# Create your views here.
def home(request):
    return render(request, 'home.html')

def All_Students(request):
    queryset = Student.objects.all() #retriving data
    context = {'students': queryset} #sending data
    return render(request, 'all_students.html',context)

def student_details(request, id):
    queryset = Student.objects.get(id = id)  
    context = {'students': queryset} #sending data

    return render(request, 'student_detail.html', context)

def marks_details(request, student_id, exam_id):
    exam = get_object_or_404(Exams, id = exam_id)   
    student = get_object_or_404(Student ,id=student_id)
    marks = Marks.objects.filter(student=student, exams = exam)
    return render(request, 'marks.html', {'student': student, 'marks': marks, 'exam': exam})

def add_marks(request):
    if request.method == "POST":

        data = request.POST
        roll_no = data.get('roll_no')
        subject_id = data.get('subject_id')
        marks_obtained = data.get('marks_obtained')
        max_marks = data.get('max_marks')
        exam_id = data.get('exam_id')

        student =get_object_or_404(Student, roll_no = roll_no)
        subject =get_object_or_404(Subject, id = subject_id)
        exams = get_object_or_404(Exams, id= exam_id)

        Marks.objects.create(
            student = student,
            subject = subject,
            marks_obtained =marks_obtained,
            max_marks = max_marks,
            exams = exams
        )

        return HttpResponse('Marks added successfully')
    
    subjects = Subject.objects.all()
    exams = Exams.objects.all()
    context = {
        'subjects': subjects,
        'exams': exams
    }
    return render(request, 'add_marks.html', context)

def search(request):
    if request.method == 'POST':
        data = request.POST
        roll_no = data.get('roll_no')
        exam = data.get('exams')
        student = get_object_or_404(Student, roll_no = roll_no)
        # exam = get_object_or_404(Exams)
        return redirect('select_exam', id = student.id)
    return render(request, 'result.html')

def select_exam(request, id):
    queryset = Student.objects.get(id = id)
    context = {'student': queryset}
    return render(request, 'exam.html', context)