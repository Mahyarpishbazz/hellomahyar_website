from django.shortcuts import render,redirect
from .models import MyProjectData, ContactBox
# Create your views here.


def index(request):

    if request.method == "POST":
        FirstName = request.POST.get('FirstNameAndFamily')
        Email = request.POST.get('Emails')
        Body = request.POST.get('BodyText')
        ContactBox.objects.create(FirstNameAndFamily=FirstName, Emails=Email, BodyText=Body)
        return redirect('/')

    while True:
        #first details for counter my work
            MyWorkList = []
            MyProjectDataTemp = MyProjectData.objects.all().count()
            MyProjectData1 = MyProjectData.objects.all()
            for i in range(0, MyProjectDataTemp):
                MyWorkList.append(i + 1)

            LastNumberOfList = MyWorkList[-1]
            # Conditinal for count Number
            if LastNumberOfList < 10:
                LastNumberOfListString = str(LastNumberOfList)
                Finally = LastNumberOfListString.zfill(2)
                return render(request, "index.html", {'myapp': Finally, 'test': MyProjectData1})
            else:
                Finally = str(LastNumberOfList)
                return render(request, "index.html", {'myapp': Finally, 'test': MyProjectData1})


