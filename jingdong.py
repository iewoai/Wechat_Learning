import itchat, time
import platform
from itchat.content import *

@itchat.msg_register(itchat.content.TEXT, isFriendChat=True)
def simple_reply(msg):
	if msg['FromUserName'] != myUserName:
		
		if (msg.text == '认证流程'):
			msg.user.send("@img@%s" % 'jd.jpg')
			msg.user.send("认证流程：\n1.使用微信“扫一扫”扫如上二维码进入\n2.微信授权或者输入手机和验证码并登陆，登陆成功后进入认证界面\n3.填写学生认证信息\n4.认证成功并截图\n5.打开京东校园并截图")
			time.sleep(0.1)
			msg.user.send("注意事项：\n1.一卡通或者校园卡上的信息要与填写的信息相对应\n2.入学时间和学制相加要大于等于2019\n3.京东账户未曾实名认证或者学生认证（否则认证流程第3步直接提示认证成功）\n4.认证完后请将认证流程中第4、5步流程的截图和自己的姓名发送给我\n5.核实完毕后支付5元报酬")
			time.sleep(0.1)
			msg.user.send("认证流程图：")
			msg.user.send("@img@%s" % 'jd1.jpg')
			time.sleep(0.1)
			msg.user.send("截图流程图：")
			msg.user.send("@img@%s" % 'jd2.png')
			msg.user.send("@img@%s" % 'jd3.png')
			msg.user.send("@img@%s" % 'jd4.png')

@itchat.msg_register(FRIENDS)
def add_friend(msg):
	if (msg['RecommendInfo']['Content'] == '京东学生认证'):
		msg.user.verify()
		msg.user.send('“%s”，感谢您来到这里，以下都是关于京东学生认证的内容，请仔细阅读。' % (msg['RecommendInfo']['NickName'], ))
		msg.user.send('操作须知：京东学生认证过程中需要您填写一些学生信息，如果您想继续，回复“认证流程”，查看操作详情。')




		# print("来自%s的信息:" % (msg['FromUserName'], ))
		# # print("个人信息：%s" % (itchat.search_friends(userName = msg['FromUserName']), ))
		# # itchat.search_friends(UserName = msg['FromUserName'])
		# msg_time_rec = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		# print("消息发送时间：%s" % (msg_time_rec, ))
		# print("消息类型：%s ————消息内容： %s" % (msg.type, msg.text))
if __name__ == '__main__':
	if platform.platform()[:7] == 'Windows':
		itchat.auto_login(enableCmdQR=False, hotReload=True)
	else:
		itchat.auto_login(enableCmdQR=True, hotReload=True)
	myUserName = itchat.search_friends()['UserName']
	itchat.run()