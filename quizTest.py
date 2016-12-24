def score():
    _score = 0;

def points(_correct, _incorrect):
    if points == _correct:
        _score = score + 1;
        print("You now have %ipoints" % (_score));
    elif points == _incorrect:
        print("Incorrect")            
_score = 0;

index = ["What year was kennedy assassinated?...\na.1962\nb.1963\nc.1964\n", "What is the capital of Spain?..."];

_ans = str(input(index[0]));

if _ans == "b":
    points = _correct + 1;
else:
    points = _incorrect;
    

