import argparse
import wget
import urllib

print("Checking for updates...")
url = "https://raw.githubusercontent.com/BritishGeekGuy/GetMyApp-CLI/main/version.txt"
file = urllib.request.urlopen(url)
for line in file:
    decoded_line = line.decode("utf-8")
    Float = float(decoded_line)  

    if Float > 0.2:
        print("Update Found, Downloading...")

parser = argparse.ArgumentParser(
    description='GetMyApp-CLI is a Command Line Application to install programs'
)

parser.add_argument('-i', '--install', metavar='install', required=True, help='Find and Install Application from Database')
parser.add_argument('-s', '--source', metavar='source', required=False, help='Download Source Code of a Application to your Documents (If the creator posted it)')
parser.add_argument('-u', '--uninstall', metavar='uninstall', required=False, help='Find and Uninstall Application from your Computer')

args = parser.parse_args()

print(args.install)
if args.install:
    print("Welcome to GetMyApp-CLI 0.1")
    wget.download("https://github.com/BritishGeekGuy/GetMyApp-CLI/raw/packages/SavingsCalc.zip")
elif args.source:
    wget.download("https://github.com/BritishGeekGuy/GetMyApp-CLI/raw/source/DesktopNotiTest.zip")