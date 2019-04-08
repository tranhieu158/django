from django.shortcuts import render
from django.http import HttpResponse
from .models import question
from .models import News
import MySQLdb
#from .models import
#from .models import web
# Create your views here.


def index(request):
    return render(request, "polls/index.html",)
def viewlist(request):
    list_question = question.objects.all()
    context = {"dsrequest": list_question }

    return render(request, "polls/list.html", context)
def detailview(request, question_id):
    q = question.objects.get(pk = question_id )

    return render(request, "polls/detail_question.html", {"qs": q})
def vote(request, question_id):
    q = question.objects.get(pk=question_id)
    try:
        dulieu = request.POST["choice"]
        c = q.choice_set.get(pk=dulieu)
    except:
        HttpResponse("Loi khong co du lieu")
    c.vote = c.vote + 1
    c.save()
    return render(request, "polls/result.html", {"q": q})

#def show_database(request):
 #   obj = News.objects.all()


  #  return render(request, "polls/database.html", {'obj':obj})
def show_database(request):
    #obj = News.objects.all()
    obj = MySQLdb.connect(user='root',db='testpython',passwd='tranhieu123',host='localhost')
  #  obj1 = MySQLdb.connect(user='root', db='testpython', passwd='tranhieu123', host='localhost')
   # obj2 = MySQLdb.connect(user='root', db='testpython', passwd='tranhieu123', host='localhost')
    cursor = obj.cursor()
  #  cursor1 = obj1.cursor()
  #  cursor2 = obj2.cursor()
    cursor.execute('select * from polls_choice')
 #   cursor1.execute('select * from polls_choice')
 #   cursor2.execute('select * from polls_choice')
    obj = [row for row in cursor.fetchall()]
  #  obj1 = [col[1] for col in cursor1.fetchall()]
  #  obj2 = [row[2] for row in cursor2.fetchall()]
    #return render(request, "testdb/index.html", {'obj':obj,'obj1':obj1,'obj2':obj2},)
    return render(request, "polls/database.html", {'obj':obj},)
