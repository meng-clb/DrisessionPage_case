import os
import time
from DrissionPage import ChromiumPage
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

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


def get_font(id):
	"""
	根据图片名称获取对应的字体。

	:param id: 图片对应的名称
	:return: 字体对应的文字
	"""
	for font in font_list:
		if id == font['code']:
			return font['word']
	print(f"未找到对应的字体: {id}, 请联系作者.")
	return '[]'


def generate_links(base_url, total_pages):
	"""
	根据总页数生成所有目录页链接。

	:param base_url: 原始链接
	:param total_pages: 总页数
	:return: 目录页的所有链接
	"""
	links = [base_url] if total_pages == 1 else [f"{base_url.rstrip('/')}_{i}/" for i in
	                                             range(1, total_pages + 1)]
	return links


def wait_for_page_load(page, timeout=10):
	"""
	等待页面加载完成。

	:param page: 页面对象
	:param timeout: 超时时间
	"""
	page.wait.load_start(timeout=timeout)


def get_book_name(page):
	"""
	获取书本名称，处理特殊字符（如 '/'）。

	:param page: 页面对象
	:return: 书本名称
	"""
	book_name = page.ele('tag:h1').text
	return book_name.replace('/', '_') if '/' in book_name else book_name


def get_end_page(page):
	"""
	获取目录页的最后一页。

	:param page: 页面对象
	:return: 最后一页的页码
	"""
	end_page_url = page.ele('xpath://div[@class="pagelistbox"]/div[@class="page"]/a['
	                        '@class="endPage"]').attr('href')
	return end_page_url.split('_')[-1].replace('/', '')


def get_chapter_contents(book_contents, page):
	"""
	获取整本书的所有章节链接。

	:param book_contents: 目录页链接列表
	:param page: 页面对象
	:return: 所有章节的链接
	"""
	chapter_contents = []
	for content_url in book_contents:
		print(f"开始获取 {content_url} 目录详情")
		page.get(content_url)
		wait_for_page_load(page)

		if '真人' in page.ele('tag:p').text:
			print('手动通过真人验证')
			input('按任意键继续...')

		chapter_list = page.eles('xpath://div[@class="mod block update chapter-list"]')[-1] \
			.eles('xpath:.//ul[@class="list"]/li/a')

		for url in chapter_list:
			chapter_url = url.attr('href')
			chapter_contents.append(chapter_url)

	print('目录获取完成')
	return chapter_contents


def get_img_content(tab):
	"""
	获取章节中的图片替换内容，并将图片替换为文字。

	:param tab: 页面控制对象
	:return: 替换后的文本内容
	"""
	while True:
		try:
			html_content = tab.ele(
				'xpath://div[@id="ChapterView"]/div[@class="bd"]/div[@class="page-content '
				'font-large"]/p').html
			if not html_content:  # 如果没有找到元素
				print("未找到元素，正在刷新页面...")
				tab.refresh()
				wait_for_page_load(tab)
				continue  # 重新尝试获取内容

			soup = BeautifulSoup(html_content, 'lxml')

			for img in soup.find_all('img'):
				img_id = img['src'].split('/')[-1].split('.')[0]
				font = get_font(img_id)
				img.replace_with(font)

			new_soup = BeautifulSoup(str(soup), 'lxml')
			content = new_soup.get_text(separator='\n')

			return content

		except Exception as e:
			print(f"发生错误: {e}")
			break


def save_chapter_to_file(book_name, chapter_url, chapter_content):
	"""
	保存章节内容到文件。

	:param book_name: 书名，用于命名文件
	:param chapter_url: 章节链接，用于记录章节信息
	:param chapter_content: 章节内容
	"""
	file_name = f"{book_name}.txt"
	try:
		with open(file_name, "a", encoding="utf-8") as file:
			# file.write(f"章节链接: {chapter_url}\n")
			file.write(f"{chapter_content}\n")
			file.write("=" * 50 + "\n")  # 分隔符
		print(f"章节已保存到 {file_name}")
	except Exception as e:
		print(f"保存章节内容失败: {e}")


def process_chapters(chapter_contents, tab, book_name):
	"""
	处理所有章节的内容，包括分页和图片替换。

	:param chapter_contents: 章节链接列表
	:param tab: 页面控制对象
	"""
	for chapter_url in chapter_contents:
		tab.get(chapter_url)
		wait_for_page_load(tab)
		if '真人' in tab.ele('tag:p').text:
			print('手动通过真人验证')
			input('按任意键继续...')

		while True:
			try:
				content = get_img_content(tab)
				save_chapter_to_file(book_name, chapter_url, content)
				print("章节内容：\n", content)
				time.sleep(3)

				center = tab.ele('xpath://center[@class="chapterPages"]')
				page_links = center.eles('xpath:.//a')
				current_page = center.ele('xpath:.//a[@class="curr"]')
				current_index = page_links.index(current_page)

				if current_index < len(page_links) - 1:
					next_page = page_links[current_index + 1]
					next_page_href = next_page.attrs.get('href', '')
					if next_page_href:
						print(f"准备点击下一页: {next_page_href}")
						next_page.click()
						wait_for_page_load(tab)
					else:
						print("下一页链接未找到")
						break
				else:
					print("已到最后一页")
					break

			except Exception as e:
				print(f"发生错误: {e}")
				break


def main():
	"""
	主函数，控制程序执行流程。
	"""
	page = ChromiumPage()
	tab = page.new_tab()

	book_url = 'https://www.banzhu11111.com/35/35780/'
	page.get(book_url)
	wait_for_page_load(page)

	if '真人' in page.ele('tag:p').text:
		print('手动通过真人验证')
		input('按任意键继续...')

	book_name = get_book_name(page)
	print(f"书名: {book_name}")

	end_page = get_end_page(page)
	print(f"最后一页: {end_page}")

	book_contents = generate_links(book_url, int(end_page))
	print(f"目录页链接: {book_contents}")

	chapter_contents = get_chapter_contents(book_contents, page)
	print(f"章节链接: {chapter_contents}")

	process_chapters(chapter_contents, tab, book_name)


if __name__ == '__main__':
	main()
