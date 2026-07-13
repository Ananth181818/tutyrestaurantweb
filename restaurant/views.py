from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.urls import path
from .models import RoomBooking
from datetime import datetime
def menu_veg(request):
    # Vegetarian items
    veg_items = [
        {'name': 'Paneer Butter Masala', 'price': 220, 'desc': 'Creamy tomato gravy with paneer cubes'},
        {'name': 'Veg Biryani', 'price': 180, 'desc': 'Basmati rice with mixed vegetables & spices'},
        {'name': 'Dal Tadka', 'price': 150, 'desc': 'Yellow dal with garlic tadka'},
        {'name': 'Gobi 65', 'price': 160, 'desc': 'Crispy cauliflower with spices'},
        {'name': 'Veg Meals', 'price': 120, 'desc': 'Rice, sambar, rasam, 3 curries, papad'},
    ]
    return render(request, 'menu_partial.html', {'items': veg_items, 'type': 'Vegetarian'})
def menu_nonveg(request):
    # Non-Vegetarian items
    nonveg_items = [
        {'name': 'Chicken Biryani', 'price': 250, 'desc': 'Dum cooked basmati with tender chicken'},
        {'name': 'Fish Curry Meals', 'price': 280, 'desc': 'Rice with meen kuzhambu & 2 sides'},
        {'name': 'Mutton Chukka', 'price': 320, 'desc': 'Spicy dry mutton roast'},
        {'name': 'Chicken 65', 'price': 200, 'desc': 'Spicy deep fried chicken chunks'},
        {'name': 'Prawn Masala', 'price': 300, 'desc': 'Prawns in onion-tomato gravy'},
    ]
    return render(request, 'menu_partial.html', {'items': nonveg_items, 'type': 'Non-Vegetarian'})
def index_view(request):
    return render(request, 'index.html')
def knowmore_view(request):
    return render(request, 'knowmore.html')
def aboutus_view(request):
    return render(request, 'aboutus.html')
def contact_view(request):
    return render(request, 'contact.html')
def party_view(request):
    return render(request, 'party.html')
def orders_view(request):
    item_name = request.GET.get('name')
    item_price = request.GET.get('price')
    context = {}
    if item_name and item_price:
        context['ordered_item'] = {
            'name': item_name,
            'price': item_price
        }
    return render(request, 'orders.html', context)
def roombook_view(request):
    if request.method == 'POST':
        guest_name = request.POST.get('guest_name')
        guest_phone = request.POST.get('guest_phone')
        room_type = request.POST.get('room_type')
        price = request.POST.get('price')
        check_in_str = request.POST.get('check_in')
        check_out_str = request.POST.get('check_out')

        if not (guest_name and guest_phone and room_type and check_in_str and check_out_str):
            return render(request, 'roombook.html', {
                'room_type': room_type,
                'price': price,
                'error': 'Please fill out all booking fields.',
                'guest_name': guest_name,
                'guest_phone': guest_phone,
                'check_in': check_in_str,
                'check_out': check_out_str,
            })
        
        try:
            check_in = datetime.strptime(check_in_str, '%Y-%m-%d').date()
            check_out = datetime.strptime(check_out_str, '%Y-%m-%d').date()
            
            booking = RoomBooking.objects.create(
                guest_name=guest_name,
                guest_phone=guest_phone,
                room_type=room_type,
                price=price,
                check_in=check_in,
                check_out=check_out
            )
            return render(request, 'roombook.html', {
                'success': True,
                'booking': booking
            })
        except Exception as e:
            return render(request, 'roombook.html', {
                'room_type': room_type,
                'price': price,
                'error': f'Booking failed: {str(e)}',
                'guest_name': guest_name,
                'guest_phone': guest_phone,
                'check_in': check_in_str,
                'check_out': check_out_str,
            })
            
    room_type = request.GET.get('room_type', 'Standard Room')
    price = request.GET.get('price', '1200')
    return render(request, 'roombook.html', {
        'room_type': room_type,
        'price': price
    })
def couple_view(request):
    return render(request, 'couple.html')
def couplenon_view(request):
    return render(request, 'couplenon.html')
def family_view(request):
    return render(request, 'family.html')
def familynon_view(request):
    return render(request, 'familynon.html')
def veg_menu(request):
    return render(request, 'projecthotelnav.html')

def nonveg_menu(request):
    return render(request, 'projecthotelnon.html')

# --- Authentication API Endpoints ---

def login_api(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        
        if not email or not password:
            return JsonResponse({'success': False, 'error': 'Please fill in all fields.'})
        
        # Authenticate using email as the username
        user = auth.authenticate(request, username=email, password=password)
        
        if user is not None:
            auth.login(request, user)
            return JsonResponse({
                'success': True,
                'user': {
                    'name': user.first_name or user.username,
                    'email': user.email
                }
            })
        else:
            # Check if user exists to give better feedback
            if User.objects.filter(username=email).exists():
                return JsonResponse({'success': False, 'error': 'Incorrect password.'})
            else:
                return JsonResponse({'success': False, 'error': 'No account found with this email. Please register.'})
                
    return JsonResponse({'success': False, 'error': 'Invalid request method.'})


def register_api(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        
        if not name or not email or not password:
            return JsonResponse({'success': False, 'error': 'Please fill in all fields.'})
            
        if User.objects.filter(username=email).exists():
            return JsonResponse({'success': False, 'error': 'An account with this email already exists.'})
            
        try:
            # Create user using email as username
            user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
            user.save()
            
            # Log the user in immediately after registration
            auth.login(request, user)
            
            return JsonResponse({
                'success': True,
                'user': {
                    'name': user.first_name,
                    'email': user.email
                }
            })
        except Exception as e:
            return JsonResponse({'success': False, 'error': f'Registration failed: {str(e)}'})
            
    return JsonResponse({'success': False, 'error': 'Invalid request method.'})


def logout_api(request):
    if request.method == 'POST':
        auth.logout(request)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request method.'})



def projecthotelnav(request):
    return render(request, 'projecthotelnav.html')

def projecthotelnon(request):
    return render(request, 'projecthotelnon.html')