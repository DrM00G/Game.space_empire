import os
import difflib
import filecmp

class Logger:

    def __init__(self, file_name,log_bool):
        self.log_bool=log_bool
        self.file_name = file_name
        self.logging_file = self.make_logging_file()

    def make_logging_file(self):
        return open(os.path.join('logs', self.file_name), 'a+')

    def log(self, string):
        if self.log_bool:
          self.logging_file.write(str(string) + '\n')

    def close_file(self):
        self.logging_file.close()
