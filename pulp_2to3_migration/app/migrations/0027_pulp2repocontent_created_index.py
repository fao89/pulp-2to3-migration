# Generated by Django 2.2.19 on 2021-03-22 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pulp_2to3_migration', '0026_p2content_UQ'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='pulp2repocontent',
            index=models.Index(fields=['pulp2_created'], name='pulp_2to3_m_pulp2_c_267ffa_idx'),
        ),
    ]