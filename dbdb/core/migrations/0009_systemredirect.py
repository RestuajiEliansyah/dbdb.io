# Generated by Django 2.0.3 on 2018-06-14 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_fix_countries'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemRedirect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='redirects', to='core.System')),
            ],
        ),
    ]
