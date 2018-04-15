import re
#              арифметические операции тоже         вот тут пробелы можно убрать.
REGEX_FINAL = "(\+|-|\/|&|\^|%|\|)|('[^']*')|(\'|\"|\s|\*|;)|(%20|%27|%22|%3b|%2a)|(\([^']*\))|(\b(OR|AND|ALTER|CREATE|DELETE|DROP|EXEC|EXECUTE|INSERT|INTO|MERGE|SELECT|UPDATE|UNION|ALL|WHERE|SET|VALUE|value|set||where|or|and|alter|create|delete|drop|exec|execute|insert|into|merge|select|update|union|all|FROM|from%4f%52|%6f%72|%41%4e%44|%41%4c%54%45%52|%43%52%45%41%54%45|%44%45%4c%45%54%45|%44%52%4f%50|%45%58%45%43|%45%58%45%43%55%54%45|%49%4e%53%45%52%54|%49%4e%54%4f|%4d%45%52%47%45|%53%45%4c%45%43%54|%55%50%44%41%54%45|%55%4e%49%4f%4e|%41%4c%4c)\b)"

REGEX_FINAL_2 = "(?i)(\+|-|\/|&|\^|%|\|)|('[^']*')|(\'|\"|\*|;)|(%20|%27|%22|%3b|%2a)|(\([^']*\))|(\b(OR|AND|ALTER|CREATE|DELETE|DROP|EXEC|EXECUTE|INSERT|INTO|MERGE|SELECT|UPDATE|UNION|ALL|FROM|%4f%52|%6f%72|%41%4e%44|%41%4c%54%45%52|%43%52%45%41%54%45|%44%45%4c%45%54%45|%44%52%4f%50|%45%58%45%43|%45%58%45%43%55%54%45|%49%4e%53%45%52%54|%49%4e%54%4f|%4d%45%52%47%45|%53%45%4c%45%43%54|%55%50%44%41%54%45|%55%4e%49%4f%4e|%41%4c%4c)\b)"
REGEX_FINAL_3 = "(?i)(\+|-|\/|&|\^|%|\|)|('[^']*')|(\'|\"|\*|;)|(%20|%27|%22|%3b|%2a)|(\([^']*\))|(\b(OR|AND|ALTER|CREATE|DELETE|DROP|EXEC|EXECUTE|INSERT|INTO|MERGE|UPDATE|UNION|SELECT (ALL|\*) FROM|SELECT%20(ALL|\*)%20FROM|SELECT (\w+) FROM|SELECT%20(\w+)%20FROM|substring|information_schema|concat|sleep\(\d\)|BENCHMARK\(|%4f%52|%6f%72|%41%4e%44|%41%4c%54%45%52|%43%52%45%41%54%45|%44%45%4c%45%54%45|%44%52%4f%50|%45%58%45%43|%45%58%45%43%55%54%45|%49%4e%53%45%52%54|%49%4e%54%4f|%4d%45%52%47%45|%53%45%4c%45%43%54|%55%50%44%41%54%45|%55%4e%49%4f%4e|%41%4c%4c))"

REGEX_FINAL_4 = "(?i)(\+|-|\/|&|\^|\|)|('[^']*')|(\'|\"|\*|;)|%\w{2}|(\([^']*\))|(\b(OR|AND|ALTER|CREATE|DELETE|DROP|EXEC|EXECUTE|INSERT|INTO|MERGE|UPDATE|UNION|SELECT (ALL|\*) FROM|SELECT%20(ALL|\*)%20FROM|SELECT (\w+) FROM|SELECT%20(\w+)%20FROM|substring|information_schema|concat|sleep\(\d\)|BENCHMARK\())"

REGEX_FINAL_FINAL = "(?i)(\+|-|\/|&|\^|\|)|('[^']*')|(\'|\"|\*|;)|%\w{2}|(\([^']*\))|(\b(ALTER|CREATE TABLE ('\w+')|DELETE|DROP|EXEC|INSERT INTO ('\w+')|MERGE|UPDATE ('\w+')|UNION SELECT|SELECT (ALL|\*) FROM|SELECT (\w+) FROM|substring\(|information_schema|concat\(|sleep\(\d\)|BENCHMARK\())"

REGEX_FINAL_FINAL_FINAL = "(?i)(\+|-|\/|&|\^|\|)|('[^']*')|(\'|\"|\*|;)|%\w{2}|(\([^']*\))|(\b(ALTER|CREATE *TABLE ('\w+')|DELETE|DROP *TABLE|EXEC|INSERT *INTO *('\w+')|MERGE|UPDATE *('\w+')|UNION *SELECT|SELECT *(ALL|\*) *FROM|SELECT *(\w+) *FROM|substring\(|information_schema|concat\(|sleep\(\d\)|BENCHMARK\())"

REGEX = "(?i)(\b(OR|AND|ALTER|CREATE|DELETE|DROP|EXEC|EXECUTE|INSERT|INTO|MERGE|SELECT|UPDATE|UNION|ALL|or|and|alter|create|delete|drop|exec|execute|insert|into|merge|select|update|union|all|FROM|from|%4f%52|%6f%72|%41%4e%44|%41%4c%54%45%52|%43%52%45%41%54%45|%44%45%4c%45%54%45|%44%52%4f%50|%45%58%45%43|%45%58%45%43%55%54%45|%49%4e%53%45%52%54|%49%4e%54%4f|%4d%45%52%47%45|%53%45%4c%45%43%54|%55%50%44%41%54%45|%55%4e%49%4f%4e|%41%4c%4c)\b)"


pattern = re.compile(REGEX)

def filter(string,match,not_match):
    result = pattern.findall(string)
    print (result)
    return result

if __name__ == "__main__":
    match = 0
    not_match = 0
    string = ""
    while string != "quit":
        string = input("Введите строку:")
        result = filter(string,match,not_match)
        if len(result) == 0:
            not_match += 1
        else:
            match += len(result)
        print("Match: {}".format(match))
        print("Not match: {}".format(not_match))
    print("Used: " + REGEX)
