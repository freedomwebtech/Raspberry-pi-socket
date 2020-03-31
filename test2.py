import socket
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)





s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('192.168.0.103', 80))

s.listen(5) 




a= (bytes('<title>Raspberry-pi Web Server</title><h1>hello</h1><a href="/?led=on">ON</a>   <a href="/?led=off">OFF</a>','utf-8'))


while True:
     conn,adder = s.accept()
     request = conn.recv(1024)
     request = str(request)
     led_on = request.find('/?led=on')
     led_off = request.find('/?led=off')
     conn.sendall(a)
     conn.close()
     if led_on == 6:
       print('LED ON')
       GPIO.output(23, GPIO.HIGH)
     if led_off == 6:
       print('LED OFF')
       GPIO.output(23, GPIO.LOW)
   
 
