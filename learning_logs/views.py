from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    """Página principal do learning_log"""
    return render(request, "learning_logs/index.html")

def topics(request):
    """Página referente aos tópicos"""
    topics = Topic.objects.order_by("date_added")
    context = {"topics": topics}
    return render(request, "learning_logs/topics.html", context)

def topic(request, topic_id):
    """Mostra um único assunto e as suas respectivas entradas"""
    topic = Topic.objects.get(id = topic_id)
    entries = topic.subject_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "learning_logs/topic.html", context)
