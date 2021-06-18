from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

import random,math
import re
from seller.otp_code import sendSMS
from .models import Cust_acc, Cust_store
from rest_framework.authtoken.models import Token

def sendotp(request):
    mobile_no =request.POST['mobile']
    phonenumber = str(mobile_no)
    regex = "\w{10}"
    if re.search(regex, phonenumber):
        string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        global otp
        otp = ''
        length = len(string)
        for i in range(6):
            otp += string[math.floor(random.random() * length)]
        mesg = 'please login with this OTP :' + otp
        # smsinfo = sendSMS(mobile_no,mesg)
        # print(smsinfo)
        print(mesg)
        return render(request,'Seller Templates/otp_validation.html',{'data':mobile_no})
    else:
        mobile_info = 'Mobile number should be 10 digits'
        return render(request, 'Seller Templates/login_register.html', {'data':mobile_info })

def check_user(request):
    phone_No = request.POST['phone']
    entered_otp = request.POST['otp']
    if otp == entered_otp:
        return render(request, 'Seller Templates/Account_details.html',{'data':phone_No})
    else:
        msg = 'you entered wrong otp'
        return render(request,'Seller Templates/login_register.html',{'data':msg})





def c_account(request):
    qs=Cust_acc.objects.all()
    lid = [i.id for i in qs]
    try:
        idno=lid[-1]+1
    except IndexError:
        idno =100
    request.session['user_id']=idno
    name = request.POST['name']
    mail = request.POST['mail']
    add = request.POST['add']
    #user = get_user_model().objects.first()
    #tkn = Token.objects.get_or_create(user=user)
    #print(tkn.key)
    tkn = random.randint(100000,999999)
    mobile = request.POST['num']
    if len(mobile)==10:
        phone=mobile
    else:
        if len(mobile)>10:
            p='Number should be 10 digits only'
        else:
            p='Number should be 10 digits'
        return render(request,'Seller Templates/Account_details.html',{'mobile_info':p})

    Cust_acc.objects.create(id=idno,name=name,mobile=phone,email=mail,
                            address=add,token=tkn).save()
    return redirect('crt_str')

# sample login page---- for practice purpose

def logout(request):
    del request.session['user_id']
    return redirect('buyer_seller')

def store(request):
    store_qs = Cust_store.objects.all()
    lid = [i.id for i in store_qs]
    liph = [i.number for i in store_qs]
    try:
        idno = lid[-1] + 1
    except IndexError:
        idno = 1000
    name = request.POST['name']
    num = request.POST['number']
    if len(num) == 10:
        if int(num) not in liph:
            phone = num
        else:
            p = 'your given is already exist'
            return render(request, 'Seller Templates/store.html', {'phonedata': p})
    else:
        p = 'Phone number should be 10 digits,you given {}'.format(len(num))
        return render(request, 'Seller Templates/store.html', {'phonedata': p})

    add = request.POST['add']
    mail = request.POST['mail']
    Cust_store.objects.create(id=idno, name=name, number=phone, mail=mail, address=add, cust_id=(Cust_acc.objects.get(id = request.session['user_id']))).save()

    return redirect('crt_str')


def my_stores(request):
    stores = Cust_store.objects.filter(cust_id_id=request.session['user_id'])
    return render(request, 'Seller Templates/mystores.html', {'store_data': stores})


def find_store(request):
    name = request.POST['store_name']
    try:
        qs = Cust_store.objects.get(name=name.title())
        return render(request, 'Seller Templates/str_details.html', {'data': qs})
    except:
        data = 'given store not exist'
        return render(request, 'Seller Templates/single_store.html',{'data':data})

