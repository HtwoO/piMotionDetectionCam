piMotionDetectionCam
====================

A simple motion detection camera program running over the raspberry pi.

###Prerequisite
Install the following python packages on Raspbian first.

    sudo apt-get install python3-pil python3-picamera

Install [qiniu](https://github.com/qiniu/python-sdk/) with the following command:

    pip install qiniu

###Run the program

Register a [QiNiu](http://www.qiniu.com/) account, Fill in the appropriate infomation in the file credentials.py with your own QiNiu service info.

>QINIU_ACCESS_KEY = ''
>QINIU_SECRET_KEY = ''
>QINIU_BUCKET_NAME = ''

    python3 piMotionDetectionCam.py
