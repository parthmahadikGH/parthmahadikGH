from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    
    peoples = [
       {'name' : 'Parth Mahadik' , 'age' : 23},
       {'name' : 'Sakshi A' , 'age' : 32},
       {'name' : 'Shubham C' , 'age' : 34},
       {'name' : 'Gayatri D' , 'age' : 25},
    ]
    
    
      for people in peoples:
          print(people)
          
          
       return render(request , "home/index.html", context = {'peoples' : peoples})
   
def Front_page(request):
      return HttpResponse("<h1>HOME PAGE</h1")