from django.shortcuts import render
from .models import Blogs

def search(request):
  query = request.GET.get('q')
  if query:
    results = Blogs.objects.filter(title__icontains=query) | Blogs.objects.filter(content__icontains=query)
  else:
    results = Blogs.objects.all()
  return render(request, 'search_bar.html', {'results': results, 'query': query})
