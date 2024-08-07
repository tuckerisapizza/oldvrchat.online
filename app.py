import os 
from typing import List
from typing import Any
from dataclasses import dataclass
import json
from flask import Flask,redirect,send_file,request,json

app = Flask(__name__)

@app.route('/')
def main():
    return "VRChat Custom Server, by @tuckerisapizza. Supports version 0.12.0." # 

@app.route('/<path:text>', methods=['GET', 'POST', 'PUT'])
def all_routes(text):
    #for header in dict(request.headers):
        #print(header + " | " + request.headers.get(header))
    print(text)
    isCDN = False
    file = ""
    send = ""
    bracketresponse = "[]"
    # bracketresponse can be sent as a bullshit response and the game will unwillingly accept it
    data = request.get_data().decode().replace("b'", "").replace("'", "")
    # by default flask has weird characters in request data, this remotes them
    print("data recieved")
    print(data)
    
    # contains all variables for changing things with the game, called on startup
    if text.startswith('config'):
        configfile3 = {"clientApiKey": "vrchatsex","hubWorldId": "Tuscany_01","homeWorldId": "wrld_2aec30df-6bbb-4272-89c1-3f2d4a1848cb","tutorialWorldId": "wld_7d3d25ec-663e-406e-96a3-e2c4fc0d8104","currentTOSVersion": "0", "whiteListedAssetUrls": ["http://localhost:2200/"]}
        
        configfile2 = {"clientApiKey": "vrchatsex","hubWorldId": "wld_97fda4a1-f820-4f09-a88c-2d2a95b668f7","homeWorldId": "wrld_2aec30df-6bbb-4272-89c1-3f2d4a1848cb","tutorialWorldId": "wld_7d3d25ec-663e-406e-96a3-e2c4fc0d8104","currentTOSVersion": "0", "whiteListedAssetUrls": ["http://localhost:2200/"]}
        configfile = {
            "messageOfTheDay": "",
            "timeOutWorldId": "wrld_5b89c79e-c340-4510-be1b-476e9fcdedcc",
            "gearDemoRoomId": "2282253502",
            "releaseServerVersionStandalone": "public_server_01",
            "downloadLinkWindows": "http://d8zlo8exwu24u.cloudfront.net/stable/VRChat_Oculus_0.11.7p6.exe",
            "releaseAppVersionStandalone": "0.12.0p3",
            "devAppVersionStandalone": "0.12.0p3",
            "devServerVersionStandalone": "dev_server_01",
            "devDownloadLinkWindows": "www.vrchat.net",
            "currentTOSVersion": 5,
            "releaseSdkUrl": "https://files.vrchat.cloud/sdk/VRCSDK-2018.05.24.18.24_Public.unitypackage",
            "releaseSdkVersion": "2018.05.24.18.24",
            "devSdkUrl": "https://files.vrchat.cloud/sdk/VRCSDK-2018.05.24.18.24_Public.unitypackage",
            "devSdkVersion": "2018.05.24.18.24",
            "whiteListedAssetUrls": [
                "http://" + "localhost:2200" + "/",
                "http://" + "localhost:2200" + "/",
                "http://" + request.headers.get("Host") + "/",
                "https://" + request.headers.get("Host") + "/",
                "https://github.com/",
                "https://github.com/tuckerisapizza/oldvrchat.online/raw/main/",
                "https://raw.githubusercontent.com",
                "https://raw.githubusercontent.com/tuckerisapizza/oldvrchat.online/main/"
            ],
            "clientApiKey": "oldvrchat",
            "viveWindowsUrl": "http://store.steampowered.com/app/438100/",
            "sdkUnityVersion": "5.6.3p1",
            "hubWorldId": "wrld_eb7a5096-9c93-41db-a9d7-7b349a5d4815",
            "homeWorldId": "wrld_a0ad5ad3-2b2c-4a77-8220-d372d299b412",
            "tutorialWorldId": "wld_7d3d25ec-663e-406e-96a3-e2c4fc0d8104",
            "disableEventStream": False,
            "disableAvatarGating": False,
            "disableFeedbackGating": False,
            "sdkNotAllowedToPublishMessage": "Welcome the VRChat SDK!\r\n\r\nBefore you can upload avatars or worlds to VRChat, you'll need to spend more time enjoying the app. We do this for security reasons, and so you can learn more about us.\r\n\r\nWhen you get the ability to upload, we will notify you via email and in VRChat. For now, you can learn and test on your own device.\r\n\r\nTo get started, check out the resources below.\r\n\r\nThank you for your patience, we can't wait to see what you'll build!",
            "sdkDeveloperFaqUrl": "https://www.vrchat.com/developerfaq",
            "sdkDiscordUrl": "https://discord.gg/vrchat",
            "notAllowedToSelectAvatarInPrivateWorldMessage": "For security reasons, you're not yet allowed to select avatars in private worlds or upload content. Please continue to enjoy VRChat and we'll message you when you've been unlocked. Thanks and have fun!",
            "address": "1062 Folsom St., Suite 200, San Francisco, CA, 94103",
            "contactEmail": "hello@vrchat.com",
            "supportEmail": "support@vrchat.com",
            "jobsEmail": "jobs@vrchat.com",
            "copyrightEmail": "copyright@vrchat.com",
            "moderationEmail": "moderation@vrchat.com",
            "appName": "VrChat",
            "serverName": "green-api-1959",
            "deploymentGroup": "green",
            "buildVersionTag": "build-05-06-18-major-meat",
            "apiKey": "oldvrchat",
            "plugin": [
                "http://" + "localhost:2200" + "/",
                "http://" + request.headers.get("Host") + "/",
                "https://" + request.headers.get("Host") + "/",
                "https://github.com/",
                "https://github.com/tuckerisapizza/oldvrchat.online/raw/main/",
                "https://raw.githubusercontent.com",
                "https://raw.githubusercontent.com/tuckerisapizza/oldvrchat.online/main/"
            ],
            "defaultAvatar": "avtr_c38a1615-5bf5-42b4-84eb-a8b6c37cbd11",
            "TwitterUserScreenName": [
                "http://" + "localhost:2200" + "/",
                "http://" + request.headers.get("Host") + "/",
                "https://" + request.headers.get("Host") + "/",
                "https://github.com/",
                "https://github.com/tuckerisapizza/oldvrchat.online/raw/main/",
                "https://raw.githubusercontent.com",
                "https://raw.githubusercontent.com/tuckerisapizza/oldvrchat.online/main/"
            ]
            }

        send = json.dumps(configfile2)

    # too lazy to disable eventstream, plus it helps sometimes. it can be disabled by remoteconfig
    if text.startswith('eventstream'):
        send = bracketresponse

    if (text.startswith("auth/user")):
        # moderation api isnt used yet, i just put some bullshit working responses in
        if text.startswith('auth/user/player'):
            moderatefile = open("apis/playermoderations.json", "r")
            send = moderatefile.read()
        if text.startswith('auth/user/moderations'):
            moderatefile = open("apis/moderations.json", "r")
            send = moderatefile.read()
        if text.startswith("auth/user/notifications"):
            send = bracketresponse
        if text.startswith("auth/user/friends"):
            send = bracketresponse
        
        
        # THIS IS THE PROFILE CODE LETS FUCKING GOOOOO
        if send == "":
            print("getting user profile")
            # added new code to write and read profiles
            if os.path.exists("apis/players/" + str(request.headers.get("X-Macaddress"))):
                profile = open("apis/players/" + str(request.headers.get("X-Macaddress")), "r")
                send = profile.read()
    # PROFILE CREATION
    if (text.startswith("auth/register")):
        jsonData = json.loads(data)
        profile = {
            "id": str(request.headers.get("X-Macaddress")),
            "username": str(jsonData.get("username")),
            "displayName": str(jsonData.get("username")),
            "emailVerified": "true",
            "hasEmail": "true",
            "hasBirthday": "true",
            "acceptedTOSVersion": 999,
            "currentAvatar": "avtr_c38a1615-5bf5-42b4-84eb-a8b6c37cbd11",
            "currentAvatarAssetUrl": "https://raw.githubusercontent.com/tuckerisapizza/oldvrchat.online/main/vrca/avtr_c38a1615-5bf5-42b4-84eb-a8b6c37cbd11.vrca",
            "developerType": "trusted",
            }
        filewrite = open("apis/players/" + str(request.headers.get("X-Macaddress")), "w")
        filewrite.write(json.dumps(profile))
        send = json.dumps(profile)
    
    # UHH UH STUPID USERS API THAT I DONT KNOW WHAT IT DOES
    if(text.startswith("users")):
        if os.path.exists("apis/players/" + str(request.headers.get("X-Macaddress"))):
                profile = open("apis/players/" + str(request.headers.get("X-Macaddress")), "r")
                send = profile.read()
        else:
            send = "WTF! THIS ISNT SUPPOSED TO HAPPEN!!"

    # AVATARS API
    if (text.startswith("avatars")):
        avatar = text.replace("avatars/", "").replace("?apiKey=oldvrchat&organization=vrchat&maxUnityVersion=5.6.3p1&minUnityVersion=5.5.0f1&maxAssetVersion=1&minAssetVersion=0&platform=standalonewindows", "")
        print("getting avatars..")
        if os.path.exists("apis/avatars/" + avatar + ".json"):
                avatarjson = open("apis/avatars/" + avatar + ".json", "r")
                send = avatarjson.read()
        if request.args.get('sort') == "order":
            final = ""
            for filename in os.listdir("vrca"):
                f = os.path.join("vrca", filename)
                # checking if it is a file
                if os.path.isfile(f):
                    filename = filename.replace(".vrca", "")
                    try:
                        avatarjson = open("apis/avatars/" + filename + ".json", "r", encoding="utf8")
                        jsondata = avatarjson.read()
                    except:
                        avatarjson = {
                            "id": filename,
                            "name": filename,
                            "description": "Avatar description. Avatar is available to use, however has been created automatically by the server. Please fix.",
                            "imageUrl": "http://"+ request.headers.get("Host") + "/Images/" + filename + ".png",
                            "authorName": "vrchat",
                            "authorId": "vrchat",
                            "assetUrl": "https://raw.githubusercontent.com/tuckerisapizza/oldvrchat.online/main/vrca/" + filename + ".vrca",
                            "tags": [
                                "avatar"
                            ],
                            "unityVersion": "5.6.3p1",
                            "version": 1,
                            "assetVersion": "1",
                            "platform": "standalonewindows",
                            "releaseStatus": "public"
                            }
                        print("not found, creating")
                        filewrite = open("apis/avatars/" + filename + ".json", "w")
                        filewrite.write(json.dumps(avatarjson))
                        jsondata = json.dumps(avatarjson)
                    final = final + jsondata.lstrip("") + ","
                    print(f)
            final = final.rstrip(",").lstrip(",") + "]"
            send = "[" + final
        if send == "":
            # it creates an automatic json file if it doesnt exist, i dont wanna 
            # go through the trouble of creating all the files by hand lmao
            
            avatarjson = {
                "id": avatar,
                "name": avatar,
                "description": "Avatar description. Avatar is available to use, however has been created automatically by the server. Please fix.",
                "imageUrl": "http://"+ request.headers.get("Host") + "/Images/" + avatar + ".png",
                "authorName": "vrchat",
                "authorId": "vrchat",
                "assetUrl": "https://raw.githubusercontent.com/tuckerisapizza/oldvrchat.online/main/vrca/" + avatar + ".vrca",
                "tags": [
                    "avatar"
                ],
                "unityVersion": "5.6.3p1",
                "version": 1,
                "assetVersion": "1",
                "platform": "standalonewindows",
                "releaseStatus": "public"
                }
            filewrite = open("apis/avatars/" + avatar + ".json", "w")
            filewrite.write(json.dumps(avatarjson))
            send = json.dumps(avatarjson)
            
    # WORLDS API
    if text.startswith("worlds"): 
        world = ""
        try:
             world2 = text.replace("worlds/", "")
             world1 = world2.replace("?apiKey=oldvrchat&organization=vrchat&maxUnityVersion=5.6.3p1&minUnityVersion=5.5.0f1&maxAssetVersion=3&minAssetVersion=0&platform=standalonewindows", "")
             world0 = world1.replace("/1?apiKey=oldvrchat","")
             world00 = world0.replace("/","")
             world000 = world00.replace("/metadata?apiKey=oldvrchat&organization=vrchat","")
             world = world000
             print(world + "HEREYE")
        finally: 
            
            if "/1" in text:
                instanceid = text.replace("apis/worlds/" + world +  "/", "").replace("?apiKey=vrchatsex", "")
                instancejson = {
                    "id": instanceid,
                    "private": False,
                    "friends": False,
                    "users": [],
                    "roomName": instanceid
                    }
                send = json.dumps(instancejson)

            if "metadata" in text:
                worldjson = {
                    "id": world.replace("metadata",""),
                    "metadata": {}
                    }

                send = json.dumps(worldjson)
            if request.args.get('sort') == "order":
                final = ""
                for filename in os.listdir("vrcw"):
                    f = os.path.join("vrcw", filename)
                    # checking if it is a file
                    if os.path.isfile(f):
                        filename = filename.replace(".vrcw", "")
                        try:
                            worldjson = open("apis/worlds/" + filename + ".json", "r", encoding="utf8")
                            jsondata = worldjson.read()
                        except:
                            worldjson = {
                                "id": filename,
                                "name": filename,
                                "description": "World description. World is available to use, however has been created automatically by the server. Please fix.",
                                "imageUrl": "http://"+ request.headers.get("Host") + "/cdn/Images/" + filename + ".png",
                                "authorName": "vrchat",
                                "authorId": "vrchat",
                                "assetUrl": "https://raw.githubusercontent.com/tuckerisapizza/oldvrchat.online/main/vrcw/" + filename + ".vrcw",
                                "tags": [
                                    "world"
                                ],
                                "unityVersion": "5.6.3p1",
                                "version": 1,
                                "assetVersion": "1",
                                "platform": "standalonewindows",
                                "releaseStatus": "public",
                                "capacity": 8,
                                "pluginUrl": "https://raw.githubusercontent.com/tuckerisapizza/oldvrchat.online/main/dll/" + filename + ".dll",
                                "occupants": 0,
                                "thumbnailImageUrl": "http://"+ request.headers.get("Host") + "/cdn/Images/" + filename + ".png"
                                
                                }
                            print("not found, creating")
                            filewrite = open("apis/worlds/" + filename + ".json", "w")
                            filewrite.write(json.dumps(worldjson))
                            jsondata = json.dumps(worldjson)
                        final = final + jsondata.lstrip("") + ","
                        print(f)
                final = final.rstrip(",").lstrip(",") + "]"
                send = "[" + final
                filewrite = open("apis/uhhworldsquestionmark.json", "w")
                filewrite.write(send)


            if send == "":
                if os.path.exists("apis/worlds/" + world + ".json"):
                    worldjson = open("apis/worlds/" + world + ".json", "r")
                    send = worldjson.read()
                else:
                    worldjson = {
                        "id": world,
                        "name": world,
                        "description": "World description. World is available to use, however has been created automatically by the server. Please fix.",
                        "imageUrl": "http://"+ request.headers.get("Host") + "/cdn/Images/" + world + ".png",
                        "authorName": "vrchat",
                        "authorId": "vrchat",
                        "assetUrl": "https://raw.githubusercontent.com/tuckerisapizza/oldvrchat.online/main/vrcw/" + filename + ".vrcw",
                        "tags": [
                            "world"
                        ],
                        "unityVersion": "5.6.3p1",
                        "version": 1,
                        "assetVersion": "1",
                        "platform": "standalonewindows",
                        "releaseStatus": "public",
                        "capacity": 8,
                        "pluginUrl": "https://raw.githubusercontent.com/tuckerisapizza/oldvrchat.online/main/dll/" + filename + ".dll",
                        "occupants": 0,
                        "thumbnailImageUrl": "http://"+ request.headers.get("Host") + "/cdn/Images/" + world + ".png"
                        }
                    filewrite = open("apis/worlds/" + world + ".json", "w")
                    filewrite.write(json.dumps(worldjson))
                    send = json.dumps(worldjson)

   
 
       


    #rewriting the ENTIRE files api because somehow IT GOT FUCKING DELETED OVER THE COURSE OF 5 MONTHS!!
    if text.startswith("cdn/"):
        filename = text.replace("cdn/", "")
        if ".vrca" in text:
            print("VRCA called for!")
            isCDN = True
            file = "vrca\\" + filename

        if ".vrcw" in text:
            print("VRCW called for!")
            isCDN = True
            file = "vrcw\\" + filename

        if ".dll" in text:
            print("DLL called for!")
            isCDN = True
            file = "dll\\" + filename

        send = file

    # CDN API, serves files and shit
    

    print (request.args.get('sort'))
    print("data to send:")
    print(send)
    if (isCDN):
        isCDN = False
        try:
            return send_file(send)
        except:
            if ".dll" in text:
                return send_file("dll\\fallbackdll.dll")

    else:  
        return send

       
    
    
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 2200))
    app.run(host='0.0.0.0', port=port)

    


