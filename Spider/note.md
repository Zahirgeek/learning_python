# urllib
- 包含模块
	- urllib.request: 打开和读取urls
	- urllib.error: 包含urllib.request产生的常见的错误,使用try 捕捉
	- urllib.parse: 包含解析url的方法
	- urllib.robotparse: 解析robots.txt文件
	- 案例(urlopen_z.py)

- 网页编码问题解决
	- chardet: 可以自动检测页面文件的编码格式,但是,可能有误
	- 需要安装, conda
	- 案例(chardet_z.py)

- urlopen的返回对象
	- 案例(response_z.py)
	- geturl: 返回请求对象的url
	- info: 请求反馈对象的meta信息
	- getcode: 返回http code

- request.data 的使用
	- 访问网络的两种方法
		- get: 
			- 利用参数给服务器传递信息
			- 参数为dict,然后用parse编码
			- 案例(parse_z.py)
		- post
			- 一般向服务器传递参数使用
			- post是把信息自动加密处理
			- 我们如果想使用post信息,需要用到data参数
			- 使用post,意味着http的请求头可能需要更改:
				- Content-Type: application/x-www.form-urlencode
				- Content-Length: 数据长度
				- 简而言之,一旦更改请求方法,请注意其他请求头部信息相适应
			- urllib.parse.urlencode可以将字符串自动转换成上面的
			- 案例(parse2_z.py)