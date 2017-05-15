# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
import datetime
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView

from .models import blog2, user, blog1


# def blogeditdelete(request,id):
def delete(request, id):
    print "Helloworld"
    x = blog2.objects.get(pk=id)
    x.delete()
    # print x
    print "hello2"
    y = blog2.objects.all()
    print("Hello3")
    # print "hello"
    # print y['title']
    # print(y.title)
    # print y[0].title
    if request.session['type'] == '0':
        return render(request,'mainpage.html', {'blog2': blog2.objects.all(), 'type': '0'})
    elif request.session['type'] == '2':
        my_blogs = get_my_blogs(request.session['user'])
        rest_blog = blog2.objects.all()
        return render(request, 'mainpage.html', {'rest_blog': rest_blog, 'self_blog': my_blogs, 'type': '2'})
    else:
        return HttpResponse("You are not allowed")


@csrf_exempt
def edit(request, id):
    x = blog2.objects.get(pk=id)
    if request.method == 'GET':
        return render(request, 'editpage.html', {'blog_title': x.title, 'blog_content': x.content, 'blog_id': x.id})
    if request.method == 'POST':
        form = request.POST
        x.title = form['title']
        x.content = form['content']
        x.save()
        y = blog2.objects.all()
        if request.session['type'] == '0':
            return render(request, 'mainpage.html',
                          {'blog_title': y.title, 'blog_content': y.content, 'blog_id': y.id, "type": "0"})
        elif request.session['type'] == '2':
            my_blogs = get_my_blogs(request.session['user'])
            rest_blog = blog2.objects.all()
            return render(request, 'mainpage.html', {'rest_blog': rest_blog, 'self_blog': my_blogs, 'type': '2'})
        else:
            return HttpResponse("You are not allowed")


def blog(request, id):
    if 'user' in request.session:
        x = blog2.objects.get(pk=id)
        if request.session['type'] == '1':
            return render(request, 'blog.html',
                          {'blog_title': x.title, 'blog_content': x.content, 'blog_id': x.id, "type": "1"})
        elif request.session['type'] == '0':
            return render(request, 'blog.html',
                          {'blog_title': x.title, 'blog_content': x.content, 'blog_id': x.id, "type": "0"})
        elif request.session['type'] == '2':
            return render(request, 'blog.html',
                          {'blog_title': x.title, 'blog_content': x.content, 'blog_id': x.id, "type": "2"})
        else:
            return HttpResponse('YOU are not alloweded')


@csrf_exempt
def login(request):
    if request.method == 'GET':
        if 'user' in request.session:
            if request.session['type'] == '1':
                return render(request, 'mainpage.html', {'blog2': blog2.objects.all(), 'type': '1'})
            elif request.session['type'] == '0':
                return render(request, 'mainpage.html', {'blog2': blog2.objects.all(), 'type': '0'})
            elif request.session['type'] == '2':
                self_blog = []

                usr = user.objects.get(pk=request.session['user'])
                temp_self_blog = blog1.objects.filter(author_id=usr.id)

                test_blog = blog2.objects.all()

                for val in temp_self_blog:
                    for val2 in test_blog:
                        if val2 == val.blog_id:
                            self_blog.append(val2)

                rest_blog = blog2.objects.all()

                print self_blog

                print rest_blog

                print("Hello")

                return render(request, 'mainpage.html', {'rest_blog': rest_blog, 'self_blog': self_blog, 'type': '2'})
        else:
            return render(request, 'login.html', {"message": "Please Login"})

    if request.method == 'POST':
        x = request.POST
        # print(x)
        tempuser = user.objects.filter(email=x['email'], password=x['password'])
        # print(x)
        if tempuser[0]:
            request.session['user'] = tempuser[0].pk
            request.session['type'] = tempuser[0].type
            # print(request.session['type'])
            if request.session['type'] == '1':
                return render(request, 'mainpage.html', {'blog2': blog2.objects.all(), 'type': '1'})
            elif request.session['type'] == '0':
                return render(request, 'mainpage.html', {'blog2': blog2.objects.all(), 'type': '0'})
            elif request.session['type'] == '2':
                my_blogs = get_my_blogs(request.session['user'])
                rest_blog = blog2.objects.all()
                return render(request, 'mainpage.html', {'rest_blog': rest_blog, 'self_blog': my_blogs, 'type': '2'})
        else:
            return render(request, 'login.html', {"message": "Login again"})


@csrf_exempt
def mainpage(request):
    if request.method == 'GET':
        if 'user' in request.session:
            if request.session['type'] == '1':
                return render(request, 'mainpage.html', {'blog2': blog2.objects.all(), 'type': '1'})
            elif request.session['type'] == '0':
                return render(request, 'mainpage.html', {'blog2': blog2.objects.all(), 'type': '0'})
            elif request.session['type'] == '2':
                my_blogs = get_my_blogs(request.session['user'])
                rest_blog = blog2.objects.all()
                return render(request, 'mainpage.html', {'rest_blog': rest_blog, 'self_blog': my_blogs, 'type': '2'})

        else:
            return render(request, 'login.html', {"message": "Please Login"})
    if request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        rest_blog = blog2.objects.all()
        blog = blog2(title=title, content=content, created=datetime.datetime.now())
        # print blog['id']
        blog.save()

        my_blogs = get_my_blogs(request.session['user'])
    return render(request, 'mainpage.html', {'rest_blog': rest_blog, 'self_blog': my_blogs, 'type': '2'})


def logout(request):
    try:
        del request.session['user']
        del request.session['type']
    except:
        pass
    return render(request, 'login.html', {"message": "You are logged out"})


@csrf_exempt
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    # if request.method == 'POST':
    #     x = request.POST
    #     user = user()
    if request.method == 'POST':  # if the form has been filled

        form = user(request.POST)

        # if form.is_valid():  # All the data is valid
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        type = request.POST.get('type', '')
        # creating an user object containing all the data
        user_obj = user(name=name, email=email, password=password,type=type)
        # saving all the data in the current object into the database
        user_obj.save()

        return render(request, 'login.html')  # Redirect after POST

    else:
        form = user()  # an unboundform

        return render(request, 'signup.html', {'form': form})

def view_blog(request,id):
    if request.method == 'GET':
        if 'user' in request.session:
            x = blog2.objects.get(pk=id)
            return render(request, 'views_blog.html',{'blog_title': x.title, 'blog_content': x.content})
        else:
            return render(request, 'login.html', {"message": "Please Login"})


def get_my_blogs(z):
    self_blog = []
    usr = user.objects.get(pk=z)
    temp_self_blog = blog1.objects.filter(author_id=usr.id)
    test_blog = blog2.objects.all()
    for val in temp_self_blog:
        for val2 in test_blog:
            if val2 == val.blog_id:
                self_blog.append(val2)

    return self_blog

# def test(request):
#     request.path = '/login/'
#     print(request.path)
#     return HttpResponse("hello")