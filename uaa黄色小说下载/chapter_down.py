import time
from DrissionPage import ChromiumPage

page = ChromiumPage()
tab = page.new_tab()
print('等待页面加载完成.....')
page.get('https://www.uaa001.com/')

while True:
	# print('请你登录账号, 登录完成之后输入"1"继续进行操作')
	# chapter_url = 'https://www.uaa004.com/novel/chapter?id=207401'
	chapter_url = input('请你登录账号, 登录完成之后输入你要下载的书本章节: \n')
	print('开始解析章节链接.....')
	# 通过章节链接,获取到书本名和章节信息
	tab.get(chapter_url)
	tab.wait(1, 3)
	chapter_name = tab.ele('tag:h2').text

	if '/' in chapter_name:
		book_name = chapter_name.replace('/', '_')
	print(chapter_name)

	with open(chapter_name + '.txt', 'w', encoding='utf-8') as f:
		print(f'开始写入 {chapter_name}....')
		f.write(chapter_name)
		f.write('\n\n')
		try:
			# print(page.html)
			contents = tab.eles('xpath://div[@class="line"]')
			for content in contents:
				# print(content.text)
				if '以下正文内容已隐藏' in content.text:
					print('\n出现检测, 请检查是否登录或者是VIP章节, 需要购买后下载...\n')
					input('出现检测, 如果是验证码请手动过检测后 输入任意键 继续下载...\n\n')
					tab.get(chapter_name)
					contents = tab.eles('xpath://div[@class="line"]')
					for content in contents:
						f.write(content.text)
						f.write('\n')
				else:
					f.write(content.text)
					f.write('\n')
			f.write('\n\n')
			print('\n下载完成!!!\n')
		except Exception as e:
			print(f'{chapter_name}下载失败!!! 请重试!!!')
			print('请检查是否是网络波动原因!!!')

		print('\n请输入链接, 如果不需要直接关闭软件!!!')
