from django.utils import timezone
from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

def post_list(request):
    post_list=Post.objects.all().order_by('-id')
    
    return render(request, "blog/post_list.html", 
                  {"post_list" : post_list} 
    )

def post_detail(request,pk) :
    post_detail= get_object_or_404(Post, id=pk)  
    
    return render(request, "blog/post_detail.html", {"post_detail": post_detail}) #두 번째 거는 렌더링할 url. 세 번째 거는 이 페이지에서 사용할 데이터를 지정. 템플릿

def post_write(request):
    if request.method=="POST": 
        form_data=request.POST #딕셔너리로 들어옴
        #이제 저장해보자. 
        if form_data["title"] !="" and form_data["text"] is not None:
            post=Post.objects.create(
                title=form_data["title"],
                text=form_data["text"],
                author=request.user, #로그인 된 유저를 자동반환해줌
                published_date=timezone.now(),
            )
            
            return redirect('post_detail',pk=post.id)
            
    return render(request,"blog/post_write.html")

def user_login(request):
    if request.method == "POST":
        us=request.POST["username"] 
        ps=request.POST["password"] #login에서의 post의 username, password
        user=authenticate(request,username=us,password=ps)
        
        if user is not None: 
            login(request,user) #현재 request 한 브라우저를 로그인시킨다
            return redirect("post_list")
        
    return render(request, "blog/login.html")

def user_logout(request):
    logout(request)
    
    return redirect("post_list")

def user_signup(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        
        user_already = User.objects.filter(username=username)
        
        if username != "" and password !="":
            if len(user_already) == 0 : 
                user=User.objects.create_user(username,"",password) #만든 다음에 variable에 리턴까지 해 줌. 
                login(request,user)
                return redirect("post_list") #urls.py의 html path name에 해당되는 애.
            else :
                None
        
    return render(request, "blog/signup.html")

def post_edit(request,pk):
    post = Post.objects.get(id=pk)
    if request.method=="POST":
        title=request.POST["title"]
        text=request.POST["text"]
        
        post.title=title
        post.text=text
        
        post.save() # 포스트에 저장
        return redirect("post_detail", pk=post.id) 
    
    return render(request, "blog/post_edit.html", {"post" : post})