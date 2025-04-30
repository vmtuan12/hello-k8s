import os
from time import sleep

env = os.environ

print("title", env['title'])
print("auth", env['auth'])
print("publish_date", env['publish_date'])

sleep(10000000)
