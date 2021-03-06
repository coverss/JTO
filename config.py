import os


class Config(object):
    SECRET_KEY = os.urandom(32)

    S3_BUCKET = os.environ.get("S3_BUCKET")
    S3_KEY = os.environ.get("S3_KEY")
    S3_SECRET = os.environ.get("S3_SECRET_ACCESS_KEY")
    S3_LOCATION = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)

#test new branch

class DevelopmentConfig(Config):
    TEMPLATES_AUTO_RELOAD = True
    POSTGRES = {
        'user': 'postgres',
        'pw': '1',
        'db': 'jto',
        'host': 'localhost',
        'port': '5432',
    }
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    POSTGRES = {
        'user': 'postgres',
        'pw': '!J.0.0.0',
        'db': 'jtodb',
        #'host': 'jto-instance.cwa9qfrslztl.us-west-2.rds.amazonaws.com',
        'host' : 'jtodb1.cdfuep09ddqw.us-east-1.rds.amazonaws.com',
        'port': '5432',
    }
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
