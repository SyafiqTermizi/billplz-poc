# Generated by Django 3.0.4 on 2020-03-21 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Billplzbill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_id', models.CharField(max_length=255)),
                ('collection_id', models.CharField(max_length=255)),
                ('paid', models.BooleanField(default=False)),
                ('paid_amount', models.IntegerField(default=0)),
                ('amount', models.IntegerField()),
                ('paid_at', models.DateTimeField(blank=True, null=True)),
                ('due_at', models.DateTimeField()),
                ('description', models.TextField(blank=True)),
                ('url', models.URLField()),
                ('state', models.CharField(choices=[('due', 'due'), ('paid', 'paid')], default='due', max_length=255)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='receipts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BillPlzUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(max_length=255)),
                ('bill', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='billplz.Billplzbill')),
            ],
        ),
    ]
