import tkinter as tk
import webbrowser

def open_imdb_page():
    movie_name = entry.get()
    url = f"https://www.imdb.com/find?q={movie_name}&ref_=nv_sr_sm"
    webbrowser.open_new(url)

root = tk.Tk()
root.title("IMDb Movie Page")

label = tk.Label(root, text="Enter a movie name to open its page on IMDb:")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

button = tk.Button(root, text="Open IMDb Page", command=open_imdb_page)
button.pack()

root.mainloop()
