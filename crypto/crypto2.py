import requests

url = "http://10.10.12.10:1177/guess_bit?bit="
n = 60505224578178250268769149421209698338275029440510185120605407695789340818418756500300051727057652321576128268897484446630657037625231942113483187711696345851610894270061043856659436308377493678886935651866411097349641713647364701490384626467048846763824867759429900028769018175949357658454033517529351750853

flag = []
for i in range(134):
    element = ""
    for j in range(300):
        r = requests.get(f"{url}{i}")
        if r.json()["guess"] < n // 2:
            flag.append(1)
            # print(''.join(map(str, flag)))
            break
    else:
        # print(''.join(map(str, flag)))

        flag.append(0)

    td = hex(int("".join(map(str, flag)), 2))[2:]

    try:
        print(bytes.fromhex(td).decode("utf-8"))

    except:
        print(td)