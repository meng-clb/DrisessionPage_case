import os
import time

from DrissionPage import ChromiumPage
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

page = ChromiumPage()
tab = page.new_tab()

# 反爬字体对应的文字
font_list = [{'code': '7074467222', 'word': '逼'}, {'code': '0678663477', 'word': '情'},
             {'code': '3043454467', 'word': '日'}, {'code': '2276251664', 'word': '嫩'},
             {'code': '0486110525', 'word': '水'},
             {'code': '0923672614', 'word': '死'}, {'code': '5318824731', 'word': '妈'},
             {'code': '2965616717', 'word': '爱'}, {'code': '2063259833', 'word': '色'},
             {'code': '6197424834', 'word': '中'}, {'code': '5260398634', 'word': '指'},
             {'code': '0473556214', 'word': '含'}, {'code': '0146287633', 'word': '露'},
             {'code': '8478694653', 'word': '主'}, {'code': '9134848937', 'word': '做'},
             {'code': '2173857009', 'word': '高'}, {'code': '1082275499', 'word': '合'},
             {'code': '3296363576', 'word': '欲'}, {'code': '1040782805', 'word': '奸'},
             {'code': '2471389451', 'word': '湿'}, {'code': '7051993783', 'word': '硬'},
             {'code': '2174754224', 'word': '暴'}, {'code': '4436421269', 'word': '党'},
             {'code': '6514831790', 'word': '血'}, {'code': '0026372214', 'word': '丝'},
             {'code': '1947937898', 'word': '粉'}, {'code': '4538628495', 'word': '挤'},
             {'code': '6281647881', 'word': '流'}, {'code': '5229950952', 'word': '肉'},
             {'code': '9860153795', 'word': '麻'}, {'code': '5110754259', 'word': '吸'},
             {'code': '4740869798', 'word': '操'}, {'code': '2525826615', 'word': '狗'},
             {'code': '3089649511', 'word': '宫'}, {'code': '1218400718', 'word': '虐'},
             {'code': '8997927012', 'word': '灭'}, {'code': '9720548295', 'word': '杜'},
             {'code': '7508904751', 'word': '帮'}, {'code': '7228562021', 'word': '纪'},
             {'code': '5969522288', 'word': '亲'}, {'code': '6855685283', 'word': '摇'},
             {'code': '5732450242', 'word': '母'}, {'code': '5329628684', 'word': '辱'},
             {'code': '5265224411', 'word': '干'}, {'code': '5245263419', 'word': '轮'},
             {'code': '2158558763', 'word': '幼'}, {'code': '2811411890', 'word': '亡'},
             {'code': '9829762678', 'word': '妇'}, {'code': '5105645092', 'word': '温'},
             {'code': '2548022544', 'word': '奴'}, {'code': '8666880661', 'word': '凌'},
             {'code': '5946892177', 'word': '淫'}, {'code': '5758773674', 'word': '棍'},
             {'code': '4017050851', 'word': '交'}, {'code': '2293535402', 'word': '兽'},
             {'code': '8087788059', 'word': '国'}, {'code': '4933790542', 'word': '枪'},
             {'code': '4766000693', 'word': '精'}, {'code': '9173059916', 'word': '毒'},
             {'code': '2090369734', 'word': '熟'}, {'code': '9763512263', 'word': '美'},
             {'code': '9821815185', 'word': '裸'}, {'code': '9925956069', 'word': '处'},
             {'code': '2444947917', 'word': '性'}, {'code': '7051410763', 'word': '马'},
             {'code': '7618693335', 'word': '呻'}, {'code': '0975893408', 'word': '吟'},
             {'code': '0092238155', 'word': '阴'}, {'code': '5213317466', 'word': '具'},
             {'code': '2633701054', 'word': '棒'}, {'code': '5736430795', 'word': '内'},
             {'code': '0783213298', 'word': '丁'}, {'code': '5429058065', 'word': '弟'},
             {'code': '8261828414', 'word': '肛'}, {'code': '2761875847', 'word': '胸'},
             {'code': '0720742117', 'word': '乳'}, {'code': '6050660618', 'word': '屁'},
             {'code': '9928120606', 'word': '腿'}, {'code': '8954155954', 'word': '炮'},
             {'code': '2769203094', 'word': '未'}, {'code': '6259252852', 'word': '杀'},
             {'code': '0423651377', 'word': '插'}, {'code': '3746262645', 'word': '舔'},
             {'code': '6768988724', 'word': '鸡'}, {'code': '9308659858', 'word': '射'},
             {'code': '0961296593', 'word': '弹'}, {'code': '9572021917', 'word': '尿'},
             {'code': '4006928252', 'word': '吞'}, {'code': '6789528781', 'word': '学'},
             {'code': '3342690501', 'word': '舌'}, {'code': '0551722925', 'word': '唇'},
             {'code': '8280163404', 'word': '蛋'}, {'code': '8861933232', 'word': '婊'},
             {'code': '0813524594', 'word': '妓'}, {'code': '5318162318', 'word': '贱'},
             {'code': '4808579862', 'word': '臀'}, {'code': '7130632296', 'word': '席'},
             {'code': '6378369235', 'word': '胡'}, {'code': '5910985788', 'word': '足'},
             {'code': '1810002091', 'word': '九'}, {'code': '1063785572', 'word': '搞'},
             {'code': '3382216428', 'word': '义'}, {'code': '5004143384', 'word': '乱'},
             {'code': '5518664754', 'word': '骚'}, {'code': '0756494362', 'word': '偷'},
             {'code': '5366734122', 'word': '共'}, {'code': '8698737337', 'word': '奶'},
             {'code': '0050897572', 'word': '涛'}, {'code': '1801354585', 'word': '勃'},
             {'code': '0519063805', 'word': '秽'}, {'code': '4481675898', 'word': '荡'},
             {'code': '0551252288', 'word': '龟'}, {'code': '4488426878', 'word': '缝'},
             {'code': '2553168545', 'word': '穴'}, {'code': '9636759436', 'word': '药'},
             {'code': '6534003186', 'word': '蜜'}, {'code': '8993789017', 'word': '洞'},
             {'code': '4668655063', 'word': '潮'}, {'code': '4472054519', 'word': '咪'},
             {'code': '1607055014', 'word': '酸'}, {'code': '6560841485', 'word': '伦'},
             {'code': '2781961287', 'word': '厥'}, {'code': '8926554707', 'word': '炸'},
             {'code': '4704630913', 'word': '茎'}, {'code': '2033008053', 'word': '撸'},
             {'code': '2022721869', 'word': '漏'}, {'code': '1697595086', 'word': '斩'},
             {'code': '6957748176', 'word': '尸'}, {'code': '8051876761', 'word': '漪'},
             {'code': '3893173869', 'word': '介'}, {'code': '4510436554', 'word': '菊'},
             {'code': '3309926634', 'word': '宰'}, {'code': '3780302075', 'word': '氓'},
             {'code': '5710915044', 'word': '童'}, {'code': '6388602220', 'word': '鹏'},
             {'code': '8025291368', 'word': '锦'}, {'code': '0261725863', 'word': '泽'},
             {'code': '0351216125', 'word': '坑'}, {'code': '2729628100', 'word': '颅'},
             {'code': '8592042303', 'word': '腐'}, {'code': '1024850854', 'word': '嫡'},
             {'code': '7736423818', 'word': '剖'}, {'code': '5034779980', 'word': '锡'},
             {'code': '1253164472', 'word': '铀'}]


