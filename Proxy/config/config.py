from configparser import ConfigParser
import os


class ConfigRead(object):

    def __init__(self, file):
        path = os.path.join(os.path.dirname(__file__)+file)
        self.conf = ConfigParser()
        self.conf.read(path)

    def getvalue(self, section, key):
        if self.conf.has_section(section):
            if self.conf.has_option(section=section, option=key):
                value = self.conf.get(section=section, option=key)
                return value

if __name__ == "__main__":

    cf = ConfigRead("/../config.ini")  # relative path compared with this file.
    name = cf.getvalue("DB", "DBNAME")
    collec = cf.getvalue("DB", "COLLECTION")
    print(name, collec)
