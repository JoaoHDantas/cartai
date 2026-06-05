from django.shortcuts import render, get_object_or_404
from .models import Chat, Message
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Chat, Message
from chatbot.services.ai_service import perguntar

def chat_list(request):

    chats = Chat.objects.filter(
        usuario=request.user
    ).order_by('-created_at')

    return render(
        request,
        'chat/chat_list.html',
        {
            'chats': chats
        }
    )

def chat_detail(request, chat_id):

    chat = get_object_or_404(
        Chat,
        id=chat_id,
        usuario=request.user
    )

    mensagens = chat.messages.all()

    return render(
        request,
        'chat/chat_detail.html',
        {
            'chat': chat,
            'mensagens': mensagens
        }
    )

def novo_chat(request):

    chat = Chat.objects.create(
        usuario=request.user,
        titulo="Nova conversa"
    )

    return redirect(
        'chat_detail',
        chat_id=chat.id
    )

def enviar_mensagem(request, chat_id):

    chat = get_object_or_404(
        Chat,
        id=chat_id,
        usuario=request.user
    )

    pergunta = request.POST.get("pergunta")

    if not pergunta:
        return redirect(
            "chat_detail",
            chat_id=chat.id
        )

    Message.objects.create(
        chat=chat,
        role="user",
        content=pergunta
    )

    resposta = perguntar(pergunta)

    Message.objects.create(
        chat=chat,
        role="assistant",
        content=resposta
    )

    return redirect(
        "chat_detail",
        chat_id=chat.id
    )