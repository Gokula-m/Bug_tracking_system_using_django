from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Bug, Project, Comment
from .forms import BugForm, CommentForm


def bug_list(request):
    bugs = Bug.objects.all().order_by('-created_at')
    status_filter = request.GET.get('status')
    if status_filter:
        bugs = bugs.filter(status=status_filter)
    return render(request, 'bugs/bug_list.html', {'bugs': bugs})


def bug_detail(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
    comments = bug.comments.all().order_by('-created_at')

    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.bug = bug
            comment.author = request.user
            comment.save()
            return redirect('bug_detail', pk=pk)
    else:
        form = CommentForm()

    return render(request, 'bugs/bug_detail.html', {
        'bug': bug,
        'comments': comments,
        'form': form
    })


@login_required
def bug_create(request):
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.reported_by = request.user
            bug.save()
            messages.success(request, 'Bug reported successfully!')
            return redirect('bug_detail', pk=bug.pk)
    else:
        form = BugForm()
    return render(request, 'bugs/bug_form.html', {'form': form})


@login_required
def bug_update(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
    if request.method == 'POST':
        form = BugForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bug updated successfully!')
            return redirect('bug_detail', pk=pk)
    else:
        form = BugForm(instance=bug)
    return render(request, 'bugs/bug_form.html', {'form': form, 'bug': bug})

