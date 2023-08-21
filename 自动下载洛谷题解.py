from selenium import webdriver as web
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
import pyperclip
import time
import os

#打开驱动
wd=web.Chrome()
wd.maximize_window()
wd.implicitly_wait(20)

# 绕过浏览器检测
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_argument("disable-blink-features=AutomationControlled")
option.add_experimental_option('useAutomationExtension', False)
wd.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => false
    })
  """
})



# 进洛谷
wd.get("https://www.luogu.com.cn")

# 定位到登录
login=wd.find_element(By.CSS_SELECTOR,"#app > div.main-container > div.wrapper.wrapped.lfe-body.header-layout.tiny > div.container > nav > a:nth-child(2) > span")
login.click()
# 定位用户名
user=wd.find_element(By.CSS_SELECTOR,"#app > div.main-container > main > div > div > div > div > div > div > div:nth-child(1) > div > input")
user.send_keys("大橙子老师")
# 定位密码
password=wd.find_element(By.CSS_SELECTOR,"#app > div.main-container > main > div > div > div > div > div > div > div:nth-child(2) > div > input")
password.send_keys("luogu19990326")
# 验证码
identifyingCode=wd.find_element(By.CSS_SELECTOR,"#app > div.main-container > main > div > div > div > div > div > div > div:nth-child(3) > div > div.refined-input.input-wrap.frame > input")
identifyingCode.click()
# time.sleep(5)
# 点击头像
head=wd.find_element(By.CSS_SELECTOR,"#app > div.main-container > div.wrapper.wrapped.lfe-body.header-layout.tiny > div.container > nav > span > span > a > img")
head.click()
# 我的
my=wd.find_element(By.CSS_SELECTOR,"#app > div.main-container > main > div > div.card.user-header-container.padding-0 > div.user-header-bottom > div.menu > ul > li:nth-child(4) > span")
my.click()
# 我加入的团队
mygroup=wd.find_element(By.CSS_SELECTOR,"#app > div.main-container > main > div > div.full-container > div > div.sub-header > div > ul > li:nth-child(2) > span")
mygroup.click()
# 大橙子和他的学生们
orangeAndStudent=wd.find_element(By.CSS_SELECTOR,"#app > div.main-container > main > div > div.full-container > div > div.sub-body > div > div:nth-child(2) > div > a")
orangeAndStudent.click()

# 所有题单
problemlists=wd.find_element(By.CSS_SELECTOR,"#app > div.main-container > main > div > div.card.padding-none > div > ul > li:nth-child(4) > span")
problemlists.click()

# 单个题单
problemlist=wd.find_element(By.CSS_SELECTOR,"#app > div.main-container > main > div > div.card.padding-default > div:nth-child(2) > div.block > div > div:nth-child(7) > div > div.box.left-box > a")
# 创建一个文件夹
path=problemlist.text
if not os.path.exists(path):
  os.mkdir(path)
problemlist.click()
time.sleep(2)

# 题目列表
newproblemlist=wd.find_element(By.CSS_SELECTOR,"#app > div.main-container > main > div > div.card.padding-none > div > ul > li:nth-child(2) > span")
newproblemlist.click()

time.sleep(3)
# for循环遍历所有题目
divlist=wd.find_element(By.CSS_SELECTOR,"#app > div.main-container > main > div > div.card.padding-default > div > div.border.table > div.row-wrap")
# 题目的div列表
divlists = divlist.find_elements(By.XPATH, "./div")#获取到当前元素的第一层所有的div子元素



# 遍历div列表
for i in range(len(divlists)):
    problem=divlists[i].find_element(By.TAG_NAME,"div").find_element(By.TAG_NAME,"a")
    problem.click()
    time.sleep(1)
    # 切换到新标签页
    tips= wd.window_handles
    wd.switch_to.window(tips[1])

    # 获取文件名称
    filename=wd.find_element(By.CSS_SELECTOR,"#app > div.main-container > div.wrapper.wrapped.lfe-body.header-layout.normal > div.header > h1 > span").text
    filename=filename.replace("/","")
    # 提交记录
    commitRecord=wd.find_element(By.CSS_SELECTOR,"#app > div.main-container > main > div > section.side > div:nth-child(1) > a:nth-child(2)")
    commitRecord.click()
    time.sleep(2)

    # 用户名
    username=wd.find_element(By.CSS_SELECTOR,"#app > div.main-container > main > div > section > div > section:nth-child(1) > div > div > div:nth-child(2) > input")
    username.send_keys("大橙子老师\n")
    time.sleep(2)

    # accepted
    accepted=wd.find_element(By.CSS_SELECTOR,"#app > div.main-container > main > div > div > div > div.border.table > div > div > div.status > a > span.lfe-caption.tag.status-name")
    accepted.click()
    time.sleep(1)

    # 切换到新标签页
    tips= wd.window_handles
    wd.switch_to.window(tips[-1])

    # 源代码
    sourcecode=wd.find_element(By.CSS_SELECTOR,"#app > div.main-container > main > div > section.main > section > div.card.padding-none > div > ul > li:nth-child(2) > span")
    sourcecode.click()
    # time.sleep(1)

    # copy
    copy=wd.find_element(By.CSS_SELECTOR,"#app > div.main-container > main > div > section.main > section > div:nth-child(2) > div > div > button")
    copy.click()

    # 尝试直接创建文件并写入，不用dev-cpp
    text=pyperclip.paste()
    # filePath="2、运算符与分支结构/"
    filePathComplete=path+"/"+filename+".cpp"
    newfile=os.open(filePathComplete,os.O_CREAT | os.O_RDWR)
    # 处理多余回车
    text = text.replace("\r", "")
    text=text.encode("gbk")
    os.write(newfile,text)
    os.close(newfile)

    # 获取到所有窗口句柄
    all_handles = wd.window_handles

    # 关闭右边的标签页
    for handle in all_handles[1:]:
        wd.switch_to.window(handle)
        wd.close()

    # 切换到第一个标签页
    wd.switch_to.window(all_handles[0])

    # break

#打一个中断
input()
