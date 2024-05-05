# JAV media tools for jellyfin

A little python script to scrap the JAV metadatas and thumbnails for jellyfin(maybe emby too idk).  
Metadata includes Actress, thumbnail, tags, studios and labels, stored in .nfo fileformat.  
This script will also rename and organize your directories to suit jellyfin file structure.  
The movie file itself won't be renamed but it will be put into a folder with proper name.  
Folder name will be following this format: XXX-YYY [studio] - title (year).  
Currently only using JAV GURU site.  
Also includes some simple tools like creating hardlink for all files in folder, renaming, manaul creating nfo file .etc.
  
一个爬虫脚本，帮你从java guru网站上爬取适用于jellyfin（或许emby也行？）的影片metadata.  
Metadata包括：女优，封面图，标签，工作室，和系列名。以.nfo文件储存。  
AV会被移动到相应名字的文件夹中，文件夹的命名格式为：XXX-YYY [工作室] - 标题 (年份).  
其它还包括一些非常简单的小工具，诸如批量重命名，手动创建NFO文件，批量创建硬链接等。


## Dependencies:

requests  
BeautifulSoup4
ttkbootstrap  


## Usage/使用

Your JAV files must contain the series number, eg. ABF-666, dhsuehf@ABF-666shrjf.  
You have to manually visit the Jav Guru site first to get the cookie value and user agent, fill the value in the GUI accordingly.  

AV的名字必须要有番号，比如ABF-666, dhsuehf@ABF-666shrjf等.  
然后你需要事先登一下JAVGURU网站来获取你的浏览器user agency，和对应的cookie值，填入GUI中，点击绿色按钮即可。  


### EXE
Download in release.  
Due to the mysterious Windows Defender flagging them as viruses randomly, providing two versions of executables.  
They are functionally the same, the console version will have a windows cmd opening with it.  
If both version got flagged as virus, and you are really sure about this, just run the original python file.  

由于神秘的Windows防火墙会随机把文件测成病毒，所以给了两个版本。  
两个版本功能是一样的，只是console版本会同时打开一个windows命令行。  
如果两个版本都被标记成病毒，你也不想冒险的话，只好运行python原文件了。  


### running python/运行python
Download all source files.  
Use pip to install the above dependencies.  
Run MediaTool_v0.3.py  

解压源文件。  
安装上述Dependencies  
运行MediaTool_v0.3.py  
  

## others
Hardlink--input target directory and link directory, create a hardlink to every file in the target directory, put them in the link directory. (Jellyfin can read hardlinks)  
Hardlink--输入文件夹及目标文件夹，为文件夹下的所有文件创建hardlink硬链放置到目标文件夹。（Jellyfin可以读取硬链，方便管理。）  
  
Rename--Simple rename tool.  
Rename--简单的改名脚本。  

remove XML--simple tool to remove every thing in a .nfo file but keep the XML tags. Only remove values. Sometimes jellyfin have weird behaviors...this might be a fix?  
remove XML--移除.nfo文件中所有的值，保留nfo文件的XML tag. 偶尔jellyfin会有奇怪的分类行为...用一下这个试试。  

manual create .nfo--manually input .nfo information  
manual create .nfo--手动输入并创建.nfo文件  

  
## RECOMMEND CONNECTING A VPN OR RISKING A BAN FROM JAV GURU
## 推荐使用VPN，不然有可能被jav guru防机器人ban
