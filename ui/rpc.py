from core.settings import AMQP_CONFIG
from nameko.standalone.rpc import ClusterRpcProxy


def get_data_from_cardreader(rid):
    with ClusterRpcProxy(AMQP_CONFIG) as rpc:
        try:
            fx = getattr(rpc, rid)
            return fx.get_data()
        except Exception as e:
            print(f"error: {e}")
            return None

