import time, random;

count = 0;
hand = 0;
_inp = "";

def deal():
    global count;
    global handCount;
    
    x = random.randint(0, 11);
    if x <= 0:
        handCount = 2;
        playerHandCount(handCount);
    elif x == 1:
        handCount = 3;
        playerHandCount(handCount);
    elif x == 2:
        handCount = 4;
        playerHandCount(handCount);
    elif x == 3:
        handCount = 5;
        playerHandCount(handCount);
    elif x == 4:
        handCount = 6;
        playerHandCount(handCount);
    elif x == 5:
        handCount = 7;
        playerHandCount(handCount);
    elif x == 6:
        handCount = 8;
        playerHandCount(handCount);
    value = _cards[x];
    y = random.randint(0, 3);
    suit = _suits[y];
    card = value, suit;
    playerHand.append(card);
    print("%s of %s" % (value, suit));
    count = count + 1;


def playerHandCount(handCount):
    global hand;
    hand += handCount;
    
    

def drawCard():
    global count;
    global handCount;
    
    x = random.randint(0, 11);
    if x <= 0:
        handCount = 2;
        playerHandCount(handCount);
    elif x == 1:
        handCount = 3;
        playerHandCount(handCount);
    elif x == 2:
        handCount = 4;
        playerHandCount(handCount);
    elif x == 3:
        handCount = 5;
        playerHandCount(handCount);
    elif x == 4:
        handCount = 6;
        playerHandCount(handCount);
    elif x == 5:
        handCount = 7;
        playerHandCount(handCount);
    elif x == 6:
        handCount = 8;
        playerHandCount(handCount);
    value = _cards[x];
    y = random.randint(0, 3);
    suit = _suits[y];
    card = value, suit;
    playerHand.append(card);
    
def command(_inp):
    _inp = str(input("Enter a command :"));
    return _inp

_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "Jack", "Queen", "King", "Ace"];
_suits = ["Clubs", "Spades", "Hearts", "Diamonds"];

playerHand = [];

while count < 2:
    deal();

print(hand);


