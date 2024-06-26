# Generated by Django 4.2.5 on 2023-09-26 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("signal_server", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="participant",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="participants",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="Offer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sdp", models.TextField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "caller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="offers",
                        to="signal_server.participant",
                    ),
                ),
                (
                    "target",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="offer_targets",
                        to="signal_server.participant",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IceCandidate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("candidate", models.TextField()),
                ("sdp_mid", models.CharField(max_length=255)),
                ("sdp_mline_index", models.PositiveIntegerField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "participant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ice_candidates",
                        to="signal_server.participant",
                    ),
                ),
                (
                    "target",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ice_candidate_targets",
                        to="signal_server.participant",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Answer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sdp", models.TextField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "caller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="answers",
                        to="signal_server.participant",
                    ),
                ),
                (
                    "target",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="answer_targets",
                        to="signal_server.participant",
                    ),
                ),
            ],
        ),
    ]
