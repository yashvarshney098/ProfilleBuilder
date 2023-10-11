from django.shortcuts import redirect, render
from .models import User
import re
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password



def profile(request,id):
    if request.method=='GET':
        if id is not None:
            user = User.objects.get(id=id)
            return render(request,'app/profile.html',{'user':user})

def extract_instagram_id(url):
    pattern = r"(?:https?:\/\/)?(?:www\.)?instagram\.com\/([A-Za-z0-9_\.]+)"
    match = re.search(pattern, url)
    
    if match:
        return match.group(1)
    else:
        return None
    
def extract_twitter_id(url):
    pattern = r"(?:https?:\/\/)?(?:www\.)?twitter\.com\/([A-Za-z0-9_\.]+)"
    match = re.search(pattern, url)
    
    if match:
        return match.group(1)
    else:
        return None


def register(request):
    if request.method=='GET':
        return render(request,'app/register.html')
    else:
        username, firstname, lastname, phone, gradyear, posprimary, possecondary, instagram, twitter, facebook, school, city, state, ncaa, height, weight, vertical, time40, gpa, actscore, classrank, satscore, url1, url2, sbp1, sbp2, sbp3, sbp4, abp1, abp2, abp3, abp4, s1date, s1event, s1location, s2date, s2event, s2location, s3date, s3event, s3location, coachmessage  =  None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        password=request.POST['password']
        phone = request.POST['phone']
        gradyear = request.POST['gradyear']
        posprimary = request.POST['posprimary']
        possecondary = request.POST['possecondary']
        if request.method == "POST" and 'profileimage' in request.FILES:
                image = request.FILES['profileimage']
        if 'instagram' in request.POST:
            instagram = request.POST['instagram']
            instagram_id = extract_instagram_id(instagram)
        if 'twitter' in request.POST:
            twitter = request.POST['twitter']
            twitter_id = extract_twitter_id(twitter)
        if 'facebook' in request.POST:
            facebook = request.POST['facebook']
        school = request.POST['school']
        city =request.POST['city']
        state = request.POST['state'] 
        if 'ncaa' in request.POST:
            ncaa = request.POST['ncaa']
        height = request.POST['height']
        weight = request.POST['weight']
        vertical =  request.POST['vertical'] if 'vertical' in request.POST else None
        time40 = request.POST['40time']  if '40time' in request.POST else None
        if 'gpa' in request.POST:
            gpa = request.POST['gpa']
        if 'actscore' in request.POST:
            actscore  = request.POST['actscore']
        if 'classrank' in request.POST:          
            classrank = request.POST['classrank']
        if 'satscore' in request.POST:
            satscore = request.POST['satscore']
        if 'url1' in request.POST:
            url1 = request.POST['url1']
            url1 = url1.replace("watch?v=", "embed/")
        if 'url2' in request.POST:
            url2 = request.POST['url2']
            url2 = url2.replace("watch?v=", "embed/")
        if 'sbp1' in request.POST:
            sbp1  =request.POST['sbp1']
        if 'sbp2' in request.POST:
            sbp2 = request.POST['sbp2']
        if 'sbp3' in request.POST:
            sbp3 = request.POST['sbp3']
        if 'sbp4' in request.POST:
            sbp4 = request.POST['sbp4']
        if 'abp1' in request.POST:
            abp1 = request.POST['abp1']
        if 'abp2' in request.POST:
            abp2 = request.POST['abp2']
        if 'abp3' in request.POST:
            abp3 = request.POST['abp3']
        if 'abp4' in request.POST:
            abp4 = request.POST['abp4']
        if 's1date' in request.POST:
            s1date = request.POST['s1date']
        if 's1event' in request.POST:
            s1event = request.POST['s1event']
        if 's1location' in request.POST:
            s1location = request.POST['s1location']
        if 's2date' in request.POST:
            s2date = request.POST['s2date']
        if 's2event' in request.POST:
            s2event = request.POST['s2event']
        if 's2location' in request.POST:
            s2location = request.POST['s2location']
        if 's3date' in request.POST:
            s3date = request.POST['s3date']
        if 's3event' in request.POST:
            s3event = request.POST['s3event']
        if 's3location' in request.POST:
            s3location = request.POST['s3location']
        if 'coachmessage' in request.POST:
            coachmessage = request.POST['coachmessage'] 
        print( username, firstname, lastname, phone, gradyear, posprimary, possecondary, instagram, twitter, facebook, school, city, state, ncaa, height, weight, vertical, time40, gpa, actscore, classrank, satscore, url1, url2, sbp1, sbp2, sbp3, sbp4, abp1, abp2, abp3, abp4, s1date, s1event, s1location, s2date, s2event, s2location, s3date, s3event, s3location, coachmessage  )
        user = User.objects.create(username = username, firstname = firstname,lastname = lastname, phone = phone,profileimage = image, gradyear = gradyear, posprimary = posprimary, possecondary = possecondary, instagram = instagram_id, twitter = twitter_id, facebook = facebook, school = school, city = city, state = state, ncaa = ncaa, height = height, weight = weight, vertical = vertical, time40 = time40, gpa = gpa, actscore = actscore, classrank = classrank, satscore = satscore, url1 = url1, url2 = url2, sbp1 = sbp1, sbp2 = sbp2, sbp3 = sbp3, sbp4 = sbp4, abp1 = abp1, abp2 = abp2, abp3 = abp3, abp4 = abp4, s1date = s1date, s1event = s1event, s1location = s1location, s2date = s2date, s2event = s2event, s2location = s2location, s3date = s3date, s3event = s3event, s3location = s3location, coachmessage = coachmessage)
        user.set_password(password)
        user.save()
        return redirect('login')

