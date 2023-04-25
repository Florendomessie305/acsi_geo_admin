# Generated by Django 4.2 on 2023-04-22 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategorieCimetiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_categorie', models.CharField(max_length=200, unique=True)),
                ('description', models.CharField(default='description de la categorie', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cimetiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_cimetiere', models.CharField(max_length=200, unique=True)),
                ('superficie', models.FloatField()),
                ('description', models.TextField()),
                ('categorie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cimetieres', to='api.categoriecimetiere')),
            ],
        ),
        migrations.CreateModel(
            name='Defunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.CharField(max_length=200)),
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(blank=True, max_length=200, null=True)),
                ('genre', models.CharField(blank=True, choices=[('Monsieur', 'Monsieur'), ('Madame', 'Madame'), ('Mademoiselle', 'Mademoiselle')], max_length=15)),
                ('nationalite', models.CharField(max_length=200)),
                ('date_naiss', models.DateField()),
                ('date_deces', models.DateField()),
                ('date_inhumation', models.DateField()),
                ('statut', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Localite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_localite', models.CharField(max_length=200, unique=True)),
                ('superficie', models.FloatField()),
                ('description', models.TextField(default='description')),
            ],
        ),
        migrations.CreateModel(
            name='Tombe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_tombe', models.CharField(max_length=200)),
                ('lat', models.FloatField(default=0.0)),
                ('lon', models.FloatField(default=0.0)),
                ('cimetiere', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tombes', to='api.cimetiere')),
            ],
        ),
        migrations.CreateModel(
            name='Exhumation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_exhumation', models.DateField()),
                ('defunt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhumations', to='api.defunt')),
                ('last_cimetiere', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exhumations', to='api.cimetiere')),
                ('new_cimetiere', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='new_r_inhumations', to='api.cimetiere')),
            ],
        ),
        migrations.AddField(
            model_name='defunt',
            name='tombe',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='defunt', to='api.tombe'),
        ),
        migrations.AddField(
            model_name='cimetiere',
            name='localite',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cimetieres', to='api.localite'),
        ),
    ]