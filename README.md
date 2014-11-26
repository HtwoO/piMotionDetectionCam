piMotionDetectionCam
====================

A simple motion detection camera program running over the raspberry pi.

###Prerequisite
Install the following python packages on Raspbian first.

    sudo apt-get install python3-picamera python3-pil python3-pip

Install [qiniu](https://github.com/qiniu/python-sdk/) with the following command:

    pip3 install qiniu

Signup for a [QiNiu Cloud Storage（七牛云存储）](http://www.qiniu.com/) account. Fill in the appropriate field in the file credentials.py with your own QiNiu service information.
```
QINIU_ACCESS_KEY = ''
QINIU_SECRET_KEY = ''
QINIU_BUCKET_NAME = ''
```

###Run the program

    python3 piMotionDetectionCam.py
