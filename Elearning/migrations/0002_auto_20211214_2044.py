# Generated by Django 3.2.9 on 2021-12-14 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Elearning', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('enseignant_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Elearning.enseignant')),
            ],
            options={
                'db_table': 'responsable_tab',
            },
            bases=('Elearning.enseignant',),
        ),
        migrations.RemoveField(
            model_name='enseignant',
            name='module',
        ),
        migrations.AddField(
            model_name='modulea',
            name='ens',
            field=models.ManyToManyField(to='Elearning.Enseignant'),
        ),
        migrations.AlterModelTable(
            name='modulea',
            table='Module_tab',
        ),
    ]
