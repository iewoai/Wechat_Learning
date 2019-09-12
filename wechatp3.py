import itchat, re
import matplotlib.pyplot as plt  # 数学绘图库
import jieba  # 分词库
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator  # 词云库
from PIL import Image
import numpy as np

'''
取所有好友的个性签名并做成词云图
'''

# 先登录
# itchat.login()
itchat.auto_login(True)

signature_list = []
zn_StopWordPath = "F:\\py学习\\wordcloud\\zn_STOPWORDS.txt"
imagePath = "wechat.jpg"
fontPath = "yahei.ttc"
imageSavePath = "个性签名词云图.jpg"

def txt2set(zn_StopWordPath):
	'''
	读取本地中文停用词文本并转换为列表
	:param zn_StopWordPath: 中文停用词文本路径
	:return stopWordList: 一个装有中文停用词的列表
	'''
	with open(zn_StopWordPath) as f:
		text = f.read()
		stopWordList = text.split(';\n')
		return stopWordList

# 获取好友列表
friends = itchat.get_friends(update=True)[0:]
for i in friends:
	# 获取个性签名 Signature
	if i["Signature"] != '':
		signature = i["Signature"].strip().replace("span", "").replace("class", "").replace("emoji", "")
		# 正则匹配过滤掉emoji表情，例如emoji1f3c3等
		signature = re.sub(r"1f\d.+", "", signature)
		try:
			signature_list.append(signature)
		except:
			continue
text = "".join(signature_list)
cut_text = jieba.cut(text, cut_all=False)
result = '/'.join(cut_text)

zn_StopWords = txt2set(zn_StopWordPath)
stopwords = set(zn_StopWords)
stopwords.add('个性')
stopwords.add('签名')

image = np.array(Image.open(imagePath))
# 获取背景图片颜色
image_colors = ImageColorGenerator(image)

# 创建WordCloud实例并自定义设置参数(如背景色,背景图片和停用词等)
wc = WordCloud(font_path=fontPath, background_color='white', max_words=20000, scale=4,
				 mask=image, stopwords=stopwords, random_state=42, max_font_size=60)
# 根据设置的参数，统计词频并生成词云图
wc.generate(result)

plt.rcParams['font.sans-serif']=['SimHei']
plt.title('%s的微信好友个性签名词云图' % (friends[0]['NickName'], ))

# 以图片的形式显示词云,并依据背景色重置词的颜色
plt.imshow(wc.recolor(color_func=image_colors))

# 关闭图像坐标系
plt.axis('off')
plt.show()
wc.to_file(imageSavePath)