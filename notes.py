def take_notes(val):
    note = open('notes.txt', 'a')
    note.write(val)
    note.write(" ")
    note.close()
    print('Notes taken sir')


def read_notes():
    note = open('notes.txt', 'r')
    data = note.read()
    note.close()
    if data != '':
        print(data)
        return data
    else:
        return 'Notes are empty'
