from django.shortcuts import render
from .models import Course, Question, Choice, Submission

def exam(request):
    course = Course.objects.first()

    if not course:
        return render(request, "exam.html", {"questions": []})

    questions = Question.objects.filter(course=course)

    return render(request, "exam.html", {
        "questions": questions,
        "course": course
    })


def submit(request):
    if request.method == "POST":
        score = 0
        total = 0

        course = Course.objects.first()
        questions = Question.objects.filter(course=course)

        for q in questions:
            total += 1
            selected = request.POST.get(str(q.id))

            if selected:
                try:
                    choice = Choice.objects.get(id=selected)
                    if choice.is_correct:
                        score += 1
                except Choice.DoesNotExist:
                    pass

        submission = Submission.objects.create(
            user="student",
            score=score,
            total=total
        )

        return render(request, "result.html", {
            "score": score,
            "total": total,
            "submission": submission
        })


def show_exam_result(request):
    submission = Submission.objects.last()

    course = Course.objects.first()
    questions = Question.objects.filter(course=course)

    return render(request, "result.html", {
        "score": submission.score,
        "total": submission.total,
        "result": submission,
        "questions": questions,
    })