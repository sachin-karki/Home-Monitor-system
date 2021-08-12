# Home Monitor System
##### *This README will thoroughly describe HMS.*
## Introduction - What is "Home Monitor System" and How does it Work?
  
##### Home monitor is a DIY surveillance system that is powered by Raspberry Pi that uses an external image sensor or simply a camera that takes visual feed and sends an email as push notifications to alert the home owners. Everytime a motion via the Infrared Sensor is detected the PiCamera will record a 5-10 sec video and a still image. The motion alert will be notified to the user in their dedicated phone number. The message will be delivered from an email client.  The short footage and still image will be locally stored in a folder which also acts as a network drive for the Google Drive. Every video and photo will be transfered to Cloud (google drive) via RClone.  The whole system is powered by a python script that should be executed in order to get the HMS started. To enable support in a headless format and easy execution, cron job has been configured to run the python script during its boot. Everytime the Raspberry Pi boots or reboots, the python script will run on it s own without needing any manual execution from the user.

## Things You Will Need
1. Essential Raspberry Pi Kit (4 recommended)
![image alt](https://cdn.sparkfun.com//assets/parts/1/7/1/5/0/17980-SparkFun_Raspberry_Pi_4_Basic_Kit_-_8GB-01.jpg)
2. PiCamera
![image alt](http://cdn.shopify.com/s/files/1/0176/3274/products/std-camera.jpg?v=1568673984)
3. Infrared Sensor
![image alt](https://i5.walmartimages.com/asr/c54b9f2c-5c5f-4bc0-bf68-5dbba72c0afc_1.96c132be815cac9908d0d6abc7f8b4b9.jpeg)

## What the Setup Will Look Like
![image info](images/setup.HEIC)


##### The complete guide and references that we used to get this project done is listed below. 

## References 
1. [The Visual Guide We Used](https://www.youtube.com/watch?v=xA9rzq5_GFM&t=266s)
2. [RClone setup for Google Drive](https://www.youtube.com/watch?v=zlz3OtI1n9w)
3. [Cron Job Configuration](https://www.youtube.com/watch?v=rErAOjACT6w)
4. [Sending Alerts Using Python](https://www.youtube.com/watch?v=B1IsCbXp0uE) 
