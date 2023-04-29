from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.utils import timezone
from forum.models import Postagem


def index(request):
    # Recupera as sessões ativas
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    user_id_list = []

    # Recupera os IDs de usuário das sessões ativas
    for session in sessions:
        data = session.get_decoded()
        user_id_list.append(data.get('_auth_user_id', None))

    # Recupera os objetos de usuário com base nos IDs de usuário
    users_online = User.objects.filter(id__in=user_id_list)


    postagem = Postagem.objects.get(pk=1)
    context = {
        'users_online': users_online,
        'postagem': postagem,
    }
    return render(request, 'index.html', context)