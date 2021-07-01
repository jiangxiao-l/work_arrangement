# *_* coding : UTF-8 *_*
# Author ： jiangxiaolong
# time   ： 2021/5/26  下午3:06

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from app01 import routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(  # 使用AuthMiddlewareStack，后续在视图类中可以取出self.scope，相当于request对象
        URLRouter(
            routing.websocket_urlpatterns  # 指明路由文件是django_websocket/routing.py,类似于路由分发
        )
    )
    # 'websocket': URLRouter(
    #     routing.websocket_urlpatterns  # 指明路由文件是django_websocket/routing.py,类似于路由分发
    # ),
})
