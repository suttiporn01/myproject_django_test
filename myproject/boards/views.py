from django.shortcuts import render,redirect
from django.template import loader  
# Create your views here.
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User,auth
from django.contrib import messages
#from django.contrib.auth import authenticate

def home(request):
    return HttpResponse('Hello, World!')

def hello(request):
        return render(request,'hello.html')
def page1(request):
        return render(request,'page1.html')
def home2(request):
    return HttpResponse('Hello home2')
def hello2(request):
    text="<h1>Hello World</h1>"
    return HttpResponse(text)

#ส่งค่า layout
def index2(request):
    tags=['น้ำตก','ธรรมชาติ','หน้าฝน','mountain']
    rating=5
    return render(request,'index.html',{'name':'บทความท่องเที่ยวภาคเหนือ',
    'anther':'Suttiporn poominat',
    'tags':tags,
    'rating':rating
    })
def hello3(request):  
   template = loader.get_template('hello.html')
   return HttpResponse(template.render()) 

def createForm(request):
    return render(request,'form.html')

#ส่งค่า GET 
def addBlog1(request):
    name=request.GET['name']
    description=request.GET['description']
    return render(request,'result.html',{
        'name':name,
        'description' : description

    })
#ส่งค่า post
#เพิ่ม {% csrf_token %} ใน form
def addBlog2(request):
    name=request.POST['name']
    description=request.POST['description']
    return render(request,'result.html',{
        'name':name,
        'description' : description

    })


#เเสดงข้อมูลหน้าเเรก
def index(request):
    #Query data
    data=Post.objects.all()
    #return HttpResponse('Hello home2')
    return render(request,'index.html',{'posts':data})

#ลงทะเบียน
def addBlog(request):
    username=request.POST['username']
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    email=request.POST['email']
    password=request.POST['password']
    confirmpassword=request.POST['confirmpassword']
    
    if password==confirmpassword :
        if User.objects.filter(username=username).exists():
            #print("username นี้มีคนใช้งานเเล้ว")
            messages.info(request,'UserName นี้มีคนใช้เเล้วครับ')
            return redirect('/createForm')
        elif User.objects.filter(email=email).exists():
            #print("Email นี้เคยลงทะเบียนเเล้ว")
            #return HttpResponse("Email นี้เคยลงทะเบียนเเล้ว") 
            messages.info(request,'Email นี้เคยลงทะเบียนเเล้ว')
            return redirect('/createForm')
        else :
            user=User.objects.create_user(
        username=username,
        password=password,
        email=email,
        first_name=firstname,
        last_name=lastname,
        )

        user.save()
        return redirect('/createForm')
    
    else :
        messages.info(request,'password มันผิดโว้ยยย!!!!')
        return redirect('/addForm')
       
      #return HttpResponse("") 


def loginform(request):
       return render(request,'login.html')
def login(request):
    
    username=request.POST['username']
    password=request.POST['password']
    user=auth.authenticate(username=username, password=password)
    print(username)

    if user is not None :
        auth.login(request,user)
        return redirect('/')
        
    else :
        print(username)
        messages.info(request,'ไม่พบข้อมูล')
        return redirect('/loginform')
    
    #return render(request,'index.html')

