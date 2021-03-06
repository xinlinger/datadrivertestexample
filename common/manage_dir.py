
import time
import os

def getScreenShotDir():
    # return './screenshots/'
    current_file_dir = os.path.dirname(os.path.abspath(__file__))
    rootdir = os.path.split(current_file_dir)[0]
    newdir= os.path.join(rootdir,"screenshots")
    if os.path.exists(newdir):
        print('ok')
    else:
        os.mkdir(newdir)
    return newdir

def getPngfileName():
    screenshotsDir = getScreenShotDir()
    current_time = time.time()

    #作业：用时间命名文件 （to do filename） 2018_05_27_15_30_30.png
    filename = os.path.join(screenshotsDir,str(current_time)+'.png')
    return filename