# Presentation Remote

A remote made for making presentations easier by enabling all the members to have access to change the slide and control the flow of the presentation in real time.

## Components
The primary functionality of this application is divided into two modules:
- A remote control that transfers the signal to the receiver
- The receiver receives the commands and executes them on the host computer.

## How the magic happens
When you interact with the remote, a document is added to the database (firestore), which is picked up by the receiver, which is always listening for these events. The receiver then simulates the necessary keystroke on the host system.

## How to make it work
You will need python and a firebase project to enable this software to solve your presenting troubles.
- You can download and install python [here](https://www.python.org/downloads/)
- Install the requirements by running `pip install -r .\requirements.txt`
- Create a firebase project from the [console](https://console.firebase.google.com/) and then download the admin sdk credentials from the project settings as credentials.json in the root of the directory
- Just run `python remote.py` on the device which wants to remotely control the presentation
- Run `python receiver.py` on the host machine i.e. where the keys needs to be simulated

## Make a executable
You can make a executable using pyinstaller, instructions by GeeksForGeeks can be found [here](https://www.geeksforgeeks.org/convert-python-script-to-exe-file/). Just be sure to substitute the path to credentials.json in the code with the contents of the credentials.json file. You can then send this compiled binary to other people who then will not need to do any setup, just run the .exe and they will be good to go.

Example:
```py
# From
	creds = credentials.Certificate("./credentials.json")
# To
	myCredentials = {...} # Content in the credentials.json
	creds = credentials.Certificate(myCredentials)
```

## Features
- Go to the previous slide
- Go to the next slide

## Coming soon
- Start/Stop Presentation functionality
- A third dashboard module which can:
	- Create user accounts and bind them to the MAC address
	- Create user roles
	- Limit access to features as per the user / user role
