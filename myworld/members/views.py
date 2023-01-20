from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import redirect
from .models import*
import bcrypt
from django.contrib import messages
from django.db.models import Q
from django.contrib import messages
import time, datetime

CTM = RegistetUser()
        
def CountPd():
  temp=Cart.objects.filter(idctm=CTM.id)
  Dem=0
  for x in temp:
    Dem+=1
  return Dem

def get_values_from(table,attribute):
      values = list(set(table.objects.values_list(attribute)))
      return list(map(lambda x: x[0], values))
      
def SearchPd(a):
      check=Product.objects.filter(
        Q(namepd__icontains=a) |
        Q(typepd__icontains=a)
        )
      typeid=set()
      for x in check:
            typeid.add(x.typepd)
      context = {
        'title': 'home',
        'loaisp': typeid,
        'pd': check,
        'sigin':CTM,
        'Count':CountPd
      }
      return context
      
def home(request):
  template = loader.get_template(f'home.html')

  typepd = get_values_from(Product,'typepd')
  home_pd = []
  for type in typepd:
    home_pd += Product.objects.filter(typepd=type)[:5]

  context = {
    'title': 'home',
    'loaisp': typepd,
    'pd': home_pd,
    'sigin':CTM,
    'Count':CountPd,
  }
  if request.method=="GET":
    if request.GET.get('Search') != None:
      Search=request.GET.get('Search')
      context= SearchPd(Search)
  return HttpResponse(template.render(context, request))

def cart(request):
  total=0
  template = loader.get_template('cart.html')
  temp=Cart.objects.filter(idctm=CTM.id)
  for x in temp:
    a=x.idpd.price
    a=a.replace(".","")
    total=(total+int(a)*int(x.amount))
  context = {
    'title': 'cart',
    'cart': temp,
    'sigin':CTM,
    'Toal':int(total),
    'Count':CountPd
  }
  if request.method=="GET":
        if request.GET.get('Search') != None:
          Search=request.GET.get('Search')
          context= SearchPd(Search)
          template = loader.get_template(f'home.html') 
  return HttpResponse(template.render(context, request))

def deleteCart(request, idpd):
  Cart.objects.get(idctm=CTM.id, idpd=idpd[-3:-1]).delete()
  return HttpResponseRedirect(reverse(cart))

def service(request):
  template = loader.get_template('service.html')
  context = {
    'title': 'service',
    'sigin':CTM,
    'Count':CountPd,
    'SVs':Service.objects.all()
  }
  #
  if request.method=="POST":
    tempCtm=Customer.objects.get(idctm=CTM.id)
    tempSv=Service.objects.get(idsv=request.POST.get('TypeSv'))
    book = BookService(idctm=tempCtm, idsv=tempSv)
    book.book_date=request.POST.get('Date')
    if datetime.datetime.strptime(book.book_date,"%Y-%m-%d") <= datetime.datetime.now():
      messages.error(request,"Can't not book today or in the past!")
    else:
      try:
        book.save()
        messages.success(request,"Booking service successfully!")
      except:
        messages.error(request,"The service is already booked!")
  if request.method=="GET":
        if request.GET.get('Search') != None:
          Search=request.GET.get('Search')
          context= SearchPd(Search)
          template = loader.get_template(f'home.html') 
  return HttpResponse(template.render(context, request))

def signup(request):
  template = loader.get_template('signup.html')
  context = {
    'title': 'signup'
  }
  if request.method=='POST':
        res=RegistetUser()
        res.email=request.POST.get('email')
        res.username=request.POST.get('name')
        pass_1=request.POST.get('pass')
        pass_2=request.POST.get('pass1')
        pass_1=pass_1.encode('utf-8')
        pass_2=pass_2.encode('utf-8')
        res.password=bcrypt.hashpw(pass_1,bcrypt.gensalt())
        if bcrypt.checkpw(pass_2,res.password):
              res.password=str(res.password)
              res.save()
              return HttpResponseRedirect(reverse(signin))
  return HttpResponse(template.render(context, request))

def signin(request):
  global CTM
  template = loader.get_template('signin.html')
  context = {
    'title': 'signin'
  }
  if request.method=='POST':
    try:
      temp=RegistetUser.objects.get(username=request.POST.get('Username'))
      t=request.POST.get('pass')
      t=t.encode('utf-8')
      z=temp.password[2:-1]
      z=z.encode('utf-8')
      
      if bcrypt.checkpw(t,z):
        CTM=temp
        los=Customer.objects.values_list('idctm')
        KQ_los=[]
        for x in los:
              KQ_los.append(x[0]) 
        if CTM.id in KQ_los:
          return HttpResponseRedirect(reverse(home))
        else:
          return HttpResponseRedirect(reverse(EnterProfile)) 
      else:
        messages.error(request, "Wrong password!") 

    except:
      messages.error(request, "User does not exist!") 
  return HttpResponse(template.render(context, request))


