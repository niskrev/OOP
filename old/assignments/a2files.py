import datetime

class WriteFile(object):

    def __init__(self, fname):
        self.fname = fname

    def write(self, text):
        with open(self.fname, 'a') as f:
            f.write(text + '\n')


class LogFile(WriteFile):

    def write(self, text):
        super(LogFile, self).write(self.add_time_to_text(text))

    @staticmethod
    def add_time_to_text(text):
        dt_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        return dt_str + ' ' + text


class DelimFile(WriteFile):

    def __init__(self, fname, delim):
        super(DelimFile, self).__init__(fname)
        self.delim = delim

    def write(self, text):
        super(DelimFile, self).write(self.get_line(self.delim, text))

    @staticmethod
    def get_line(delim, text):
        return delim.join(text)



# log = LogFile('log1.txt')
# log.write('this is a log message')
# log.write('this is another log message')
#
# c = DelimFile('text.csv', ',')
# c.write(['a', 'b', 'c', 'd'])
# c.write(['1', '2', '3', '4'])

