filename = str(input("File name: ")).lower().strip()

if ".gif" in filename:
    print("image/gif")

if ".png" in filename:
    print("image/png")

if ".jpg" or ".jpeg" in filename:
    print("image/png")

else:
    print("application/octet-stream")


