#!/usr/bin/env python
#coding: utf-8

import sys
import io, picamera
from time import sleep
from datetime import datetime
from PIL import Image

def captureTestImage(res=(128, 96)):
    stream = io.BytesIO()
    with picamera.PiCamera() as camera:
        camera.resolution = res
        camera.capture(stream, format='jpeg')
        stream.seek(0)
        img = Image.open(stream)
        # stream.close()
        return img


def captureHiResImage(p, res=(800, 600)):
    with picamera.PiCamera() as camera:
        camera.resolution = res
        camera.capture(p)


def motionDetected(lastImg, curImg):
    brightnessThreshold = 10
    motionThreshold = 30

    numMotionPixel = 0
    width, height = curImg.size
    for x in range(width):
        for y in range(height):
            r0, g0, b0 = lastImg.getpixel((x,y))
            r1, g1, b1 = curImg.getpixel((x,y))
            if numMotionPixel > motionThreshold:
                return True
            # for more accurate result, all color channel should be considered.
            if abs(g0-g1) > brightnessThreshold:
                numMotionPixel += 1
    return False


if __name__ == '__main__':
    lowRes = (80, 60)
    hiRes = (1024, 768)
    srcDir = '/home/pi/pi_camera/MotionImages/'
    # dstDir = '/path/to/dst/dir/'

    image0 = captureTestImage(lowRes)
    while True:
        image1 = captureTestImage(res=lowRes)
        if motionDetected(image0, image1):
            time = datetime.now()
            timeStamp = '%4d%02d%02d-%02d%02d%02d' % (time.year, time.month,
                    time.day, time.hour, time.minute, time.second)
            fileName = 'MotionImage_' + timeStamp + '.jpg'
            filePath = srcDir + fileName
            captureHiResImage(p=filePath, res=hiRes)
            print('Motion Detected.\n')
            # backupToSomewhere(srcFilePath, dstDir)
            image0 = image1
            sleep(3)

    sys.exit()
