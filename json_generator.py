FILE_PATH = 'json_text.txt'
NEW_FILE_NAME = 'formatted_json.json'

with open(FILE_PATH) as f1:
    with open(NEW_FILE_NAME, 'w') as f2:

        # format database
        f2.write('{\n')
        f2.write('\t"businesses": [\n')
        f2.write('\t\t{\n')

        # rewrite title
        line = f1.readline().split(':')[0] + ","
        f2.write(f'\t\t\t"name": {line}\n')

        # begin iterating
        curr = 1

        while curr < 13:

            # read line
            line = f1.readline()

            # format line
            line = line.replace('“', '"')
            line = line.replace('”', '"')
            line = line.replace('’', "'")
            if ('Policies' in line) or ('Delivery' in line) or ('Reservations' in line) or \
                ('Price Range' in line) or ('Discounts' in line):
                continue

            # write line
            line = '\t\t' + line
            f2.write(line)

            curr += 1

        f2.write('\t]\n}')
