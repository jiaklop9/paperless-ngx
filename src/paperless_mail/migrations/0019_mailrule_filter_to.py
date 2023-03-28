# Generated by Django 4.1.7 on 2023-03-11 21:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("paperless_mail", "0018_processedmail"),
    ]

    operations = [
        migrations.AddField(
            model_name="mailrule",
            name="filter_to",
            field=models.CharField(
                blank=True,
                max_length=256,
                null=True,
                verbose_name="filter to",
            ),
        ),
    ]
