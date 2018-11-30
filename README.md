#Advertising Mirror :-
 
 This is an IOT based project which is implemented to change normal mirror to a advertising platform.
 A CRM panel developed using ASP.NET and MYSQL is used to store data about Advertisers and Device Registration and Links to download the videos are obtained from APIs developed with this website.
 Each device downloads videos associated to them and whenever an object stays for more than a second onfron of this device an advertisment is triggered and played on the screen.
 
#Setup of Device:-
 
 Each device is controlled using Raspberry Pi Micro-controller which is setup with raspbian OS(Linux- Debian built ). 
 A Sharp sensor connected to ADC is supplied with power using GPIO pins of raspberry pi.
 And a monitor is used to as display device.
 
#Programming Module:-
 
 Python 2.7 is used for all the device end programming.
 Each device has five python modules working simutaneously in diffrent thread as soon as our device starts.
 Del.py module runs after an interval of 1 hour which is used to remove expired advertising campaigns from device.
 Upload_Counts.py runs after every minute which uploads counts of each campaings triggered to the CRM panel.
 video.py is used to get links of videos associated to the device and download them to the device.
 reg.py is GUI based module used for registration of device when with its MAC address to the CRM panel.
 ir_vid_ofl.py is our main module which triggers all the other module along with this it also starts taking reading from the Sharp sensor.
 default.mp4 is a default video which is triggered if there are no videos present on the device or if there is any error playing a video.
 
#Installation of device:-

Each device is setup in a manner that the ir_vid_ofl.py module is executed as soon as the device is booted,
we just have to plug the raspberrypi and monitor adpater to power supply.

Scope of this project:-

By implementing Gender and age detection and using a camera instead of IR sensor we can improve selection of advertisment according to person standing infront of mirror,
which me result in a better advertising concept and might be benificial for advetiser.


 
