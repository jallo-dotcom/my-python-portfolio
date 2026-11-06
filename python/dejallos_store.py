#updated version for better experience run in another platform because of sololearn requires all the inputs before it can run
import time
print('===🛍Dejallos Luxurious Store===')
time.sleep(2)
print('Please create a profile with us for purchases below👇👇')
def name():
  user_name= input('Name : ')
  return user_name
real_name = name()
def call():
    number= input('Mobile : ')
    while not number.isdigit():
      print ('invalid please insert numbers only')
      number = input('Mobile : ')
    return number
mobile = call()
def country():
    place = input ('Country : ')
    return place
home = country()
def state():
  town = input('State : ')
  return town
city = state()
def house():
    home = input('Residence : ')
    return home
residence = house()
print ('Profile created!!!')
print ('Create Your Password')
password = input('password ')
while len(password) <8:
    print ('Password should not be less than eight characters')
    password = input('password : ')
confirm = input ('confirm password : ')
while confirm != password:
    print ('Password do not match')
    confirm = input('confirm password : ')
print ('Password successfully created') 
print('Loading.......')
time.sleep(3)
print('===========L=O=G=I=N=P=A=G=E===========') 
space_1 = input('Mobile : ')  
while space_1 != mobile:
    print('incorrect details please enter a valid number')
    space_1 = input('Mobile : ')
space_2 = input('Password : ')
while space_2 != password:
    print ('incorrect password')
    space_2 = input('Password : ')
print('Loading.......')
time.sleep(3)
print('==========Authorized==========')
print('Loading.......')
time.sleep(3)   
print('================================')
print('=====Good day',real_name,'=====')
print('======Welcome to Dejallos🛍🛍======')
print('================================')
print('==========DASHBOARD=========')
print('1:Products')
print('2:Profile')
print('3:Exit')
need = input('using numbers do as you like ')
while need not in ('1','2','3'):
    print(' invalid ')
    need = input('using numbers do as you like ') 
if need == '1':
  print('====Products====')
  products = ['1 : T-shirt ','2 : Trousers ','3 : Shoes',]
  print (products[0])
  print(products[1])
  print(products[2])
  choice = input('Using numbers what would you like to buy ')
  while choice not in ('1','2','3',):
      print('invalid')
      choice = input('Using numbers what would you like to buy ')
  def products(size = input('size : '),color = input('color : ')):
      size1 = size
      color1 = color
      return size1,color1
  if choice == '1':
    products()
    shirt_size,shirt_color = products()
    price1 = '₦10,000'
    print ('T_shirt')
    print('size : ' + shirt_size)
    print('color : ' + shirt_color)
    print('Price : ' + price1)
    ask1 = input('Would you like to continue with the purchase Y/n :').lower()
    while ask1 not in ('y','n'):
      print ('invalid please use y or n')
      ask1 = input('Would you like to continue with the purchase Y/n : ')
    if ask1 == 'y':
        for i in range(40):
            print('Loading......')
        for i in range(40):
            print('Processing payment......')
        for i in range(40):
            print('Payment successful✅✅')
        route = input('Choose your delivery option sea/flight :').capitalize()      
        while route not in ('Sea','Flight'):
            print('Not available please from the options that are available')
            route = input('Choose your delivery option sea/flight :').capitalize()   
        print('====Purchase Successful 🛍🛍====')
        print('===Product Details===')  
        print ('Product : ' + 'T_shirt')
        print('size : ' + shirt_size)
        print('color : ' + shirt_color)
        print('Price :' + price1)
        print('===Delivery Details===')
        print('name : ' + real_name)
        print('mobile : ' + mobile)
        print('Address : ' + residence + ' , ' + city + ' , ' + home)
        print('Route✈️ : ',route)
        print('==========Thanks🎉🎉 for having as our customer',real_name,'wish to see you again==========')
    else:
        print('====Nice having you with us====')
  elif choice =='2':
    products()
    trouser_size,trouser_color = products()
    price2 = '₦20,000'
    print('Trouser') 
    print('size : ' + trouser_size)      
    print('color : ' + trouser_color)
    print('Price : ' + price2)
    ask2 = input('Would you like to continue with the purchase Y/n :').lower()
    while ask2 not in ('y','n'):
      print ('invalid please use y or n')
      ask2 = input('Would you like to continue with the purchase Y/n : ')
    if ask2 == 'y':
        for i in range(40):
            print('Loading......')
        for i in range(40):
            print('Processing payment......')
        for i in range(40):
            print('Payment successful✅✅')
        route = input('Choose your delivery option sea/flight :').capitalize()      
        while route not in ('Sea','Flight'):
            print('Not available please from the options that are available')
            route = input('Choose your delivery option sea/flight :').capitalize()   
        print('====Purchase Successful 🛍🛍====')
        print('===Product Details===')  
        print ('Product : ' + 'Trouser')
        print('size : ' + trouser_size)
        print('color : ' + trouser_color)
        print('Price : ' + price2)
        print('===Delivery Details===')
        print('name : ' + real_name)
        print('mobile : ' + mobile)
        print('Address : ' + residence + ' , ' + city + ' , ' + home)
        print('Route ✈️ : ' + route)
        print('==========Thanks🎉🎉 for having as our customer',real_name,'wish to see you again==========')
    else:
        print('====Nice having you with us====')
  elif choice == '3':
      products()
      shoe_size,shoe_color = products()
      price3 = '₦10,000'
      print('Shoe')
      print('size : ' + shoe_size)
      print('color : ' + shoe_color)
      print('Price : ' + price3)
      ask3 = input('Would you like to continue with the purchase Y/n :').lower()
      while ask3 not in ('y','n'):
        print ('invalid please use y or n')
        ask3 = input('Would you like to continue with the purchase Y/n : ')
      if ask3 == 'y':
        for i in range(40):
            print('Loading......')
        for i in range(40):
            print('Processing payment......')
        for i in range(40):
            print('Payment successful✅✅')
        route = input('Choose your delivery option sea/flight :').capitalize()      
        while route not in ('Sea','Flight'):
            print('Not available please from the options that are available')
            route = input('Choose your delivery option sea/flight :').capitalize()   
        print('====Purchase Successful 🛍🛍====')
        print('===Product Details===')  
        print ('Product : ' + 'Shoe')
        print('size : ' + shoe_size)
        print('color : ' + shoe_color)
        print('Price : ' + price3)
        print('===Delivery Details===')
        print('name : ' + real_name)
        print('mobile : ' + mobile)
        print('Address : ' + residence + ' , ' + city + ' , ' +home)
        print('Route✈️ : ' + route)
        print('==========Thanks🎉🎉 for having as our customer',real_name,'wish to see you again==========')
        print('====================DE JALLOS🛍🛍====================')
      else:
        print('====Nice having you with us====')
        print('====================DE JALLOS🛍🛍====================')
