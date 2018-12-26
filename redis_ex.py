import redis
try:
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.set('d', 'k')
    r.set('a', 2)
    pipe = r.pipeline()
    r.set('b', 'b')
    r.set('c', '2')
    pipe.get('d')
    print(pipe.execute())
    print(r.get('b'))
except Exception as e:
    print("Can not connect redis", e)
