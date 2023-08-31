from django.conf import settings
from daibeisi_tools.mini_program import MiniProgram

mp = MiniProgram(appid=settings.MP_APPID, secret=settings.MP_SECRET)
