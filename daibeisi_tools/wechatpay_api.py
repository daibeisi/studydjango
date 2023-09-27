from wechatpayv3 import WeChatPay, WeChatPayType


class WechatPayAPI:

    def __init__(self, mchid, private_key, cert_serial_no, apiv3_key, appid, notify_url, cert_dir):
        self._wechatpay_type = WeChatPayType.MINIPROG,
        self._mchid = mchid
        self._private_key = private_key
        self._cert_serial_no = cert_serial_no
        self._appid = appid
        self._apiv3_key = apiv3_key
        self._notify_url = notify_url
        self._cert_dir = cert_dir
        self.wxpay = WeChatPay(
            wechatpay_type=self._wechatpay_type,
            mchid=self._mchid,
            private_key=self._private_key,
            cert_serial_no=self._cert_serial_no,
            appid=self._appid,
            apiv3_key=self._apiv3_key,
            notify_url=self._notify_url,
            cert_dir=self._cert_dir
        )