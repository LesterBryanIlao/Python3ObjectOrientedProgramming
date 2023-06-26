import re
import sys


def match_regex(filename, regex):
    with open(filename) as file:
        lines = file.readlines()
    for line in reversed(lines):
        match = re.match(regex, line)
        if match:
            regex = yield match.groups()[0]


def get_serials(filename):
    ERROR_RE = "XFS ERROR (\[sd[a-z]\])"
    matcher = match_regex(filename, ERROR_RE)
    device = next(matcher)
    while True:
        try:
            bus = matcher.send(
                "(sd \S+) {}.*".format(re.escape(device)))
            serial = matcher.send("{} \(SERIAL=([^)]*)\)".format(bus))
            yield serial
            device = matcher.send(ERROR_RE)
        except StopIteration:
            matcher.close()
            return


# get file name from input command line
file = sys.argv[1]
for serial_number in get_serials(file):
    print(serial_number)
