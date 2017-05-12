# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView

from .models import *

# def blogeditdelete(request,id):
def delete(request,id):
    x = blog2.objects.get(pk=id)
    x.delete()
    return render(request, 'mainpage.html', {'blog2': blog2.objects.all(), 'type': '0'})

@csrf_exempt
def edit(request,id):
    x = blog2.objects.get(pk = id)
    if request.method == 'GET':
        return render(request,'editpage.html',{'blog_title':x.title,'blog_content':x.content,'blog_id':x.id})
    if request.method == 'POST':
        form = request.POST
        x.title = form['title']
        x.content = form['content']
        x.save()
        return render(request,'mainpage.html',{'blog2': blog2.objects.all(), 'type': '0'})

def blog(request,id):
    if 'user' in request.session:
        x = blog2.objects.get(pk=id)
        if request.session['type'] == '1':
             return render(request,'blog.html',{'blog_title':x.title,'blog_content':x.content,'blog_id':x.id,"type":"1"})
        elif request.session['type'] == '0':
            return render(request, 'blog.html', {'blog_title': x.title, 'blog_content': x.content, 'blog_id': x.id, "type":"0"})
        else:
            return HttpResponse('YOU are not alloweded')

@csrf_exempt
def login(request):
    if request.method == 'GET':
        if 'user' in request.session:
            if request.session['type'] == '1':
                return render(request,'mainpage.html',{'blog2':blog2.objects.all(),'type':'1'})
            elif request.session['type'] == '0':
                return render(request,'mainpage.html',{'blog2':blog2.objects.all(),'type':'0'})
            elif request.session['type'] == '2':
                self_blog = []
                rest_blog = []
                usr = user.objects.get(pk=request.session['user'])
                temp_self_blog = blog1.objects.filter(author_id=usr.id)
                # self_blog = blog2.objects.filter(id=temp_self_blog)
                test_blog = blog2.objects.all()
                # print temp_self_blog
                # print self_blog
                for val in temp_self_blog:
                    for val2 in test_blog:
                        if val2==val.blog_id:
                            self_blog.append(val2)
                        # else:
                        #     if val2 not in rest_blog:
                        #         rest_blog.append(val2)
                        #     try:
                        #         rest_blog.remove(val.blog_id)
                        #     except:
                        #         pass
                rest_blog = blog2.objects.all()

                print self_blog
                # rest_blog.append(val2)
                # print(blg1.blog_id))
                # print self_blog[]
                # print(self_blog)
                # print(self_blog)
                print rest_blog
                # blg2 = blog2.objects.all()
                # print(rest_blog)
                print("Hello")
                # for value in blg2:
                # for value in blg2:
                #     print("value ID", value.id)
                #     for x in blg1:
                #         print("My Blog Id",x.blog_id.id)
                #         if x.blog_id == value.id:
                #             self_blog.append(value)
                #         else:
                #             rest_blog.append(value)
                return render(request, 'mainpage.html', {'rest_blog': rest_blog, 'self_blog': self_blog, 'type': '2'})
        else:
            return render(request, 'login.html',{"message":"Please Login"})

    if request.method == 'POST':
        x = request.POST
        # print(x)
        tempuser = user.objects.filter(email=x['email'],password=x['password'])
        # print(x)
        if tempuser[0]:
            request.session['user'] = tempuser[0].pk
            request.session['type'] = tempuser[0].type
            # print(request.session['type'])
            if request.session['type'] == '1':
                return render(request,'mainpage.html',{'blog2':blog2.objects.all(),'type':'1'})
            elif request.session['type'] == '0':
                return render(request,'mainpage.html',{'blog2':blog2.objects.all(),'type':'0'})
            elif request.session['type'] == '2':
                self_blog = []
                rest_blog = []
                usr = user.objects.get(pk=request.session['user'])
                temp_self_blog = blog1.objects.filter(author_id=usr.id)
                # self_blog = blog2.objects.filter(id=temp_self_blog)
                test_blog = blog2.objects.all()
                # print temp_self_blog
                # print self_blog
                for val in temp_self_blog:
                    for val2 in test_blog:
                        if val2==val.blog_id:
                            self_blog.append(val2)
                        # else:
                        #     if val2 not in rest_blog:
                        #         rest_blog.append(val2)
                        #     try:
                        #         rest_blog.remove(val.blog_id)
                        #     except:
                        #         pass
                rest_blog = blog2.objects.all()

                print self_blog
                # rest_blog.append(val2)
                # print(blg1.blog_id))
                # print self_blog[]
                # print(self_blog)
                # print(self_blog)
                print rest_blog
                # blg2 = blog2.objects.all()
                # print(rest_blog)
                print("Hello")
                # for value in blg2:
                # for value in blg2:
                #     print("value ID", value.id)
                #     for x in blg1:
                #         print("My Blog Id",x.blog_id.id)
                #         if x.blog_id == value.id:
                #             self_blog.append(value)
                #         else:
                #             rest_blog.append(value)
                return render(request, 'mainpage.html', {'rest_blog': rest_blog, 'self_blog': self_blog, 'type': '2'})
                return render(request,'mainpage.html',{'rest_blog':rest_blog,'self_blog':self_blog,'type':'2'})
        else:
            return render(request,'login.html',{"message":"Login again"})

def mainpage(request):
    if request.method == 'GET':
        if 'user' in request.session:
            if request.session['type'] == '1':
                return render(request,'mainpage.html',{'blog2':blog2.objects.all(),'type':'1'})
            elif request.session['type'] == '0':
                return render(request,'mainpage.html',{'blog2':blog2.objects.all(),'type':'0'})
        else:
            return render(request, 'login.html',{"message":"Please Login"})
    if request.method == 'POST':
        x = request.POST
        blog2.title = x['title']
        # blog2.
    return render(request, 'mainpage.html')

def logout(request):
    try:
        del request.session['user']
        del request.session['type']
    except:
        pass
    return render(request,'login.html',{"message":"You are logged out"})

csrf_exempt
def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    # if request.method == 'POST':
    #     x = request.POST
    #     user = user()
    if request.method == 'POST':  # if the form has been filled

        form = user(request.POST)

        # if form.is_valid():  # All the data is valid
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        # creating an user object containing all the data
        user_obj = user(name=name, email=email, password=password)
        # saving all the data in the current object into the database
        user_obj.save()

        return render(request, 'login.html')  # Redirect after POST

    else:
        form = user()  # an unboundform

        return render(request, 'signup.html', {'form': form})
