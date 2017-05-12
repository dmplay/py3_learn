# -*- coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.INFO)
import pdb

try:
    print('try...')
    logging.info('n =sdasdasd')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    logging.exception(e)
except ZeroDivisionError as e:
    logging.exception(e)
finally:
    print('finally...')
print('END')
