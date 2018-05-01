from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *
from pycricbuzz import Cricbuzz
i=0
# Create your views here.
def index(request):
    global i
    i=i+1
    return HttpResponse("You are "+str(i))
class HomeView(TemplateView):
    template_name = 'home.html'
class HomeView1(TemplateView):
    template_name = 'home1.html'
def test(request,x,y):
    bat=x['scorecard'][0]['batcard']
    bowl=x['scorecard'][0]['bowlcard']
    bat1 = x['scorecard'][1]['batcard']
    bowl1 = x['scorecard'][1]['bowlcard']
    minfo=x['matchinfo']
    team=[]
    team.append(x['scorecard'][0]['batteam'])
    team.append(x['scorecard'][1]['batteam'])
    board = {}
    board['score'] = x['scorecard'][0]['runs']
    board['wick'] = x['scorecard'][0]['wickets']
    board['overs'] = x['scorecard'][0]['overs']
    board['rr'] = x['scorecard'][0]['runrate']
    board['score1'] = x['scorecard'][1]['runs']
    board['wick1'] = x['scorecard'][1]['wickets']
    board['overs1'] = x['scorecard'][1]['overs']
    board['rr1'] = x['scorecard'][1]['runrate']
    return render(request,"scorecard.html",{'batlists': bat,'bowllists' : bowl,'bat1lists': bat1,'bowl1lists' : bowl1,
                  'matchinfo' : minfo ,'batseq' :team[0] ,'bowlseq' :team[1],'comm':y['commentary'],'board':board})
def test1(request,x,y):
    bat = x['scorecard'][0]['batcard']
    bowl = x['scorecard'][0]['bowlcard']
    minfo = x['matchinfo']
    team = []
    team.append(x['scorecard'][0]['batteam'])
    team.append(x['scorecard'][0]['bowlteam'])
    board={}
    board['score']=x['scorecard'][0]['runs']
    board['wick']=x['scorecard'][0]['wickets']
    board['overs']=x['scorecard'][0]['overs']
    board['rr']=x['scorecard'][0]['runrate']
    return render(request,"scorecard1.html",{'batlists': bat,'bowllists': bowl,'matchinfo': minfo,
                                             'batseq':team[0],'bowlseq':team[1],'comm': y['commentary'],'board':board})
def clist(request):
    z=Cricbuzz()
    c=z.matches()
    return render(request,"cric.html",{'clists': c})
def Scorecard(request,id):
    Z=Cricbuzz()
    m=Z.scorecard(str(id))
    comm=Z.commentary(str(id))
    if m['matchinfo']['mchstate']=="Result":
        return test(request,m,comm);
    elif (m['matchinfo']['mchstate']=="inprogress") or (m['matchinfo']['mchstate']=="innings break"):
        if len(m['scorecard'])==2:
            return test(request,m,comm)
        elif len(m['scorecard'])==1:
            return test1(request,m,comm)
    return len(m)