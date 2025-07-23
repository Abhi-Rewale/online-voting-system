from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from .models import Election, Candidate, Vote

@login_required
def election_list(request):
    elections = Election.objects.all()
    return render(request, 'election/election_list.html', {'elections': elections})

@login_required
def election_detail(request, election_id):
    election = get_object_or_404(Election, id=election_id)
    candidates = Candidate.objects.filter(election=election)

    # ✅ Check if user has already voted
    user_has_voted = Vote.objects.filter(voter=request.user, candidate__election=election).exists()

    return render(request, 'election/election_detail.html', {
        'election': election,
        'candidates': candidates,
        'user_has_voted': user_has_voted
    })

@login_required
def vote(request, election_id):
    election = get_object_or_404(Election, id=election_id)

    # ✅ Prevent duplicate vote before processing form
    if Vote.objects.filter(voter=request.user, candidate__election=election).exists():
        messages.warning(request, "⚠️ You have already voted in this election.")
        return redirect('election_detail', election_id=election.id)

    if request.method == 'POST':
        candidate_id = request.POST.get('candidate')

        # ✅ Check if a candidate was selected
        if candidate_id:
            candidate = get_object_or_404(Candidate, id=candidate_id, election=election)
            Vote.objects.create(voter=request.user, candidate=candidate, election=election)
            messages.success(request, "✅ Thank you for voting!")
        else:
            messages.error(request, "⚠️ Please select a candidate before submitting.")

        return redirect('election_detail', election_id=election.id)

    # ✅ Only POST is allowed
    return redirect('election_detail', election_id=election.id)


@login_required
def election_results(request, election_id):
    election = get_object_or_404(Election, pk=election_id)
    candidates = Candidate.objects.filter(election=election)

    vote_counts = Vote.objects.filter(candidate__in=candidates)\
                              .values('candidate__name')\
                              .annotate(total=Count('id'))

    labels = [vc['candidate__name'] for vc in vote_counts]
    data = [vc['total'] for vc in vote_counts]

    context = {
        'election': election,
        'labels': labels,
        'data': data,
    }
    return render(request, 'election/election_result.html', context)


@login_required
def my_votes(request):
    user_votes = Vote.objects.select_related('election', 'candidate')\
                             .filter(voter=request.user)\
                             .order_by('-voted_at')

    return render(request, 'election/my_votes.html', {'user_votes': user_votes})