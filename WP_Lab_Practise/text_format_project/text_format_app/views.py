from django.shortcuts import render

def text_formatter(request):
    formatted_text = ""
    if request.method == "POST":
        name = request.POST.get("name", "")
        message = request.POST.get("message", "")
        bold = "bold" if request.POST.get("bold") else ""
        italic = "italic" if request.POST.get("italic") else ""
        underline = "underline" if request.POST.get("underline") else ""
        color = request.POST.get("color", "#000000")

        formatted_text = f"<span style='color: {color}; font-weight: {bold}; font-style: {italic}; text-decoration: {underline};'>{name}: {message}</span>"

    return render(request, "text_format_app/index.html", {"formatted_text": formatted_text})
