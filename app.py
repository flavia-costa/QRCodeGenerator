import qrcode
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def generate_qr():
    link = url_entry.get()
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    img_tk = ImageTk.PhotoImage(image=img)

    canvas.image = img_tk
    canvas.create_image(200, 200, image=img_tk)

    file_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[("PNG files", '*.png')])
    if not file_path:
        return
    img.save(file_path)

root = Tk()
root.geometry('400x500')
root.title('Gerador de QR Code')

Label(root, text="Adicionar link:").pack()
url_entry = Entry(root, width=40)
url_entry.pack()

generate_button = Button(root, text="Gerar QR Code", command=generate_qr)
generate_button.pack()

canvas = Canvas(root, width=400, height=400)
canvas.pack()

root.mainloop()