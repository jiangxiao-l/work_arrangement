# *_* coding : UTF-8 *_*
# Author ： jiangxiaolong
# time   ： 2021/5/26  下午3:09

import json
from urllib.parse import unquote
from channels.generic.websocket import AsyncWebsocketConsumer


class Chatting(AsyncWebsocketConsumer):

    async def connect(self):
        print('connect')
        # AuthMiddlewareStack：封装了django的auth模块，使用这个配置我们就可以在consumer中通过下边的代码获取到用户的信息
        print(self.scope)
        self.room_group_name = 'xiaoyuanqujing'
        print({"channel_name": self.channel_name})
        # 加入聊天室
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # 离开聊天室
        print('disconnect')
        print(self.scope)
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # 通过WebSocket，接收数据
    async def receive(self, text_data):
        print('receive')
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # print({"text_data_json": text_data_json})
        print({"query_string": self.scope['query_string']})
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',  # 写一个当前类中的方法名，会触发该方法执行,组里有多少人会触发多少次
                'message': message,
                'username': str(self.scope['query_string'])  # 把当前客户端的名字传入（也可以去ip地址）
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        # 取出发言人的名字和说的话
        user_name = unquote(event['username'], 'utf-8')
        message = user_name + event['message']

        # 通过WebSocket发送
        await self.send(text_data=json.dumps({
            'message': message
        }))
