s = input()

if s.find('-'):
    x = s.find('-')
    c = s[0:x]
    c = int(c)
    d = s[x+1:]
    d = int(d)
    print(c-d)

