import os , customtkinter , requests , shutil 
import tkinter as tk
from tkinter import messagebox as box
import subprocess as sub
from zipfile import ZipFile


#Img url
img = 'https://cdn.discordapp.com/attachments/981448833940742154/1013518850907709511/di.png'

img_exists = os.path.exists('C:\Program Files (x86)\Microsoft\Temp\di.png')

if img_exists == False:
    r2 = requests.get(img, allow_redirects=True)
    open('C:\Program Files (x86)\Microsoft\Temp\di.png', 'wb').write(r2.content)

#Settings
urlClient = "https://pastebin.com/raw/8gXTNSKk"#pastbin with minecraft url
url2 = "https://filetransfer.io/data-package/j2ykxYny/download"#minecraft library url (Launcher.zip)
app = customtkinter.CTk() 
customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("blue") 
frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)
label_1 = customtkinter.CTkLabel(master=frame_1, justify=tk.LEFT,text="DLoader")
label_1.pack(pady=12, padx=10) 
app.geometry("350x400")
app.resizable(width=False,height=False)
app.title("DLoader")
app.iconphoto(False, tk.PhotoImage(file='C:\Program Files (x86)\Microsoft\Temp\di.png'))
app.wm_attributes('-alpha', 0.95) 

def InstallF():
    url = requests.get(urlClient).text
    response = requests.get(url)
    response2 = requests.get(url2)
    game_exists = os.path.exists('C:\Launcher')
    if game_exists == True:
        shutil.rmtree("C:\Launcher")
    open("C:\Launcher.zip", "wb").write(response2.content)
    ZipFile("C:\Launcher.zip").extractall("C:\\")
    open("C:\Launcher\minecraft.jar", "wb").write(response.content)
    os.remove("C:\Launcher.zip")
    tk.messagebox.showinfo(title="D-Info", message="Installed")

def LaunchF():
    game_exists = os.path.exists('C:\Launcher')
    if game_exists == True:
        Name = entry.get()
        app.destroy()
        sub.call(f'javaw -noverify -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX:G1HeapRegionSize=32M -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:+ParallelRefProcEnabled -Xms524M -Xmx524M -Dfile.encoding=UTF-8 -Dlog4j.configurationFile=C:/Launcher/assets/log_configs/patched-variant-2.7.xml -Dfml.ignoreInvalidMinecraftCertificates=true -Dfml.ignorePatchDiscrepancies=true -Djava.net.useSystemProxies=true -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump "-Dos.name=Windows 10" -Dos.version=10.0 "-Djava.library.path=C:/Launcher/natives" -Dminecraft.launcher.brand=java-minecraft-launcher -Dminecraft.launcher.version=1.6.84-j "-Dminecraft.client.jar=C:/Launcher/minecraft.jar" -cp "C:/Launcher/libraries/com/turikhay/ca-fixer/1.0/ca-fixer-1.0.jar;C:/Launcher/libraries/ru/tlauncher/patchy/1.0.0/patchy-1.0.0.jar;C:/Launcher/libraries/oshi-project/oshi-core/1.1/oshi-core-1.1.jar;C:/Launcher/libraries/net/java/dev/jna/jna/4.4.0/jna-4.4.0.jar;C:/Launcher/libraries/net/java/dev/jna/platform/3.4.0/platform-3.4.0.jar;C:/Launcher/libraries/com/ibm/icu/icu4j-core-mojang/51.2/icu4j-core-mojang-51.2.jar;C:/Launcher/libraries/net/sf/jopt-simple/jopt-simple/5.0.3/jopt-simple-5.0.3.jar;C:/Launcher/libraries/com/paulscode/codecjorbis/20101023/codecjorbis-20101023.jar;C:/Launcher/libraries/com/paulscode/codecwav/20101023/codecwav-20101023.jar;C:/Launcher/libraries/com/paulscode/libraryjavasound/20101123/libraryjavasound-20101123.jar;C:/Launcher/libraries/com/paulscode/librarylwjglopenal/20100824/librarylwjglopenal-20100824.jar;C:/Launcher/libraries/com/paulscode/soundsystem/20120107/soundsystem-20120107.jar;C:/Launcher/libraries/io/netty/netty-all/4.1.9.Final/netty-all-4.1.9.Final.jar;C:/Launcher/libraries/com/google/guava/guava/21.0/guava-21.0.jar;C:/Launcher/libraries/org/apache/commons/commons-lang3/3.5/commons-lang3-3.5.jar;C:/Launcher/libraries/commons-io/commons-io/2.5/commons-io-2.5.jar;C:/Launcher/libraries/commons-codec/commons-codec/1.10/commons-codec-1.10.jar;C:/Launcher/libraries/net/java/jinput/jinput/2.0.5/jinput-2.0.5.jar;C:/Launcher/libraries/net/java/jutils/jutils/1.0.0/jutils-1.0.0.jar;C:/Launcher/libraries/com/google/code/gson/gson/2.8.0/gson-2.8.0.jar;C:/Launcher/libraries/by/ely/authlib/3.2.38.0-cafixer/authlib-3.2.38.0-cafixer.jar;C:/Launcher/libraries/com/mojang/realms/1.10.22/realms-1.10.22.jar;C:/Launcher/libraries/org/apache/commons/commons-compress/1.8.1/commons-compress-1.8.1.jar;C:/Launcher/libraries/org/apache/httpcomponents/httpclient/4.3.3/httpclient-4.3.3.jar;C:/Launcher/libraries/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar;C:/Launcher/libraries/org/apache/httpcomponents/httpcore/4.3.2/httpcore-4.3.2.jar;C:/Launcher/libraries/it/unimi/dsi/fastutil/7.1.0/fastutil-7.1.0.jar;C:/Launcher/libraries/org/apache/logging/log4j/log4j-api/2.8.1/log4j-api-2.8.1.jar;C:/Launcher/libraries/org/apache/logging/log4j/log4j-core/2.8.1/log4j-core-2.8.1.jar;C:/Launcher/libraries/org/lwjgl/lwjgl/lwjgl/2.9.4-nightly-20150209/lwjgl-2.9.4-nightly-20150209.jar;C:/Launcher/libraries/org/lwjgl/lwjgl/lwjgl_util/2.9.4-nightly-20150209/lwjgl_util-2.9.4-nightly-20150209.jar;C:/Launcher/libraries/com/mojang/text2speech/1.10.3/text2speech-1.10.3.jar;C:/Launcher/libraries/misc/tweaker/1.2/tweaker-1.2.jar;C:/Launcher/libraries/misc/tweaker/net.minecraft.client.main.Main/tweaker-net.minecraft.client.main.Main.jar;C:/Launcher/minecraft.jar" misc.tweaker.StubMain --username {Name} --version "Optifine 1.12.2" --gameDir C:/Launcher --assetsDir C:/Launcher/assets --assetIndex test --uuid df0f762d2a4035dabcbf4b8ae9216347 --accessToken df0f762d2a4035dabcbf4b8ae9216347 --userType legacy --versionType release --width 925 --height 530',shell=False)
        exit()
    else:
        tk.messagebox.showerror(title="D-Error", message="Need to install")







entry = customtkinter.CTkEntry(master=app,width=135,placeholder_text="Name")
entry.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)
LaunchB = customtkinter.CTkButton(master=app, text="Launch", command=LaunchF)
LaunchB.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
InstallB = customtkinter.CTkButton(master=app, text="Install", command=InstallF)
InstallB.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

app.mainloop()