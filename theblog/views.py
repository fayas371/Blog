
from django.shortcuts import render,get_object_or_404,HttpResponseRedirect

from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import Post,Category
from .forms import PostForm,EditForm
from django.urls import reverse_lazy,reverse
from bs4 import BeautifulSoup
# Create your views here.
def LikeView(request,pk):
    post=get_object_or_404(Post,id=request.POST.get('post_id'))
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('article-detail',args=[str(pk)]))



class HomeView(ListView):
    model = Post
    template_name='home.html'
    ordering=['-id']
    context_object_name='object_list'

    def get_context_data(self, *args,**kwargs):
        cat_menu=Category.objects.all()
        context=super(HomeView,self).get_context_data(*args,**kwargs)
        context["cat_menu"]=cat_menu
        posts = context['object_list']
        for post in posts:
            post.first_image_url = post.get_first_image_url()
            post.total_likes = post.likes.count()


        return context


def CategoryView(request,cats):

    category_posts = Post.objects.filter(category=cats.replace('-', ' '))

    for post in category_posts:
            post.first_image_url = post.get_first_image_url()
        

    return render(request,'categories.html',{'category_posts':category_posts})
    

class ArticleDetailView(DetailView):
    model=Post
    template_name='article_details.html'

    def get_context_data(self, *args,**kwargs):
        cat_menu=Category.objects.all()
        context=super(ArticleDetailView,self).get_context_data(*args,**kwargs)

        stuff=get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes=stuff.total_likes()
        liked=False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True

        context["cat_menu"]=cat_menu
        context["total_likes"]=total_likes
        context["liked"]=liked

        return context


class AddPostView(CreateView):
    model=Post
    
    form_class=PostForm
    template_name='add_post.html'

    def form_valid(self, form):
        # Set the author field to the currently logged-in user before saving the form data
        form.instance.author = self.request.user
        return super().form_valid(form)
    
def CategoryListView(request):
    cat_menu_list=Category.objects.all()
    return render(request,'category_list.html',{'cat_menu_list':cat_menu_list})


class AddCategory(CreateView):
    model=Category
    template_name='add_category.html'
    fields='__all__'



class EditPost(UpdateView):
    model=Post
    template_name='update_post.html'
    form_class=EditForm


class DeletePost(DeleteView):
    model=Post
    template_name='delete_post.html'
    success_url=reverse_lazy('home')

class AllPostView(ListView):
    model = Post
    template_name='posts.html'
    ordering=['-id']
    context_object_name='object_list'

    def get_context_data(self, *args,**kwargs):
        cat_menu=Category.objects.all()
        context=super(AllPostView,self).get_context_data(*args,**kwargs)
        context["cat_menu"]=cat_menu
        posts = context['object_list']
        for post in posts:
            post.first_image_url = post.get_first_image_url()
        return context
