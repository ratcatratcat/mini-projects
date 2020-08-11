import pyshorteners
url = input("enter an URL:\n")
print("URL after shortening: ", pyshorteners.Shortener().tinyurl.short(url))
