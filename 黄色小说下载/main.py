import time
from DrissionPage import ChromiumPage

page = ChromiumPage()
tab = page.new_tab()
print('等待页面加载完成.....')
page.get('https://www.uaa001.com/')
# print('请你登录账号, 登录完成之后输入"1"继续进行操作')
book_url = input('请你登录账号, 登录完成之后输入你要下载的书本链接: \n')
print('开始解析书本链接.....')
# 通过书本的详情页链接, 获取书本的目录信息
page.get(book_url)
# page.get('https://www.uaa.com/novel/intro?id=11302895')  # 2000 大章节
# page.get('https://www.uaa.com/novel/intro?id=1017583002777161728')

# 获取到书本的信息
book_name = page.ele('tag:h1').text
if '/' in book_name:
	book_name = book_name.replace('/', '_')
print(book_name)

# 根据不同的书本目录, 获取到全部的目录信息
a_list = page.eles('xpath://ul[@class="catalog_ul"]//li[@class="child " or @class="child '
                   'hide"]/a') or \
         page.eles('xpath://ul[@class="catalog_ul"]//li[@class="menu " or @class="menu hide"]/a')


# print(a_list)
# print(len(a_list))
print(f'共获取到{len(a_list)}章节目录')
# time.sleep(10000)

with open(book_name + '.txt', 'w', encoding='utf-8') as f:
	for a in a_list:
		chapter_name = a.text
		chpater_url = a.attr('href')
		# print(chapter_name, chpater_url) 
		print(f'开始写入 {chapter_name}....')
		# print(chpater_url)
		f.write(chapter_name)
		f.write('\n\n')
		try:
			# time.sleep(1)
			tab.get(chpater_url)
			tab.wait(1, 3)
			# print(page.html)
			contents = tab.eles('xpath://div[@class="line"]')
			for content in contents:
				# print(content.text)
				if '以下正文内容已隐藏' in content.text:
					print('\n出现检测, 请检查是否登录或者是VIP章节, 需要购买后下载...\n')
					input('出现检测, 如果是验证码请手动过检测后 输入任意键 继续下载...\n\n')
					tab.get(chpater_url)
					contents = tab.eles('xpath://div[@class="line"]')
					for content in contents:
						f.write(content.text)
						f.write('\n')
				else:
					f.write(content.text)
					f.write('\n')
			f.write('\n\n')
		except Exception as e:
			print(f'{chapter_name}下载失败!!! 跳过此章节!!!')
			print('请检查是否是网络波动原因!!!')
			input('输入任意键继续下载!!!')
input('程序运行结束, 按下任意键退出程序......')
