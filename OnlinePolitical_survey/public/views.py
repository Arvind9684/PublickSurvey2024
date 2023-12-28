from django.shortcuts import render,HttpResponse,redirect
from public.utils import utils_change,get_location,images_list
from googletrans import Translator
from .models import contact_detail,chat_detail,public_votting
from django.db.models import Sum


def index(request):
    contact_detail.objects.all().delete()
    chat_detail.objects.all().delete()
    public_votting.objects.all().delete()
    content_data=utils_change('hi')
    return render(request,'index.html',{'content_data':content_data})
def change_language(request,option_id):
    
    if option_id==2:
        dest_lang='en'
    else:
        dest_lang='hi'
    content_data=utils_change(dest_lang)
    return render(request,'index.html',{'content_data':content_data})
def reg_mobile(request):
    image_list=images_list()
    if request.method=='POST':
        mobile=request.POST['mobile']
        location_data=get_location()
        try:
            check_mobile=contact_detail.objects.get(mobile=mobile)
            yesMobile='yesMobile'
            request.session['mobile']=mobile
            return render(request,'index.html',{'yesMobile':mobile,'image_list':image_list})
        except:
            ins=contact_detail(mobile=mobile,country=location_data['Country'],city=location_data['City'],date=location_data['date'],time=location_data['time'])
            ins.save()
            request.session['mobile']=mobile
            return render(request,'index.html',{'yesMobile':mobile,'image_list':image_list})
    mobile=request.session['mobile']
    return render(request,'index.html',{'yesMobile':mobile,'image_list':image_list})
            
def logout(request):
    request.session.clear()
    content_data=utils_change('hi')
    return render(request,'index.html',{'content_data':content_data})
def insertchat(request):
    if request.method=="GET":
        content_data=utils_change('hi')
        return render(request,'index.html',{'content_data':content_data})
    else:
        image_list=images_list()
        location_data=get_location()
        mobile=request.session['mobile']
        contact_instance, created = contact_detail.objects.get_or_create(mobile=mobile)
        chat=request.POST['chat']
        ins=chat_detail(mobile=contact_instance,country=location_data['Country'],city=location_data['City'],Chat=chat,Latitude=location_data['Latitude'],Longitude=location_data['Longitude'],date=location_data['date'],time=location_data['time'])
        ins.save()
        chat_data=chat_detail.objects.all()
        return render(request,'index.html',{'chat_data':chat_data,'image_list':image_list,'yesMobile':mobile})
def votting(request):
    mobile=request.session['mobile']
    get_name=request.GET['text']
    party_name=get_name.split('\\')[-1]
    party_name=party_name.split('.')[0]
    location_data=get_location()
    contact_instance, created = contact_detail.objects.get_or_create(mobile=mobile)
    ins=public_votting(mobile=contact_instance,country=location_data['Country'],city=location_data['City'],party_name=party_name,Latitude=location_data['Latitude'],Longitude=location_data['Longitude'],date=location_data['date'],time=location_data['time'])
    ins.save()
    return redirect('reg_mobile')   
def show_result(request):
    mobile=request.session['mobile']
    image_list=images_list()
    grouped_data = public_votting.objects.values('party_name').annotate(total_votes=Sum('result'))
    chat_data=chat_detail.objects.all()
    if len(grouped_data)==0:
        error="Data Not Found"
        return render(request,'index.html',{'image_list':image_list,'chat_data':chat_data,'yesMobile':mobile,'error':error})
    else:
        return render(request, 'index.html', {'chat_data':chat_data,'grouped_data': grouped_data,'yesMobile':mobile})
    