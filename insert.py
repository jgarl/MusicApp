import os
import main
import mp3handler
from pytube import YouTube
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 


class InsertWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("MusicApp")
        self.setWindowIcon(QIcon('icon.ico'))
        
        self.setFixedSize(700, 650)
        screen = QDesktopWidget().screenGeometry()
        x = int(screen.width()/2 - 700/2)
        y = int(screen.height()/2 - 650/2)
        self.move(x,y)
        
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setAlignment(Qt.AlignTop)

        #first title label
        title1 = QLabel("Download Music")
        title1.setFont(QFont('Times',18))
        title1.setAlignment(Qt.AlignCenter)
        margin = title1.contentsMargins()
        margin.setBottom(0)
        title1.setContentsMargins(margin)
        layout.addWidget(title1)
        
        #first layout frame
        self.firstDownloadFrame = QFrame()
        self.firstDownloadFrame.setFrameStyle(QFrame.Box)

        #first layout
        self.firstDownloadLayout = QVBoxLayout()
        self.firstDownloadLayout.setSpacing(15)

        #form layout
        self.downloadFormLayout = QFormLayout()
        self.label1 = QLabel("Youtube Url:")
        self.url = QLineEdit()
        self.downloadFormLayout.addRow(self.label1,self.url)
        self.downloadFormLayout.setAlignment(Qt.AlignTop)
        self.firstDownloadLayout.addLayout(self.downloadFormLayout)

        #progress bar
        self.progress = QProgressBar()
        self.progress.setGeometry(0, 0, 300, 25)
        self.progress.setMaximum(100)
        self.progress.hide()
        self.firstDownloadLayout.addWidget(self.progress)

        #download button
        self.downloadBtn = QPushButton("Download")
        self.downloadBtn.setFixedSize(170,30)
        self.downloadBtn.clicked.connect(download)
        self.firstDownloadLayout.addWidget(self.downloadBtn, alignment=Qt.AlignCenter)

        self.firstDownloadFrame.setLayout(self.firstDownloadLayout)
        self.topDownloadLayout = QVBoxLayout()
        self.topDownloadLayout.addWidget(self.firstDownloadFrame)
        
        layout.addLayout(self.topDownloadLayout)

        #second title label
        title2 = QLabel("Insert Music")
        title2.setFont(QFont('Times',18))
        title2.setAlignment(Qt.AlignCenter)
        margin = title2.contentsMargins()
        margin.setBottom(0)
        margin.setTop(30)
        title2.setContentsMargins(margin)
        layout.addWidget(title2)

        #second layout frame
        self.secondDownloadFrame = QFrame()
        self.secondDownloadFrame.setFrameStyle(QFrame.Box)

        #second layout
        self.secondDownloadLayout = QVBoxLayout()
        self.secondDownloadLayout.setSpacing(15)
        self.secondDownloadLayout
        
        #second form layout
        self.horFileLayout = QHBoxLayout()
        self.fileFormLayout = QFormLayout()
        self.label2 = QLabel("Selected File:")
        self.filePath = QLineEdit()
        self.filePath.setReadOnly(True)
        self.fileFormLayout.addRow(self.label2,self.filePath)
        self.fileFormLayout.setAlignment(Qt.AlignTop)
        self.horFileLayout.addLayout(self.fileFormLayout)

        #file bottom search
        self.fileBtn = QPushButton("Open")
        self.fileBtn.clicked.connect(self.openFile)
        self.horFileLayout.addWidget(self.fileBtn)
        self.secondDownloadLayout.addLayout(self.horFileLayout)

        #third title label
        f = QFont('Times',13)
        f.setUnderline(True)
        title3 = QLabel("Edit Properties:")
        title3.setFont(f)
        title3.setFixedSize(150, 30)
        title3.setAlignment(Qt.AlignCenter)
        margin = title3.contentsMargins()
        margin.setLeft(30)
        title3.setContentsMargins(margin)
        self.secondDownloadLayout.addWidget(title3)

        #third form layout
        self.filePropFormLayout = QFormLayout()
        self.filePropFormLayout.setFormAlignment(Qt.AlignCenter)
        self.labelN = QLabel("Name:")
        self.fileName = QLineEdit()
        self.fileName.setFixedSize(175, 30)
        self.labelAr = QLabel("Artist(s):")
        self.fileArtist = QLineEdit()
        self.fileArtist.setFixedSize(175, 30)
        self.labelAl = QLabel("Album:")
        self.fileAlbum = QLineEdit()
        self.fileAlbum.setFixedSize(175, 30)
        self.filePropFormLayout.addRow(self.labelN,self.fileName)
        self.filePropFormLayout.addRow(self.labelAr,self.fileArtist)
        self.filePropFormLayout.addRow(self.labelAl,self.fileAlbum)
        self.secondDownloadLayout.addLayout(self.filePropFormLayout)
        
        #fourth layout
        self.bottomLayout = QHBoxLayout()
        #update file buttom
        self.updateFileBtn = QPushButton("Update Properties")
        self.updateFileBtn.clicked.connect(self.updateFile)
        self.bottomLayout.addWidget(self.updateFileBtn)

        #insert file buttom
        self.insertFileBtn = QPushButton("Insert to DB")
        self.insertFileBtn.clicked.connect(self.insertFile)
        self.bottomLayout.addWidget(self.insertFileBtn)

        self.secondDownloadLayout.addLayout(self.bottomLayout)

        self.secondDownloadFrame.setLayout(self.secondDownloadLayout)
        self.bottomDownloadLayout = QVBoxLayout()
        self.bottomDownloadLayout.addWidget(self.secondDownloadFrame)

        layout.addLayout(self.bottomDownloadLayout)

        #back and question button
        bottomBtnsLayout = QHBoxLayout()
        backBtn = QPushButton("Back")
        backBtn.setFixedSize(100,30)
        backBtn.clicked.connect(self.switch_m)
        bottomBtnsLayout.addWidget(backBtn, alignment=Qt.AlignLeft)
        questionBtn = QPushButton("?")
        questionBtn.setFixedSize(30,30)
        questionBtn.clicked.connect(self.onQuestionClicked)
        bottomBtnsLayout.addWidget(questionBtn, alignment=Qt.AlignRight)
        layout.addLayout(bottomBtnsLayout, 1)
        
        #principal layout and frame
        self.topFrame = QFrame()
        self.topFrame.setFrameStyle(QFrame.Box)
        self.topFrame.setLineWidth(3)
        self.topFrame.setLayout(layout)
        caca = QVBoxLayout()
        caca.addWidget(self.topFrame)
        self.setLayout(caca)

    def setDB(self, db):
        self.db = db

    def getUrl(self):
        return self.url.text()

    def setProgressBar(self, v):
        self.progress.show()
        self.progress.setValue(v)
        self.progress.update()

    def setDownBtn(self, str):
        self.downloadBtn.setText(str)
        self.downloadBtn.update()

    def openFile(self):
        if os.path.exists("./Downloads"):
            path = "./Downloads"
        else:
            path = "."
        fname = QFileDialog.getOpenFileName(self, 'Open file', path,"MP3 files (*.mp3)")
        if fname[0] != '':
            self.currentFile(fname[0])

    def openDialog(self, message):
        dlg = QMessageBox(self)
        dlg.setText(message)
        dlg.exec()

    def updateFile(self):
        if self.filePath.text() == '':
            self.openDialog("No file selected")
        else:
            try:
                mp3handler.setTags(self.file, self.fileName.text(), self.fileArtist.text(), self.fileAlbum.text())
                new_path = os.path.split(self.file)[0] + '/' + self.fileName.text() + '.mp3'
                os.rename(self.file,new_path)
                self.currentFile(new_path)
            except:
                self.openDialog("Error while updating file properties")
        
    def insertFile(self):
        if self.filePath.text() == '':
            self.openDialog("No file selected")
        else:
            try:
                tags = mp3handler.getTags(self.file)
                error = self.db.insert(tags[0],tags[1],tags[2])
                if error:
                    self.openDialog("File inserted successfully")
                else:
                    self.openDialog("Error while inserting file to database")
            except:
                self.openDialog("Error while inserting file to database")
        


    def currentFile(self, f):
        self.file = f
        self.filePath.setText(f)
        try:
            tags = mp3handler.getTags(f)
            if len(tags) == 0:
                self.openDialog("Error while opening file")
            else:
                self.fileName.setText(tags[0])
                self.fileArtist.setText(tags[1])
                self.fileAlbum.setText(tags[2])
        except Exception as e:
            self.openDialog("Error while opening file")

    def onQuestionClicked(self):
        message = "For more than one artist,\nwrite Name1;Name2;..."
        self.openDialog(message)

    def switch_m(self):
        self.cams = main.MainWindow()
        self.cams.show()
        self.close()

    def closeEvent(self, event):
        self.cams = main.MainWindow()
        self.cams.show()
        self.close()
        
        event.accept()

def progress_function(stream, chunk, bytes_remaining):
        iw.setProgressBar((float(file_size-bytes_remaining)/float(file_size))*float(50))

def download():
    iw.setProgressBar(0)
    iw.setDownBtn("Accessing the URL...")
    video_link = iw.getUrl()
    try:
        #configure de mp4 download        
        yt = YouTube(video_link, on_progress_callback=progress_function)
        video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        global file_size
        file_size = video.filesize

        iw.setDownBtn("Converting to mp3...")
        if os.path.exists("./Downloads"):
            path = "Downloads"
        else:
            path = ""
        out_file = video.download(path, yt.title)

        #convert to mp3 and delete mp4
        path = mp3handler.toMp3(out_file)
        mp3handler.setTags(path,yt.title,yt.author,'')

        iw.setProgressBar(100)
        iw.setDownBtn("Download")
        message = "File in " + path
        iw.currentFile(path)
        iw.openDialog(message)
    except:
        iw.setDownBtn("Download")
        iw.openDialog("Check Connection or URL")

def init(db):
    global iw
    iw = InsertWindow()
    iw.setDB(db)
    iw.show()

