# Generated by Django 4.2.2 on 2023-06-29 08:23

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('geometry', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plots', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
