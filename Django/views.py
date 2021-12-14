
from django.http import HttpResponse
import random

from django.template.loader import render_to_string

from articles.models import horario
from articles.models import dirigente
from articles.models import entidad
from articles.models import sala




def home_view(request):

    #name = "yo"
    #number = random.randint(10,20)

    #article_title = article_obj.title
    #article_content = article_obj.content


    horario_obj = horario.objects.get(id=2)

    context = {
        "dirigente": horario_obj.dirigente,
        "sala": horario_obj.sala
    }
    HTML_String = render_to_string("home-view.html", 
    context = context
    )
    # HTML_String ="""
    # <h1>{dirigente}</h1> 
    # <p>{sala}</p>""".format(**context)

    return HttpResponse(HTML_String)