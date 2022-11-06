from multiprocessing import context
from django.shortcuts import render
import requests

# Create your views here.

#home page
def Home(request):


    context={

    }

    return render(request,'home.html',context)





#all blood group
def all_doner_blood_group(request):

    url="https://nirjon.pythonanywhere.com/information/json_view_all/"


    r = requests.get(url).json()
    #print(r)

    doner_list=[]


    for pp in r:

     doner_info ={
        'Name': pp['name'],
        'Email': pp['email'],
        'Phone': pp['phone'],
        'Age': pp['age'],
        'Gender': pp['gender'],
        'Blood_group': pp['blood_group'],
        'author' :pp['author'],
     }
    
    #print(doner_info)
     doner_list.append(doner_info)

    context={
        'doner_list':doner_list

    }
    return render(request,'blood_group.html',context)





#search view
def search_blood_group(request):
    doner_list=[]
    msg =''
    errmsg = ''
    msgclass = ''



    url="https://nirjon.pythonanywhere.com/information/search/?search={}"
    

    if 'query' in request.POST:
       query =request.POST['query']
     #  print("the name of blood is : ",query)
       r = requests.get(url.format(query)).json()

       
       if not r:
            errmsg= "OOPS! There are no blood group in this blood bank."
            doner_list=[]

            
            if errmsg:
                msg = errmsg
                msgclass = 'text-danger'

            else:
                msg = "Successfully find this blood group"
                msgclass = 'text-success'


       else:
          #  print(" lets do it... that not so easy")
           for pp in r:

            doner_info ={
                'Name': pp['name'],
                'Email': pp['email'],
                'Phone': pp['phone'],
                'Age': pp['age'],
                'Gender': pp['gender'],
                'Blood_group': pp['blood_group'],
                'author' :pp['author'],
            }
            
            #print(doner_info)
            doner_list.append(doner_info)

           # print(r)

            if errmsg:
                msg = errmsg
                msgclass = 'is-danger'

            else:
                msg = "successfully find this blood group"
                msgclass = 'text-success'
        

    context={
        'doner_list': doner_list,
        'msg': msg,
        'msgclass': msgclass

    }
    return render(request,'search_blood_result.html',context)
