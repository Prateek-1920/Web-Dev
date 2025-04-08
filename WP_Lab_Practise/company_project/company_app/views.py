from django.shortcuts import render
from .models import Works, Lives

def search_company(request):
    result = []
    company = ""

    if request.method == 'POST':
        company = request.POST['company_name']
        works = Works.objects.filter(company_name=company)

        for person in works:
            try:
                city = Lives.objects.get(person_name=person.person_name).city
            except Lives.DoesNotExist:
                city = "City Unknown"
            result.append((person.person_name, city))

    return render(request, 'search.html', {'results': result, 'company': company})
