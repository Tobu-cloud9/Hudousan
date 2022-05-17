# coding=utf-8
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HudousanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    url = scrapy.Field()
    # //基本情報//
    link = scrapy.Field()  # URL
    image = scrapy.Field()  # 画像
    price = scrapy.Field()  # 賃料
    operation = scrapy.Field()  # 管理費
    deposit = scrapy.Field()  # 保証金
    reward = scrapy.Field()  # 礼金
    renewal = scrapy.Field()  # 更新料
    layout = scrapy.Field()  # 間取り
    age = scrapy.Field()  # 築年数
    # //所在地・地図//
    location = scrapy.Field()  # 場所
    space = scrapy.Field()  # 建築面積
    access = scrapy.Field()  # アクセス
    # //中古住宅の物件概要//
    water = scrapy.Field()  # 水道料金
    parking = scrapy.Field()  # 2台無料
    window = scrapy.Field()  # 総戸数
    available = scrapy.Field()  # 入居・利用可能日
    now = scrapy.Field()  # 現状
    term = scrapy.Field()  # 契約期間
    expenses = scrapy.Field()  # 区費及び町内会費
    construction = scrapy.Field()  # 建築構造
    contract = scrapy.Field()  # 契約形態
    transaction = scrapy.Field()  # 取引形態
    # //特徴・設備//
    waterworks = scrapy.Field()  # 上水道
    sewage = scrapy.Field()  # 下水道
    waterline = scrapy.Field()  # 水道種別
    electrical = scrapy.Field()  # 電力会社
    supply = scrapy.Field()  # 給油
    toilet = scrapy.Field()  # トイレ
    bath = scrapy.Field()  # バス
    aircon = scrapy.Field()  # エアコン
    dehumidifier = scrapy.Field()  # 浴室乾燥機
    shower = scrapy.Field()  # シャワー
    BS = scrapy.Field()  # BSアンテナ
    land = scrapy.Field()  # 地目
