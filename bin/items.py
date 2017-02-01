# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UserItem(scrapy.Item):
    # user information
    userFirstName = scrapy.Field()
    userBirthdayEpoch = scrapy.Field()
    userGender = scrapy.Field()
    userZodiac = scrapy.Field()
    userChineseZodiac = scrapy.Field()
    userHeight = scrapy.Field()
    userLocation = scrapy.Field()
    userCity = scrapy.Field()
    userState = scrapy.Field()
    userCountry = scrapy.Field()
    userLanguage = scrapy.Field()
    userEducation = scrapy.Field()
    userCollege = scrapy.Field()
    userGraduateSchool = scrapy.Field()
    userIncome = scrapy.Field()
    userCompany = scrapy.Field()
    userOccupation = scrapy.Field()
    userJobTitle = scrapy.Field()
    userMaritalStatus = scrapy.Field()
    userEthnicity = scrapy.Field()
    userBodyType = scrapy.Field()
    userBirthCountry = scrapy.Field()
    userHasChildren = scrapy.Field()
    userWillRelocate = scrapy.Field()
    userImmigration = scrapy.Field()
    userFirstArrive = scrapy.Field()
    userReligion = scrapy.Field()
    userSmoking = scrapy.Field()
    userDrinking = scrapy.Field()
    userInterest = scrapy.Field()
    userImageUrlOriginal = scrapy.Field()
    userAboutMe = scrapy.Field()
    userOpenAnswers = scrapy.Field()

    # target information
    targetGender = scrapy.Field()
    targetAgeMax = scrapy.Field()
    targetAgeMin = scrapy.Field()
    targetHeight = scrapy.Field()
    targetLocation = scrapy.Field()
    targetLanguage = scrapy.Field()
    targetEducation = scrapy.Field()
    targetIncome = scrapy.Field()
    targetOccupation = scrapy.Field()
    targetMaritalStatus = scrapy.Field()
    targetEthnicity = scrapy.Field()
    targetBodyType = scrapy.Field()
    targetBirthCountry = scrapy.Field()
    targetHasChildren = scrapy.Field()
    targetImmigration = scrapy.Field()
    targetReligion = scrapy.Field()
    targetSmoking = scrapy.Field()
    targetDrinking = scrapy.Field()

    pass
