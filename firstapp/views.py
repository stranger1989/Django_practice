from django.shortcuts import render

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'firstapp/post_list.html', {'posts':posts})

