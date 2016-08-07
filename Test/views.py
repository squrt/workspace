import os
from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
from django.template import loader, Context
from django import forms
# from builtins import str
from Test.models import Employee, Author, Book


# Create your views here.


def index(req, id):
    ''' if-elif-else
    if id=='1':
        return index1(req)
    elif id=='2':
        index2(req)
    elif id=='3':
       return  index3(req)
    else:
       pass
    return
   '''
    # dic + lanmda表达式实现
    fun = {'1': lambda req: index1(req), '2': lambda req: index2(req), '3': lambda req: index3(req),}
    return fun[id](req)  # return  fun[id].__call__(req)


def index1(req):
    return HttpResponse('Hello World!')


def index2(req):
    t = loader.get_template('index.html')
    c = Context({})
    return HttpResponse(t.render(c))


class Person(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def Say(self):
        return "我是" + self.name + ',年龄' + str(self.age)


def index3(req):
    # return render_to_response('index.html',Context())
    person = Person('person', 11, 'F')
    user = {'name': 'test', 'age': 12, 'sex': 'm'}
    book_list = ['Python', 'DjangoApp', 'MySQL']
    # if  userForIF={'name':'test','age':12,'sex':'m'}
    # return render_to_response('index.html',{'user':user,'title':'index3','person':person,'book_list':book_list,'userForIF':userForIF})
    return render_to_response('index.html', {'user': user, 'title': 'index3', 'person': person, 'book_list': book_list})


def index4(req):
    c = Employee.objects.all().count()
    if c < 20:
        e = Employee(name='test' + str(c))
        e.save()

    emps = Employee.objects.all()
    emps1 = tuple(emps)
    return render_to_response('employee.html', {'emps': emps, 'emps1': emps1})


def show_author(req):
    authors = Author.objects.all()
    return render_to_response('showdb.html', {'title': '操作数据库', 'authors': authors})


def show_book(req):
    books = Book.objects.all()
    return render_to_response('showdb.html', {'title': '操作数据库', 'books': books})


class UserForm(forms.Form):
    name = forms.CharField()
    imgfile = forms.FileField()


from Test.models import ImgFile


def register(req):
    if req.method == 'POST':
        try:
            form = UserForm(req.POST, req.FILES)
            print(form)
            if form.is_valid():
                print(form.cleaned_data['name'])
                print(form.cleaned_data['imgfile'])

                '''直接写文件
                img=form.cleaned_data['imgfile'].read()
                f=open('/home/kqb/'+form.cleaned_data['imgfile'].name,'wb')
                f.write(img)
                f.close()
                '''
                f = ImgFile()
                f.name = form.cleaned_data['name']
                f.imgfile = form.cleaned_data['imgfile']
                f.save()
                return HttpResponse('OK')
        except:
            return HttpResponse('Failed')
    else:
        form = UserForm()

    return render_to_response('form.html', {'form': form})