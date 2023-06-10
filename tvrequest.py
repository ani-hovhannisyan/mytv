import requests

mainUrl = "https://kinodaran.org/upload/video/storage/7b/90/7b90e96ece4a62e7554b4d06bdd90677.m3u8/segment015.ts"
cert_file = "/home/user/mytv/kcert.pem"

def generate_video_file(url, fragment):

    response = requests.get(url)

    if response.status_code == 200:
        #filename = url.split("/")
        #filename = filename[len(filename) - 1]
        with open("tottoro/" + fragment, "wb") as f:
            f.write(response.content)
            print("Saved video file:", "tottoro/" + fragment)
    else:
        print("Request failed with status code:", response.status_code)

videoSeconds = {
        "Tottoro": 5104,
        "XX": 10
    }

def init():
    #TODO: Prepare loop for many videos lists
    length = videoSeconds["Tottoro"]
    l = int(length/10) + 1
    print(l)
    for i in range(1, l):
        fragment = "segment" + f"{i:03d}"
        url = mainUrl.replace("segment015", fragment)
        print("-----", f"{i:03d}", url)
        generate_video_file(url, fragment)

init()
