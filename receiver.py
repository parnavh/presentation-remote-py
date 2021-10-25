import time
from firebase_admin import credentials, initialize_app, firestore
from pynput.keyboard import Controller, Key

keyboard = Controller()
lock = True

# Action was performed by the remote
def onSnapshot(snapshot, hmm, time):
    global lock
    if lock:
        lock = False
        return
    
    send_input(hmm[0].document.to_dict()["action"])

def send_input(action):
    keyboard.press(eval(f"Key.{action}"))

def main():
    creds = credentials.Certificate("./credentials.json")
    initialize_app(creds)

    db = firestore.client()

    db.collection("remote").document("current").collection("clicks").on_snapshot(onSnapshot)

    # Keep the program running
    while True:
        time.sleep(60)

if __name__ == "__main__":
    main()