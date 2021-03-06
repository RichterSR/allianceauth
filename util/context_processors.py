from django.conf import settings
from django.utils import timezone


def is_corp(request):
    return {'IS_CORP': settings.IS_CORP}

def corp_id(request):
    return {'CORP_ID': settings.CORP_ID}

def corp_name(request):
    return {'CORP_NAME': settings.CORP_NAME}

def alliance_id(request):
    return {'ALLIANCE_ID': settings.ALLIANCE_ID}

def alliance_name(request):
    return {'ALLIANCE_NAME': settings.ALLIANCE_NAME}

def jabber_url(request):
    return {'JABBER_URL': settings.JABBER_URL}

def member_api_mask(request):
    return {'MEMBER_API_MASK': settings.MEMBER_API_MASK,
            'MEMBER_API_ACCOUNT': settings.MEMBER_API_ACCOUNT}

def blue_api_mask(request):
    return {'BLUE_API_MASK': settings.BLUE_API_MASK,
            'BLUE_API_ACCOUNT': settings.BLUE_API_ACCOUNT}

def domain_url(request):
    return {'DOMAIN': settings.DOMAIN, 'MUMBLE_URL': settings.MUMBLE_URL,
            'FORUM_URL': settings.FORUM_URL,
            'ENABLE_AUTH_FORUM': settings.ENABLE_AUTH_FORUM,
            'ENABLE_AUTH_JABBER': settings.ENABLE_AUTH_JABBER,
            'ENABLE_AUTH_MUMBLE': settings.ENABLE_AUTH_MUMBLE,
            'ENABLE_AUTH_IPBOARD': settings.ENABLE_AUTH_IPBOARD,
            'ENABLE_AUTH_TEAMSPEAK3': settings.ENABLE_AUTH_TEAMSPEAK3,
            'ENABLE_AUTH_DISCORD': settings.ENABLE_AUTH_DISCORD,
            'ENABLE_AUTH_DISCOURSE': settings.ENABLE_AUTH_DISCOURSE,
            'ENABLE_AUTH_IPS4': settings.ENABLE_AUTH_IPS4,
            'ENABLE_AUTH_SMF': settings.ENABLE_AUTH_SMF,
            'ENABLE_AUTH_SEAT': settings.ENABLE_AUTH_SEAT,
            'ENABLE_AUTH_XENFORO': settings.ENABLE_AUTH_XENFORO,
            'ENABLE_AUTH_MARKET': settings.ENABLE_AUTH_MARKET,
            'ENABLE_AUTH_PATHFINDER': settings.ENABLE_AUTH_PATHFINDER,
            'ENABLE_AUTH_FLEETUP': settings.ENABLE_AUTH_FLEETUP,
            'ENABLE_BLUE_JABBER': settings.ENABLE_BLUE_JABBER,
            'ENABLE_BLUE_FORUM': settings.ENABLE_BLUE_FORUM,
            'ENABLE_BLUE_MUMBLE': settings.ENABLE_BLUE_MUMBLE,
            'ENABLE_BLUE_IPBOARD': settings.ENABLE_BLUE_IPBOARD,
            'ENABLE_BLUE_TEAMSPEAK3': settings.ENABLE_BLUE_TEAMSPEAK3,
            'ENABLE_BLUE_DISCORD': settings.ENABLE_BLUE_DISCORD,
            'ENABLE_BLUE_DISCOURSE': settings.ENABLE_BLUE_DISCOURSE,
            'ENABLE_BLUE_IPS4': settings.ENABLE_BLUE_IPS4,
            'ENABLE_BLUE_SMF': settings.ENABLE_BLUE_SMF,
            'ENABLE_BLUE_SEAT': settings.ENABLE_BLUE_SEAT,
            'ENABLE_BLUE_MARKET': settings.ENABLE_BLUE_MARKET,
            'ENABLE_BLUE_PATHFINDER': settings.ENABLE_BLUE_PATHFINDER,
            'ENABLE_BLUE_XENFORO': settings.ENABLE_BLUE_XENFORO,
            'ENABLE_BLUE_FLEETUP': settings.ENABLE_BLUE_FLEETUP,
            'TEAMSPEAK3_PUBLIC_URL': settings.TEAMSPEAK3_PUBLIC_URL,
            'JACK_KNIFE_URL': settings.JACK_KNIFE_URL,
            'DISCORD_SERVER_ID': settings.DISCORD_GUILD_ID,
            'KILLBOARD_URL': settings.KILLBOARD_URL,
<<<<<<< HEAD
            'SEAT_URL': settings.SEAT_URL,
=======
            'SEAT_URL': settings.SEAT_URL, 
>>>>>>> origin/master
            'DISCOURSE_URL': settings.DISCOURSE_URL,
            'IPS4_URL': settings.IPS4_URL,
            'SMF_URL': settings.SMF_URL,
            'MARKET_URL': settings.MARKET_URL,
            'PATHFINDER_URL': settings.PATHFINDER_URL,
            'EXTERNAL_MEDIA_URL': settings.EXTERNAL_MEDIA_URL,
            'FLEETUP_URL': settings.FLEETUP_URL,
            'FLEETUP_JOIN_URL': settings.FLEETUP_JOIN_URL,
            'SLACK_URL': settings.SLACK_URL,
<<<<<<< HEAD
            'WIKI_URL': settings.WIKI_URL,
=======
>>>>>>> origin/master
            'CURRENT_UTC_TIME': timezone.now()}

def character_ids(request):
     character_id = None
     corporation_id = None
     alliance_id = None
     if request.user.is_authenticated():
         from authentication.managers import AuthServicesInfoManager
         auth = AuthServicesInfoManager.get_auth_service_info(request.user)
         if auth.main_char_id:
             from eveonline.models import EveCharacter
             try:
                 char = EveCharacter.objects.get(character_id=auth.main_char_id)
                 character_id = char.character_id
                 corporation_id = char.corporation_id
                 alliance_id = char.alliance_id
             except EveCharacter.DoesNotExist:
                 pass
     return { 'CHARACTER_CHARACTER_ID': character_id,
              'CHARACTER_CORPORATION_ID': corporation_id,
              'CHARACTER_ALLIANCE_ID': alliance_id}

