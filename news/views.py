from django.shortcuts import render_to_response, get_object_or_404
from wammu_web.wammu.helpers import WammuContext
from wammu_web.news.models import Entry, Category

from django.core.paginator import Paginator

from django.conf import settings

# Create your views here.

def entry(request, slug, day = None, month = None, year = None):
    entry = get_object_or_404(Entry, slug = slug)
    return render_to_response('news/entry.html', WammuContext(request, {
        'entry': entry,
    }))

def index(request):
    allnews = Entry.objects.order_by('-pub_date')
    paginator = Paginator(allnews, settings.NEWS_PER_PAGE)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        news = paginator.page(page)
    except (EmptyPage, InvalidPage):
        news = paginator.page(paginator.num_pages)

    return render_to_response('news/index.html', WammuContext(request, {
        'news': news,
    }))

def category(request, slug):
    return ''