# 通过图片的名字, 获取到对应的字体
def get_font(id):
	"""
	通过图片的名字, 获取到对应的字体
	:param id: 图片对应的名字
	:return: 对应图片的字体
	"""
	for font in font_list:
		if id == font['code']:
			return font['word']
	else:
		print('未找到对应的字体, 请联系作者.')
		return '[]'


# 转化目录页链接的函数
def generate_links(base_url, total_pages):
	"""
	处理目录页的链接
	:param base_url: 原始的链接
	:param total_pages: 总共有多少页目录
	:return links: 目录页的所有链接
	"""
	links = []
	for i in range(1, total_pages + 1):
		if i == 1:
			links.append(base_url)  # 第一页不需要带下划线和页码
		else:
			links.append(f"{base_url.rstrip('/')}_{i}/")  # 其余页加下划线和页码
	return links


print('等待页面加载完成.....')
# page.get('https://www.banzhu33333.com/')


# 输入书本的链接
book_url = 'https://www.banzhu11111.com/35/35780/'
# book_url = 'https://www.banzhu33333.com/'
page.get(book_url)
if '正在验证' in page.ele('tag:p').text:
	print('手动通过真人验证\n')
	input('按任意键继续...')
# 开始获取目录和书本信息
book_name = page.ele('tag:h1').text
if '/' in book_name:
	book_name = book_name.replace('/', '_')
print(book_name)

# 找到目录的最后一页,并根据目录的页数获取到全部的目录
endPage = page.ele('xpath://div[@class="pagelistbox"]/div[@class="page"]/a['
                   '@class="endPage"]').attr('href').split('_')[-1].replace('/', '')
print(endPage)

# 获取到所有目录页的链接
book_contents = generate_links(book_url, int(endPage))
# TODO 在这里修改, 上一行打开注释, 下一行删除
book_contents = generate_links(book_url, 3)
print(book_contents)


