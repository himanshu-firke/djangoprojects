from django.shortcuts import render
from .forms import TextForm
import markdown  # To handle Markdown conversion

def convert_text(request):
    html_output = None  # To store the converted HTML

    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            html_output = markdown.markdown(text)  # Convert text to HTML
    else:
        form = TextForm()
    
    return render(request, "converter/index.html", {"form": form, "html_output": html_output})
