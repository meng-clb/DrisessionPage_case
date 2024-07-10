from DrissionPage import ChromiumPage, ChromiumOptions

co = ChromiumOptions().set_user_data_path(
	r'C:\Users\clb14\AppData\Local\Temp\DrissionPage\userData_9222').set_local_port(9333)

page = ChromiumPage(co)
print(co.address)
print(co.user_data_path)