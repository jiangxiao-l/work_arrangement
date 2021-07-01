# *_* coding : UTF-8 *_*
# Author ： jiangxiaolong
# time   ： 2021/5/26  下午3:08

from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/chat', consumers.Chatting),  # consumers.Chatting 是该路由的消费者
]
