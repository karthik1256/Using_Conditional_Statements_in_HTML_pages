from django.shortcuts import render

# Create your views here.

def IF(request):
    d1={'a':20,'b':30}
    return render(request,'IF.html',d1)


def IF_ELSE(request):
    d2={'a':22,'b':33}
    return render(request,'IF_ELSE.html',d2)


def IF_ELIF(request):
    d3={'a':33,'b':44,'c':55}
    return render(request,'IF_ELIF.html',d3)


def NESTED_IF(request):
    d4={'a':33,'b':44,'c':55}
    return render(request,'NESTED_IF.html',d4)
