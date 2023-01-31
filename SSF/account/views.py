from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout as user_logout
from django.contrib.auth.models import User
from django.views import View

# def dashboard(request):
#     if request.user.is_authenticated:
#         print(request.user)
#         print(request.user.landmarks.iterator)
#         context = {
#                    "user": request.user,
#                    "profiles": request.user.profiles.iterator
#                    }
#         return render(request, "index.html", context)
#     else:
#         return HttpResponseRedirect("/account/login/")

prefix_login_url = '/account/login/'
postfix_login_url = '/'


class LoginView(View):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(postfix_login_url)
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):

        if not self.request.user.is_authenticated:

            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(postfix_login_url)

            return render(request, self.template_name, {"error": "password is incorrect"})

        return HttpResponseRedirect(postfix_login_url)


class SignUpView(View):
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):

        errors = []

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # name = request.POST.get('name')
        username = request.POST.get('username')
        # email = request.POST.get('email') or ""
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if User.objects.filter(username=username).exists():
            errors.append("username have already taken")

        # if User.objects.exists(email=email):
        #     errors["email"] = "الايميل موجود مسبقا"

        if password != password1:
            errors.append("password is not match")

        if errors == []:
            user_creater = User(username=username, is_superuser=False,
                                first_name=first_name, last_name=last_name, )
            user_creater.set_password(raw_password=password1)
            user_creater.save()

            user = authenticate(request, username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(postfix_login_url)

        return render(request, self.template_name, {"errors": errors})


def logout(request):

    if request.user.is_authenticated:
       user_logout(request)

    return HttpResponseRedirect(prefix_login_url)
