from django.http import HttpResponse
from webapp.models import UserDetails
from webapp.models import data
from Contentbased import get_recommendations
from Contentbased import get_recommendationstemp
from Contentbased import get_recommendationstemp2
from music import getTopRecommandations
from django.shortcuts import render
from random import randint, sample
import requests


def index(request):
    y = []
    if 'name' in request.session:
        userdata = data.objects.all().filter(user=request.session['name'])
        m = len(userdata)
        if 1 < m <= 5:
            r = randint(0, m - 1)
            y = get_recommendationstemp(userdata[r].movie)
            return render(request, './templateFiles/home.html', {'username': request.session['name'],
                                                                 'yop': 'not done',
                                                                 'haha': y})
        elif m > 5:
            c = list(range(0, m-1))
            c = sample(c, 5)
            y1 = get_recommendationstemp2(userdata[c[0]].movie)
            y2 = get_recommendationstemp2(userdata[c[1]].movie)
            y3 = get_recommendationstemp2(userdata[c[2]].movie)
            y4 = get_recommendationstemp2(userdata[c[3]].movie)
            y5 = get_recommendationstemp2(userdata[c[4]].movie)
            return render(request, './templateFiles/home.html', {'username': request.session['name'],
                                                                 'yop': 'not done',
                                                                 'haha': y1,
                                                                 'haha1': y2,
                                                                 'haha2': y3,
                                                                 'haha3': y4,
                                                                 'haha4': y5})
        else:
            y = get_recommendationstemp('Avatar')
            return render(request, './templateFiles/home.html', {'username': request.session['name'],
                                                                 'yop': 'not done',
                                                                 'haha': y})

    else:
        return render(request, 'templateFiles/home.html', {'username': 'nope'})


def index3(request):
    return render(request, 'templateFiles/convertcsv2.json')


def index4(request):
    return render(request, 'templateFiles/book json.json')


def admin(request):
    return render(request, 'templateFiles/admin.html',
                  {'userDetails': UserDetails.objects.all(), 'whoAdmin': 'DhruvFromLj'})


def authentication(request):
    username = request.POST['fname1']
    password = request.POST['password']
    password2 = request.POST['email']
    if password == password2:
        x = ""
        all1 = UserDetails.objects.all()
        isthere = 0
        for rr in all1:
            if rr.user == username:
                isthere = 1
                return render(request, 'templateFiles/home.html', {'username': 'nope', 'Again': 'true',
                                                                   'statement': 'this person already exist try again'})

        if isthere == 0:
            b = UserDetails(user=username, password=password)
            b.save()
            request.session['name'] = username
            return render(request, 'templateFiles/home.html', {'username': request.session['name']})
    else:
        return render(request, 'templateFiles/home.html', {'username': 'nope', 'Again': 'true',
                                                           'statement': 'Password is not matched! try again.'})


def login(request):
    username = request.POST['fname5']
    password = request.POST['fname6']
    x = ""
    all1 = UserDetails.objects.all()
    isthere = 0
    for rr in all1:
        if rr.user == username:
            if rr.password == password:
                isthere = 1
                request.session['name'] = username
                userdata = data.objects.all().filter(user=request.session['name'])
                m = len(userdata)
                if 1 < m <= 5:
                    r = randint(0, m - 1)
                    y = get_recommendationstemp(userdata[r].movie)
                    return render(request, './templateFiles/home.html', {'username': request.session['name'],
                                                                         'yop': 'not done',
                                                                         'haha': y})
                elif m > 5:
                    c = list(range(0, m - 1))
                    c = sample(c, 5)
                    y1 = get_recommendationstemp2(userdata[c[0]].movie)
                    y2 = get_recommendationstemp2(userdata[c[1]].movie)
                    y3 = get_recommendationstemp2(userdata[c[2]].movie)
                    y4 = get_recommendationstemp2(userdata[c[3]].movie)
                    y5 = get_recommendationstemp2(userdata[c[4]].movie)
                    return render(request, './templateFiles/home.html', {'username': request.session['name'],
                                                                         'yop': 'not done',
                                                                         'haha': y1,
                                                                         'haha1': y2,
                                                                         'haha2': y3,
                                                                         'haha3': y4,
                                                                         'haha4': y5})
                else:
                    y = get_recommendationstemp('Avatar')
                    return render(request, './templateFiles/home.html', {'username': request.session['name'],
                                                                         'yop': 'not done',
                                                                         'haha': y})

    if isthere == 0:
        b = UserDetails(user=username, password=password)
        b.save()
        return render(request, 'templateFiles/home.html', {'username': 'nope', 'Again': 'true',
                                                           'statement': 'Your Username or Password is wrong!'})