# 获取所有章节链接
def get_chapter_contents(get_contents):
	"""
	获取到整本书的所有章节链接
	:param get_contents: 目录页的链接
	:return chapter_contents: 所有章节的链接
	"""
	# 开始获取目录
	chapter_contents = []
	for content_url in book_contents:
		print(f'开始获取{content_url}目录详情\n')
		page.get(content_url)
		page.wait.load_start(timeout=10)
		if '正在验证' in page.ele('tag:p').text:
			print('手动通过真人验证\n')
			input('按任意键继续...')

		chapter_list = page.eles('xpath://div[@class="mod block update chapter-list"]')[-1] \
			.eles('xpath:.//ul[@class="list"]/li/a')
		print(chapter_list)
		for url in chapter_list:
			chapter_url = url.attr('href')
			chapter_contents.append(chapter_url)
	print('目录获取完成')
	return chapter_contents


# 获取有文字替换的小说内容
def get_img_content(tab):
	"""
	把tab标签传入进来, 获取文章内有图片替换的内容
	:param tab: 页面控制
	:return:
	"""
	# 小说中有图片替换了文字
	html_content = tab.ele('xpath://div[@id="ChapterView"]/div[@class="bd"]/div['
	                       '@class="page-content '
	                       'font-large"]/p').html

	# print(html_content)
	soup = BeautifulSoup(html_content, 'lxml')

	for img in soup.find_all('img'):
		img_id = img['src'].split('/')[-1].split('.')[0]
		# print(img_id)
		font = get_font(img_id)
		img.replace_with(font)

	new_soup = BeautifulSoup(str(soup), 'lxml')
	content = new_soup.get_text(separator='\n')
	print('============>\n')
	print(content)
	print('============>\n')


# exit()

chapter_contents = get_chapter_contents(book_contents)
print(chapter_contents)

# TODO
# 拿到p标签内的源码, 进行替换源码中的img对应位置的文字
for chapter_url in chapter_contents:
	# tab.get(chapter_url)
	tab.get('https://www.banzhu999999.com/35/35780/7321.html')
	tab.wait.load_start()
	if '正在验证' in page.ele('tag:p').text:
		print('手动通过真人验证\n')
		input('按任意键继续...')

	# 获取章节内小说的页数
	pages = tab.eles('xpath://center[@class="chapterPages"]/a')
	print(pages)
	time.sleep(5)

	while True:
		try:
			# 提取当前页的内容
			get_img_content(tab)

			# 定位到当前页面中 class 为 "chapterPages" 的中心区域
			center = tab.ele('xpath://center[@class="chapterPages"]')
			if not center:
				print("未找到分页区域，可能页面结构发生变化或加载异常")
				break

			# 找到所有的页码链接
			page_links = center.eles('xpath:.//a')

			# 定位到当前页后面的“下一页”链接
			current_page = center.ele('xpath:.//a[@class="curr"]')  # 当前页标记为 class="curr"
			if not current_page:
				print("未找到当前页的标记，可能页面结构发生变化")
				break

			current_index = page_links.index(current_page)  # 获取当前页索引

			# 判断是否有下一页
			if current_index < len(page_links) - 1:
				# 点击下一页
				next_page = page_links[current_index + 1]
				next_page_href = next_page.attrs.get('href', '')
				if next_page_href:
					print(f"准备点击下一页: {next_page_href}")
					next_page.click()

					# 等待页面加载完成
					tab.wait.load_start(timeout=10)  # 等待页面完全加载完成，超时时间可调整
					time.sleep(3)
					print("页面加载完成，继续抓取下一页内容")
				else:
					print("下一页链接未找到，可能页面结构发生变化或链接为空")
					break
			else:
				# 已经是最后一页，退出循环
				print("已到最后一页")
				break

		except Exception as e:
			print(f"发生错误: {e}")
			# 可选择在发生错误时，强制刷新页面后重试
			# tab.reload()
			break

	"""
	def get_img_content(tab):
		# 小说中有图片替换了文字
		html_content = tab.ele('xpath://div[@id="ChapterView"]/div[@class="bd"]/div['
		                       '@class="page-content '
		                       'font-large"]/p').html

		print(html_content)
		soup = BeautifulSoup(html_content, 'lxml')

		for img in soup.find_all('img'):
			img_id = img['src'].split('/')[-1].split('.')[0]
			print(img_id)
			font = get_font(img_id)
			img.replace_with(font)

		new_soup = BeautifulSoup(str(soup), 'lxml')
		content = new_soup.get_text(separator='\n')
		print(content)
	"""

	exit()

time.sleep(1000)
