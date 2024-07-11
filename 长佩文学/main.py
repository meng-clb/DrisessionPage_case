from DrissionPage import WebPage
import json
page = WebPage()

page.get('https://m.gongzicp.com/novel-1184818.html')
# page.ele('text=立即阅读').click()
page.get('https://m.gongzicp.com/read-5995154.html')

page.change_mode('s')
page.get('https://m.gongzicp.com/webapi/novel/chapterGetInfo?cid=5903450&server=0')
print(page.json)


