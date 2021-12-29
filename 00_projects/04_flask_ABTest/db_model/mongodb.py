import pymongo

MONGO_HOST = 'localhost'

def conn_mongodb():
MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))
    try:
        MONGO_CONN.admin.command('ismaster')
        blog_ab = MONGO_CONN.blog_session_db.blog_ab
    except:
        MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))
        blog_ab = MONGO_CONN.blog_session_db.blog_ab

    return blog_ab
