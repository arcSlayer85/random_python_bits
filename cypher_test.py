x = 0;
y = 0;

_wordList = [];

cypher = {};

encoded = [];

_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

_string = str(input('Enter a word : '));

_inp = _string.upper();

print(_inp);

while x != int(len(_inp)):
    for _letter in _inp:
        _wordList.append(_letter);
        x += 1;

print(_wordList);

for _char in _alpha:
    y += 1;
    cypher.update({str(_char) : int(y)});
    
for k,v in cypher.items():
    for i in _wordList:
        if i == k:
            print(v)
        
    
print(encoded);

print(cypher);

    

rev_List = _wordList[:: -1];


print(rev_List);


        
    
