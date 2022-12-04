# Generated by Django 3.2.7 on 2022-12-04 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0002_rename_rating_profile_rating_profile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('timestampeduuidmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.timestampeduuidmodel')),
                ('rating_rate', models.IntegerField(choices=[(1, 'Poor'), (2, 'Fair'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')], default=0, help_text='1=Poor, 2=Fair, 3=Good, 4=Very Good, 5=Excellent', verbose_name='Rating')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agent_review', to='profiles.profile', verbose_name='Agent being rated')),
                ('rater', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User Providing the rating')),
            ],
            options={
                'unique_together': {('rater', 'agent')},
            },
            bases=('common.timestampeduuidmodel',),
        ),
    ]
