# Generated by Django 4.1.1 on 2024-11-02 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('rating', models.IntegerField(default=None)),
                ('released', models.DateField(default=None)),
                ('description', models.TextField(default=None)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('genre', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='viewer.genre')),
            ],
        ),
    ]