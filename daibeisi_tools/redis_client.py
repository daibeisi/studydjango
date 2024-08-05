"""Redis客户端"""
import redis
from .utils import SingletonMeta


class RedisClient(SingletonMeta):
    """Redis客户端"""

    def __init__(self, host, port, password):
        self.pool = redis.ConnectionPool(host=host, port=port, password=password)
        self._conn = None

    @property
    def conn(self):
        if not hasattr(self, '_conn'):
            self.get_connection()
        return self._conn

    def get_connection(self):
        self._conn = redis.Redis(connection_pool=self.pool)
