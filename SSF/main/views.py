from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from .models import Portfolio, Collection, Invesment, target_money_time
import json

prefix_login_url = '/account/login/'
postfix_login_url = '/'


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/account/login/")

    print(request.user)
    print(request.user.portfolios.iterator)

    context = {
            "user": request.user,
            "portfolios": request.user.portfolios.iterator,
            }
    return render(request, "index.html", context)


# portfolios
def portfolio_create(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(prefix_login_url)
    return render(request, "portfolio.html")


# This function for get profiles and output as json
# @csrf_exempt
def collections(request):

    if not request.user.is_authenticated:
        return JsonResponse({'status': 'error', 'message': 'Unauthorized'}, status=401)

    if request.method != "POST":
        return HttpResponseRedirect(prefix_login_url)
        # return JsonResponse({"error": "404"})

    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.decoder.JSONDecoderError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        # users = User.objects.all().values('first_name', 'last_name')  # or simply .values() to get all fields
        # users_list = list(users)  # important: convert the QuerySet to a list object
        # return JsonResponse(users_list, safe=False)
        portfolio = {
                # "user": request.user.first_name,
                "name"         : data.get("name"),
                "basic_balance": data.get("basic_balance"),
                "monthly_pay"  : data.get("monthly_pay"),
                "target_money" : data.get("target_money"),
                }

        collections = [
                {
                 "id": collection.id,
                 "profit": int(collection.profit),
                 "risk": int(collection.risk)
                 }

                for collection in Collection.objects.filter(portfolio__isnull=True)
                # for collection in Collection.objects.all()
                ]

        data = {
                 "portfolio": portfolio,
                 "collections": collections
               }
        return JsonResponse(data)


def select_collection(request, id, name, b, mp, tm):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(prefix_login_url)
    # print(id, name, b, mp, tm)

    Portfolio.objects.create(
            name=name, basic_balance=b, monthly_pay=mp, target=tm,
            investor=request.user, collection=Collection.objects.get(id=id)
            )
    return HttpResponseRedirect("/")


def settings(request):
    return render(request, 'settings.html')


def about(request):
    return render(request, "about.html")
