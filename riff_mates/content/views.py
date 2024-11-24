from django.shortcuts import render
from django.shortcuts import render, redirect 

from content.forms import CommentForm

def comment(request):
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']

            message = f"""
            Received comment from {name}\n\\n
            {comment}
            """

            send_mail("Received comment", message,
                      "admin@gmail.com", ["admin@gmail.com"],
                      fail_silently=False)

            return redirect('comment_accepted')
    
    data = {
        "form": form,
    }

    return render(request, "comment.html", data)


def comment_accepted(request):
    data = {
        "content": """
<h1>Comment Accepted</h1>

<p>Thanks for submitting a comment to <i>RiffMates</i>.</p>
"""
    }

    return render(request, "general.html", data)