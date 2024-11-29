from django.shortcuts import render,redirect

# Create your views here.
subject=[]


def index(request):
    if request.method=='POST': 
        l=len(subject)
        slno=l+1
        sub=request.POST['text']
        subject.append({'slno':slno,'sub':sub})
    return render(request,'index.html' ,{'subjects':subject})
def todo_update(request,slno):
    for i in subject:
        if i['slno']==slno:
            sub=i['sub']
            if request.method=='POST':
                todo_sub=request.POST['todo']
                for i in subject:
                    if i['slno']==slno:
                        i['sub']=todo_sub
                    return redirect(index)
        return render(request,'todo_update.html',{'sub':sub,'slno':slno})
