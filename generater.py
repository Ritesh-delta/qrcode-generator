import qrcode as qr
#take input from the user 
data = input("enter text or url :")
# now create qr code
qr = qr.QRCode(
    version = None,  #auto detect the version user can paste as long as short text and url code auto detect the version 
    box_size=10,  #size of each box in the qr code
    border=4,  #border size of the qr code
)
# add data
qr.add_data(data)
qr.make(fit=True)  #automatically fit the size of the qr code based on the data
# create image
img = qr.make_image(fill_color="blue", back_color="pink")
# save img
img.save("auto_qr.png")
 
print("QR code generated successfully")
print ("THANKS FOR USING THIS CODE! VIST AGAIN")
