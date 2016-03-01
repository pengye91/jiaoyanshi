# from django.shortcuts import render
# from django.template import RequestContext
from models import *
from django.http import HttpResponse


# Create your views here.
def posts(request):
    john = User(email='john@hotmail.com', first_name='John', last_name='Foo').save()
    ross = User(email='ross@hotmail.com', first_name='Ross', last_name='Bar').save()
    text_post_1 = TextPost(title='test text post 1 for John.',
                           author=john)
    text_post_1.content = 'This is the first time to check the bug.'
    text_post_1.tags = ['nodebug', 'mongoengine', 'djano']
    text_post_1.save()

    link_post_1 = LinkPost(title='test link post 1 for ross',
                           author=ross)
    link_post_1.link_url = 'http://docs.mongoengine.com/'
    link_post_1.tags = ['nodebug', 'mongoengine', 'django']
    link_post_1.save()

    post_num = Post.objects(tags='debug').count()
    return HttpResponse(post_num)


def index(request):
    return HttpResponse('Hello,you are looking at the test project for the Fucking paper of my graduation.')