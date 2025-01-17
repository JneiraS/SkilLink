# Generated by Django 4.2.16 on 2024-11-13 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mutual_support', '0003_alter_creneau_user_alter_profile_user_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCompetence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_offering', models.BooleanField(default=True)),
                ('competence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mutual_support.competence')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mutual_support.profile')),
            ],
        ),
    ]
