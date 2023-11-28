from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QPixmap
import os


class Annotate:
    def __init__(self):
        pass


class imgSlider:
    def __init__(self, imgPath=None, imgList=None, pointer=0):
        self.imgList = imgList
        self.pointer = pointer
        self.imgPath = imgPath


def showImg(imgPath, imgWidget):
    pixmap = QPixmap(imgPath)
    imgWidget.setScaledContents(True)
    imgWidget.setPixmap(pixmap)


def getNextImg(imgWidget):
    try:
        if not iS.pointer >= len(iS.imgList) - 1 and iS.imgList is not None:
            iS.pointer += 1
            if iS.imgList[iS.pointer].endswith(".jpg") or iS.imgList[iS.pointer].endswith(".jpeg") or iS.imgList[iS.pointer].endswith(".png"):
                imgPath = os.path.join(iS.imgPath, iS.imgList[iS.pointer])
                showImg(imgPath, imgWidget)
            else:
                getNextImg(imgWidget)
    except NameError as e:
        print("You need to open a directory in order to use this button")


def getPrevImg(imgWidget):
    try:
        if not iS.pointer <= 0:
            iS.pointer -= 1
            if iS.imgList[iS.pointer].endswith(".jpg") or iS.imgList[iS.pointer].endswith(".jpeg") or iS.imgList[iS.pointer].endswith(".png"):
                imgPath = os.path.join(iS.imgPath, iS.imgList[iS.pointer])
                showImg(imgPath, imgWidget)
            else:
                getPrevImg(imgWidget)
    except NameError:
        print("You need to open a directory in order to use this button")


def getImageFile(imgWidget):
    imgPath = QFileDialog.getOpenFileName(filter="Image files (*.jpg, *.jpeg, *.png)")
    if imgPath:
        showImg(imgPath[0], imgWidget)


def getImageFolder(imgWidget):
    global iS
    imgDir = QFileDialog.getExistingDirectory()
    if imgDir:
        imgList = os.listdir(imgDir)
        iS = imgSlider(imgDir, imgList)
        cur = 0
        while True:
            if imgList[cur].endswith(".png") or imgList[cur].endswith(".png") or imgList[cur].endswith(".png"):
                showImg(os.path.join(imgDir, imgList[cur]), imgWidget)
                break
            else:
                cur += 1


def drawBB():
    pass
