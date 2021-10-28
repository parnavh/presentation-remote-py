# Presentation Remote

A remote made for making presentations easier by enabling all the members to have access to change the slide and control the flow of the presentation in real time.

## How the magic happens 🪄
The primary functionality of this application is divided into two modules:
- A remote control that transfers the signal to the receiver
- The receiver receives the commands and executes them on the host computer

When you interact with the remote, a document is added to the database (firestore)

```py
# Send info to receiver
def add_doc(self, action):
	self.db.collection("remote").document("current").collection("clicks").add({
		"action": action
	})
```

Which is then picked up by the receiver, which is always listening for these events. The receiver then simulates the necessary keystroke on the host system.

```py
# Action was performed by the remote
def onSnapshot(snapshot, doc, time):
	send_input(doc[0].document.to_dict()["action"])
```

And this is all there is to it

## How to make it work ⚙️
You will have to setup a few things before you can get this working
- Setup python and have the dependencies installed
- Setup your firebase project and place the admin sdk credentials as `credentials.json` file in the same directory
- Optionally converting this application into a binary for easier sharing and usage

Checkout my [blog](https://parnavh.hashnode.dev/presentation-remote-using-python) for a full setup guide

If you want a ready-made executable make sure to checkout the releases but it will require the `credentials.json` file everywhere you run the executable hence I suggest you build an executable specifically for you which includes the credentials in the code. A full walkthrough is available on my [blog](https://parnavh.hashnode.dev/presentation-remote-using-python)

## Features
- Go to the previous slide
- Go to the next slide

## Coming soon
- Start/Stop Presentation functionality
- A third dashboard module which can:
	- Create user accounts and bind them to the MAC address
	- Create user roles
	- Limit access to features as per the user / user role
