from django.conf import settings
from django.db import models


class Chat(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="chats"
    )

    titulo = models.CharField(
        max_length=255,
        default="Nova conversa"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Message(models.Model):
    ROLE_CHOICES = [
        ("user", "Usuário"),
        ("assistant", "Assistente"),
    ]

    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        related_name="messages"
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]