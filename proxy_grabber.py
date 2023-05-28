import requests
import sys
import time
import os
import socket

links = [
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangPreoxy/https/https.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt",
    "https://raw.githubusercontent.com/UptimerBot/proxy-list/master/proxies/http.txt",
    "https://api.proxyscrape.com/?request=displayproxies&proxytype=http",
    "https://raw.githubusercontent.com/JadaDev/proxylist/main/http-https.txt",
    "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/caliphdev/Proxy-List/master/http.txt",
    "https://raw.githubusercontent.com/officiaalputuid/KangProxy/KangProxy/httpes/https.txt",
    "https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/parserpp/ip_ports/main/proxyinfo.txt",
    "https://raw.githubusercontent.com/zuoxiaolei/proxys/main/proxys/proxys.txt",
    "https://www.proxy-list.download/api/v1/get?type=http",
    "https://raw.githubusercontent.com/fahimscirex/proxybd/master/proxylist/http.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/https.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
]

output_file = "proxy.txt"
interval = 3600  # 1 hour in seconds

def is_valid_proxy(line):
    parts = line.strip().split(':')
    if len(parts) != 2:
        return False
    ip, port = parts
    if not ip or not port:
        return False
    if not ip.isdigit():
        try:
            socket.gethostbyname(ip)
        except socket.error:
            return False
    if not port.isdigit():
        return False
    return True

def grab_text_from_link(link):
    try:
        response = requests.get(link.strip()) 
        if response.status_code == 200:
            return response.text
        else:
            print(f"Error grabbing link: {link}")
            print(f"Error details: Status Code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error grabbing link: {link}")
        print(f"Error details: {e}")
    return None

def update_output_file(text):
    with open(output_file, "w") as file:
        file.write(text)

def remove_empty_lines():
    with open(output_file, "r+") as file:
        lines = file.readlines()
        file.seek(0)
        file.writelines(line for line in lines if line.strip())
        file.truncate()

def remove_duplicates():
    with open(output_file, "r+") as file:
        lines = file.readlines()
        unique_lines = list(set(lines))
        duplicate_count = len(lines) - len(unique_lines)
        file.seek(0)
        file.writelines(unique_lines)
        file.truncate()
        return duplicate_count

def process_links():
    total_links = len(links)
    proxies_added = 0
    duplicates_removed = 0
    for index, link in enumerate(links, start=1):
        print(f"Grabbing Proxies from Link {index}/{total_links}")
        grabbed_text = grab_text_from_link(link)
        if grabbed_text:
            lines = grabbed_text.strip().split('\n')
            valid_lines = [line for line in lines if is_valid_proxy(line)]
            with open(output_file, "a") as file:
                file.write('\n'.join(valid_lines) + "\n")
            proxies_added += len(valid_lines)
            print("Link Grabbed successfully!")
            print(f"Proxies Added: {len(valid_lines)}")
        else:
            print("Failed to grab link.")
        print()
        sys.stdout.flush()  # Flush the output to force immediate printing
        time.sleep(2)

    remove_empty_lines()
    print("Proxies Added Successfully!")
    sys.stdout.flush()  # Flush the output to force immediate printing

    duplicates_removed = remove_duplicates()
    print(f"Duplicates Removed: {duplicates_removed}")
    print(f"Total Proxies Added: {proxies_added}")
    sys.stdout.flush()  # Flush the output to force immediate printing

def run_once():
    if os.path.exists(output_file):
        os.remove(output_file)
    process_links()
    sys.exit(0)

if len(sys.argv) > 1 and sys.argv[1] == "now":
    run_once()
else:
    if os.path.exists(output_file):
        os.remove(output_file)
    while True:
        process_links()
        time.sleep(interval)