# Generated by Django 3.2.9 on 2021-12-14 19:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.IntegerField()),
                ('commentaire', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupe_name', models.CharField(max_length=50)),
                ('nbEtudiants', models.IntegerField()),
                ('mailG', models.EmailField(max_length=30)),
                ('niveau', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ModuleA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_module', models.CharField(max_length=50, unique=True)),
                ('nbheure', models.IntegerField()),
                ('typem', models.CharField(choices=[('optionnel', 'Model optionnel'), ('obligatoire', 'Model obligatoire')], default='optionnel', max_length=11)),
                ('niveauM', models.IntegerField()),
                ('groupeM', models.ManyToManyField(to='Elearning.Groupe')),
            ],
            options={
                'db_table': 'ModuleA_tab',
            },
        ),
        migrations.CreateModel(
            name='Travail_a_Rendre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titreT', models.CharField(max_length=100)),
                ('date_lancement', models.DateField(default=django.utils.timezone.now)),
                ('date_limite', models.DateField(default=django.utils.timezone.now)),
                ('descrip', models.CharField(max_length=150)),
                ('nature_travail', models.CharField(max_length=50)),
                ('pieceTa', models.TextField(max_length=60)),
                ('etat', models.BooleanField()),
                ('eval', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Elearning.evaluation')),
                ('idmodule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Elearning.modulea')),
            ],
            options={
                'db_table': 'Travail_a_Rendre_tab',
            },
        ),
        migrations.CreateModel(
            name='SeancePresontiel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Heure_Debut', models.DateTimeField()),
                ('Heure_Fin', models.DateTimeField()),
                ('objectif', models.TextField(max_length=120)),
                ('resume', models.TextField(max_length=200)),
                ('typeS', models.CharField(choices=[('Normale', 'Normale Seance'), ('Rattrapage', 'Rattrapage Seance'), ('Soutien', 'Soutien Seance'), ('Formation', 'Formation Seance')], default='Normale', max_length=11)),
                ('EtatS', models.CharField(choices=[('En_cours', 'En cours'), ('Terminée', 'Terminée'), ('Anulée', 'Anulée'), ('Différée', 'Différée')], default='Différée', max_length=11)),
                ('numSalle', models.CharField(max_length=4)),
                ('outils', models.CharField(max_length=50)),
                ('idModule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Elearning.modulea')),
            ],
            options={
                'db_table': 'SeancePresontiel_tab',
            },
        ),
        migrations.CreateModel(
            name='SeanceEnLigne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Heure_Debut', models.DateTimeField()),
                ('Heure_Fin', models.DateTimeField()),
                ('objectif', models.TextField(max_length=120)),
                ('resume', models.TextField(max_length=200)),
                ('typeS', models.CharField(choices=[('Normale', 'Normale Seance'), ('Rattrapage', 'Rattrapage Seance'), ('Soutien', 'Soutien Seance'), ('Formation', 'Formation Seance')], default='Normale', max_length=11)),
                ('EtatS', models.CharField(choices=[('En_cours', 'En cours'), ('Terminée', 'Terminée'), ('Anulée', 'Anulée'), ('Différée', 'Différée')], default='Différée', max_length=11)),
                ('idModule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Elearning.modulea')),
            ],
            options={
                'db_table': 'SeanceEnLigne_tab',
            },
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('dateEt', models.DateField(blank=True)),
                ('imageEt', models.ImageField(blank=True, null=True, upload_to='storage/images')),
                ('mailEt', models.EmailField(max_length=60)),
                ('etatEt', models.CharField(choices=[('present', 'Etudiant present'), ('abscent', 'Etudiant abscent'), ('retard', 'Etudiant en retard'), ('exclu', 'Etudiant exclu')], default='present', max_length=11)),
                ('situationEt', models.CharField(choices=[('nouveau', 'Nouveau etudiant'), ('redoublant', 'Etudiant redoublant'), ('derogataire', 'Etudiant derogataire'), ('autre', 'Etudiant autre')], default='autre', max_length=11)),
                ('idgroupe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Elearning.groupe')),
                ('travailarendreE', models.ManyToManyField(to='Elearning.Travail_a_Rendre')),
            ],
            options={
                'db_table': 'Etudiant_tab',
            },
        ),
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_nameens', models.CharField(max_length=50)),
                ('last_nameens', models.CharField(max_length=50)),
                ('mailPerso', models.EmailField(max_length=30)),
                ('mailTravail', models.EmailField(max_length=30)),
                ('imageEns', models.ImageField(blank=True, null=True, upload_to='storage/images')),
                ('module', models.ManyToManyField(to='Elearning.ModuleA')),
            ],
        ),
        migrations.CreateModel(
            name='Enregistrement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomENR', models.CharField(max_length=50, unique=True)),
                ('urlENR', models.CharField(blank=True, max_length=50)),
                ('contenuENR', models.TextField()),
                ('typeENR', models.CharField(blank=True, choices=[('mp4', 'mp4'), ('flv', 'flv'), ('mov', 'mov'), ('avi', 'avi'), ('wmv', 'wmv')], max_length=3)),
                ('descriptionENR', models.CharField(max_length=50)),
                ('dateENR', models.DateField(default=django.utils.timezone.now)),
                ('idseanceEN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Elearning.seanceenligne')),
            ],
            options={
                'db_table': 'Enregistrement_tab',
            },
        ),
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateA', models.DateField(default=django.utils.timezone.now)),
                ('motif', models.TextField(blank=True, max_length=100)),
                ('justificatif', models.TextField(max_length=100)),
                ('idetudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Elearning.etudiant')),
                ('seanceEN', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Elearning.seanceenligne')),
                ('seanceP', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Elearning.seancepresontiel')),
            ],
            options={
                'db_table': 'Absence_tab',
            },
        ),
    ]