def show(request):
    x = request.GET['fname11']
    a = get_recommendations(x)
    if 'name' in request.session:
        userdata = data.objects.all().filter(user=request.session['name'])
        mt = len(userdata)
        flag = 0
        if mt > 0:
            for i in range(0, mt):
                movies = userdata[i].movie
                if str(x) == movies:
                    flag = 1
            if flag == 0:
                y = data(user=request.session['name'], movie=str(x))
                y.save()
        elif mt == 0:
            y = data(user=request.session['name'], movie=str(x))
            y.save()

        m = len(userdata)
        if 1 < m <= 5:
            r = randint(0, m - 1)
            y = get_recommendationstemp(userdata[r].movie)
            return render(request, './templateFiles/showResult.html', {'a': a,
                                                                       'username': request.session['name'],
                                                                       'yop': 'not done',
                                                                       'haha': y})
        elif m > 5:
            c = list(range(0, m - 1))
            c = sample(c, 5)
            y1 = get_recommendationstemp2(userdata[c[0]].movie)
            y2 = get_recommendationstemp2(userdata[c[1]].movie)
            y3 = get_recommendationstemp2(userdata[c[2]].movie)
            y4 = get_recommendationstemp2(userdata[c[3]].movie)
            y5 = get_recommendationstemp2(userdata[c[4]].movie)
            return render(request, './templateFiles/showResult.html', {'a': a,
                                                                       'username': request.session['name'],
                                                                       'yop': 'not done',
                                                                       'haha': y1,
                                                                       'haha1': y2,
                                                                       'haha2': y3,
                                                                       'haha3': y4,
                                                                       'haha4': y5})
        else:
            y = get_recommendationstemp('Avatar')
            return render(request, './templateFiles/showResult.html', {'a': a,
                                                                       'username': request.session['name'],
                                                                       'yop': 'not done',
                                                                       'haha': y})

    else:
        return render(request, './templateFiles/showResult.html', {'a': a, 'username': 'nope'})


def music(request):
    x = str(request.GET['ArtistName'])
    x = x.split(' ')
    s = ''
    for i in range(len(x)):
        if i is 0:
            s = x[i]
        else:
            s = s + '+' + x[i]
    s = 'https://tastedive.com/api/similar?q=' + s + '&type=music&info=1&k=308176-Reco-L89EUX2C'
    r = requests.get(s)
    r.encoding
    r = r.json()
    r1 = r['Similar']['Info']
    r2 = r['Similar']['Results']
    r2 = r2[0:10]
    if 'name' in request.session:
        return render(request, './templateFiles/showMusic.html', {'a': r1, 'b': r2, 'username': request.session['name']})
    else:
        return render(request, './templateFiles/showMusic.html',
                      {'a': r1, 'b': r2, 'username': 'nope'})

def book(request):
    x = str(request.GET['bookname'])
    x = x.split('-')
    a = getTopRecommandations(int(x[1]))
    if 'name' in request.session:
        return render(request, './templateFiles/showBook.html', {'a': a, 'username': request.session['name']})
    else:
        return render(request, './templateFiles/showBook.html', {'a': a, 'username': 'nope'})


def logout(request):
    del request.session['name']
    return render(request, 'templateFiles/home.html', {'username': 'nope'})

