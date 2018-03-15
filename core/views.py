from django.shortcuts import render

def hi(request, w, q):
    return render(request,'hi.html',{
        'sum': w + q,
    })

def r(request,start,stop):
    if start > stop:
        start, stop = stop, start
        rr = range(start,stop + 1)
        rr = reversed(rr)
    else:
        rr = range(start,stop + 1)
    return render(request,'r.html',{
        'rr': rr,
    })