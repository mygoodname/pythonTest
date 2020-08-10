import os
import sys
import peewee
from peewee import *
import datetime

# db = MySQLDatabase("guest", host="127.0.0.1", port=3306, user="root", passwd="123456")
db = os.path.join(os.path.dirname(sys.argv[0]), 'mydata.db')
connect = peewee.SqliteDatabase(db)


class BaseModel(Model):
    class Meta:
        database = connect


class User(BaseModel):
    username = CharField(unique=True)


class Tweet(BaseModel):
    id = PrimaryKeyField()
    Title = CharField(max_length=255, null=False, default='书本')
    ExternalId = TextField(null=False, default='')
    contentId = BigIntegerField()
    effective_word = TextField(null=False, default='')
    invalid_word = TextField(null=False, default='')
    IsOnShelf = BooleanField()
    IsDeleted = BooleanField()
    IsPrivate = BooleanField()
    IsPublished = BooleanField()
    create_date = DateTimeField(null=False, default=datetime.datetime.now)
    update_date = DateTimeField(null=False, default=datetime.datetime.now)
    class Meta:
        table_alias = 'tweet'

    @staticmethod
    def insertModel(model):
        model_id = Tweet.insert(model).execute()
        return model_id

if __name__ == "__main__":
    # 创建表
    # User.create_table()  # 创建User表
    Tweet.create_table()  # 创建Tweet表
    Tweet.insert({'invalid_word': inva, 'effective_word': effective})
