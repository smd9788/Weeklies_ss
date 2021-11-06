from django.db import models
from django.utils import timezone

class SecurityPool(models.Model):
    title = models.CharField(max_length=200)
    securities = models.ManyToManyField('Security')
    start_price = models.DecimalField(max_digits=10, decimal_places=2)
    end_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['id']

    def get_final_price_change(self):
        return self.end_price - self.start_price

    def __str__(self):
        return self.title


class Contest(models.Model):
    end_date = models.DateTimeField('end date', default=None)
    entry_fee = models.DecimalField(max_digits=8, decimal_places=2)
    num_contestants = models.IntegerField(default=2)
    start_date = models.DateTimeField('start date', default=None)
    security_pool_id = models.ForeignKey(SecurityPool, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title
        

class Security(models.Model):
    last_price = models.DecimalField(max_digits=10, decimal_places=2)
    price_date = models.DateTimeField('price date')
    security_name = models.CharField(max_length=140)
    ticker = models.CharField(max_length=8)

    class Meta:
        ordering = ['ticker']

    def was_priced_today(self):
        t = timezone.now()
        pd = self.price_date

        today = t.year + t.month + t.day
        price_date = pd.year + pd.month + pd.day

        return price_date == today

    def __str__(self):
        return self.ticker
