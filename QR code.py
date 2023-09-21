import qrcode
a = "https://www.linkedin.com/in/deepanraj-k-b263a1233/"
url = qrcode.make(a)
url.save("Linkedin.png")
print(url)