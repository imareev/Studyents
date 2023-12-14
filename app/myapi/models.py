from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models import Count, Sum


class Hero(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    course_description = models.TextField(default="This is the default content.")
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Module(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    number_of_tests = models.IntegerField(null=True, default=0)
    number_of_completed_tests = models.IntegerField(default=0)

    def update_number_of_tests(self):
        test_count = Test.objects.filter(lesson__module=self).count()
        self.number_of_tests = test_count
        self.save()
    def __str__(self):
        return self.title


class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    theory = models.TextField(default="This is the default content.")
    video = models.FileField(
        null=True,
        blank=True,
        upload_to='theory_files/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )
    file = models.FileField(
        null=True,
        blank=True,
        upload_to='theory_files/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])]
    )

    def get_tests(self):
        # Выполните запрос к модели Test, связанный с текущим уроком
        tests = Test.objects.filter(lesson=self)
        return tests
    def __str__(self):
        return self.title



class Test(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    number_of_tasks = models.IntegerField(default=0)
    number_of_completed_tasks = models.IntegerField(default=0)

    def update_number_of_tasks(self):
        task_count = Task.objects.filter(test=self).count()
        self.number_of_tasks = task_count
        self.save()
    def __str__(self):
        return self.title


class Task(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    def __str__(self):
        return self.question

class Answer(models.Model):
    correct = models.BooleanField(default=False)
    id = models.AutoField(primary_key=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    def __str__(self):
        return self.answer
