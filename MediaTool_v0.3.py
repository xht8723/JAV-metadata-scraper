import ttkbootstrap as tb
import threading

import rename
import utilities as ut
import hardlink
import removeXMLtag
import manualNFO
import scrapper

def on_close():
    ut.saveJson('ga', cookieGa.get())
    ut.saveJson('ga83', cookieGa83.get())
    ut.saveJson('sessid', cookieSESSID.get())
    ut.saveJson('AV dir', fileLB.cget('text'))
    root.destroy()
    return

def renameWindow():
    dir = ut.dirDialog()

    newWin = tb.Toplevel()
    newWin.geometry('512x800')
    newWin.minsize(512, 800)
    newWin.title('Rename')

    frame = tb.Frame(newWin)
    frame.pack(pady= 50)

    filenameLabel = tb.Label(frame, text=dir, bootstyle='info, inverse')
    dirSelect = tb.Button(frame, bootstyle='primary, outline',text='Select Directory' ,command=lambda: ut.dirDialog(dir, filenameLabel))
    dirSelect.pack()
    filenameLabel.pack(pady=10)
   
    targetStringLable = tb.Label(newWin, text='String to Replace:', bootstyle = 'primary')
    targetStringLable.pack()
    targetString = tb.Entry(newWin, bootstyle = 'primary')
    targetString.pack(pady=10)

    replaceToLable = tb.Label(newWin, text='Replace to:', bootstyle = 'primary')
    replaceToLable.pack()
    replaceTo = tb.Entry(newWin, bootstyle = 'primary')
    replaceTo.pack(pady=10)
    
    logs = tb.ScrolledText(newWin, height = 10)
    logs.configure(state='disabled')

    btn = tb.Button(newWin, bootstyle = 'primary', text='Rename',command=lambda:rename.rename_files(filenameLabel.cget('text'), targetString.get(), replaceTo.get(), logs))
    btn.pack(pady=50)
    logs.pack(pady=20)

    return

def mkHardlink():
    newWin = tb.Toplevel()
    newWin.geometry('512x700')
    newWin.minsize(512, 700)
    newWin.title('Hard link')
    frame = tb.Frame(newWin)
    frame.pack(pady= 20)
    frame2 = tb.Frame(newWin)
    frame2.pack(pady= 20)

    target_directory = tb.Label(frame, text='Select target directory:', bootstyle='info, inverse')
    link_directory = tb.Label(frame2, text='Select link directory:', bootstyle='info, inverse')
    targetDirSelect = tb.Button(frame, bootstyle='primary, outline',text='Select Directory' , command=lambda: ut.dirDialog('', target_directory))
    linkDirSelect = tb.Button(frame2, bootstyle='primary, outline',text='Select Directory', command=lambda: ut.dirDialog('', link_directory))
    targetDirSelect.pack(pady=10)
    target_directory.pack(pady=10)
    linkDirSelect.pack(pady=10)
    link_directory.pack(pady=10)


    logs = tb.ScrolledText(newWin, height = 10)
    logs.configure(state='disabled')

    hardlink_run = tb.Button(newWin, bootstyle='primary', text='Create Hard Links', command=lambda: hardlink.make_hl(target_directory.cget('text'), link_directory.cget('text'), logs))
    hardlink_run.pack(pady=50)
    logs.pack(pady=20)

    return

def removeXML():
    newWin = tb.Toplevel()
    newWin.geometry('512x650')
    newWin.minsize(512, 650)
    newWin.title('Remove XML tags')
    frame = tb.Frame(newWin)
    frame.pack(pady= 50)

    logs = tb.ScrolledText(newWin, height = 10)
    logs.configure(state='disabled')
    target_directory = tb.Label(frame, text='Select target directory:', bootstyle='info, inverse')
    targetDirSelect = tb.Button(frame, bootstyle='primary, outline',text='Select Directory' , command=lambda: ut.dirDialog('', target_directory))
    run = tb.Button(newWin, bootstyle='primary', text = 'Remove all XML tags for all nfo', command=lambda: removeXMLtag.removeXMLtag(target_directory.cget('text'), logs))

    targetDirSelect.pack(pady=10)
    target_directory.pack(pady=10)
    run.pack(pady=50)
    logs.pack(pady=50)

    return

