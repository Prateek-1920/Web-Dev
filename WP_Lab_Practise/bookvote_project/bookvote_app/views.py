from django.shortcuts import render

votes = {'Good' : 0, 'Satisfactory' : 0, 'Bad' : 0}

def vote_view(request):
    global votes
    
    if request.method=='POST':
        choice = request.POST.get('vote')
        if choice in votes:
            votes[choice]+=1
    
    total_votes = sum(votes.values())
    percentages = {
        key : (value/total_votes) * 100 if total_votes >0 else 0 for key, value in votes.items()
    }
    
    return render(request,'bookvote_app/vote.html',
                  {
                      'votes' : votes,
                      'percentages' : percentages,
                      'total_votes' : total_votes
                  })

    