import re

regex = r"(?i)(\+|-|\/|&|\^|\|)|('[^']*')|(\'|\"|\*|;)|%\w{2}|(\([^']*\))|(\b(ALTER|CREATE *TABLE ('\w+')|DELETE|DROP *TABLE|EXEC|INSERT *INTO *('\w+')|MERGE|UPDATE *('\w+')|UNION *SELECT|SELECT *(ALL|\*) *FROM|SELECT *(\w+) *FROM|substring\(|information_schema|concat\(|sleep\(\d\)|BENCHMARK\())"

test_str = input("Введите строку: ")

matches = re.finditer(regex, test_str)

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
