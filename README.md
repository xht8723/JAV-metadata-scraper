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
For windows, scrapper.py  
Use pip to install the above dependencies.  
Your JAV files must contain the series number, eg. ABF-666, dhsuehf@ABF-666shrjf.  
You have to manually visit the Jav Guru site first to get the cookie value and user agent.  
simply fill your cookie value and user agent in "headers" variable. _PHPSISID seems the important one here.  
Put the .py file into the folder where your Jav resides, then run the py there.  

仅测试过Windows,文件是scrapper.py
先安装上面写的两个python库，AV的名字必须要有番号，比如ABF-666, dhsuehf@ABF-666shrjf等.  
然后你需要事先登一下JAVGURU网站来获取你的浏览器user agency，和cookie值。_PHPSISID是必要的cookie值，其它的可以删除（当然最好有）。  
在脚本的header变量里面输入相应的user agency和cookie值就可以了。  
最后把脚本放进AV相同的文件夹，然后运行即可。  
  
  
  
Hardlink--input target directory and link directory, create a hardlink to every file in the target directory, put them in the link directory. (Jellyfin can read hardlinks)  
Hardlink--输入文件夹及目标文件夹，为文件夹下的所有文件创建hardlink硬链放置到目标文件夹。（Jellyfin可以读取硬链，方便管理。）  
  
Rename--Simple rename tool.  
Rename--简单的改名脚本。  

removeXMLtag--simple tool to remove every thing in a .nfo file but keep the XML tags. Only remove values. Sometimes jellyfin have weird behaviors...this might be a fix?
removeXMLtag--移除.nfo文件中所有的值，保留nfo文件的XML tag. 偶尔jellyfin会有奇怪的分类行为...用一下这个试试。

  
## RECOMMEND CONNECTING A VPN OR RISKING A BAN FROM JAV GURU
## 推荐使用VPN，不然有可能被jav guru防机器人ban
