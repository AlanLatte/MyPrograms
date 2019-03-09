import re

regex = r">.*<"

test_str = ("<h1 class=\"release-title\" style=\"overflow: hidden; white-space: nowrap; text-overflow: ellipsis; margin-bottom: 0px;\">\n"
	"			Мастера Меча Онлайн: Алисизация / Sword Art Online: Alicization\n"
	"		</h1>")

matches = re.search(regex, test_str, re.DOTALL)

if matches:
    print ("Match was found at {start}-{end}: {match}".format(start = matches.start(), end = matches.end(), match = matches.group()))

    for groupNum in range(0, len(matches.groups())):
        groupNum = groupNum + 1

        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = matches.start(groupNum), end = matches.end(groupNum), group = matches.group(groupNum)))
