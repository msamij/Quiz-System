from django.shortcuts import render, redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Question, Student, StudentAnswer


@ensure_csrf_cookie
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        batch_name = request.POST.get('batch_name')
        batch_time = request.POST.get('batch_time')

        student = Student.objects.create(
            name=name,
            batch_name=batch_name,
            batch_time=batch_time
        )
        return redirect('quiz_form', student_id=student.id)

    return render(request, 'quiz/register.html')


@ensure_csrf_cookie
def quiz_form(request, student_id):
    if request.method == 'POST':
        student = Student.objects.get(id=student_id)
        for key, value in request.POST.items():
            if key.startswith('q'):
                question_id = key[1:]
                choice_value = value
                question = Question.objects.get(id=question_id)

                StudentAnswer.objects.create(
                    student=student,
                    question=question,
                    choice=choice_value
                )

        return render(request, 'quiz/thankyou.html')
    questions = Question.objects.all().filter(id__gte=13, id__lte=28)
    return render(request, 'quiz/quiz_form_new.html', {'questions': questions})
