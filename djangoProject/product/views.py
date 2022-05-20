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

##camera
import picamera
import time
import requests
import smtplib
import imageio
from PIL import Image
import shutil

## camera
class ProductListAPI(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        print(queryset)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

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
def test(request, email):
    try:
        if not os.path.exists('./static/'+email):
            os.makedirs('./static/'+email)
    except OSError:
        print ('Error: Creating directory. ' )
    return render(request,'a.html',{'email':email})
@api_view(['GET'])
def test2(request,email):
    photos=[]
    cnt=0
    for i in range(4):
            if os.path.exists('./static/'+email+'/'+str(i)):
                cnt+=1
    for j in range(cnt):
        photos.append('/static/'+email+'/'+str(j)+'/'+'main.gif')
    print(photos)

    return render(request,'b.html',{'photos':photos})


def test3(request,email):
    
    cnt=0
    for i in range(4):
        if os.path.exists('./static/'+email+'/'+str(i)):
            cnt+=1
    if cnt==4:
        shutil.rmtree('./static/'+email+'/'+str(0))
        for i in range(1,4):
            os.rename('./static/'+email+'/'+str(i),'./static/'+email+'/'+str(i-1))
        idx=3
    else:
        idx=cnt
    os.makedirs('./static/'+email+'/'+str(idx))

    for i in range(10):
        camera=picamera.PiCamera()
        camera.resolution=(1024,768)
        camera.capture('./static/'+email+'/'+str(idx)+'/'+str(i)+'.jpg')
        camera.close()
    path = ['./static/'+email+'/'+str(idx)+'/'+str(i) for i in os.listdir('./static/'+email+'/'+str(idx))]
    imgs = [ Image.open(i) for i in path]
    imageio.mimsave('./static/'+email+'/'+str(idx)+'/'+'main.gif', imgs, fps=2.0)
    return redirect('../')