def ViewAllPd(request, type1):
  template=loader.get_template('ViewAllPd.html')
  pd = Product.objects.filter(typepd=type1)
  context={
    'title': type1,
    'Pd': pd,
    'sigin':CTM,
    'Count':CountPd
  }
  if request.method=="GET":
        if request.GET.get('Search') != None:
          Search=request.GET.get('Search')
          context= SearchPd(Search)
          template = loader.get_template(f'home.html') 
  return HttpResponse(template.render(context, request))

def ViewPd(request,pk):
  template=loader.get_template('ViewPd.html')
  pd = Product.objects.get(idpd=pk)
  context={
    'Pd': pd,
    'sigin':CTM,
    'Count':CountPd,
  }
  if request.method=="POST":
    temp=Cart()
    if Cart.objects.filter(idctm=CTM.id, idpd=pd.idpd):
      temp=Cart.objects.get(idctm=CTM.id, idpd=pd.idpd)
      temp.amount+=int(request.POST.get("Input_number"))
    else:
      tempCtm=Customer.objects.get(idctm=CTM.id)
      temp.idctm=tempCtm
      temp.amount=int(request.POST.get("Input_number"))
      temp.idpd=pd

    if temp.amount < pd.amount:
      temp.save()
      messages.success(request,"Product is added successfully!")
    else:
      messages.error(request,"Fail! We don't have enough product!")
  if request.method=="GET":
        if request.GET.get('Search') != None:
          Search=request.GET.get('Search')
          context= SearchPd(Search)
          template = loader.get_template(f'home.html') 
  return HttpResponse(template.render(context, request))


def Logoutpage(request):
  global CTM
  CTM = RegistetUser()
  return HttpResponseRedirect(reverse(home))

def EnterProfile(request):
    template=loader.get_template('EnterProfile.html')
    context={
      'titel': "EnterProfile",
      'sigin':CTM,
      'Count':CountPd
    } 
    if request.method=="POST":
          temp=Customer()
          temp.idctm=RegistetUser.objects.get(id=CTM.id)
          temp.namectm=request.POST.get('Name')
          temp.address_field=request.POST.get('Address')
          temp.phone=request.POST.get('Phone')
          if len(request.FILES) != 0:
            temp.Avatar=request.FILES['image']
          temp.save()
          return HttpResponseRedirect(reverse(home))
    if request.method=="GET":
        if request.GET.get('Search') != None:
          Search=request.GET.get('Search')
          context= SearchPd(Search)
          template = loader.get_template(f'home.html') 
    return HttpResponse(template.render(context, request))

def ViewProfile(request):
    template=loader.get_template('ViewProfile.html')
    temp=Customer.objects.get(idctm=CTM.id)
    context={
      'titel': "ViewProfile",
      'Customer': temp,
      'sigin':CTM,
      'Count':CountPd
    }
    if request.method=="GET":
        if request.GET.get('Search') != None:
          Search=request.GET.get('Search')
          context= SearchPd(Search)
          template = loader.get_template(f'home.html') 
    return HttpResponse(template.render(context, request))

def Payment(request):
    template=loader.get_template('Payment.html')
    temp=Customer.objects.get(idctm=CTM.id)
    Cus_pd=Cart.objects.filter(idctm=CTM.id)
    total=0
    Dem=0
    for x in Cus_pd:
      Dem+=1
      a=x.idpd.price
      a=a.replace(".","")
      total=(total+int(a)*int(x.amount))
    context={
      'titel': "ViewProfile",
      'Customer': temp,
      'Cart':Cus_pd,
      'Total':total,
      'sigin':CTM,
      'Count':Dem
    }  
    if request.method=="POST":
      fail = False
      for pd in Cus_pd:
        wareHouse_pd = Product.objects.get(idpd=str(pd.idpd)[-3:-1])
        if pd.amount > wareHouse_pd.amount:
          fail = True
          messages.error(request,f"Fail! We don't have enough product {pd.idpd.namepd}!")
        else:
          t = Order()
          _2day_later = datetime.datetime.now() + datetime.timedelta(days=2)
          try:
            t=Order.objects.get(idctm=CTM.id, idpd=pd.idpd, ship_date=_2day_later)
            t.ship_amount+=int(pd.amount)
          except:
            t.idpd = pd.idpd
            t.idctm = pd.idctm
            t.ship_amount = pd.amount
            t.ship_date = _2day_later

          wareHouse_pd.amount -= t.ship_amount
          wareHouse_pd.save()
          t.save()
          pd.delete()
      if not fail:
        return HttpResponseRedirect(reverse(home))
    if request.method=="GET":
        if request.GET.get('Search') != None:
          Search=request.GET.get('Search')
          context= SearchPd(Search)
          template = loader.get_template(f'home.html') 
    return HttpResponse(template.render(context, request))