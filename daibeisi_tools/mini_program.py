# -*- coding: utf-8 -*-
from functools import wraps
import datetime
import json
import requests
from .utils import SingletonMeta


class MiniProgramAPI(SingletonMeta):
    """小程序接口"""

    def __init__(self, appid: str, secret: str) -> None:
        self.__appid = appid
        self.__secret = secret
        self.access_token = None
        self.access_token_expires_time = datetime.datetime.now()

    def get_access_token(self):
        """获取access_token"""
        url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential" \
        f"&appid={self.__appid}&secret={self.__secret}"
        try:
            res = requests.get(url=url, timeout=5)
        except Exception as exc:
            raise RuntimeError("微信auth.getAccessToken接口网络连接错误") from exc
        res_json = res.json()
        errcode = res_json.get("errcode", 0)
        if errcode == 0:
            expires_in = res_json.get("expires_in", 7200) - 200
            self.access_token_expires_time = datetime.datetime.now() + datetime.timedelta(seconds=expires_in)
            self.access_token = res_json.get("access_token")
        else:
            errmsg = res_json.get("errmsg")
            raise RuntimeError(f"微信auth.getAccessToken接口{url}获取access_token失败{errcode}{errmsg}")

    @staticmethod
    def ensure_access_token_effective(func):
        """确认access_token有效"""
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            now_datetime = datetime.datetime.now()
            if not self.access_token or now_datetime >= self.access_token_expires_time:
                self.get_access_token()
            return func(self, *args, **kwargs)

        return wrapper

    def get_user_id_info(self, js_code):
        """获取用户openid、session_key、unionid

        :param str js_code: 通过 wx.login 接口获得临时登录凭证 code
        :return: id_info = {openid、session_key、unionid（绑定开放平台才有）}
        """
        url = f"https://api.weixin.qq.com/sns/jscode2session?appid={self.__appid}" \
        f"&secret={self.__secret}&js_code={js_code}&grant_type=authorization_code"
        try:
            res = requests.get(url=url, timeout=5)
        except Exception as exc:
            raise RuntimeError("微信auth.code2Session接口网络连接错误") from exc
        res_json = res.json()
        errcode = res_json.get("errcode", 0)
        if errcode == 0:
            user_id_info = res_json
            return user_id_info

        errmsg = res_json.get("errmsg")
        raise RuntimeError(f"微信auth.code2Session接口{url}获取openid、session_key、unionid失败{errcode}{errmsg}")

    @ensure_access_token_effective
    def get_phone_info(self, code):
        """获取手机号"""
        url = "https://api.weixin.qq.com/wxa/business/getuserphonenumber" \
              f"?access_token={self.access_token}"
        headers = {'Content-Type': 'application/json', "Accept": "application/json"}
        data = {"code": code}
        try:
            res = requests.post(url=url, data=json.dumps(data), headers=headers, timeout=5)
        except Exception as exc:
            raise RuntimeError("微信phonenumber.getPhoneNumber接口网络连接错误") from exc
        res_json = res.json()
        errcode = res_json.get("errcode", 0)
        if errcode == 0:
            phone_info = res_json.get("phone_info")
            return phone_info
        else:
            errmsg = res_json.get("errmsg")
            raise RuntimeError(f"微信phonenumber.getPhoneNumber接口获取phone_number失败{errcode}{errmsg}")

    @ensure_access_token_effective
    def generate_scheme(self):
        """获取scheme码"""
        url = f"https://api.weixin.qq.com/wxa/generatescheme?access_token={self.access_token}"
        headers = {'Content-Type': 'application/json', "Accept": "application/json"}
        try:
            res = requests.post(url=url, headers=headers, timeout=5)
        except Exception as exc:
            raise RuntimeError("微信获取scheme码接口网络连接错误") from exc
        res_json = res.json()
        errcode = res_json.get("errcode", 0)
        if errcode == 0:
            openlink = res_json.get("openlink")
            return openlink

        errmsg = res_json.get("errmsg")
        raise RuntimeError(f"获取scheme码接口{url}失败{errcode}{errmsg}")
    