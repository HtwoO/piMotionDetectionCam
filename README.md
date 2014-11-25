piMotionDetectionCam
====================

A simple motion detection camera program running over the raspberry pi.

###Prerequisite
Install the following python packages on Raspbian first.

    sudo apt-get install python3-picamera python3-pil

Install [qiniu](https://github.com/qiniu/python-sdk/) with the following command:

    pip install qiniu

###Run the program

Signup a [QiNiu Cloud Storage（七牛存存储）](http://www.qiniu.com/) account. Fill in the appropriate field in the file credentials.py with your own QiNiu service information.
```
QINIU_ACCESS_KEY = ''
QINIU_SECRET_KEY = ''
QINIU_BUCKET_NAME = ''
```

    python3 piMotionDetectionCam.py
