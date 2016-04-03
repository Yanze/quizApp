from django.conf.urls import patterns, url
from . import views

"""
 - r'^$ basically means empty string
 - r is Regular Expression , it tells Python that a tring is "raw" that
    nothing in the string should be escaped
 - to capture a value from url, just put parenthesis around it (captured argument is
    always a Python string)
"""

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^quiz/$', views.quiz, name='quiz'),
    url(r'^quiz/(?P<question_id>\d+)/$', views.show, name='show'),

)
