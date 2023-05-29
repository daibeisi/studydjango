from datetime import timedelta
from .settings import SECRET_KEY


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),  # 指定访问令牌有效时间
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),  # 指定刷新令牌有效时间
    # 设置为 时True，如果将刷新令牌提交给 TokenRefreshView，则新的刷新令牌将与新的访问令牌一起返回。
    # 这个新的刷新令牌将通过 JSON 响应中的“刷新”键提供。新的刷新令牌将有一个更新的到期时间，
    # 该时间是通过将设置中的 timedelta 添加REFRESH_TOKEN_LIFETIME 到发出请求时的当前时间来确定的。
    # 如果黑名单应用程序正在使用中并且BLACKLIST_AFTER_ROTATION设置为True，则提交到刷新视图的刷新令牌将被添加到黑名单中。
    "ROTATE_REFRESH_TOKENS": False,
    # 设置为 时，如果黑名单应用程序正在使用且设置设置True为 ，则提交给 的刷新令牌 将被添加到黑名单。您需要在设置文件中添加才能使用此设置。
    # TokenRefreshViewROTATE_REFRESH_TOKENSTrue'rest_framework_simplejwt.token_blacklist',INSTALLED_APPS
    "BLACKLIST_AFTER_ROTATION": False,
    # 设置为 时True，auth_user 表中的 last_login 字段在登录时更新 (TokenObtainPairView)。
    # 警告：更新 last_login 将显着增加数据库事务的数量。滥用视图的人可能会降低服务器速度，这可能是一个安全漏洞。
    # 如果你真的想要这个，至少要用 DRF 来限制端点。
    "UPDATE_LAST_LOGIN": False,
    # 来自 PyJWT 库的算法将用于对令牌执行签名/验证操作。要使用对称 HMAC 签名和验证，可以使用以下算法：'HS256', 'HS384', 'HS512'.
    # 选择 HMAC 算法时，该SIGNING_KEY设置将同时用作签名密钥和验证密钥。在这种情况下，该 VERIFYING_KEY设置将被忽略。
    # 要使用非对称 RSA 签名和验证，可以使用以下算法：'RS256', 'RS384', 'RS512'.
    # 选择 RSA 算法时，SIGNING_KEY必须将设置设置为包含 RSA 私钥的字符串。同样，该 VERIFYING_KEY设置必须设置为包含 RSA 公钥的字符串。
    "ALGORITHM": "HS256",
    # 用于对生成的令牌内容进行签名的签名密钥。对于 HMAC 签名，这应该是一个随机字符串，其数据位数至少与签名协议所需的一样多。
    # 对于 RSA 签名，这应该是一个包含 2048 位或更长的 RSA 私钥的字符串。由于 Simple JWT 默认使用 256 位 HMAC 签名，
    # 因此该设置默认为您的 django 项目的设置SIGNING_KEY值。SECRET_KEY虽然这是 Simple JWT 可以提供的最合理的默认值，
    # 但建议开发人员将此设置更改为独立于 django 项目密钥的值。这将使更改用于令牌的签名密钥在它被破坏时更容易。
    "SIGNING_KEY": SECRET_KEY,
    # 用于验证生成的令牌内容的验证密钥。如果设置指定了 HMAC 算法ALGORITHM，则 设置将被忽略并 使用设置VERIFYING_KEY的值。
    # SIGNING_KEY如果设置指定了 RSA 算法 ALGORITHM，则VERIFYING_KEY设置必须设置为包含 RSA 公钥的字符串。
    "VERIFYING_KEY": "",
    # 要包括在生成的令牌中和/或在解码的令牌中验证的受众主张。当设置为 "无 "时，该字段被排除在令牌之外，并且不被验证。
    "AUDIENCE": None,
    # 将包括在生成的令牌中和/或在解码的令牌中验证的发行者主张。当设置为 "无 "时，该字段被排除在令牌之外，并且不被验证。
    "ISSUER": None,
    "JSON_ENCODER": None,
    # JWK_URL用于动态解析验证令牌签名所需的公钥。例如，当使用Auth0时，
    # 你可以将其设置为'https://yourdomain.auth0.com/.well-known/jwks.json'。当设置为None时，
    # 该字段被排除在令牌后端，在验证过程中不被使用。
    "JWK_URL": None,
    # 回旋余地是用来给过期时间一些余地。这可以是一个秒的整数，也可以是一个datetime.timedelta。
    # 更多信息请参考https://pyjwt.readthedocs.io/en/latest/usage.html#expiration-time-claim-exp。
    "LEEWAY": 0,

    # 需要认证的视图所接受的授权头类型。例如，"Bearer "的值意味着需要认证的视图将寻找具有以下格式的头：授权：Bearer <token>。
    # 这个设置也可以包含一个可能的头类型的列表或元组（例如（'Bearer', 'JWT'））。如果以这种方式使用列表或元组，并且认证失败，
    # 集合中的第一项将被用来构建响应中的 "WWW-Authenticate "头。
    "AUTH_HEADER_TYPES": ("Bearer",),
    # 用于认证的授权标头名称。默认是HTTP_AUTHORIZATION，它将接受请求中的授权头。例如，如果你想在你的请求头中使用X_Access_Token，
    # 请在设置中指定AUTH_HEADER_NAME为HTTP_X_ACCESS_TOKEN。
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    # 来自用户模型的数据库字段，将包括在生成的令牌中以识别用户。建议这个设置的值指定一个字段，一旦它的初始值被选中，
    # 通常不会改变。例如，指定 "用户名 "或 "电子邮件 "字段将是一个糟糕的选择，因为账户的用户名或电子邮件可能会改变，
    # 这取决于特定服务中账户管理的设计方式。这可能允许用一个旧的用户名创建一个新的账户，而现有的令牌仍然有效，它使用该用户名作为用户标识。
    "USER_ID_FIELD": "id",
    # 生成的令牌中的主张，将用于存储用户标识符。例如，设置值为'user_id'将意味着生成的令牌包括一个包含用户标识符的 "user_id "要求。
    "USER_ID_CLAIM": "user_id",
    # 可调用，以确定用户是否被允许进行认证。这个规则在处理了一个有效的token后被应用。用户对象作为一个参数被传递给可调用程序。
    # 默认的规则是检查is_active标志是否仍然为真。该可调用程序必须返回一个布尔值，如果授权则为真，否则为假，导致401状态代码。
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    # 指明允许用来证明认证的令牌类型的类的点状路径列表。更多信息见下面的 "令牌类型 "部分。
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    # 用于存储令牌类型的索赔名称。更多信息请参见下面的 "令牌类型 "部分。
    "TOKEN_TYPE_CLAIM": "token_type",
    # 一个无状态的用户对象，由一个经过验证的令牌支持。仅用于JWTStatelessUserAuthentication认证后端。
    # 该值是指向你的rest_framework_simplejwt.models.TokenUser子类的点状路径，这也是默认值。
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    # 用于存储一个令牌的唯一标识符的声称名称。该标识符用于识别黑名单应用程序中被撤销的令牌。
    # 在某些情况下，除了默认的 "jti "声称外，可能需要使用另一个声称来存储这样的值。
    "JTI_CLAIM": "jti",

    # 用于存储滑动令牌刷新期的过期时间的索赔名称。更多信息请参见下面的 "滑动令牌 "部分。
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    # 一个datetime.timedelta对象，指定滑动令牌的有效时间，以证明认证。在令牌生成过程中，
    # 这个timedelta值会加到当前的UTC时间上，以获得令牌的默认 "exp "声明值。更多信息请参见下面的 "滑动令牌 "部分。
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    # 一个datetime.timedelta对象，它指定了滑动令牌的有效时间，可以刷新。在令牌生成过程中，这个timedelta值被添加到当前的UTC时间中，
    # 以获得令牌的默认 "exp "声称值。更多信息请参见下面的 "滑动令牌 "部分。
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}