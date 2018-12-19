# note

## 1.urllib2

+ User-Agent

  ```python
  # FireFox
  User-Agent	
  Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/64.0
  
  # Chrome
  User-Agent: 
  Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
  ```

+ code

  ```python
  # -*- coding:utf-8 -*-
  import urllib2
  
  #
  ua_headers = {
      "User-Agent":"Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/64.0"
      # "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
  }
  
  # 通过Request构造请求对象
  request = urllib2.Request("http://www.baidu.com/",headers = ua_headers)
  # 向指定的url地址发动请求
  response = urllib2.urlopen(request)
  
  # 服务器返回的类文件对象支持Python文件对象的操作方法
  # 读取文件中的内容 返回字符串
  html = response.read()
  
  # 返回响应码
  # print response.getcode()
  
  # 返回实际数据的url 防止重定向的问题
  # print response.geturl()
  
  # 返回服务器响应的http报头
  # print response.info()
  
  # 打印响应内
  '''
  默认User-Agent:Python-urllib
  '''
  print html
  ```

+ `IOError: [Errno 22] invalid mode ('w') or filename: '\xe7\xac\xac1\xe9\xa1\xb5.html'`

  [Solution](https://blog.csdn.net/weixin_38278878/article/details/79214220?utm_source=blogxgwz8)

  ```python
  f = open(filename.decode('utf-8'), 'w')
  f.write(html)
  ```

  成功运行，因为是Python中的字符串的大概分为为`str`和`Unicode`两种形式，其中`str`常用的编码类型为`utf-8`,`gb2312`,`gbk`等等，`Python`使用`Unicode`作为编码的基础类型，`open(filename, ‘w’)`这个方法中，filename这个参数必须是`Unicode`编码的参数

+ 贴吧案例

  ```python
  # -*- coding:utf-8 -*-
  
  import urllib
  import urllib2
  
  # http://tieba.baidu.com/f?kw=%E4%BC%A0%E6%99%BA%E6%92%AD%E5%AE%A2&ie=utf-8&pn=100
  
  headers = {
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/64.0"
      }
  
  
  def loadPage(url,filename):
      '''
      跟怒url 发送数据请求 获取服务器响应文件
      url 爬取网站
      filename 处理的文件名
      :return:
      '''
      print "正在下载" + filename
      request = urllib2.Request(url,headers=headers)
      response = urllib2.urlopen(request)
      return response.read()
  
  
  def writePage(html,filename):
      '''
      将html写入本地
      :return:
      '''
      print "正在保存..." + filename
  
      with open(filename.decode("utf-8"), "w") as f:
          f.write(html)
      print "-" * 30
  
  def tiebaSpider(url, beginPage, endPage):
      '''
      贴吧爬虫调度器
      :return:
      '''
      for page in range(beginPage,endPage + 1):
          pn = (page - 1)*50
          filename = "第" + str(page) + "页.html"
          fullurl = url + "&pn=" + str(pn)
          # print fullurl
          html = loadPage(fullurl,filename)
          writePage(html,filename)
          print "谢谢使用..."
  
  
  if __name__ == "__main__":
      kw = raw_input("请输入需要爬去的贴吧名")
      beginPage = raw_input("请输入起始页")
      endPage = raw_input("请输入结束页")
      url = "http://tieba.baidu.com/f?"
      key = urllib.urlencode({"kw":kw})
  
      fullurl = url + key
  
      tiebaSpider(fullurl,int(beginPage),int(endPage))
  
  
  ```

+ 有道翻译的消息头

  ```python
  # POST http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule HTTP/1.1
  
  "Host": "fanyi.youdao.com"
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0"
  "Accept": "application/json, text/javascript, */*; q=0.01"
  "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"
  "Referer": "http://fanyi.youdao.com/"
  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
  "X-Requested-With": "XMLHttpRequest"
  "Content-Length": "260"
  
  ```
