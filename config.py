class Config:
    SECRET_KEY = "2lpxt96qt@jl)3gr^gnejy#we-pstw%+l+74-dfgzr!a3c*6s%"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:123@192.168.99.100/jwt_users"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Dev(Config):
    Debug=True
    API_PREFIX='/api/v1'
    JWT_TOKEN_LOCATION='headers'

class Prod(Config):
    pass

class Test(Config):
    pass


config = {
    'dev': Dev,
    'prod': Prod
}