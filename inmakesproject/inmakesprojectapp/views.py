
from .forms import ReviewForm
from .forms import MovieForm
from .models import Category,Movie,Review
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator,EmptyPage,InvalidPage






# Create your views here.
def allMovieCat(request,c_slug=None):
    c_page=None
    movies_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        movies_list=Movie.objects.all().filter(category=c_page)

    else:
        movies_list=Movie.objects.all().filter()
    paginator=Paginator(movies_list,12)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        movies=paginator.page(page)
    except(EmptyPage,InvalidPage):
        movies=paginator.page(paginator.num_pages)

    return render(request,'category.html',{'category':c_page,'movies':movies})

def movieDetail(request,c_slug,movie_slug):
    try:
        movie=Movie.objects.get(category__slug=c_slug,slug=movie_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'movie':movie})

def add_movie(request):
    if request.method=="POST":
        title=request.POST.get('title',)
        slug=request.POST.get('slug',)
        description=request.POST.get('description',)
        category=request.POST.get('category',)
        poster=request.FILES['img']
        releasedate = request.POST.get('releasedate', )
        actors=request.POST.get('actors',)
        link=request.POST.get('link',)
        added_by=request.POST.get('added_by',)
        movie=Movie(title=title,slug=slug,description=description,category=category,poster=poster,releasedate=releasedate,actors=actors,link=link,added_by=added_by)
        movie.save()
        return redirect('/')
    return render(request,'add.html')





def update(request,movie_slug):
    movie=Movie.objects.get(id=movie_slug)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,movie_slug):
    if request.method=='POST':
       movie=Movie.objects.get(id=movie_slug)
       movie.delete()
       return redirect('/')
    return render(request,'delete.html')



def movie_review(request,title_id):
    title= get_object_or_404(Movie,pk=title_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.title =title
            review.save()
            return redirect('inmakesprojectapp:movie_review',title_id=title.id)

    else:
        form = ReviewForm()
    reviews = Review.objects.all()
    return render(request, 'review_page.html', {'movie':title, 'form': form, 'reviews': reviews})


def demo(request,c_slug):
    obj = Category.objects.all()
    return render(request, "category.html", {'result': obj})


def user_movie(request):
    user_movies = Movie.objects.filter(added_by=request.user)
    return render(request, 'user_movie.html', {'user_movies': user_movies})



