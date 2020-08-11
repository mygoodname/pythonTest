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
    title = CharField(max_length=255, null=False, default='书本')
    contentId = BigIntegerField()
    externalId = TextField(null=False, default='')
    invalid_word = TextField(null=False, default='')
    effective_word = TextField(null=False, default='')
    removeDuplicate_invalid_word = TextField(null=False, default='')
    isOnShelf = BooleanField()
    isDeleted = BooleanField()
    isPrivate = BooleanField()
    isPublished = BooleanField()
    create_date = DateTimeField(null=False, default=datetime.datetime.now)
    update_date = DateTimeField(null=False, default=datetime.datetime.now)

    class Meta:
        table_alias = 'tweet'

    @staticmethod
    def insertModel(model):
        model_id = -1
        if 'contentId' in model.keys():
            tweet = Tweet.isInner(model['contentId'])
            if tweet:
                Tweet.updateArticle(model)
            else:
                model_id = Tweet.insert(model).execute()
        return model_id



    @staticmethod
    def selectByContentId(contentId):
        tweet = Tweet.select().where(Tweet.contentId == contentId).get()
        return tweet

    @staticmethod
    def isInner(contentId):
        tweet = Tweet.select().where(Tweet.contentId == contentId).dicts()
        if len(tweet) > 0:
            return True
        else:
            return False

    @staticmethod
    def updateArticle(dic):
        if 'contentId' in dic.keys() and Tweet.isInner(dic['contentId']):
            tweet = Tweet.selectByContentId(dic['contentId'])
            tweet.update_date = datetime.datetime.now()
            if 'invalid_word' in dic.keys():
                tweet.invalid_word = dic['invalid_word']
            if 'effective_word' in dic.keys():
                tweet.effective_word = dic['effective_word']
            if 'removeDuplicate_invalid_word' in dic.keys():
                tweet.removeDuplicate_invalid_word = dic['removeDuplicate_invalid_word']
            tweet.save()

    @staticmethod
    def delete_by_contentId(contentId):
        if Tweet.isInner(contentId):
            tweet = Tweet.selectByContentId(contentId)
            tweet.delete_instance()


if __name__ == "__main__":
    # 创建表
    # User.create_table()  # 创建User表
    # Tweet.create_table()  # 创建Tweet表
    # Tweet.insertModel(
    #     {'title': '我好', 'contentId': '20435', "externalId": "P00001-01-978-7-121-32708-7-Epub", 'invalid_word': '20435',
    #      'effective_word': '1232134123432', 'isOnShelf': True, 'isDeleted': False, 'isPrivate': True, 'isPublished': True})
    # Tweet.updateArticle(
    #     {'contentId': '20435','invalid_word': '修改20431', 'effective_word': 'dadfc', 'removeDuplicate_invalid_word': 'ajdlkfjalkdjflkdjdafj'})
    Tweet.delete_by_contentId(20430)
