<<<<<<< HEAD
import sys
import os
import shutil
import requests
import re
from bs4 import BeautifulSoup
from datetime import date, datetime
import utilities as ut


#script_dir = os.path.dirname(os.path.abspath(__file__))


#manage the file structure for jellyfin. create nfo and download image
def manageStructure(headers, directory, progressbar):
    file_format = [
    '.mp4',
    '.MP4',
    '.mkv',
    '.rmvb',
    '.AVI',
    '.avi'
    ]
    # Get the list of files in the specified directory
    file_list = os.listdir(directory)
    pattern = re.compile('([a-zA-Z]+\d*?-\d+[a-zA-Z]?)')
    fileNum = len(file_list)
    step = 100/fileNum
    ut.setGauge(progressbar, 0)
    progressbar.configure(subtext = 'Processing..')
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
                sys.exit(1)
            data = findData_javguru(banngo, headers)

            #clean the name to avoid invlaid title name for folder
            folder_name = banngo + ' [' + data['studio'] + '] -' + data['title'] + ' (' + data['release date'].split('-')[0] + ')'
            invalid_chars_pattern = r'[<>:"/\\|?*]'
            if (len(folder_name) > 200):
                folder_name = banngo + ' [' + data['studio'] + '] -' + data['title'][:100] + ' (' + data['release date'].split('-')[0] + ')'
            folder_name = re.sub(invalid_chars_pattern, '-', folder_name)

            #Move the file into a folder with proper name
            try:
                folder_path = os.path.join(directory, folder_name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                full_path = directory + '/' + file
                shutil.move(full_path, folder_path)
            except AttributeError as e:
                #do nothing
                pass

            #download image
            image = downloadImage(data)
            shutil.move(image, folder_path)

            #create nfo file
            nfo_name = filename + ".nfo"
            createNFO(nfo_name, data, folder_path + '\\' + image)
            shutil.move(nfo_name, folder_path)
        ut.updateGauge(progressbar, step)
    ut.setGauge(progressbar, 100)
    progressbar.configure(subtext = 'Complete!')    
    

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
        f.write('\t<art>\n')
        f.write('\t\t<poster>' + image + '</poster>\n')
        f.write('\t\t<fanart>' + image + '</fanart>\n')
        f.write('\t</art>\n')
        for eachAct in data['actress']:
            f.write('\t<actor>\n')
            f.write('\t\t<name>' + eachAct + '</name>\n')
            f.write('\t\t<role>Actress</role>\n')
            f.write('\t\t<type>Actor</type>\n')
            f.write('\t</actor>\n')
        f.write('\t<set>' + data["studio"] + '</set>\n')
        f.write('\t<thumb>' + data['image'] + '</thumb>\n')
        f.write('</movie>')


#Function to extract metadata from javguru
def findData_javguru(banngo, headers):
    javguru_search_url = "https://jav.guru/?s="
    #compile regex to match from url
    if 'MIUM' in banngo:
        banngo = '300' + banngo
    regex = re.compile(r'<a title="\[' + re.escape(banngo) + r'\] .*"')
    try:
        search = requests.get(javguru_search_url + banngo, headers = headers)
        result = regex.search(search.text)
        result = result.group() + ''
    except:
        try:
            secondTry = re.compile(r'<a title="\[.*?\] .*"')
            search = requests.get(javguru_search_url + banngo, headers = headers)
            result = secondTry.search(search.text).group()
        except:
            sys.exit(1)

    #extract title and url from previous match
    regex = re.compile(r'<a title="(?P<title>.*?)" href="(?P<href>.*?)"')
    try:
        match = regex.search(result)
        title = match.group('title')
        invalidBracket = '\[.*\]'
        title = re.sub(invalidBracket, '', title)
        target_url = match.group('href')
    except:
        try:
            secondTry = re.compile(r'<a title="(.*?)"')
            match = secondTry.findall(result)
            title = match[0]
            invalidBracket = '\[.*\]'
            title = re.sub(invalidBracket, '', title)
            secondTry = re.compile(r'href="(.*?)"')
            target_url = match[0]
        except Exception as e:
            sys.exit(1)

    #open target url to extract metadata
    search = requests.get(target_url, headers = headers)
    soup = BeautifulSoup(search.text, 'html.parser')
    try:
        targetinfo = soup.find('div', class_ = 'infoleft')
        targetinfo = str(targetinfo)
    except:
        sys.exit(1)

    #extract metadata
    try:
        release_date = re.search(r'Release Date: </strong>(\d{4}-\d{2}-\d{2})', targetinfo).group(1)
    except:
        release_date = str(date.today())
    try:
        director = re.search(r'Director: </strong> <a href=".*" rel="tag">(.*)</a>', targetinfo).group(1)
    except:
        director = 'unknown'
    try:
        studio = re.search(r'Studio: </strong> <a href=".*" rel="tag">(.*)</a>', targetinfo).group(1)
    except:
        studio = 'unknown'
    try:
        label = re.search(r'Label: </strong> <a href=".*" rel="tag">(.*)</a>', targetinfo).group(1)
    except:
        label = 'unknown'
    try:
        tags = re.findall(r'Tags: </strong>(.*)</li>', targetinfo)[0]
        regex = re.compile('([A-Za-z]*)<\/a>')
        tags = regex.findall(tags)
    except:
        tags = ''
    try:
        soupActress = BeautifulSoup(targetinfo, 'html.parser')
        actress = []
        actress_list = soupActress.findAll('li', class_='w1')
        actressRegex = re.compile(r'([a-zA-Z]+ [a-zA-Z]+)<\/a>')
        actress = actressRegex.findall(str(actress_list[3]))
        #actress = re.search(r'Actress: </strong> <a href=".*" rel="tag">(.*)</a>', targetinfo).group(1)
    except Exception as e:
        actress = 'unknown'

    #find image adress
    try:
        imageAdress = soup.find('div', class_ = 'large-screenimg')
        imageAdress = str(imageAdress)
        soupImage = BeautifulSoup(imageAdress, 'html.parser')
        imageAdress = soupImage.find('img')['src']
    except:
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
        pass
=======
import sys
import os
import shutil
import requests
import re
from bs4 import BeautifulSoup
from datetime import date, datetime
import utilities as ut


#script_dir = os.path.dirname(os.path.abspath(__file__))


#manage the file structure for jellyfin. create nfo and download image
def manageStructure(headers, directory, progressbar):
    file_format = [
    '.mp4',
    '.MP4',
    '.mkv',
    '.rmvb',
    '.AVI',
    '.avi'
    ]
    # Get the list of files in the specified directory
    file_list = os.listdir(directory)
    pattern = re.compile('([a-zA-Z]+\d*?-\d+[a-zA-Z]?)')
    fileNum = len(file_list)
    print('Pending processing:', fileNum)
    step = 100/fileNum
    ut.setGauge(progressbar, 0)
    progressbar.configure(subtext = 'Processing..')
    processed_files = []
    #looping
    for file in file_list:
        #optimize file name and prepare for more process
        filename, format = os.path.splitext(file)
        if format in file_format:
            print('Processing:', filename)
            match = pattern.findall(filename)
            if match:
                banngo = match[0].upper()
                try:
                    data = findData_javguru(banngo, headers)
                except Exception as e:
                    print(f'Search for {banngo} failed, pls check the file name.' )
                    continue
                processed_files.append(banngo)
            else:
                print('Process failed for', filename)
                continue


            #clean the name to avoid invlaid title name for folder
            folder_name = banngo + ' [' + data['studio'] + '] -' + data['title'] + ' (' + data['release date'].split('-')[0] + ')'
            invalid_chars_pattern = r'[<>:"/\\|?*]'
            if (len(folder_name) > 200):
                folder_name = banngo + ' [' + data['studio'] + '] -' + data['title'][:100] + ' (' + data['release date'].split('-')[0] + ')'
            folder_name = re.sub(invalid_chars_pattern, '-', folder_name)

            #Move the file into a folder with proper name
            try:
                folder_path = os.path.join(directory, folder_name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                full_path = directory + '/' + file
                shutil.move(full_path, folder_path)
            except AttributeError as e:
                print('make dir failed')
                #do nothing
                pass

            #download image
            image = downloadImage(data)
            try:
                shutil.move(image, folder_path)
            except shutil.Error:
                print('Duplicate AV:', data['banngo'])
                pass

            #create nfo file
            nfo_name = filename + ".nfo"
            createNFO(nfo_name, data, folder_path + '\\' + image)
            shutil.move(nfo_name, folder_path)
        ut.updateGauge(progressbar, step)
    ut.setGauge(progressbar, 100)
    progressbar.configure(subtext = 'Complete!')    
    

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
        f.write('\t<art>\n')
        f.write('\t\t<poster>' + image + '</poster>\n')
        f.write('\t\t<fanart>' + image + '</fanart>\n')
        f.write('\t</art>\n')
        for eachAct in data['actress']:
            f.write('\t<actor>\n')
            f.write('\t\t<name>' + eachAct + '</name>\n')
            f.write('\t\t<role>Actress</role>\n')
            f.write('\t\t<type>Actor</type>\n')
            f.write('\t</actor>\n')
        f.write('\t<set>' + data["studio"] + '</set>\n')
        f.write('\t<thumb>' + data['image'] + '</thumb>\n')
        f.write('</movie>')


#Function to extract metadata from javguru
def findData_javguru(banngo, headers):
    javguru_search_url = "https://jav.guru/?s="
    #compile regex to match from url
    if 'MIUM' in banngo:
        banngo = '300' + banngo
    regex = re.compile(r'<a title="\[' + re.escape(banngo) + r'\] .*"')
    try:
        search = requests.get(javguru_search_url + banngo, headers = headers)
        result = regex.search(search.text)
        result = result.group() + ''
    except Exception as e:
        print('Second try:', banngo)
        try:
            secondTry = re.compile(r'<a title="\[.*?\] .*"')
            search = requests.get(javguru_search_url + banngo, headers = headers)
            result = secondTry.search(search.text).group()
        except Exception as e:
            print('Coundn\'t find url for', banngo)
            raise(e)

    #extract title and url from previous match
    regex = re.compile(r'<a title="(?P<title>.*?)" href="(?P<href>.*?)"')
    try:
        match = regex.search(result)
        title = match.group('title')
        invalidBracket = '\[.*\]'
        title = re.sub(invalidBracket, '', title)
        target_url = match.group('href')
    except Exception as e:
        try:
            secondTry = re.compile(r'<a title="(.*?)"')
            match = secondTry.findall(result)
            title = match[0]
            invalidBracket = '\[.*\]'
            title = re.sub(invalidBracket, '', title)
            secondTry = re.compile(r'href="(.*?)"')
            target_url = match[0]
        except Exception as e:
            print('Coundn\'t find reg match')
            raise(e)

    #open target url to extract metadata
    search = requests.get(target_url, headers = headers)
    soup = BeautifulSoup(search.text, 'html.parser')
    try:
        targetinfo = soup.find('div', class_ = 'infoleft')
        targetinfo = str(targetinfo)
    except Exception as e:
        print('Coundn\'t open page')
        raise(e)

    #extract metadata
    try:
        release_date = re.search(r'Release Date: </strong>(\d{4}-\d{2}-\d{2})', targetinfo).group(1)
    except Exception as e:
        release_date = str(date.today())
    try:
        director = re.search(r'Director: </strong> <a href=".*" rel="tag">(.*)</a>', targetinfo).group(1)
    except Exception as e:
        director = 'unknown'
    try:
        studio = re.search(r'Studio: </strong> <a href=".*" rel="tag">(.*)</a>', targetinfo).group(1)
    except Exception as e:
        studio = 'unknown'
    try:
        label = re.search(r'Label: </strong> <a href=".*" rel="tag">(.*)</a>', targetinfo).group(1)
    except Exception as e:
        label = 'unknown'
    try:
        tags = re.findall(r'Tags: </strong>(.*)</li>', targetinfo)[0]
        regex = re.compile('([A-Za-z]*)<\/a>')
        tags = regex.findall(tags)
    except Exception as e:
        tags = ''
    try:
        soupActress = BeautifulSoup(targetinfo, 'html.parser')
        actress = []
        actress_list = soupActress.findAll('li', class_='w1')
        actressRegex = re.compile(r'([a-zA-Z]+ [a-zA-Z]+)<\/a>')
        actress = actressRegex.findall(str(actress_list[3]))
        #actress = re.search(r'Actress: </strong> <a href=".*" rel="tag">(.*)</a>', targetinfo).group(1)
    except Exception as e:
        actress = 'unknown'

    #find image adress
    try:
        imageAdress = soup.find('div', class_ = 'large-screenimg')
        imageAdress = str(imageAdress)
        soupImage = BeautifulSoup(imageAdress, 'html.parser')
        imageAdress = soupImage.find('img')['src']
    except Exception as e:
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
    except Exception as e:
        print('failed to download img for', data['banngo'])
        pass
>>>>>>> bug
    return 'folder.jpg'