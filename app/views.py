from tokenize import Name
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
# Create your views here.


def index(request):
    return render(request,"app/index3.html")

def about(request):
    return render(request,"app/about.html")

def insert(request):
    name2= request.POST.get("name",False)
    Emaill = request.POST.get("emailname",False)
    Phone = request.POST.get("phonenumber",False)
    Mssg = request.POST.get("Message",False)

    #data insert in mysql
    user = contact.objects.create(Name1=name2,
                                    Email=Emaill,
                                    Phone_no=Phone,
                                    Msg=Mssg)
    
    return HttpResponse("Data Insert Successfully......")

def insert_register(request):
    r_name=request.POST.get("rname",False)
    r_phone=request.POST.get("rphone",False)
    r_password=request.POST.get("rpassword",False)
    r_cpassword=request.POST.get("rcpassword",False)
    r_email=request.POST.get("remail",False)
    r_address=request.POST.get("raddress",False)

    meta_data = register.objects.filter(reg_email=r_email)

    if meta_data:
        mssg = "Email Already Register"
        return render(request,"app/register_form.html",{'msg1':mssg})
    else:
        if r_password==r_cpassword:
            newuser = register.objects.create(reg_name=r_name,
                                        reg_email=r_email,
                                        reg_phone=r_phone,
                                        reg_address=r_address,
                                        reg_password=r_password)
            mssg1= "Successfully Register."
            return render(request,"app/register_form.html",{'msg1':mssg1})
    
        else:
            mssg = "Both Password are not same."
            return render(request,"app/register_form.html",{'msg1':mssg})
    

def login(request):
    return render(request,'app/login.html')

def login_user(request):
    try:
        user_name = request.POST.get("username",False)
        password = request.POST.get("password",False)

        user = register.objects.get(reg_email=user_name)

    
        if user:
            if user.reg_password == password:
                # return HttpResponse("Login Successfully")
                user_name = user.reg_name
                return render(request,'app/index3.html',{'name':user_name})
            else:
                mssg = "Password Invalid."
                return render(request,"app/login.html",{'msg1':mssg})
        else:
            mssg="User is does not exist"
            return render(request,"app/login.html",{'msg1':mssg})
    except Exception as e:
        mssg="User is does not exist"
        return render(request,"app/login.html",{'msg1':mssg})       


def image_upload_show(request): #render image uplading page
    return render(request,"app/image.html")

def image_insert(request): #insert data in database
    
    image_name = request.POST.get("imgname",False)
    image = request.FILES.get("imgupload",False)
    
    user_image_data = Imgsdata.objects.create(Imagename=image_name,
                                                Image=image)

    return redirect("show_image")
    
def imagefetch(request):
    all_img = Imgsdata.objects.all()
    return render(request,"app/show_image.html",{'img':all_img})




    
 







    