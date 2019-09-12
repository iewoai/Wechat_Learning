import itchat
# echarts 作图包
from echarts import Echart, Legend, Pie
from pyecharts import Pie
import matplotlib
import matplotlib.pyplot as plt
'''
获取好友性别并生成饼图
'''
# 先登录
# itchat.login()

# 命令行获取二维码
# itchat.auto_login(enableCmdQR=True)

# 手机直接确认登陆
itchat.auto_login(True)

# 获取好友列表
friends = itchat.get_friends(update=True)[0:]

# 初始化计数器，有男有女，当然，有些人是不填的
male = female = other = 0

# 遍历这个列表，列表里第一位是自己，所以从"自己（friends[1:]）"之后开始计算
# 1表示男性，2女性
for i in friends[1:]:
	sex = i["Sex"]
	if sex == 1:
		male += 1
	elif sex == 2:
		female += 1
	else:
		other += 1

# 总数算上，好计算比例啊～
total = len(friends[1:])

# 好了，打印结果
print("您总共有%d位好友！" % (total, ))
print(u"男性好友：%.2f%%" % (float(male) / total * 100))
print(u"女性好友：%.2f%%" % (float(female) / total * 100))
print(u"其他：%.2f%%" % (float(other) / total * 100))

print("正在生成饼图：")

# 用echarts 生成饼图出现gbk错误(懒得管)
# chart = Echart(u'%s的微信好友性别比例：' % (friends[0]['NickName'], ))
# chart.use(Pie('WeChat',
# 				[{'value': male, 'name': u'男性 %.2f%%' % (float(male) / total * 100)},
# 				{'value': female, 'name': u'女性 %.2f%%' % (float(female) / total * 100)},
# 				{'value': other, 'name': u'其他 %.2f%%' % (float(other) / total * 100)}],
# 				radius=["50%", "70%"]))
# chart.use(Legend(["male", "female", "other"]))
# del chart.json["xAxis"]
# del chart.json["yAxis"]
# chart.plot()

# 采用pyecharts
attr = ["男性好友", "女性好友", "其他好友"]
v1 = [float(male), float(female), float(other)]
pie = Pie('%s的微信好友性别比例：' % (friends[0]['NickName'], ))
pie.add("", attr, v1, is_label_show = True)
pie.show_config()

# 生成.html文件
pie.render()

# 采用matplotlib
# labels = '男性好友', '女性好友', '其他好友'
# sizes = [float(male), float(female), float(other)]
# explode = (0,0.1,0)

# fig1, ax = plt.subplots()

# # explode=explode, pctdistance=1.2 一部分转移出去
# ax.pie(sizes, autopct='%1.2f%%', shadow=True, startangle=90,
# 	explode=explode, pctdistance=1.2)

# plt.title('%s的微信好友性别比例：' % (friends[0]['NickName'], ))
# # 解决中文乱码问题
# plt.rcParams['font.sans-serif']=['SimHei']
# ax.axis('equal')

# ax.legend(labels=labels, loc='upper right')

# plt.show()