def home(request):
    if request.user.is_authenticated:
        return render(request, 'app/index.html', {'id':request.user.id})
    return render(request, 'app/index.html')

def loginView(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password'] 
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            request.session['username'] = username
            request.session.save()
            login(request, user)
            return redirect('/')
    return render(request, 'app/login.html')

def logoutView(req):
    del req.session['username']
    req.session.save()
    logout(req)
    return redirect('/')

def userprofile(req):
    return render(req, 'app/userprofile.html',{'id':req.user.id})



@login_required(login_url="login")
def changepassword(request):
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        print(user.password)
        if check_password(request.POST.get("password"),user.password):
            if request.POST.get("new_password") == request.POST.get("repeat_password"):
                user.set_password(request.POST.get("new_password"))
                user.save()
                return render(request, "app/userprofile.html", {'id':request.user.id,"user": user,"message":"Password Changed Successfully"})
            else:
                return render(request, "app/changepassword.html", {'id':request.user.id,"user": user, "message": "Passwords did not match"})
        else:
            return render(request, "app/changepassword.html", {'id':request.user.id,"user": user, "message": "Old Password did not match"})
    return render(request, "app/changepassword.html", {'id':request.user.id,"user": user})

@login_required(login_url="login")
def editprofile(request):
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        user.firstname = request.POST.get("firstname")
        user.lastname = request.POST.get("lastname")
        user.profileimage = request.FILES['profileimage'] if 'profileimage' in request.FILES else user.profileimage
        user.phone = request.POST.get("phone")
        user.username = request.POST.get("username")
        user.gradyear = request.POST.get("gradyear")
        user.posprimary = request.POST.get("posprimary")
        user.possecondary = request.POST.get("possecondary")
        user.instagram = request.POST.get("instagram")
        user.twitter    = request.POST.get("twitter")
        user.facebook = request.POST.get("facebook")
        user.school = request.POST.get("school")
        user.city = request.POST.get("city")
        user.state = request.POST.get("state")
        user.ncaa = request.POST.get("ncaa")
        user.weight = request.POST.get("weight")
        user.height = request.POST.get("height")
        user.vertical = request.POST.get("vertical")
        user.time40 = request.POST.get("time40")
        user.gpa = request.POST.get("gpa")
        user.actscore = request.POST.get("actscore")
        user.satscore   = request.POST.get("satscore")
        user.classrank = request.POST.get("classrank")
        user.url1  =  request.POST.get("url1")
        user.url2 = request.POST.get("url2")
        user.sbp1 = request.POST.get("sbp1")
        user.sbp2 = request.POST.get("sbp2")
        user.sbp3 = request.POST.get("sbp3")
        user.sbp4 = request.POST.get("sbp4")
        user.abp1 = request.POST.get("abp1")
        user.abp2 = request.POST.get("abp2")
        user.abp3 = request.POST.get("abp3")
        user.abp4 = request.POST.get("abp4")
        user.coachmessage = request.POST.get("coachmessage")
        user.s1date = request.POST.get("s1date")
        user.s1event = request.POST.get("s1event")
        user.s1location = request.POST.get("s1location")
        user.s2date = request.POST.get("s2date")
        user.s2event = request.POST.get("s2event")
        user.s2location = request.POST.get("s2location")
        user.s3date = request.POST.get("s3date")
        user.s3event = request.POST.get("s3event")
        user.s3location = request.POST.get("s3location")
        user.save()
        return render(request, "app/userprofile.html", {"user": user, "message": "Profile Updated Successfully",'id':request.user.id})
    return render(request, "app/editprofile.html", {"user": user , 'id':request.user.id})