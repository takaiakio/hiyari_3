# Generated by Django 5.1.1 on 2024-09-05 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nearmissreport',
            name='description',
            field=models.TextField(verbose_name='遭遇場面'),
        ),
        migrations.AlterField(
            model_name='nearmissreport',
            name='frequency',
            field=models.IntegerField(verbose_name='遭遇頻度'),
        ),
        migrations.AlterField(
            model_name='nearmissreport',
            name='mitigation',
            field=models.TextField(verbose_name='ミス回避策'),
        ),
        migrations.AlterField(
            model_name='nearmissreport',
            name='title',
            field=models.CharField(max_length=200, verbose_name='題名'),
        ),
    ]
