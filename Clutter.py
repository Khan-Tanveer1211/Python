import os
# os.rename("Cluttered folder/pngegg.png","Cluttered folder/pngegg(0).txt")
files = os.listdir("Cluttered folder")
i=1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"Cluttered folder/{file}", f"Cluttered folder/{i}.png")
        i = i+1