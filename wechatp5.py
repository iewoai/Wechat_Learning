import itchat, time
from itchat.content import *
import requests, json


@itchat.msg_register(itchat.content.TEXT, isFriendChat=True)
def simple_reply(msg):
	if msg['FromUserName'] != myUserName:
		global v_user
		if v_user[msg['FromUserName']]['flag']:
			# 设置60秒若没回复则自动退出
			v_user[msg['FromUserName']]['timeOut'] = 60
			info = msg.text
			user_name = msg['FromUserName']
			data = {
			"reqType": 0,
			"perception": {
				"inputText": {
					"text": info
				}
			},
			"userInfo": {
				"apiKey": "",
				"userId": '123'
				}
			}
			try:
				r = requests.post(url, headers=headers, data=json.dumps(data))
				result = json.loads(r.content)
				if result['intent']['code'] == 4003:
					v_user[msg['FromUserName']]['flag'] = False
					msg.user.send('小v走啦！（已退出自动聊天模式，调用次数超过限制）。')
				else:
					message = result['results'][0]['values']['text']
			except Exception as e:
				print(e)

			msg.user.send(message)

		# 检测到开启指令打开机器人接口(只对发送指令的人用机器人回复)
		if (v_user[msg['FromUserName']]['flag'] == False and msg.text == 'hello小v'):
			v_user[msg['FromUserName']]['flag'] = True
			msg.user.send('小v来啦！（已开启自动聊天模式，回复quit()退出）')

		if (v_user[msg['FromUserName']]['flag'] == True and msg.text == 'quit()'):
			v_user[msg['FromUserName']]['flag'] = False
			msg.user.send('小v走啦！（已退出自动聊天模式，回复hello小v开启）。')

if __name__ == '__main__':
	url = 'http://openapi.tuling123.com/openapi/api/v2'
	headers = {
		'Content-Type': 'application/json',
		'Host': 'openapi.tuling123.com',
		'User-Agent': 'Mozilla/5.0 (Wi`ndows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3486.0 '
				'Safari/537.36 '
	}
	v_user = {}
	itchat.auto_login(True)
	friends = itchat.get_friends(update=True)[0:]
	for friend in friends:
		v_user[friend['UserName']] = {'flag':False, 'timeOut':60}
	# search_friends()['UserName']第一个为自己的username
	myUserName = itchat.search_friends()['UserName']
	itchat.run()
# {'emotion': {'robotEmotion': {'a': 0, 'd': 0, 'emotionId': 0, 'p': 0}, 'userEmotion': {'a': 0, 'd': 0, 'emotionId': 0, 'p': 0}}, 'intent': {'actionName': '', 'code': 10004, 'intentName': ''}, 'results': [{'groupType': 1, 'resultType': 'text', 'values': {'text': 'b'}}]}
