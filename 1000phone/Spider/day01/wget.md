## wget

- 参数
	- -O	以指定文件名保存下载的文件	`wget -O test.png http://httpbin.org/image/png`
	- --limit-rate=200k	以指定的速度下载目标文件 
	- -c 断点续传
	- -b	后台下载
	- -U	设置User-Agent 
	- --mirror	镜像某个目标网站
	- -p	下载页面中的所有相关资源
	- -r	递归下载所有的链接

	### 镜像整个网站并保存到本地
	
		wget -c --mirror --limit-rate=300k -U "Mozilla" -p --convert-links http://docs.python-requests.org