def compressData(title, release_data, banngo, label, actress, studio, imageAdress, tags):
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
    return data

def manualNFOF():
    newWin = tb.Toplevel()
    newWin.minsize(500, 1500)
    newWin.geometry('500x1500')
    newWin.title('Manual Create .NFO')
    frame = tb.Frame(newWin)
    frame.pack(pady=50)
    frame2 = tb.Frame(newWin)
    frame2.pack(pady=50)

    target_directory = tb.Label(frame, text='Select target directory:', bootstyle='info, inverse')
    targetDirSelect = tb.Button(frame, bootstyle='primary, outline',text='Select Directory' , command=lambda: ut.dirDialog('', target_directory))
    targetDirSelect.pack(pady=10)
    target_directory.pack(pady=10)

    nfo_nameLB = tb.Label(frame2, bootstyle = 'primary', text= 'Enter the name for nfo:')
    titleLB = tb.Label(frame2, bootstyle = 'primary', text= 'Enter title:')
    release_dataLB = tb.Label(frame2, bootstyle = 'primary', text= 'Enter the release date(YYYY-MM-DD):')
    banngoLB = tb.Label(frame2, bootstyle = 'primary', text= 'Enter the label number:')
    labelLB = tb.Label(frame2, bootstyle = 'primary', text= 'Enter the company:')
    actressLB = tb.Label(frame2, bootstyle = 'primary', text= 'Enter actress:')
    studioLB = tb.Label(frame2, bootstyle = 'primary', text= 'Enter studio:')
    imageAdressLB = tb.Label(frame2, bootstyle = 'primary', text= 'Enter image url:')
    tagsLB = tb.Label(frame2, bootstyle = 'primary', text= 'Enter tags(separate by ,) :')

    nfo_name = tb.Entry(frame2, bootstyle = 'primary')
    title = tb.Entry(frame2, bootstyle = 'primary')
    release_data = tb.Entry(frame2, bootstyle = 'primary')
    banngo = tb.Entry(frame2, bootstyle = 'primary')
    label = tb.Entry(frame2, bootstyle = 'primary')
    actress = tb.Entry(frame2, bootstyle = 'primary')
    studio = tb.Entry(frame2, bootstyle = 'primary')
    imageAdress = tb.Entry(frame2, bootstyle = 'primary')
    tags = tb.Entry(frame2, bootstyle = 'primary')

    nfo_nameLB.pack(pady=10)
    nfo_name.pack(pady=10)
    titleLB.pack(pady=10)
    title.pack(pady=10)
    release_dataLB.pack(pady=10)
    release_data.pack(pady=10)
    banngoLB.pack(pady=10)
    banngo.pack(pady=10)
    labelLB.pack(pady=10)
    label.pack(pady=10)
    actressLB.pack(pady=10)
    actress.pack(pady=10)
    studioLB.pack(pady=10)
    studio.pack(pady=10)
    imageAdressLB.pack(pady=10)
    imageAdress.pack(pady=10)
    tagsLB.pack(pady=10)
    tags.pack(pady=10)

    done = tb.Label(newWin, bootstyle = 'primary, inverse', text='Done!')
    run = tb.Button(newWin, bootstyle = 'primary', text='Create nfo', 
                    command= lambda: [manualNFO.createNFO(target_directory.cget('text'), nfo_name.get(), 
                    compressData(title.get(), release_data.get(), banngo.get(), label.get(), actress.get(), studio.get(), imageAdress.get(),tags.get()), 
                    imageAdress.get())] [ut.updateDone(done)])
    run.pack()
    return

