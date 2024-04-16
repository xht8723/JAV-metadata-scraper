import sys
import os
import shutil
import requests
import re
from bs4 import BeautifulSoup
from datetime import date, datetime


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'output.html')

javguru_search_url = "https://jav.guru/?s="
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Cookie': '_ga=GA1.1.1355043263.1685224096; PHPSESSID=h0bn1a946dmk5p1il5ff8cjcbd; _ga_83WTHH81CR=GS1.1.1712917919.142.0.1712917929.0.0.0'
}
file_format = [
    '.mp4',
    '.MP4',
    '.mkv',
    '.rmvb',
    '.AVI',
    '.avi'
]

#manage the file structure for jellyfin. create nfo and download image
def manageStructure(directory='.'):
    # Get the list of files in the specified directory
    file_list = os.listdir(directory)
    pattern = re.compile('([a-zA-Z]+-\d+)')
    processed_files = []
    #looping
    for file in file_list:
        #optimize file name and prepare for more process
        filename, format = os.path.splitext(file)
        if format in file_format:
            match = pattern.findall(filename)
            if match:
                banngo = match[0].upper()
                processed_files.append(banngo)
            else:
                print("error in looping banngo")
                sys.exit(1)

            data = findData_javguru(banngo)
            #Move the file into a folder with proper name
            folder_name = banngo + ' [' + data['studio'] + '] - ' + data['title'] + ' (' + data['release date'].split('-')[0] + ')'
            try:
                folder_path = os.path.join('.', folder_name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                shutil.move(file, folder_path)
            except AttributeError as e:
                print(file)
                print(str(e))

            #download image
            image = downloadImage(data)
            shutil.move(image, folder_path)

            #create nfo file
            nfo_name = filename + ".nfo"
            createNFO(nfo_name, data, folder_path + image)
            shutil.move(nfo_name, folder_path)

    #create logs
    with open("logs.txt", 'w') as f:
        f.write("preocessed files: /n")
    

#using data to create the nfo file.
def createNFO(nfo_name, data, image):
    name, _ = os.path.splitext(nfo_name)
    with open(name + '.nfo', 'w+', encoding = 'utf-8') as f:
        f.write('<?xml version="1.0" encoding="utf-8" standalone="yes"?>\n')
        f.write('<movie>\n')
        f.write('\t<dateadded>' + str(date.today()) + ' ' + str(datetime.now()) + '</dateadded>\n')
        f.write('\t<title>' + data['title'] + '</title>\n')
        f.write('\t<year>' + data['release date'].split('-')[0] + '</year>\n')
        f.write('\t<mpaa>XXX</mpaa>\n')
        f.write('\t<tmdbid>' + data['banngo'] + '</tmdbid>\n')
        f.write('\t<premiered>' + data['release date'] + '</premiered>\n')
        f.write('\t<releasedate>' + data['release date'] + '</releasedate>\n')
        for eachtag in data['tags']:
            f.write('\t<genre>' + eachtag + '</genre>\n')
        f.write('\t<studio>' + data['label'] + '</studio>\n')
        f.write('\t<tag>' + data['actress'] + '</tag>\n')
        f.write('\t<art>\n')
        f.write('\t\t<poster>' + image + '</poster>\n')
        f.write('\t\t<fanart>' + image + '</fanart>\n')
        f.write('\t</art>\n')
        f.write('\t<actor>\n')
        f.write('\t\t<name>' + data['actress'] + '</name>\n')
        f.write('\t\t<role>Actress</role>\n')
        f.write('\t\t<type>Actor</type>\n')
        f.write('\t</actor>\n')
        f.write('\t<set>' + data["studio"] + '</set>\n')
        f.write('\t<thumb>' + data['image'] + '</thumb>\n')
        f.write('</movie>')


#Function to extract metadata from javguru
def findData_javguru(banngo):
    #compile regex to match from url
    regex = re.compile(r'<a title="\[' + re.escape(banngo) + r'\] .*"')
    try:
        search = requests.get(javguru_search_url + banngo, headers = headers)
        result = regex.search(search.text)
    except:
        print("did not found search result for ", banngo)
        sys.exit(1)

    #extract title and url from previous match
    regex = re.compile(r'<a title="(?P<title>.*?)" href="(?P<href>.*?)"')
    try:
        match = regex.search(result.group())
        title = match.group('title')
        title = title.split(']')[1]
        target_url = match.group('href')
    except:
        print("didnt find title information")
        sys.exit(1)

    #open target url to extract metadata
    search = requests.get(target_url, headers = headers)
    soup = BeautifulSoup(search.text, 'html.parser')
    try:
        targetinfo = soup.find('div', class_ = 'infoleft')
        targetinfo = str(targetinfo)
    except:
        print("did not find infoleft")
        sys.exit(1)

    #extract metadata
    try:
        release_date = re.search(r'Release Date: </strong>(\d{4}-\d{2}-\d{2})', targetinfo).group(1)
    except:
        print("no release date information")
        release_date = date.today()
    try:
        director = re.search(r'Director: </strong> <a href=".*" rel="tag">(.*)</a>', targetinfo).group(1)
    except:
        print("no director information")
        director = ''
    try:
        studio = re.search(r'Studio: </strong> <a href=".*" rel="tag">(.*)</a>', targetinfo).group(1)
    except:
        print("no studio information")
        studio = ''
    try:
        label = re.search(r'Label: </strong> <a href=".*" rel="tag">(.*)</a>', targetinfo).group(1)
    except:
        print("no label information")
        label = ''
    try:
        tags = re.findall(r'Tags: </strong>(.*)</li>', targetinfo)[0]
        regex = re.compile('([A-Za-z]*)<\/a>')
        tags = regex.findall(tags)
    except:
        print("no tag information")
        tags = ''
    try:
        actress = re.search(r'Actress: </strong> <a href=".*" rel="tag">(.*)</a>', targetinfo).group(1)
    except:
        print("no actress information, set actress to unknown")
        actress = 'unknown'


    #find image adress
    try:
        imageAdress = soup.find('div', class_ = 'large-screenimg')
        imageAdress = str(imageAdress)
        soup = BeautifulSoup(imageAdress, 'html.parser')
        imageAdress = soup.find('img')['src']
    except:
        print("did not find image adress")
        imageAdress = ''

    data = {
        'title':title,
        'banngo':banngo,
        'release date':release_date,
        'director':director,
        'studio':studio,
        'label':label,
        'tags':tags,
        'actress':actress,
        'image':imageAdress
    }
    return data

#download image for a movie
def downloadImage(data):
    url = data['image']
    try:
        response = requests.get(url)
        with open('folder.jpg', 'wb') as f:
            f.write(response.content)
    except:
        print("failed to save image")
    return 'folder.jpg'
    

manageStructure()