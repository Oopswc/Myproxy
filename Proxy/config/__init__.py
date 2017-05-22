from Proxy.config.config import ConfigRead

cf = ConfigRead("/../config.ini")  # relative path compared with this file.

# DB information

DBNAME = cf.getvalue("DB", "DBNAME")
COLLECTION = cf.getvalue("DB", "COLLECTION")

# Log level
CRITICAL = int(cf.getvalue("LOG", "CRITICAL"))
FATAL = int(cf.getvalue("LOG", "FATAL"))
ERROR = int(cf.getvalue("LOG", "ERROR"))
WARNING = int(cf.getvalue("LOG", "WARNING"))
WARN = int(cf.getvalue("LOG", "WARN"))
INFO = int(cf.getvalue("LOG", "INFO"))
DEBUG = int(cf.getvalue("LOG", "DEBUG"))
NOTSET = int(cf.getvalue("LOG", "NOTSET"))

# test url
URL = cf.getvalue("TEST_URL", "URL")


#headers
ACCEPTENCODING = cf.getvalue("HEADER", "ACCEPTENCODING")
COOKIE = cf.getvalue("HEADER", "COOKIE")
USERAGENT = cf.getvalue("HEADER", "USERAGENT")
HOSTKUAI = cf.getvalue("HEADER", "HOSTKUAI")
HOSTXICI = cf.getvalue("HEADER", "HOSTXICI")
HOSTYOU =  cf.getvalue("HEADER", "HOSTYOU")
