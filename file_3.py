f = open("photo.jpg" ,"rb")

view = f.read()
print(view)

# file ko open kiya read kiya imaga ka text deta print kiya 

g = open("reversephoto.jpg" , "wb")
g.write(view)
# yaha ke text deta se image ko reverse print kar diya
g.close()
f.close()




# ye morden tarika hai file ko open karne ka


with open("photo.jpg", "rb") as k, open("reversephoto.jpg", "wb") as l :
    vu = k.read()
    l.write(vu)
