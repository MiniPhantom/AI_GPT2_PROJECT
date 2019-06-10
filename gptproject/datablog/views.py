from django.shortcuts import render
from .src import interactive_conditional_samples

def home(request):
    return render(request, 'home.html' )

def new(request):
    return render(request, 'new.html')

def result(request):
    if request.method == 'POST':
        initial = request.POST['topic']
        text = interactive_conditional_samples.interact_model(initialize_text = initial)
    return render(request, 'result.html' , {'text': text , 'initial' : initial})    

def about(request):
    return render(request, 'about.html')
    
# def create(request):
#     blog = Blog()
#     blog.author = request.user
#     blog.title = request.POST['title']
#     blog.body = request.POST['body']
#     blog.pub_date = timezone.datetime.now()
#     blog.save()
#     return redirect('/blog/'+str(blog.id)) 