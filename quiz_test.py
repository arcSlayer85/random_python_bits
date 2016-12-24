score = 0;

_ans1 = int(input("What is 2+2?"));

if _ans1 == 4:
    score = score + 1;
    print ("Correct, you have %i point\s..." % (score));
else:
    print ("Incorrect");
    
_ans2 = str(input("What is the capital of Spain?"));

if _ans2 == "Madrid":
    score = score + 1;
    print ("Correct, you have %i point\s..." % (score));
else:
    print ("Incorrect");

_ans3 = int(input("What year was JFK assassinated?"));

if _ans3 == 1963:
    score = score + 1;
    print ("Correct, you have %i point\s..." % (score));
else:
    print ("Incorrect");

_ans4 = str(input("What is 31 in binary?"));

if _ans4 == "00011111":
    score = score + 1;
    print ("Correct, you have %i point\s..." % (score));
else:
    print ("Incorrect");

_ans5 = str(input("Who was the second man on the moon?"));

if _ans5 == "Buzz Aldrin":
    score = score + 1;
    print ("Correct, you have %i point\s..." % (score));
else:
    print ("Incorrect");

_ans6 = str(input("Name the guitar player from Cream..."));

if _ans6 == "Eric Clapton":
    score = score + 1;
    print ("Correct, you have %i point\s..." % (score));
else:
    print ("Incorrect");

print ("Your total score is %ipoint\s out of 6 , Well Done!!" % (score))
