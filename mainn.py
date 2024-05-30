import tkinter as tk
import customtkinter as ctk
from pytube import YouTube as yt

def on_progress(stream,chunk, bytes_remaining):
    total_size=stream.filesize
    bytes_downloaded=total_size-bytes_remaining
    percentage = bytes_downloaded / total_size * 100
    print(percentage)
    per=str(int(percentage))
    pPercentage.configure(text=per)
    pPercentage.update()
    progressBar.set(per/100)
    progressBar.update()



def startDownload():
    print("tu")
    finish_label.configure(text="robing", text_color="yellow")
    finish_label.update()
    try:
        ytLink=link.get()
        ytObject=yt(ytLink,on_progress_callback=on_progress)
        video=ytObject.streams.get_lowest_resolution()
        video.download()
    except:
        finish_label.configure(text="ERROR!", text_color="red")
    else:
        finish_label.configure(text="SuCCESS!", text_color="green")


ctk.set_appearance_mode("System")

ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.geometry("720x480")
app.title("Py YouYube Downloader 5")

title= ctk.CTkLabel(app,text="Insert a youtube link")
title.pack(padx=10, pady=10)


url_var=ctk.StringVar()
link=ctk.CTkEntry(app,width=350, height=40,textvariable=url_var)
# link.insert(0,"https://www.youtube.com/watch?v=aAcHRQ-IE0Q")

link.pack()

pPercentage=ctk.CTkLabel(app,text="0%")
pPercentage.pack();

progressBar=ctk.CTkProgressBar(app,width=400)
progressBar.set(0)
progressBar.pack(padx=10,pady=10)





finish_label=ctk.CTkLabel(app,text="")
finish_label.pack()

download=ctk.CTkButton(app, text="Start download", command=startDownload)
download.pack();






app.mainloop();




