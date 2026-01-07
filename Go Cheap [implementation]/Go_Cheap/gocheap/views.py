from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Users,Trips


@login_required(login_url='login')
def home(request):
    # جلب قيم البحث من الـ GET request
    pickup_query = request.GET.get('pickup', '')
    dropoff_query = request.GET.get('destination', '')

    trips = Trips.objects.all()

    # فلترة حسب البحث لو فيه قيمة
    if pickup_query:
        trips = trips.filter(PickupArea__icontains=pickup_query)
    if dropoff_query:
        trips = trips.filter(DropoffArea__icontains=dropoff_query)

    # ترتيب حسب السعر من الأقل للأعلى
    trips = trips.order_by('Price')


    # لو الصفحة أول مرة تتفتح ومفيش بحث، خلي الكروت افتراضيه بتاعة "0"
    if not pickup_query and not dropoff_query:
        trips = [
            {
                'Company': {'CompanyName': 'Company_0'},
                'Price': 0,
                'PickupArea': 'Pickup_0',
                'DropoffArea': 'Destination_0',
                'Driver': {'Name': 'Driver_0', 'CarModel': 'Car_0'},
                'TripDurationMin': 0,
                'DistanceKM': 0
            } for _ in range(3)
        ]

    return render(request, 'home.html', {
        'trips': trips,
        'pickup': pickup_query,
        'dropoff': dropoff_query
    })
def login_view(request):
    login_error = None
    signup_error = None

    if request.method == "POST":

        # ---------- LOGIN ----------
        if 'login' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                login_error = "Email or password is incorrect."

        # ---------- SIGNUP ----------
        elif 'signup' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            password = request.POST.get('password')

            # تحقق من عدم وجود مستخدم بنفس الإيميل
            if Users.objects.filter(email=email).exists():
                signup_error = "Email is already registered."
            else:
                user = Users.objects.create_user(
                    email=email,
                    password=password,
                    name=name,
                    phone=phone
                )
                login(request, user)
                return redirect('home')

    return render(request, 'login.html', {
        'login_error': login_error,
        'signup_error': signup_error
    })