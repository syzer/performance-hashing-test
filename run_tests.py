#!/usr/bin/python

import time
import hashlib
import csv
import timeit as t

def timeit(f):
    def timed(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        print 'func:%r took: %2.4f sec' % \
              (f.__name__, te-ts)
        return result

    return timed

@timeit
def test_md5(data):
    for line in data:
        hashlib.md5(line).hexdigest()

@timeit
def test_sha1(data):
    for line in data:
        hashlib.sha1(line).hexdigest()

@timeit
def test_sha256(data):
    for line in data:
        hashlib.sha256(line).hexdigest()

@timeit
def test_sha512(data):
    for line in data:
        hashlib.sha512(line).hexdigest()


data = []
f = open('bench.csv', 'r')
for l in f.readlines():
    data.append(l)
f.close()

# t.repeat('test_md5(data)', repeat=3, number=1000)
test_md5(data)
test_sha1(data)
test_sha256(data)
test_sha512(data)

