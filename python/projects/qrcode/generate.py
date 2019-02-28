<<<<<<< HEAD
import qrcode,image,uuid
def gen(data):
    qrcode.make(data=data).save(''.join(a for a in str(uuid.uuid4()) if a!="-")+".png")
=======
import qrcode,image,uuid
def gen(data):
    qrcode.make(data=data).save(''.join(a for a in str(uuid.uuid4()) if a!="-")+".png")
>>>>>>> Some error have exists
