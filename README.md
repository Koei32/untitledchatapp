# Untitled Chat App (indev)
###### (i couldnt come up with a clever name so here we are)

<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/c4905951cdb7520b0b3b23773792b978b819a075_image.png"/>

This is pretty much a clone of <a href="https://en.wikipedia.org/wiki/(AIM_software)"/>AOL Instant Messenger</a> written in Python using PySide6 for the UI. It is pretty basic but easier to build upon (which i plan to do in the future). Socket connections are utilised for the client-server connections. The server is hosted on <a href="https://hackclub.app">Nest</a> (thanks Hack Club).


## Features
Again, it is pretty basic. But it does what an instant messenger is supposed to do, deliver messages instantly. Most importantly, it imitates the look (debatable) and feel of AIM.
- You can register an account, and sign into it.
<br><img width=180 src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/2e6a45beaae9b94e40f0618f62619a9a6fc3bc19_image.png"/>

- and send messages to your Buddies™!
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/a6b525940ede7c2340cab38dec7b245e05d28ca3_image.png"/>

<br>Currently, everyone who is registered to the app is everyone else's buddy. I plan on changing this soon.


## Instructions
To get right to messaging, just download the `client.exe` (linux build coming soon™) executable in latest release and run it. 

Ignore the SmartScreen warning if you get one, the executable is obviously not signed (click "More info" and hit "Run anyway"). 

Register yourself. Choose a Screen Name and a password, then hit Register.

Double click your Buddy's Screen Name in the Buddy List and start chatting.


## End
This project was made for submission to Hack Club's **Summer of Making 2025** ([link](https://summer.hackclub.com/projects/2529)). I mostly wanted to make this because I wanted to learn more about making GUIs in python and also socket communication. I originally planned end-to-end encryption for this app as well but I am most definitely not going to make the deadline (perhaps in the future?). If you find any issues, please make an issue. Thanks for viewing. \o