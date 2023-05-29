# -*- coding: utf-8 -*-
import json
import datetime
import requests
import threading
from functools import wraps


class MiniProgram(object):
    _instance = None
    _lock = threading.RLock()

    def __init__(self, appid: str, secret: str) -> None:
        self.appid = appid
        self.secret = secret
        self.access_token = None
        self.access_token_expires_time = datetime.datetime.now()

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            return cls._instance
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
            return cls._instance

    def _get_access_token(self, num_tries=3):
        url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret=" \
              "{secret}".format(appid=self.appid, secret=self.secret)
        try:
            res = requests.get(url=url, timeout=5)
        except Exception as exc:
            raise RuntimeError("{0}  {1}".format(exc, "微信auth.getAccessToken接口网络连接错误"))
        else:
            res_json = res.json()
            errcode = res_json.get("errcode", 0)
            if errcode == 0:
                expires_in = res_json.get("expires_in", 7200) - 200
                self.access_token_expires_time = datetime.datetime.now() + datetime.timedelta(seconds=expires_in)
                self.access_token = res_json.get("access_token")
            elif errcode == -1 and num_tries > 0:
                self._get_access_token(num_tries - 1)
            else:
                raise RuntimeError(str(errcode) + "微信auth.getAccessToken接口获取access_token失败" + errmsg)

    def ensure_access_token_effective(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            now_datetime = datetime.datetime.now()
            if not self.access_token or now_datetime >= self.access_token_expires_time:
                self._get_access_token()
            return func(self, *args, **kwargs)

        return wrapper

    def get_user_id_info(self, js_code, num_tries=3):
        """获取用户openid、session_key、unionid

        :param str js_code: 通过 wx.login 接口获得临时登录凭证 code
        :param int num_tries: 重试次数,默认3次
        :return: id_info = {openid、session_key、unionid（绑定开放平台才有）}
        """
        url = 'https://api.weixin.qq.com/sns/jscode2session?appid={appid}&secret={secret}&js_code={js_code}&' \
              'grant_type=authorization_code'.format(appid=self.appid, secret=self.secret, js_code=js_code)
        try:
            res = requests.get(url=url, timeout=5)
        except Exception as exc:
            raise RuntimeError("{0}  {1}".format(exc, "微信auth.code2Session接口网络连接错误"))
        else:
            res_json = res.json()
            errcode = res_json.get("errcode", 0)
            if errcode == 0:
                user_id_info = res_json
                return user_id_info
            elif errcode == -1 and num_tries > 1:
                return self.get_user_id_info(js_code, num_tries - 1)
            else:
                raise RuntimeError(str(errcode) + "微信auth.code2Session接口获取openid、session_key、unionid失败")

    @ensure_access_token_effective
    def get_phone_info(self, code, num_tries=3):
        url = "https://api.weixin.qq.com/wxa/business/getuserphonenumber" \
              "?access_token={0}".format(self.access_token)
        headers = {'Content-Type': 'application/json', "Accept": "application/json"}
        data = {"code": code}
        try:
            res = requests.post(url=url, data=json.dumps(data), headers=headers, timeout=5)
        except Exception as exc:
            raise RuntimeError("{0}  {1}".format(exc, "微信phonenumber.getPhoneNumber接口网络连接错误"))
        else:
            res_json = res.json()
            errcode = res_json.get("errcode", 0)
            if errcode == 0:
                phone_info = res_json.get("phone_info")
                return phone_info
            elif errcode == -1 and num_tries > 1:
                return self.get_phone_number(code, num_tries - 1)
            else:
                raise RuntimeError(str(errcode) + "微信phonenumber.getPhoneNumber接口获取phone_number失败")


if __name__ == '__main__':
    mp = MiniProgram("", "")
    user_id_info = mp.get_user_id_info("")
    phone_info = mp.get_phone_info("")
