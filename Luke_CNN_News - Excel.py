import requests  # 用于获取网页
from bs4 import BeautifulSoup  # 用于分析网页
import re  # 用于在网页中搜索我们需要的关键字
import os  # 用于设定存储路径
import io  # 处理乱码
import sys  # 处理乱码
from datetime import datetime #加入时间输出
import xlwt #创建Excel用
import pandas
import openpyxl
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # 修改字符存储乱码
###参考文章：https://blog.csdn.net/wenxuhonghe/article/details/90047081《Python 网络爬虫实战：爬取人民日报新闻文章》

## 第一步：整理新闻链接到一个列表

from fake_useragent import UserAgent

def news_to_list():
    try:
        ua = UserAgent()
        headers = {'User-Agent': ua.random}
        url = 'http://lite.cnn.com/en'
        response = requests.get(url, headers=headers)
        html = requests.get(url)
        html.raise_for_status()
        print("The website status is:",response.status_code)
    except:
        print("Check this web")
        return ""
    soup = BeautifulSoup(html.text, 'html.parser')
    #print(soup.prettify()) (可选)格式化输出html解析页面
    newslist = soup.find('div', attrs={'class': 'afe4286c'}).ul.find_all('li') #所有文章的链接处于div/ul/li/路径下
    #print(newslist) （可选）验证上述语句范围的正确性
    news_list = []  # 将提取出来的内容放到一个列表
    for title in newslist:
        templist = title.find_all('a')
        for temp in templist:
            link = temp['href']
            if "/en/article" in link:
                page = 'http://lite.cnn.com' + link
                news_list.append(page)
#代办：如何累计所有历史新闻链接+标题存到一个excel文件，并在excel中对重复链接判断重复的不写入。
    #return news_list （可选）可下行print二选一都行，用于验证list是否成功，return只是不打印
    #print(news_list) #用于验证list是否成功
    print("Total of news:", len(news_list))

## 第二步：建立txt文档并存储新闻进去
    #newsfile = open("news.txt", "a", encoding="utf-8") （可选）同下行，建立一个文档存储路径
    #dt = str(datetime.now().strftime("%Y-%m-%d_%H%M")) （可选）配套下行给txt文件名加入日期字段
    with io.open("CNN_news.txt","a+",encoding="utf-8") as newsfile: #from Luke:如果需要引入日期，则open里面改成：dt+"CNN_news.txt"
        for cont in news_list: # count就是每条新闻对应的网址
            html1 = requests.get(cont)
            bsobj = BeautifulSoup(html1.text, 'html.parser')
            # 获取文章 标题\日期\内容
            title = bsobj.h2.text + '\t'
            thedate = bsobj.find("div", id="published datetime").get_text() + '\n'
            pList = bsobj.find('div', attrs={'id': 'mount'}).find_all('p')
            content = ""
            for p in pList:
                content += p.text + '\n' #每个p标签内文字归入一行然后回车
##代办：此处需要delete contents的最后三行内容，用正则表达式
            #下行语句测试删除新闻最后三行内容但是运行输出总是空，放弃
            #exclude = list(re.findall(r'^(Network)(experience)$',content))
            #print(exclude) #验证剔除的结果是否正确
            sy= datetime.now().strftime("%Y-%m-%d_%H%M") #每个文章后加入程序运行也就是同步的时间
            resp = "Sync Time:" + sy + "\n" + title + thedate + content + "\n"+"\n"  # 打印文章内容
            newsfile.write(resp) #调试前因为缩进问题遇到过问题。
    newsfile.close()

#第三步：用pandas库做词频分析，每日输出排行用字典形式输出
def count_words():
    f = open('CNN_news.txt',encoding= "utf-8")
    readline = f.readlines() #readlines读取文章所有行并输出列表（每行为一个元素）
    # 重点：下行语句将单词统一到小写，方便后续统计单词频次的时候不会出现同一个单词多次统计。关键字lower, isinstance
    readline = [x.lower() for x in readline if isinstance(x, str)]
    word = []  # 存储单词
    # 得到文章的单词并且存入列表中：
    for line in readline: #此时line便是每一行得内容。
        # 因为原文中每个单词都是用空格 或者逗号加空格分开的，
        line = line.replace(',', '')  # 除去逗号只要空格来分开单词
        line = line.strip() #移除每一行前后得多余得空格或换行符号（括号内空表示空格或换行）
        #用正则去除简单单词（am, is, are 等少于4个字符得单词）
        line = re.sub(r"[^a-zA-Z]+", " ", line)  # 用正则将数字、符号等剔除掉
