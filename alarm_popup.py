from playsound import playsound
import time
import threading 
import tkinter as tk
from PIL import Image, ImageTk

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def play_alarm_sound():
    playsound("music.mp3")

def show_popup():
    """Menampilkan popup di tengah layar saat alarm berbunyi."""
    popup = tk.Tk()
    popup.title("Ayo Sayang Udah Waktunya")
    
    popup_width = 500
    popup_height = 500
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    position_x = (screen_width // 2) - (popup_width // 2)
    position_y = (screen_height // 2) - (popup_height // 2)
    popup.geometry(f"{popup_width}x{popup_height}+{position_x}+{position_y}")

    img = Image.open("alarm.jpg") 
    img = img.resize((500, 500))
    photo = ImageTk.PhotoImage(img)
    image_label = tk.Label(popup, image=photo)
    image_label.image = photo
    image_label.pack(pady=10)
    
    label = tk.Label(popup, text="Sudah Waktunya!", font=("Helvetica", 16), fg="blue")
    label.pack(pady=10)

    close_button = tk.Button(popup, text="OK", command=popup.destroy, font=("Helvetica", 12))
    close_button.pack(pady=20)

    popup.mainloop()
    
def alarm(seconds):
    time_elapse = 0
    
    print(CLEAR)
    while time_elapse < seconds:
        time.sleep(1)
        time_elapse += 1

        time_left = seconds - time_elapse
        minutes_left = time_left // 60 
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Waiting {minutes_left:02d}:{seconds_left:02d}")

    sound_thread = threading.Thread(target=play_alarm_sound)
    sound_thread.daemon = True 
    sound_thread.start()
    
    show_popup()

minutes = int(input("Masukkan Menit: "))
seconds = int(input("Masukkan Detik: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)
