# Generated by Django 2.0.6 on 2019-06-07 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='kind',
            field=models.CharField(blank=True, choices=[('regular', 'Regular'), ('novel', 'Novel'), ('fiction', 'Fiction')], max_length=200, null=True),
        ),
    ]
