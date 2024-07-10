from DrissionPage import ChromiumPage, ChromiumOptions

co = ChromiumOptions()
search_val = input('请输入找的商品: ')

page = ChromiumPage()

page.get('https://tb.alicdn.com/')

# 搜索框输入内容
page.ele('#q').input(search_val)

# 点击搜索
page.ele('.btn-search tb-bg').click()
try:
	# 开始获取商品列表
	shops = page.ele('.Content--contentInner--QVTcU0M').eles('.Title--title--jCOPvpf ')
	for item in shops:
		print(item.text)
	# print(shops)
	print('获取完成')
except:
	print('请登录你的账号重新运行文件')