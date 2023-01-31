from django.contrib.auth.models import User
from django.db import models
"""
The Investor want invesment but he do not know how?
1. He will regestor in the system
2. He will login into the system
3. He will Create Portfolio with has details
                - basic_balance
                - monthly_pay

4. The AI will generate for him collection invesments depend on:
    - his basic_balance
    - his monthly_pay
    - his target time
        - long time  low   risky invesment
        - mid time   mid   risky invesment
        - short time high  risky invesment
5. The Investor can pick any Collection Invesment he want.
6. The Investor will go to has Dashboard and he see has Portfolio details:
                                                        - Graph invesment
                                                        - Profit
"""


def target_money_time(basic_bal, profit, monthly_pay, target):
    r = ((basic_bal * profit)/100)/12
    if r >= target:
        return 0
    else:
        months = 0
        while ((basic_bal * profit)/100)/12 < target:
            months += 1
            basic_bal += monthly_pay
            if months % 12 == 0:
                basic_bal += (basic_bal*profit)/100
    return months


class Invesment(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    # average_profit = models.DecimalField(max_digits=3, decimal_places=0)
    # risk = models.DecimalField(max_digits=10, decimal_places=0)
    # amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


# This Collection will Genearter by AI
class Collection(models.Model):
    id = models.BigAutoField(primary_key=True)
    profit = models.DecimalField(max_digits=50, decimal_places=0, null=False)
    risk = models.DecimalField(max_digits=50, decimal_places=0, null=False)
    invesments = models.ManyToManyField(Invesment)
    chart = models.ImageField(upload_to='images')


# This portfolio for the Investor
class Portfolio(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    basic_balance = models.DecimalField(max_digits=20, decimal_places=2)
    monthly_pay = models.DecimalField(max_digits=20, decimal_places=2)
    target = models.DecimalField(max_digits=20, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    investor = models.ForeignKey(
            User,
            related_name='portfolios',
            on_delete=models.CASCADE
            )

    collection = models.ManyToManyField(
            Collection
            )

    def __str__(self):
        return self.name

    def get_collection(self):
        return self.collection.last()

    def get_profit(self):
        return self.get_collection().profit

    def get_risk(self):
        return self.get_collection().risk

    def years(self):
        x = target_money_time(self.basic_balance, self.get_profit(),
                              self.monthly_pay, self.target)
        return 0 if (x <= 0) else x / 12

    def months(self):
        x = target_money_time(self.basic_balance, self.get_profit(),
                              self.monthly_pay, self.target)
        return 0 if (x <= 0) else x % 12

    def get_absolute_url(self):
        return '/portfolio/%d/' % self.pk

    class Meta:
        ordering = ['name', 'created']

