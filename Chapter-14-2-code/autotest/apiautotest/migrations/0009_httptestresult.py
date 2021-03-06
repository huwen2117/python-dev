# Generated by Django 2.0.5 on 2018-09-01 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiautotest', '0008_httptest_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='HttpTestResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('httprunresults', models.CharField(max_length=50, verbose_name='运行结果id')),
                ('httptest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiautotest.HttpTest', verbose_name='测试')),
            ],
        ),
    ]
