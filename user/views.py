from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, FormView, View, DetailView
from user.forms import Registrationform, UserForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from user.models import Userdetails
from master.models import Cruise, Hall, Food
import razorpay
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class Userhomeview(TemplateView):
    template_name = 'userhome.html'


class Registrationview(FormView):
    template_name = 'reg.html'
    form_class = UserForm

    def get(self, request, *args, **kwargs):
        self.object = None

        form_class = self.get_form_class()
        user_form = self.get_form(form_class)
        cust_form = Registrationform()
        return self.render_to_response(self.get_context_data(form1=user_form, form2=cust_form))

    def post(self, request, *args, **kwargs):
        self.object = None

        form_class = self.get_form_class()
        user_form = self.get_form(form_class)
        cust_form = Registrationform(self.request.POST)
        if (user_form.is_valid() and cust_form.is_valid()):
            return self.form_valid(user_form, cust_form)
        else:
            return self.form_invalid(user_form, cust_form)

    def form_valid(self, user_form, cust_form):
        self.object = user_form.save()  # User model save

        self.object.is_staff = True  # edit user object
        self.object.save()
        cust_obj = cust_form.save(commit=False)  # Customer Model save(contact,address,place)
        cust_obj.basic_data = self.object  # saving OneToOnefield ,edit cust_obj
        cust_obj.save()
        return super(Registrationview, self).form_valid(user_form)

    def form_invalid(self, user_form, cust_form):
        return self.render_to_response(self.get_context_data(form1=user_form, form2=cust_form))

    def get_success_url(self, **kwargs):
        return ('/user/success/')


class Successview(TemplateView):
    template_name = 'success.html'


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        form = LoginForm
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # print(request.user)

            try:
                user_obj = User.objects.get(username=request.user)
                cust = Userdetails.objects.get(basic_data=user_obj)

            except:
                user_obj = None
                cust = None

            if request.user.is_superuser:
                return redirect('/master/masterhome')
            else:
                return redirect('/user/userhome')
        else:
            return redirect('/user/login')


class Userprofileview(View):
    template_name = 'userprofile.html'

    def get(self, request, pk):
        uname = request.user
        user_obj = User.objects.get(username=uname)
        cust_obj = Userdetails.objects.get(basic_data=user_obj)
        context = {'customer': cust_obj,
                   }
        return render(request, self.template_name, context)


class Usercruisesview(ListView):
    template_name = 'usercruise.html'
    model = Cruise
    context_object_name = 'list'


class Uvdcruiseview(DetailView):
    template_name = 'usercruisedetails.html'
    model = Cruise


def payment(request):
    if request.method == "POST":
        name = request.POST.get('username')
        amount = 500

        client = razorpay.Client(
            auth=("rzp_test_rYcuWKCygjkElZ", "zTxPVsOVV2k9AGxlpTikUeBg"))
        payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})

    return render(request, 'payment.html')


@csrf_exempt
def success(request):
    return render(request, "success1.html")


class Bookcruiseview(DetailView):
    model = Cruise
    template_name = 'payment.html'


class Userhallview(ListView):
    template_name = 'userhall.html'
    model = Hall
    context_object_name = 'list'


class Userhalldetview(DetailView):
    template_name = 'userhalldetails.html'
    model = Hall


def payment1(request):
    if request.method == "POST":
        name = request.POST.get('username')
        amount = 500

        client = razorpay.Client(
            auth=("rzp_test_rYcuWKCygjkElZ", "zTxPVsOVV2k9AGxlpTikUeBg"))
        payment1 = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})

    return render(request, 'payment1.html')


@csrf_exempt
def success(request):
    return render(request, "success1.html")


class Bookhallview(DetailView):
    model = Hall
    template_name = 'payment1.html'


class Userfoodview(ListView):
    template_name = 'userfood.html'
    model = Food
    context_object_name = 'list'

class Userfooddetview(DetailView):
    template_name = 'userfooddetails.html'
    model = Food

def payment2(request):
    if request.method == "POST":
        name = request.POST.get('username')
        amount = 500

        client = razorpay.Client(
            auth=("rzp_test_rYcuWKCygjkElZ", "zTxPVsOVV2k9AGxlpTikUeBg"))
        payment1 = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})

    return render(request, 'payment2.html')


@csrf_exempt
def success(request):
    return render(request, "success1.html")


class Bookfoodview(DetailView):
    model = Food
    template_name = 'payment2.html'