from tkinter import Tk, StringVar, ttk, N, W, E, S

counter = 0
def update_counter():
 global counter, counter_display
 counter += 1
 counter_display.set(counter)

window = Tk()
window.title("TK gui counter")

main_frame = ttk.Frame(window)
main_frame.grid(column=0, row=0, columnspan=2, rowspan=2, sticky=(N, W, E, S))

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

counter_display = StringVar()
counter_display.set(counter)
ttk.Label(main_frame, textvariable=counter_display).grid(column=1, row=0)
ttk.Button(main_frame, text="Update", command=update_counter).grid(column=1, row=1)

main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(2, weight=1)
main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(2, weight=1)

window.mainloop()