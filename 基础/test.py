from DrissionPage import ChromiumPage, ChromiumOptions

co = ChromiumOptions().set_local_port(9333).set_user_data_path(
	r'C:\Users\clb14\AppData\Local\Google\Chrome\User Data')
page = ChromiumPage(co)
page.get('baidu.com')
print(page.tab_id)
