from django.shortcuts import render, redirect
from .models import Course, Description, Comment

# Create your views here.
def display(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'first_app/index.html', context)
def submit(request):
    if request.method == "POST":
        course = Course.objects.create(name=request.POST['name'])
        Description.objects.create(course=course, description=request.POST['description'])
    return redirect('/')
def destroy(request, id):
    context = {
        'course': Course.objects.get(id=id)
    }
    return render(request, "first_app/destroy.html", context)
def delete(request):
    if request.method == "POST":
        Course.objects.get(id=request.POST['id']).delete()
    return redirect('/')
def comments(request, id):
    context = {
        'course': Course.objects.get(id=id),
        'comments' : Comment.objects.all(),
    }
    print Comment.objects.all()
    print "***************************"
    return render(request, 'first_app/comments.html', context)
def process2(request, id):
    print request.POST['comment']
    print "HEY WE ARE HERE"
    Comment.objects.create(comment=request.POST['comment'], course=Course.objects.get(id=id))
    id = id
    return redirect('/comments/{}'.format(id))
