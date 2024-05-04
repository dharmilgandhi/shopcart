from django.shortcuts import render, redirect

from .models import Product, Contact, Orders, orderUpdate,Shopdetail
from django.contrib.auth.models import User
from django.contrib import messages
from math import ceil
from django.contrib.auth import authenticate,  login, logout
# Create your views here.
from django.http import HttpResponse


def index(request):

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])
    
    shopView = Shopdetail.objects.values('shop_id','shop_name')
    print(shopView)
    params = {'allProds': allProds,'shopView':shopView}
    return render(request, 'shop/home.html', params)




def catview(request, shop_id):
    shop_id = Product.objects.filter(shop_id=shop_id)
    shopView = Shopdetail.objects.values('shop_id', 'shop_name')
    params = {'shop_id':shop_id,'shopView':shopView}
    return render(request, 'shop/pageview.html', params)
    # return render(request, 'shop/pageview.html', {'shop_id': shop_id})


def pageview(request, **kwargs):
    i = kwargs['viewname']
    allprods = []
    catprods = Product.objects.values(
        'id', 'product_name', 'category', 'image', 'pub_date', 'desc', 'price', 'subcategory', 'shop_id')
    shopView = Shopdetail.objects.values('shop_id', 'shop_name')

    for j in range(len(catprods)):
        if catprods[j]['category'] == i:
            allprods.append(catprods[j])
    params = {'viewname': i, 'cat': allprods,'shopView':shopView}
    return render(request, 'shop/pageview.html',params)
    # return render(request, 'shop/pageview.html', {'viewname': i, 'cat': allprods})



def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == "POST":
        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')

        mobilenumber = request.POST.get('mobilenumber', '')

        query = request.POST.get('query', '')
        contact = Contact(name=name, email=email,
                          mobilenumber=mobilenumber, query=query)
        contact.save()

    return render(request, 'shop/contact.html')


def search(request):
    return render(request, 'shop/search.html')


def productView(request, myid):
    # fetch product using id
    product = Product.objects.filter(id=myid)
    shopView = Shopdetail.objects.values('shop_id', 'shop_name')
    params = {'product':product[0],'shopView':shopView}
    print(product)
    return render(request, 'shop/prodview.html', params)
    # return render(request, 'shop/prodview.html', {'product': product[0]})


def checkout(request):
    if request.method == "POST":
        

        item_json = request.POST.get('itemJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('emailCheckout', '')

        address = request.POST.get('address1', '') + \
            "" + request.POST.get('address2', '')

        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        mobilenumber = request.POST.get('mobilenumber', '')
        zip_code = request.POST.get('zip_code', '')

        order = Orders(name=name, email=email, address=address, city=city, state=state,
                    mobilenumber=mobilenumber, zip_code=zip_code, item_json=item_json)
        order.save()
        update = orderUpdate(order_id=order.order_id,
                            update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
       
    return render(request, 'shop/checkout.html')


def handleSignUp(request):
    
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']

        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username) > 10:
            messages.error(
                request, " Your user name must be under 10 characters")
            return redirect('ShopHome')

        if not username.isalnum():
            messages.error(
                request, " User name should only contain letters and numbers")
            return redirect('ShopHome')
        if (pass1 != pass2):
            messages.error(request, " Passwords do not match")
            return redirect('ShopHome')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(
            request, 'Your account has been created successfully! Please Login for shopping')
        return redirect("ShopHome")

    else:
        return HttpResponse("404 - Not found")


def handeLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpass']

        user = authenticate(username=loginusername, password=loginpassword)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("ShopHome")
        else:
            messages.error(request, "Invalid credentials! Please try again")            
            return redirect("ShopHome")

    return HttpResponse("404- Not found")


def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('ShopHome')
