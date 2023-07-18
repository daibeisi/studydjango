import os

from daibeisi_tools.mini_program import MiniProgram
from .config import cf
Django_ENV = os.environ.get('Django_ENV', "development")

mp = MiniProgram(
    appid=cf.get(Django_ENV, 'MP_APPID'),
    secret=cf.get(Django_ENV, 'MP_SECRET')
)
