# Generated by Django 4.1.7 on 2023-04-06 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("boutique", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"ordering": ["-date_added"]},
        ),
        migrations.AlterModelOptions(
            name="order",
            options={"ordering": ["-date_ordered"]},
        ),
        migrations.AlterModelOptions(
            name="orderitem",
            options={"ordering": ["-date_added"]},
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"ordering": ["-date_added"]},
        ),
        migrations.AlterModelOptions(
            name="shippingaddress",
            options={"ordering": ["-date_added"]},
        ),
        migrations.RemoveField(
            model_name="payment",
            name="amount",
        ),
        migrations.RemoveField(
            model_name="payment",
            name="transaction_id",
        ),
    ]
