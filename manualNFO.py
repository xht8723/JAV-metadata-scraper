import os
from datetime import date, datetime
import utilities as ut


def createNFO(dir, nfo_name, data, image):
    name, _ = os.path.splitext(nfo_name)
    name = dir + '\\' + name
    with open(name + '.nfo', 'w+', encoding = 'utf-8') as f:
        f.write('<?xml version="1.0" encoding="utf-8" standalone="yes"?>\n')
        f.write('<movie>\n')
        f.write('\t<dateadded>' + str(datetime.now()) + '</dateadded>\n')
        f.write('\t<title>' + data['title'] + '</title>\n')
        f.write('\t<year>' + data['release date'].split('-')[0] + '</year>\n')
        f.write('\t<mpaa>XXX</mpaa>\n')
        f.write('\t<tmdbid>' + data['banngo'] + '</tmdbid>\n')
        f.write('\t<premiered>' + data['release date'] + '</premiered>\n')
        f.write('\t<releasedate>' + data['release date'] + '</releasedate>\n')
        temp = data['tags'].split(',')
        for eachtag in temp:
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

def manualNFO(dir):
    nfo_name = str(input("Enter the name for nfo:"))
    title = str(input('Enter title:'))
    release_data = str(input('Enter the release date(YYYY-MM-DD):'))
    banngo = str(input('Enter the label number:'))
    label = str(input('Enter the company:'))
    actress = str(input('Enter the actress:'))
    studio = str(input('Enter Studio:'))
    imageAdress = str(input('Enter image url:'))
    tagsNum = int(input('how many tags?:'))
    tags = []
    for i in range(tagsNum):
        tags.append(str(input('tag:')))
    image = str(dir) + '\\folder.jpg'

    data = {
        'title':title,
        'release date':release_data,
        'banngo':banngo,
        'label':label,
        'actress':actress,
        'studio':studio,
        'image':imageAdress,
        'tags':tags
    }

    createNFO(nfo_name,data,image)
import os
from datetime import date, datetime
import utilities as ut


def createNFO(dir, nfo_name, data, image):
    name, _ = os.path.splitext(nfo_name)
    name = dir + '\\' + name
    with open(name + '.nfo', 'w+', encoding = 'utf-8') as f:
        f.write('<?xml version="1.0" encoding="utf-8" standalone="yes"?>\n')
        f.write('<movie>\n')
        f.write('\t<dateadded>' + str(datetime.now()) + '</dateadded>\n')
        f.write('\t<title>' + data['title'] + '</title>\n')
        f.write('\t<year>' + data['release date'].split('-')[0] + '</year>\n')
        f.write('\t<mpaa>XXX</mpaa>\n')
        f.write('\t<tmdbid>' + data['banngo'] + '</tmdbid>\n')
        f.write('\t<premiered>' + data['release date'] + '</premiered>\n')
        f.write('\t<releasedate>' + data['release date'] + '</releasedate>\n')
        temp = data['tags'].split(',')
        for eachtag in temp:
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

def manualNFO(dir):
    nfo_name = str(input("Enter the name for nfo:"))
    title = str(input('Enter title:'))
    release_data = str(input('Enter the release date(YYYY-MM-DD):'))
    banngo = str(input('Enter the label number:'))
    label = str(input('Enter the company:'))
    actress = str(input('Enter the actress:'))
    studio = str(input('Enter Studio:'))
    imageAdress = str(input('Enter image url:'))
    tagsNum = int(input('how many tags?:'))
    tags = []
    for i in range(tagsNum):
        tags.append(str(input('tag:')))
    image = str(dir) + '\\folder.jpg'

    data = {
        'title':title,
        'release date':release_data,
        'banngo':banngo,
        'label':label,
        'actress':actress,
        'studio':studio,
        'image':imageAdress,
        'tags':tags
    }

    createNFO(nfo_name,data,image)
