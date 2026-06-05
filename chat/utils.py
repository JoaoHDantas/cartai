def obter_historico(chat):
    
    mensagens = []

    for msg in chat.messages.all():
        mensagens.append({
            "role": msg.role,
            "content": msg.content
        })

    return mensagens