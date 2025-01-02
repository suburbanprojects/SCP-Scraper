from bs4 import BeautifulSoup, NavigableString, Tag
import requests, random, time

def getEntry():
    request = requests.get('https://scp-wiki.wikidot.com/scp-' + entryno)
    soup = BeautifulSoup(request.text, 'lxml')

    for header in soup.find_all('p'):
        nextNode = header
        #break loop if next sibling is header
        while True:
            nextNode = nextNode.nextSibling
            if nextNode is None:
                break
            if isinstance(nextNode, NavigableString):
                print(nextNode.strip())
            if isinstance(nextNode, Tag):
                if nextNode.name == "strong":
                    break
                print(nextNode.get_text(strip=True).strip())
                time.sleep(2.5) #pause 2.5 seconds
                break

def randomEntry():
    randent = random.randrange(0,9999) #I think there's this much entries?
    request = requests.get('https://scp-wiki.wikidot.com/scp-' + str(randent).zfill(3)) #add zeroes in front for entries 1 to 99

    soup = BeautifulSoup(request.text, 'lxml')
    for header in soup.find_all('p'):
        nextNode = header
        #break loop if next sibling is header
        while True:
            nextNode = nextNode.nextSibling
            if nextNode is None:
                break
            if isinstance(nextNode, NavigableString):
                print(nextNode.strip())
            if isinstance(nextNode, Tag):
                if nextNode.name == "strong":
                    break
                print(nextNode.get_text(strip=True).strip())
                time.sleep(2.5) #pause 2.5 seconds
                break

print("=======Select  function========")
print("|    1. (S)elect an Entry      |")
print("|    2. (R)andom Entry         |")
print("|    3. (Q)uit                 |")
print("="*31 )

while True:
    choice = input("Enter choice((S)elect/(R)andom/(Q)uit): ")

    if choice in ("s","S"): #just in case user keys in using lowercase
        entryno = input("SCP Entry Number: ").zfill(3)
        print(getEntry())

    if choice in ("r","R"):
        print(randomEntry())

    if choice in ("q","Q"):
        break
