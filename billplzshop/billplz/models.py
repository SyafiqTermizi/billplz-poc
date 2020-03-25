from django.db import models

from django.contrib.auth import get_user_model

UserModel = get_user_model()

bill_state_choices = [
    ('due', 'due'),
    ('paid', 'paid')
]


class Billplzbill(models.Model):
    bill_id = models.CharField(max_length=255)
    collection_id = models.CharField(max_length=255, )
    paid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(default=0)
    amount = models.IntegerField()
    paid_at = models.DateTimeField(blank=True, null=True)
    due_at = models.DateTimeField()
    description = models.TextField(blank=True)
    url = models.URLField()
    state = models.CharField(
        max_length=255,
        choices=bill_state_choices,
        default='due'
    )
    created_by = models.ForeignKey(
        UserModel,
        null=True,
        on_delete=models.SET_NULL,
        related_name='receipts'
    )

    def __str__(self):
        return self.bill_id


class BillPlzUser(models.Model):
    """
    If bill is not created django.auth.user, we create a billplz user here
    """
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=255)
    bill = models.OneToOneField(Billplzbill, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
