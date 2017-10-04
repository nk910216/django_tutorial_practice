from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from .forms import NewTopicForm, NewTopicReplyForm
from .models import Board, Topic, Post
# Create your views here.

def test_for_regex(request, key_word):
    return HttpResponse(key_word)

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
    # try:
    #    board = Board.objects.get(pk=pk)
    # except Board.DoesNotExist:
    #    raise Http404
    board = get_object_or_404(Board, pk=pk)
    topics = board.topics.order_by('-last_updated').annotate(replies=Count('posts'))
    return render(request, 'topics.html', {'board': board, 'topics': topics})

@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    # ToDO : get the currently login user
    # user = User.objects.first()

    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = request.user
            topic.save()
            post = Post.objects.create(
                    message=form.cleaned_data.get('message'),
                    topic=topic, 
                    created_by=request.user)
            return redirect('boards.topic_posts', pk=board.pk, topic_pk=topic.pk)
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'form': form, 'board': board})
'''  old method
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first()

        topic = Topic.objects.create(
                subject=subject, board=board, starter=user)

        post = Post.objects.create(
                message=message, topic=topic, created_by=user)

        return redirect('boards.topics', pk = board.pk)

    return render(request, 'new_topic.html', {'board': board})
'''

def topic_posts(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    topic.views += 1
    topic.save()
    return render(request, 'topic_posts.html', {'topic': topic})

@login_required
def topic_reply(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    if request.method == 'POST':
        form = NewTopicReplyForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()

            return redirect('boards.topic_posts', pk=pk, topic_pk=topic_pk)

    else:
        form = NewTopicReplyForm()

    return render(request, 'topic_reply.html', {'topic': topic, 'form': form})
