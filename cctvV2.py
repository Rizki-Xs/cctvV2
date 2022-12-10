from time import sleep
from os import system
import sys
import datetime

def ketik(c):
  for e in c + "\n" :
    sys.stdout.write(e)
    sys.stdout.flush()
    sleep(0.015)
    
# program
system("clear")
sleep(2)
ketik("Jangan lupa subscribe dulu ya bro")
sleep(2)
system("xdg-open https://www.youtube.com/@Rizki_Xs")
system("clear")
sleep(2)
def logo():
  print("""
\033[33;1m  _______      \033[37;1m__         \033[36;1m___ ___ _______ 
 \033[33;1m|   _   .\033[37;1m----|  |_.--.--\033[36;1m|   Y   |       |
 \033[33;1m|.  1___\033[37;1m|  __|   _|  |  |\033[36;1m.  |   |___|   |
 \033[33;1m|.  |___\033[37;1m|____|____|\___/\033[36;1m|.  |   |/  ___/ 
 \033[33;1m|:  1   |               \033[36;1m|:  1   |:  1  \ 
 \033[33;1m|::.. . |                \033[36;1m\:.. ./|::.. . |
 \033[33;1m`-------'                 \033[36;1m`---' `-------'
                                          """)
  print("\033[31;1m[\033[37;1m+\033[31;1m] \033[34;1mAuthor  : \033[37;1mMuhammad Rizki Saparulloh")
  print("\033[31;1m[\033[37;1m+\033[31;1m] \033[34;1mYoutube : \033[37;1mRizki 952 ")
  print("\033[31;1m[\033[37;1m+\033[31;1m] \033[34;1mGithub  : \033[37;1mhttps://github.com/Rizki-Xs")
  print("")
logo()
def daftar():
  print("\033[31;1m[\033[37;1m+\033[31;1m] \033[37;1mDaftar")
  nama = input("    Nama   : ")
  umur = input("    Umur   : ")
  alamat = input("    Alamat : ")
  print("")
  count = 0
  load = ">"
  for t in range(101):
    sleep(0.070)
    print(f"\r{t}% [{load}]", end="", flush=True)
    count += 1
    if count == 3:
      count = 0
      load += ">"
  print(" Success")
  sleep(1.5)
  print("\033[31;1m[\033[37;1m+\033[31;1m] \033[37;1mPendaftaran selesai")
  print("    Nama   : " + nama)
  print("    Umur   : " + umur)
  print("    Alamat : " + alamat)
  x = datetime.datetime.today()
  print("    Date   :",x)
  print("")
