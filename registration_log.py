
class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def write_bad_log(the_line, Error, c):
    with open('registrations_bad.log', mode='a', encoding='utf8') as file:
        file.write(the_line[:-1] + ' - ' + Error + '   строка {}'.format(c) + '\n')


def write_good_log(the_line):
    with open('registrations_good.log', mode='a', encoding='utf8') as file:
        file.write(the_line)


def validation(the_line, c):
    list_of_str = the_line.split(' ')
    if len(list_of_str) != 3:
        try:
            raise ValueError
        except ValueError:
            write_bad_log(the_line, 'ValueError', c)
            return False

    elif list_of_str[0].isalpha() is False:
        try:
            raise NotNameError
        except NotNameError:
            write_bad_log(the_line, 'NotNameError', c)
            return False

    elif list_of_str[1].find('@') == -1 or list_of_str[1].find('.') == -1:
        try:
            raise NotEmailError
        except NotEmailError:
            write_bad_log(the_line, 'NotEmailError', c)
            return False

    elif int(list_of_str[2]) not in range(10, 100):
        try:
            raise ValueError
        except ValueError:
            write_bad_log(the_line, 'ValueError', c)
            return False
    else:
        return True


with open("registrations.txt", 'r', encoding='utf8') as file:
    c = 1
    for line in file:
        if validation(line, c) is not False:
            write_good_log(line)
        c += 1

