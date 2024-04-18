# guruScrapper

A little python script to scrap the JAV metadatas and thumbnails for jellyfin.  
Metadata includes Actress, thumbnail, tags, studios and labels.  
Currently only using JAV GURU site.  
一个爬虫脚本，帮你从java guru网站上爬取适用于jellyfin的影片metadata.  
Metadata包括：女优，封面图，标签，工作室，和系列名。  

## Dependencies:

python3  
requests  
BeautifulSoup4  

## Usage:
For windows  
Use pip to install above dependencies.  
Your JAV files must contain the serie number, eg. ABF-666, dhsuehf@ABF-666shrjf.  


You have to manually visit the jav guru site first to get the cookie value and user agent.  
simply fill your cookie value and user agent in "headers" variable.  
Put the .py file into the folder where your jav resides, then run the py there.  

## RECOMMEND CONNECTING A VPN OR RISKING A BAN FROM JAV GURU
