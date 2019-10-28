from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,CreateView
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from gram.forms import  UserUpdateForm,ProfileUpdateForm

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']



class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    success_url = '/'
    fields =['caption', 'image_name' ,'image']

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super ().form_valid(form)


# class UserProjectListView(ListView):
#     model = Post
#     template_name='profile.html'
#     context_object_name ='posts'
#     ordering = ['-date_posted']


#     def get_queryset(self):
#         user = get_object_or_404(User, username = self.kwargs.get('username'))
        
#         return Post.objects.filter(profile=user.profile).order_by('-date_posted')



@login_required(login_url='/login/')
def likePost(request,image_id):
  image = Post.objects.get(pk = image_id)
  is_liked = False
  if image.likes.filter(id = request.user.id).exists():
      image.likes.remove(request.user)
      is_liked = False
  else:
      image.likes.add(request.user)
      is_liked = True
  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


def profile(request):
    posts = Post.objects.filter(profile=request.user.profile).all()
    context = {
        'posts':posts
    }
    return render(request, 'profile.html',context)


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'home.html', context) 


@login_required
def profile_update(request):
    posts = Post.objects.all()
    profiles = Profile.objects.all()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance = request.user)
        
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance = request.user.profile)    
        if u_form.is_valid and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context={
        'u_form':u_form,
        'p_form':p_form,
        'profiles':profiles,
        'posts':posts,
    }
    return render(request, 'profile-update.html',context)