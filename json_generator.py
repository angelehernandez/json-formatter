FILE_PATH = 'json_text.txt'

with open(FILE_PATH) as f:

    # begin reading lines
    # line = f.readline()
    curr = 0

    while curr < 3:

        # read line
        line = f.readline()
        print(f"Line {curr}: {line.strip()}")

        # format line
        line = line.replace('“', '"')
        line = line.replace('”', '"')

        # write line
        print(f"Line {curr}: {line.strip()}\n")

        curr += 1