daftar()
def tools():
  print("\033[31;1m[\033[37;1m+\033[31;1m] \033[37;1mIp CCTV")
  sleep(2)
  print("""\033[37;1m
[1] http://119.2.50.116:90/#view
[2] http://119.2.50.116:84/view/viewer_index.shtml?id=1183
[3] http://202.150.130.137:88/control/userimage.html
[4] http://118.137.102.29:8001/view/viewer_index.shtml?id=12647
[5] http://103.217.216.198:8001/#view
[6] http://103.217.216.197:8001/#view
[7] http://103.52.16.102:82/live/index.html?Language=0
[8] http://202.52.50.183:8001/#view
[9] http://103.217.216.198:8000/#view
[10] http://119.252.169.189:82/mobile.htm
[11] http://119.252.169.189:84/
[12] http://103.119.145.26:8001/live/index.html?Language=0
[13] http://36.91.83.73:8081/
[14] http://119.252.169.189:85/
[15] http://103.245.19.243/live/index.html?Language=0
[16] http://103.4.206.135:83/ui3.htm
[17] http://119.2.50.114:88/view/viewer_index.shtml?id=3941
[18] http://65.201.171.70/#view
[19] http://205.189.36.99:8082/control/userimage.html
[20] http://75.183.181.155/view/viewer_index.shtml?id=200
[21] http://12.34.170.21:8888/view/viewer_index.shtml?id=639
[22] http://128.104.206.15/view/viewer_index.shtml?id=131
[23] http://24.20.101.215:8000/view/viewer_index.shtml?id=44
[24] http://166.168.156.178:81/live/index.html?Language=0
[25] http://166.153.247.80:82/cgi-bin/guestimage.html
[26] http://75.112.32.101/view/viewer_index.shtml?id=1185
[27] http://166.247.40.1:82/#view
[28] http://67.204.149.29/control/userimage.html
[29] http://74.51.217.90:82/view/viewer_index.shtml?id=1968
[30] http://96.237.61.111:81/live/index.html?Language=0
[31] http://50.248.29.158/view/viewer_index.shtml?id=1315
[32] http://152.26.8.85/view/index.shtml
[33] http://202.73.139.110:81/live/index.html?Language=1&ViewMode=pull
[34] http://58.93.199.162:50001/live/index.html?Language=1
""")
  pil = input("    Pilih url no : ")
  if pil =="1":
     count = 0
     for t in range(101):
       sleep(0.050)
       print(f"\r    Loading... {t}%", end="", flush=True)
       count += 1
       if count == 3:
          count = 0
     print(" Done")
     sleep(1)
     system("xdg-open http://119.2.50.116:90/#view")
     sleep(3)
     back = input("    Kembali ke menu awal [y/n] : ")
     if back =="y":
        sleep(1.5)
        system("clear")
        logo()
        tools()

  if pil =="2":
     count = 0
     for t in range(101):
       sleep(0.050)
       print(f'\r    Loading...{t}%', end='', flush=True)
       count += 1
       if count == 3:
          count = 0
     print(' Done')
     sleep(1)
     system('xdg-open http://119.2.50.116:84/view/viewer_index.shtml?id=1183')
     sleep(3)
     back = input('    Kembali ke menu awal [y/n] : ')
     if back == "y":
        sleep(1.5)
        system('clear')
        logo()
        tools()
  if pil =="3":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0
        
    print(" Done")
    sleep(1)
    system("xdg-open http://202.150.130.137:88/control/userimage.html")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clsar")
      logo()
      tools()
      
  if pil =="4":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0
    print(" Done")
    sleep(1)
    system("xdg-open http://118.137.102.29:8001/view/viewer_index.shtml?id=12647")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="5":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
         count = 0
    print(" Done")
    sleep(1)
    system("xdg-open http://103.217.216.198:8001/#view")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="6":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0
    print(" Done")
    sleep(1)
    system("xdg-open http://103.217.216.197:8001/#view")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="7":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0
    print(" Done")
    sleep(1)
    system("xdg-open http://103.52.16.102:82/live/index.html?Language=0")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] ; ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="8":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0
    print(" Done")
    sleep(1)
    system("xdg-open http://202.52.50.183:8001/#view")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="9":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0
    print(" Done")
    sleep(1)
    system("xdg-open http://103.217.216.198:8000/#view")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="10":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0
    print(" Done")
    sleep(1)
    system("xdg-open http://103.4.206.135:83/ui3.html")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="11":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0 
    print(" Done")
    sleep(1)
    system("xdg-open http://119.252.169.189:84/")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="12":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1 
      if count == 3:
        count = 0 
    print(" Done")
    sleep(1)
    system("xdg-open http://103.119.145.26:8001/live/index.html?Language=0")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="13":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0
    print(" Done")
    sleep(1)
    system("xdg-open http://36.91.83.73:8081/")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="14":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0
    print(" Done")
    sleep(1)
    system("xdg-open http://119.252.169.189:85/")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="15":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0
    print(" Done")
    sleep(1)
    system("xdg-open http://103.245.19.243/live/index.html?Language=0")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="16":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0
    print(" Done")
    sleep(1)
    system("xdg-open http://103.4.206.135:83/ui3.html")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="17":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0
    print(" Done")
    sleep(1)
    system("xdg-open http://119.2.50.114:88/view/viewer_index.shtml?id=3941")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="18":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0
    print(" Done")
    sleep(1)
    system("xdg-open http://65.201.171.70/#view")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="19":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0
    print(" Done")
    sleep(1)
    system("xdg-open http://205.189.36.99:8082/control/userimage.html")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="20":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0
    print(" Done")
    sleep(1)
    system("xdg-open http://75.183.181.155/view/viewer_index.shtml?id=200")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="21":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0
    print(" Done")
    sleep(1)
    system("xdg-open http://12.34.170.21:8888/view/viewer_index.shtml?id=639")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="22":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0
    print(" Done")
    sleep(1)
    system("xdg-open http://128.104.206.15/view/viewer_index.shtml?id=131")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="23":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0
    print(" Done")
    sleep(1)
    system("xdg-open http://24.20.101.215:8000/view/viewer_index.shtml?id=44")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="24":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0
    print(" Done")
    sleep(1)
    system("xdg-open http://166.168.156.178:81/live/index.html?Language=0")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="25":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0
    print(" Done")
    sleep(1)
    system("xdg-open http://166.153.247.80:82/cgi-bin/guestimage.html")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="26":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0
    print(" Done")
    sleep(1)
    system("xdg-open http://75.112.32.101/view/viewer_index.shtml?id=1185")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="27":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0
    print(" Done")
    sleep(1)
    system("xdg-open http://166.247.40.1:82/#view")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="28":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0
    print(" Done")
    sleep(1)
    system("xdg-open http://67.204.149.29/control/userimage.html")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="29":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0
    print(" Done")
    sleep(1)
    system("xdg-open http://74.51.217.90:82/view/viewer_index.shtml?id=1968")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="30":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0
    print(" Done")
    sleep(1)
    system("xdg-open http://96.237.61.111:81/live/index.html?Language=0")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="31":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0
    print(" Done")
    sleep(1)
    system("xdg-open ")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="32":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0
    print(" Done")
    sleep(1)
    system("xdg-open http://50.248.29.158/view/viewer_index.shtml?id=1315")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="33":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0
    print(" Done")
    sleep(1)
    system("xdg-open http://152.26.8.85/view/index.shtml")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()
  if pil =="34":
    count = 0
    for t in range(101):
      sleep(0.050)
      print(f"\r    Loading...{t}%", end="", flush=True)
      count += 1
      if count == 3:
        count = 0
    print(" Done")
    sleep(1)
    system("xdg-open http://202.73.139.110:81/live/index.html?Language=1&ViewMode=pull")
    sleep(3)
    back = input("    Kembali ke menu awal [y/n] : ")
    if back =="y":
      sleep(1.5)
      system("clear")
      logo()
      tools()

tools()
