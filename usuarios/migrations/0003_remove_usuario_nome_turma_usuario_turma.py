# Generated by Django 4.1.7 on 2023-03-20 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_turma_usuario_nome_turma'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='nome_turma',
        ),
        migrations.AddField(
            model_name='usuario',
            name='turma',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.turma'),
            preserve_default=False,
        ),
    ]