from django.shortcuts import render, redirect
from .models import Bill
from .forms import BillForm

def input_bill(request):
    if request.method == 'POST':
        buyer = request.POST.get('buyer')
        selected_items = request.POST.getlist('item')
        prices = {'keyboard': 500, 'mouse': 400, 'headphones': 800, 'speakers': 100}
        bill_details = []
        total = 0
        for item in selected_items:
            # Corrected this line
            qty = int(request.POST.get(f"{item}_qty", "0"))  
            amount = qty * prices[item]
            total += amount
            bill_details.append((item, qty, amount))

        Bill.objects.create(name=buyer, total_amount=total)

        return render(request, 'bill_app/display.html', {
            'buyer': buyer,
            'bill_details': bill_details,
            'total': total
        })

    return render(request, 'bill_app/bill.html')


def all_bills(request):
    bills = Bill.objects.all()
    return render(request, 'bill_app/all_bills.html', {'bills': bills})