elif need == '2':
    Name = 'Name : ' + real_name
    Phone = 'Mobile : ' + mobile
    Address ='Address : ' + residence + ' , ' + city + ' , ' + home
    Password = '••••••••••••'
    print(Name)
    print(Phone)
    print(Address)
    print(Password)
    edit = input('Would you like to edit : Y/n').lower()
    while edit not in ('y','n'):
        print('invalid') 
        edit = input('Would you like to edit : Y/n').lower()
    if edit == 'y':
        print('1 : Name')
        print('2 : Mobile')
        print('3 : Address')
        print('4 : Password')
        print('5 : All')
        change = input('Using numbers what woukd you like to edit')
        while change not in ('1','2','3','4','5'):
            print('invalid')     
            change = input('Using numbers what woukd you like to edit')
        if change == '1':
            new_name = input('Insert new name : ')        
            real_name = new_name
            print('Name change successful')
            print('Name : ' + new_name)
            print(Phone)
            print(Address)
            print(Password)
        elif change == '2':
            new_phone = input('Insert new mobile here : ')
            while not new_phone.isdigit():
                print('invalid,insert only numbers')
                new_phone = input('Insert new mobile here : ')      
            mobile = new_phone
            print('Mobile change successful')
            print(Name)
            print('Mobile : ' + new_phone)
            print(Address)
            print(Password)
        elif change == '3':
            new_residence = input('New Residence : ').capitalize()
            new_city = input('New State : ').capitalize()
            new_country = input('New Country : ').capitalize()
            residence = new_residence
            city = new_city
            home = new_country
            print('Address change successful')
            print(Name)
            print(Phone)
            print('Address : '+new_residence+' , ' +new_city +' , ' +new_country)
            print(Password)
        elif change == '4':
            new_password = input('input old password to change your password : ')
            while new_password != password:
                print('incorrect password')
                new_password = input('input old password to change your password : ')
            new_password1 = input('input new password : ')
            while len(new_password1)<8:
                print('password should not be less than eight characters')
                new_password1 = input('input new password : ')
            new_passconfirm = input('Confirm new password : ')
            while new_passconfirm != new_password1:
                print('Password do not match')
                new_passconfirm = input('Confirm new password : ')
            password = new_passconfirm
            print('new password : ' +new_passconfirm)   
        elif change == '5':
            new_name1 = input('Insert new name : ')
            real_name = new_name1
            new_phone1 = input('Insert new mobile here : ')
            while not new_phone1.isdigit():
               print('invalid,insert only numbers')
               new_phone1 = input('Insert new mobile here : ')
            new_residence1 = input('New Residence : ').capitalize()
            new_city1 = input('New State : ').capitalize()
            new_country1 = input('New Country : ').capitalize()
            residence = new_residence1
            city = new_city1
            home = new_country1
            new_password1 = input('input old password to change your password : ')
            while new_password1 != password:
                print('incorrect password')
                new_password1 = input('input old password to change your password : ')
            new_password2 = input('input new password : ')
            while len(new_password2)<8:
                print('password should not be less than eight characters')
                new_password2 = input('input new password : ')
            new_passconfirm1 = input('Confirm new password : ')
            while new_passconfirm1 != new_password2:
                print('Password donot match')
                new_passconfirm1 = input('Confirm new password : ')
            password = new_passconfirm1
            print('===Profile change successful===')
            for i in range(10):
                  print('Loading.......')
            print('=========New Profile Updated=========')
            print('Name : ' + new_name1)
            print('Phone : ' +new_phone1)
            print('Address : ' +new_residence1,new_city1,new_country1)
            print('Password : '+ Password)   
elif need == '3':
    print('======Good bye========')
    print('====' + real_name + ' wish to see you again soon====')