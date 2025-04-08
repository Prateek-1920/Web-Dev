from django.shortcuts import render

# Prices dictionary
PRICES = {
    'Mobile': {
        'HP': 15000,
        'Nokia': 12000,
        'Samsung': 18000,
        'Motorola': 16000,
        'Apple': 70000,
    },
    'Laptop': {
        'HP': 40000,
        'Samsung': 45000,
        'Apple': 100000,
        # Nokia and Motorola may not have laptops — optional to handle
    }
}

def show_bill(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        items = request.POST.getlist('item')  # list of selected items
        quantity = int(request.POST.get('quantity'))

        bills = []
        for item in items:
            # Handle missing brand-item price gracefully
            price = PRICES.get(item, {}).get(brand)
            if price is not None:
                total = price * quantity
                bills.append({'item': item, 'brand': brand, 'price': price, 'quantity': quantity, 'total': total})
            else:
                bills.append({'item': item, 'brand': brand, 'error': 'Not Available'})

        return render(request, 'mobile_app/bill.html', {'bills': bills})

    return render(request, 'mobile_app/form.html')