def JavScrapper():
    ga = cookieGa.get()
    ga83 = cookieGa83.get()
    sessid = cookieSESSID.get()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Cookie': f'_ga={ga}; PHPSESSID={ga83}; _ga_83WTHH81CR={sessid}'
    }

    scrapper.manageStructure(headers, fileLB.cget('text'), progressMeter)
    return

def JavScrapperWrapper():
    thread = threading.Thread(target=JavScrapper)
    thread.start()

root = tb.Window(themename="yakoto")
root.protocol('WM_DELETE_WINDOW', on_close)

root.title("Media Tool pack")
#root.iconbitmap("")
root.geometry('1024x1024')
root.minsize(1024, 1024)

progressMeter = tb.Meter(root, bootstyle='primary', padding = 50, amounttotal=100, amountused=0, subtext='Fill the settings below', textright='%', metertype='semi', subtextstyle='primary')
progressMeter.pack(pady= 20)

fileFrame = tb.Frame(root)
fileFrame.pack(pady=20)

cookieFrame = tb.Frame(root)
cookieFrame.pack()
cookieGAFrame = tb.Frame(cookieFrame)
cookieGAFrame.pack(pady=20, side='left')
cookieGA83Frame = tb.Frame(cookieFrame)
cookieGA83Frame.pack(pady=20, side='left')
cookieSESSIDFrame = tb.Frame(cookieFrame)
cookieSESSIDFrame.pack(pady=20, side='left')

fileLB = tb.Label(fileFrame, text = 'Select Directory:', bootstyle = 'info, inverse')
temp = ut.readJson('AV dir')[0]
if temp != '':
    fileLB.config(text=temp)
fileSL = tb.Button(fileFrame, bootstyle='primary, outline', text='Select Directory', command=lambda:ut.dirDialog('', fileLB))
fileSL.pack()
fileLB.pack(pady=10)

cookieGaLB = tb.Label(cookieGAFrame, text='Cookie GA value:', bootstyle = 'primary')
cookieGa = tb.Entry(cookieGAFrame, bootstyle = 'primary')
cookieGa.insert(0, ut.readJson('ga')[0])
cookieGaLB.pack(padx=20)
cookieGa.pack(padx=20)

cookieGa83LB = tb.Label(cookieGA83Frame, text='Cookie GA83 value:', bootstyle = 'primary')
cookieGa83 = tb.Entry(cookieGA83Frame, bootstyle = 'primary')
cookieGa83.insert(0, ut.readJson('ga83')[0])
cookieGa83LB.pack(padx=20)
cookieGa83.pack(padx=20)

cookieSESSIDLB = tb.Label(cookieSESSIDFrame, text='Cookie PHPSESSID value:', bootstyle = 'primary')
cookieSESSID = tb.Entry(cookieSESSIDFrame, bootstyle = 'primary')
cookieSESSID.insert(0, ut.readJson('sessid')[0])
cookieSESSIDLB.pack(padx=20)
cookieSESSID.pack(padx=20)


scrapperButton = tb.Button(root, text='Javguru Scrapper', bootstyle = 'primary', command=lambda:JavScrapperWrapper())
scrapperButton.pack(pady=50, padx=50)

buttonFrame = tb.Frame(root)
buttonFrame.pack()

hardlinkButton = tb.Button(buttonFrame, text="Hardlink", bootstyle='info, outline', command=mkHardlink)
hardlinkButton.pack(pady=50, side='left', padx=50)

RnameButton = tb.Button(buttonFrame, text='Rename', bootstyle = 'info, outline', command=renameWindow)
RnameButton.pack(pady=50, side='left', padx=50)

removeXMLButton = tb.Button(buttonFrame, text='Remove XML', bootstyle = 'info, outline', command=removeXML)
removeXMLButton.pack(pady=50, side='left', padx=50)

manualNFOButton = tb.Button(buttonFrame, text='Manual create .nfo', bootstyle = 'info, outline', command=manualNFOF)
manualNFOButton.pack(pady=50, side='left', padx=50)



root.mainloop()