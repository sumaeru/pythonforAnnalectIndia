#https://realpython.com/python-logging/ have a look at this website.

import logging

#logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')