from tkinter import Tk, Frame, Button
from firebase_admin import credentials, initialize_app, firestore

class Firebase:
    def __init__(self) -> None:
        creds = credentials.Certificate("./credentials.json")
        initialize_app(creds)

        self.db = firestore.client()
        pass

    # Send info to receiver
    def add_doc(self, action):
        self.db.collection("remote").document("current").collection("clicks").add({
            "action": action
        })

def main():
    firebase = Firebase()
    window = Tk()
    window.title("Presentation Remote")
    window.geometry("320x170")
    window.resizable(False, False)
    mainframe = Frame(window)
    mainframe.pack(expand=True, fill="both")

    left_button = Button(mainframe, text="left", font=("Arial", 22), command = lambda: firebase.add_doc("left"), width=8, height=4, borderwidth=1, relief="solid")
    left_button.pack(expand=True, side="left")

    right_button = Button(mainframe, text="right", font=("Arial", 22), command = lambda: firebase.add_doc("right"), width=8, height=4, borderwidth=1, relief="solid")
    right_button.pack(expand=True, side="right")

    window.mainloop()

if __name__ == "__main__":
    main()