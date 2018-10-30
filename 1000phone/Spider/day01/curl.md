## curl
- 注意: 安装的时候可能会遇到报错,有可能是openssl没装
		
		apt install curl
		apt install openssl
		apt install openssl-dev
- 参数
	- -A	设置user-agent ```curl -A "Chrome" http://www.baidu.com```
	- -X	设置指定方法请求	`curl -X POST http://httpbin.org/post`
	- -I	只返回请求头信息	`curl -I http://www.baidu.com`
	- -d	以POST方法请求url, 并发送相应的参数   
	 `curl -d "a=1&b=2&c=3" http://httpbin.org/post`   
	 `curl -d a=1 -d b=2 -d b=3 http://httpbin.org/post`    
	 `curl -d @/filename http://httpbin.org/post`
	- -O	下载文件并以远程的文件名保存	`curl -O http://httpbin.org/image/jpeg `
	- -o	下载文件并以指定的文件名保存	`curl -o fox.jpeg http://httpbin.org/image/jpeg`
	- -L 	跟随重定向请求	`curl -IL https://baidu.com`
	- -H 设置头信息	`curl -o image.webp -H "accept:image/webp" http://httpbin.org/image`
	- -k 允许发起不安全的SSL请求 `curl -k https://12306.cn`
	- -b 设置cookies 	`curl -b a=test http://httpbin.org/cookies` 
	- -s 不显示其他无关信息

	### 自定义一个命令,查看本机外网IP

	`alias myip="curl -s http://httpbin.org/get |grep -E '[0-9]+' |grep -v User-Agent|cut -d '\"' -f4"`