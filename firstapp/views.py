from django.shortcuts import render, HttpResponse
from firstapp.models import People, Article
from django.template import Context, Template

# Create your views here.
def home(request):
    person = People(name='Spock', job='officer')
    html_string = '''
        <html>
            <head>
                <meta charset="utf-8">
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.6/semantic.css" media="screen" title="no title">
                <title>firstapp</title>
            </head>
            <body>
                <h1 class="ui center aligned icon header">
                    <i class="hand spock icon"></i>
                    Hello, {{ person.name }}
                </h1>
            </body>
        </html>
    '''
    t = Template(html_string)
    c = Context({'person':person})
    web_page = t.render(c)
    return HttpResponse(web_page)

def index(request):
    context = {}
    article_all = Article.objects.all()
    context['article_all'] = article_all
    index_page = render(request, 'index.html', context)
    return index_page
