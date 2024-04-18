# guruScrapper

A little python script to scrap the JAV metadatas and thumbnails for jellyfin.  
Metadata includes Actress, thumbnail, tags, studios and labels, stored in .nfo fileformat.  
This script will also rename and organize your directories to suit jellyfin file structure.  
The movie file itself won't be renamed but it will be put into a folder with proper name.  
Folder name will be following this format: XXX-YYY [studio] - title (year).
Currently only using JAV GURU site.  
  
一个爬虫脚本，帮你从java guru网站上爬取适用于jellyfin的影片metadata.  
Metadata包括：女优，封面图，标签，工作室，和系列名。以.nfo文件储存。
AV会被移动到相应名字的文件夹中，文件夹的命名格式为：XXX-YYY [工作室] - 标题 (年份).

## Dependencies:

python3  
requests  
BeautifulSoup4  

## Usage:
For windows  
Use pip to install the above dependencies.  
Your JAV files must contain the series number, eg. ABF-666, dhsuehf@ABF-666shrjf.  
You have to manually visit the Jav Guru site first to get the cookie value and user agent.  
simply fill your cookie value and user agent in "headers" variable.  
Put the .py file into the folder where your Jav resides, then run the py there.  

仅测试过Windows
先安装上面写的两个python库，AV的名字必须要有番号，比如ABF-666, dhsuehf@ABF-666shrjf等.  
然后你需要事先登一下JAVGURU网站来获取你的浏览器user agency，和cookie值。  
在脚本的header变量里面输入相应的user agency和cookie值就可以了。  
最后把脚本放进AV相同的文件夹，然后运行即可。  
  
## RECOMMEND CONNECTING A VPN OR RISKING A BAN FROM JAV GURU
## 推荐使用VPN，不然有可能被jav guru防机器人ban
