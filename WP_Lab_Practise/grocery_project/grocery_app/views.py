from django.shortcuts import render


selected_items = []

def grocery_form(request):
    global selected_items
    grocery_items = {
        'Milk' : 40,
        'Flour' : 150,
        'Biscuits' : 30,
        'Rice' : 100,
        'Apple' : 15,
        'Sugar': 75
    }
    
    if request.method == 'POST':
        if 'add' in request.POST:
            selected = request.POST.getlist('items')
            for item in selected:
                selected_items.append((item, grocery_items[item]))
        elif 'clear' in request.POST:
            selected_items = []
    
    return render(request,'grocery_app/grocery_form.html',{'grocery_items' : grocery_items,
        'selected_items':selected_items})