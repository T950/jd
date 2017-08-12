# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector

class GuxinlangPipeline(object):
    def process_item(self, item, spider):
        db=mysql.connector.connect(host='localhost',port=3306,user='root',password='123',db='gl')
        cursor=db.cursor()
        sql="insert into glx(a,b,c,d,e,f,g,h,i,j,k,l,m) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(item['a'],item['b'],item['c'],item['d'],item['e'],item['f'],item['g'],item['h'],item['i'],item['j'],item['k'],item['l'],item['m'])
        print(sql)
        cursor.execute(sql)
        db.commit()
        db.close()
        return item