##取消下行：下行尝试用re剔除3个字母以下单词总是结果不对，放弃
        #line = re.sub(r"\s[a-zA-Z]{1,3}\s"," ",line) #用正则将3个字母以下的单词剔除掉(刘老师建议不剔除）
        wo = line.split(' ') #对每行元素进行切割并输出列表（分割依据是空格），所以wo为一个新列表
        word.extend(wo) # extend语句合并所有wo列表。
    return word
def clear_account(lists):
    # 去除重复的值
    wokey = {}
    wokey = wokey.fromkeys(lists) #查看main的参数赋值，此处lists为countword函数返回的所有单词列表
    word_1 = list(wokey.keys()) # 用字典wokey讲单词统作为键（频次为值）然后赋值给word_1作为一个列表
    # 然后统计单词出现的次数,并将它存入一个字典中
    for i in word_1:
        wokey[i] = lists.count(i) # 此处统计单词的频次赋值给字典wokey作为值.
    del wokey['']
    return wokey
def sort_1(wokey):
    # 排序,按values进行排序，如果是按key进行排序用sorted(wokey.items(),key=lambda d:d[0],reverse=True)
    wokey_1 = {} #定义一个字典形式
    wokey_1 = sorted(wokey.items(), key=lambda d: d[1], reverse=False) #sorted行数排序，最后一个键决定降序还是升序（False为升序）
    return wokey_1
    # print(sort_1(clear_account(read_file())))
def length_words(): # 新增一列D列统计单词的长度
    web = open(r"C:\Users\xyang\OneDrive - Goldwind USA, Inc\004-Learning\003.Python\PythonPractice\wordlist.xls",encoding= "utf-8")
    web = openpyxl.load_workbook("wordlist.xls")
    sheet = web["sheet1"]
    for i in (1,20000):
        cell1 = sheet["Ai"]
        cell2 = sheet["A(i+3)"]
        cell2 = len(cell1)
    return cell2
    web.save(filename = "wordlist.xls")

def main(wokey_1):
    print("Working Time: ",datetime.now().strftime("%Y-%m-%d_%H%M"))
    news_to_list() #★★★每天8：00、22：00运行两次。
    i = 0
    for x, y in wokey_1:
        if i < 20:   #此处用于保存输出单词的数量，每次学习100单词
            print('The word: %s, counted frequency is %d' % (x, y))
            i += 1
            continue
        else:
            break
    #print(type(wokey_1)) #验证结果的类型（列表）
# 实例化输出一个工作表，名叫wordlist
    wordlist = xlwt.Workbook()
    sht1 = wordlist.add_sheet('Sheet1')
    sht2 = wordlist.add_sheet('Sheet2_spare')
# 第一个参数是行，第二个参数是列，第三个参数是值,第四个参数是格式
# 第一行做标题栏,第二行开始是单词
###代办：后续考虑存储到数据库 - 刘老师建议
    sht1.col(0).width = 256 * 20 # 定义列宽
    sht1.col(1).width = 256 * 20
    sht1.col(2).width = 256 * 40
    sht1.col(3).width = 256 * 30
    sht1.write(0, 0, '单词名称WordName')
    sht1.write(0, 1, '单词频次Frequency')
    sht1.write(0, 2, '记忆状态会/不会New/Old')
    sht1.write(0, 3, '单词长度Lenth')
    row = 1  # 行号
    for stu in wokey_1:  # 控制行,wokey_1是由单词、频次构成的字典格式
        col = 0  # 列号
        for field in stu:  # 控制列，结合上一条语句0列为单词、1列为频次
            sht1.write(row, col, field)
            col += 1
        row += 1
    wordlist.save(r'C:\Users\xyang\OneDrive - Goldwind USA, Inc\004-Learning\003.Python\PythonPractice\wordlist.xls')
    #length_words()
#代办：定义函数逆推excel每个单词对应句子，通过句子学习单词；
#代办：利用数据库格式存储单词开放（库文件mysql(刘老师推荐)、pymysql）

# 程序执行开始：
main(sort_1(clear_account(count_words())))
