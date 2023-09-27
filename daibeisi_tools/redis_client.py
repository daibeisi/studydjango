"""Redis客户端"""
import redis
from .utils import SingletonMeta


class RedisClient(SingletonMeta):
    """Redis客户端"""
    def __init__(self, host, port, password):
        self.pool = redis.ConnectionPool(host = host, port = port, password = password)

    @property
    def conn(self):
        if not hasattr(self, '_conn'):
            self.getConnection()
        return self._conn

    def getConnection(self):
        self._conn = redis.Redis(connection_pool = self.pool)

