from xml.dom import INDEX_SIZE_ERR
from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product
from rest_framework.views import APIView
from .serializers import ProductSerializer
import os
from pickle import load
from django.urls import reverse

# ##camera
# import picamera
# import time
# import requests
# import smtplib
# import imageio
# from PIL import Image
# import shutil


#aws s3
import boto3
from botocore.client import Config
#aws iot

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time
import argparse
import json

# Connect and subscribe to AWS IoT
# myAWSIoTMQTTClient.connect()
# if args.mode == 'both' or args.mode == 'subscribe':
#     myAWSIoTMQTTClient.subscribe(topic, 1, customCallback)
# time.sleep(2)

loopCount = 0




@api_view(['GET'])
def test(request, email):
    
    # os.system('python3 aws-iot-device-sdk-python-v2/samples/pubsub.py --topic hyuk-pi/a --ca_file ~/certs/AmazonRootCA1.pem --cert ~/certs/fd18991a37a08f66597744d7e45ad95ace2e193d0d63bd5c09f5231192b481b1-certificate.pem.crt --key ~/certs/fd18991a37a08f66597744d7e45ad95ace2e193d0d63bd5c09f5231192b481b1-private.pem.key --endpoint a12ugbifljut5v-ats.iot.ap-northeast-2.amazonaws.com --message awd')
    return render(request,'a.html',{'email':email})


@api_view(['GET'])
def test3(request,email):
    
    os.system('python3 /aws-iot-device-sdk-python-v2/samples/pubsub.py --topic hyuk-pi/a --ca_file AmazonRootCA1.pem --cert fd18991a37a08f66597744d7e45ad95ace2e193d0d63bd5c09f5231192b481b1-certificate.pem.crt --key fd18991a37a08f66597744d7e45ad95ace2e193d0d63bd5c09f5231192b481b1-private.pem.key --endpoint a12ugbifljut5v-ats.iot.ap-northeast-2.amazonaws.com --message '+email)

    return redirect('../')





@api_view(['POST'])
def upload_file(request):
    def handle(f):
        for i in range(1,5):
            if not os.path.isfile('./'+str(i)+'.jpg'):
                break
        destination=open('./'+str(i)+'.jpg','wb+')
        for chunk in f.chunks():
            destination.write(chunk)
        destination.close()
    print(request.data['email'])
    try:
        handle(request.FILES['file'])
        
    
    except:
        asd=1

@api_view(['GET'])
def test2(request,email):
    email=email[:-10]
    def s3_connection():
        try:
            s3 = boto3.client(
                service_name="s3",
                region_name="ap-northeast-2", # 자신이 설정한 bucket region
                aws_access_key_id='AKIA4GGDU36NPNTUB7WU',
                aws_secret_access_key='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',
            )
        except Exception as e:
            print(e)
        else:
            print("s3 bucket connected!")
            return s3
    s3 = s3_connection()
    nums=[]
    response = s3.list_objects(Bucket='hyuksoonism-bucket', Prefix=email)
    print(response)
    print(response['Contents'])
    for re in response['Contents']:
            nums.append(re['Key'][len(email)+1:-4])
    
    location = s3.get_bucket_location(Bucket="hyuksoonism-bucket")["LocationConstraint"]
    photos=[]
    if int(nums[-1])>=4:
        for i in range(int(nums[-1])-3,int(nums[-1])+1):
            photos.append("https://hyuksoonism-bucket.s3."+location+".amazonaws.com/"+email+'/'+str(i)+".gif")
    else:

        for i in range(1,int(nums[-1])+1):
            photos.append("https://hyuksoonism-bucket.s3."+location+".amazonaws.com/"+email+'/'+str(i)+".gif")   

    print(photos)

    return render(request,'b.html',{'photos':photos})


