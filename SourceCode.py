from gpiozero import LED
from time import sleep
from datetime import datetime
from gpiozero import MotionSensor
import subprocess
import smtplib
from email.message import EmailMessage
pir = MotionSensor(4)
dir = "/home/pi/Desktop/images/"

while True:
    pir.wait_for_motion()
    print("Motion Detected")
    
    def email_alert(subject, body, to):
        msg =EmailMessage()
        msg.set_content(body)
        msg['subject'] =subject
        msg['to'] = to
        
        user = "bibekmanandhar911@@gmail.com"
        msg['from'] = user
        password = "lqzyndpzvzrexodn"
        
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user, password)
        server.send_message(msg)
        
        server.quit()
    if __name__ == '__main__':
        email_alert("ALERT!!!!!","MOTION DETECTED!","2149955813@messaging.sprintpcs.com")
        
    fileName= "img_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".jpg"
    cmd = "raspistill -o " + dir + fileName
    subprocess.run(cmd, shell=True)
    
    fileNamex= "vid_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".h264"
    cmdv = "raspivid -o " + dir + fileNamex
    subprocess.run(cmdv, shell=True)
    
    #subprocess.run(["raspistill", "-o","image.jpg"])
    #subprocess.run(["raspivid", "-o","video.h264"])

    pir.wait_for_no_motion()
    print("Motion Stopped")