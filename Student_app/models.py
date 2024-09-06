from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=50, unique=True)
    section = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.section if self.section else ''}"

class Student(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100, null=True)
    roll_no = models.IntegerField(unique=True)
    standard = models.ForeignKey(Class, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to="student-photos", null=True)

    def __str__(self):
        return f"{self.name} ({self.roll_no})"

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Exams(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='marks')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    max_marks = models.DecimalField(max_digits=5, decimal_places=2)
    exams = models.ForeignKey(Exams, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}: {self.marks_obtained}/{self.max_marks}"

