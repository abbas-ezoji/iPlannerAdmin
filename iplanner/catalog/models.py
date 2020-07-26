import math
from django.db import models


class AspNetRoles(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=450)
    name = models.CharField(db_column='Name', max_length=256, blank=True, null=True)
    normalized_name = models.CharField(db_column='NormalizedName', unique=True, max_length=256, blank=True, null=True)
    concurrency_stamp = models.TextField(db_column='ConcurrencyStamp', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'AspNetRoles'


class AspNetRoleClaims(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    role = models.ForeignKey(AspNetRoles, models.DO_NOTHING, db_column='RoleId')
    claim_type = models.TextField(db_column='ClaimType', blank=True, null=True)
    claim_value = models.TextField(db_column='ClaimValue', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'AspNetRoleClaims'


class AspNetUsers(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=450)
    user_name = models.CharField(db_column='UserName', max_length=256, blank=True, null=True)
    normalized_user_name = models.CharField(db_column='NormalizedUserName', unique=True, max_length=256, blank=True,
                                            null=True)
    email = models.CharField(db_column='Email', max_length=256, blank=True, null=True)
    normalized_email = models.CharField(db_column='NormalizedEmail', max_length=256, blank=True, null=True)
    email_confirmed = models.BooleanField(db_column='EmailConfirmed')
    password_hash = models.TextField(db_column='PasswordHash', blank=True, null=True)
    security_stamp = models.TextField(db_column='SecurityStamp', blank=True, null=True)
    concurrency_stamp = models.TextField(db_column='ConcurrencyStamp', blank=True, null=True)
    phone_number = models.TextField(db_column='PhoneNumber', blank=True, null=True)
    phone_number_confirmed = models.BooleanField(db_column='PhoneNumberConfirmed')
    two_factor_enabled = models.BooleanField(db_column='TwoFactorEnabled')
    lockout_end = models.TextField(db_column='LockoutEnd', blank=True, null=True)
    lockout_enabled = models.BooleanField(db_column='LockoutEnabled')
    access_failed_count = models.IntegerField(db_column='AccessFailedCount')

    class Meta:
        managed = True
        db_table = 'AspNetUsers'


class AspNetUserClaims(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    user = models.ForeignKey(AspNetUsers, on_delete=models.PROTECT, db_column='UserId')
    claim_type = models.TextField(db_column='ClaimType', blank=True, null=True)
    claim_value = models.TextField(db_column='ClaimValue', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'AspNetUserClaims'


class AspNetUserLogins(models.Model):
    login_provider = models.CharField(db_column='LoginProvider', primary_key=True, max_length=128)
    provider_key = models.CharField(db_column='ProviderKey', max_length=128)
    provider_display_name = models.TextField(db_column='ProviderDisplayName', blank=True, null=True)
    user = models.ForeignKey(AspNetUsers, on_delete=models.PROTECT, db_column='UserId')

    class Meta:
        managed = True
        db_table = 'AspNetUserLogins'
        # unique_together = (('loginprovider', 'providerkey'),)


class AspNetUserRoles(models.Model):
    user = models.ForeignKey('Aspnetusers', on_delete=models.PROTECT, db_column='UserId', primary_key=True)
    role = models.ForeignKey(AspNetRoles, on_delete=models.PROTECT, db_column='RoleId')

    class Meta:
        managed = True
        db_table = 'AspNetUserRoles'
        # unique_together = (('userid', 'roleid'),)


class AspNetUserTokens(models.Model):
    user = models.ForeignKey(AspNetUsers, on_delete=models.PROTECT, db_column='UserId', primary_key=True)
    login_provider = models.CharField(db_column='LoginProvider', max_length=128)
    name = models.CharField(db_column='Name', max_length=128)
    value = models.TextField(db_column='Value', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'AspNetUserTokens'
        # unique_together = (('userid', 'loginprovider', 'name'),)


class EFMigrationsHistory(models.Model):
    MigrationId = models.CharField(db_column='UserId', max_length=150, primary_key=True)
    ProductVersion = models.CharField(db_column='ProductVersion', max_length=32)

    class Meta:
        managed = True
        db_table = '__EFMigrationsHistory'


class Contact(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    lang = models.SmallIntegerField(db_column='Lang')
    title = models.CharField(db_column='Title', max_length=128)
    description = models.CharField(db_column='Description', max_length=512)
    value = models.CharField(db_column='Value', max_length=64)
    contacttypecode = models.SmallIntegerField(db_column='ContactTypeCode')

    class Meta:
        managed = True
        db_table = 'Contact'


class EmergencyNeeds(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    lang = models.SmallIntegerField(db_column='Lang')
    title = models.CharField(db_column='Title', max_length=64)
    description = models.CharField(db_column='Description', max_length=1024)

    class Meta:
        managed = True
        db_table = 'EmergencyNeeds'


class WhyUs(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    lang = models.SmallIntegerField(db_column='Lang')
    title = models.CharField(db_column='Title', max_length=64)
    description = models.CharField(db_column='Description', max_length=512)

    class Meta:
        managed = True
        db_table = ' WhyUs'


class WhyUsDetail(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    lang = models.SmallIntegerField(db_column='Lang')
    why_us = models.ForeignKey(WhyUs, models.CASCADE, db_column='WhyUsId')
    title = models.CharField(db_column='Title', max_length=64)
    description = models.CharField(db_column='Description', max_length=512)

    class Meta:
        managed = True
        db_table = 'WhyUsDetail'


class About(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    lang = models.SmallIntegerField(db_column='Lang')
    title = models.CharField(db_column='Title', max_length=64)
    description = models.TextField(db_column='Description')

    class Meta:
        managed = True
        db_table = 'About'


class AirportType(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    lang = models.SmallIntegerField(db_column='Lang')
    title = models.CharField(db_column='Title', max_length=32)
    active = models.BooleanField(db_column='Active')

    class Meta:
        managed = True
        db_table = 'AirportType'


class Country(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    lang = models.SmallIntegerField(db_column='Lang')
    name = models.CharField(db_column='Name', max_length=32)
    english_name = models.CharField(db_column='EnglishName', max_length=32)
    lat = models.FloatField(db_column='Lat')
    long = models.FloatField(db_column='Long')
    border = models.TextField(db_column='Border', blank=True, null=True)
    code = models.CharField(db_column='Code', max_length=4, blank=True, null=True)
    description = models.CharField(db_column='Description', max_length=512, blank=True, null=True)
    when_to_visit = models.CharField(db_column='WhenToVisit', max_length=512, blank=True, null=True)
    iso3 = models.CharField(db_column='Iso3', max_length=4, blank=True, null=True)
    external_id = models.CharField(db_column='ExternalId', max_length=36, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Country'
        verbose_name_plural = '0_Country'

    def __str__(self):
        return self.name


class Province(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    lang = models.SmallIntegerField(db_column='Lang')
    country = models.ForeignKey(Country, on_delete=models.PROTECT, db_column='CountryId')
    name = models.CharField(db_column='Name', max_length=32)
    english_name = models.CharField(db_column='EnglishName', max_length=32)
    code = models.CharField(db_column='Code', max_length=4, blank=True, null=True)
    description = models.CharField(db_column='Description', max_length=512, blank=True, null=True)
    when_to_visit = models.CharField(db_column='WhenToVisit', max_length=512, blank=True, null=True)
    lat = models.FloatField(db_column='Lat')
    long = models.FloatField(db_column='Long')
    border = models.TextField(db_column='Border', blank=True, null=True)
    external_id = models.CharField(db_column='ExternalId', max_length=36, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Province'
        verbose_name_plural = '0_Province'

    def __str__(self):
        return self.name


class City(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    lang = models.SmallIntegerField(db_column='Lang')
    province = models.ForeignKey(Province, on_delete=models.PROTECT, db_column='ProvinceId')
    name = models.CharField(db_column='Name', max_length=32)
    english_name = models.CharField(db_column='EnglishName', max_length=32)
    code = models.CharField(db_column='Code', max_length=4, blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)
    when_to_visit = models.CharField(db_column='WhenToVisit', max_length=512, blank=True, null=True)
    lat = models.FloatField(db_column='Lat')
    long = models.FloatField(db_column='Long')
    border = models.TextField(db_column='Border', blank=True, null=True)
    external_id = models.CharField(db_column='ExternalId', max_length=36, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'City'
        verbose_name_plural = '0_City'

    def __str__(self):
        return self.name


class Department(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    lang = models.SmallIntegerField(db_column='Lang')
    title = models.TextField(db_column='Title', blank=True, null=True)
    comment = models.TextField(db_column='Comment', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Department'
        verbose_name_plural = '1_Department'

    def __str__(self):
        return self.title


class Category(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    lang = models.SmallIntegerField(db_column='Lang')
    department = models.ForeignKey(Department, on_delete=models.PROTECT, db_column='DepartmentId')
    title = models.TextField(db_column='Title', blank=True, null=True)
    comment = models.TextField(db_column='Comment', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Category'
        verbose_name_plural = '1_Category'

    def __str__(self):
        return self.department.title + ' - ' + self.title


class SubCategory(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    lang = models.SmallIntegerField(db_column='Lang')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, db_column='CategoryId')
    title = models.TextField(db_column='Title', blank=True, null=True)
    comment = models.TextField(db_column='Comment', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'SubCategory'
        verbose_name_plural = '1_Sub Category'

    def __str__(self):
        return self.category.department.title + ' - ' + self.category.title + ' - ' + self.title


class User(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    show_on_boarding = models.BooleanField(db_column='ShowOnBoarding')
    open_id = models.CharField(db_column='OpenId', max_length=36, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'User'
        verbose_name_plural = '2_Customer'

    def __str__(self):
        return self.id


class UserCity(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, db_column='UserId')
    city = models.ForeignKey(City, on_delete=models.PROTECT, db_column='CityId')
    created_date = models.DateTimeField(db_column='CreatedDate')

    class Meta:
        managed = True
        db_table = 'UserCity'
        verbose_name_plural = '2_Customer City'

    def __str__(self):
        return str(self.user.id) + ' - ' + self.city.name


class UserNickName(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, db_column='UserId')
    nick_name = models.CharField(db_column='NickName', max_length=16, blank=True, null=True)
    created_date = models.DateTimeField(db_column='CreatedDate')

    class Meta:
        managed = True
        db_table = 'UserNickName'


class OnBoardingQuestion(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    lang = models.SmallIntegerField(db_column='Lang')
    title = models.CharField(db_column='Title', max_length=128, blank=True, null=True)
    order_index = models.SmallIntegerField(db_column='OrderIndex')
    anwer_type_code = models.SmallIntegerField(db_column='AnwerTypeCode')
    can_be_skiped = models.BooleanField(db_column='CanBeSkiped')
    active = models.BooleanField(db_column='Active')

    class Meta:
        managed = True
        db_table = 'OnBoardingQuestion'
        verbose_name_plural = '3_OnBoarding Question'

    def __str__(self):
        return self.title


class Onboardingquestionanswer(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    lang = models.SmallIntegerField(db_column='Lang')
    onboarding_question = models.ForeignKey(OnBoardingQuestion, on_delete=models.PROTECT,
                                            db_column='OnBoardingQuestionId')
    title = models.CharField(db_column='Title', max_length=36, blank=True, null=True)
    icon = models.BinaryField(db_column='Icon', blank=True, null=True)
    active = models.BooleanField(db_column='Active')

    class Meta:
        managed = True
        db_table = 'OnBoardingQuestionAnswer'
        verbose_name_plural = '3_Onboarding question answer'

    def __str__(self):
        return self.title


class Privacy(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    lang = models.SmallIntegerField(db_column='Lang')
    title = models.CharField(db_column='Title', max_length=64)
    description = models.TextField(db_column='Description')

    class Meta:
        managed = True
        db_table = 'Privacy'


class UserOnBoardingQuestionAnswer(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, db_column='UserId')
    onboarding_question = models.ForeignKey(OnBoardingQuestion, on_delete=models.PROTECT,
                                            db_column='OnBoardingQuestionId')
    onboarding_question_answer = models.ForeignKey(Onboardingquestionanswer, on_delete=models.PROTECT,
                                                   db_column='OnBoardingQuestionAnswerId', blank=True, null=True)
    skiped = models.BooleanField(db_column='Skiped')
    onboarding_question_index = models.IntegerField(db_column='OnBoardingQuestionIndex')
    created_date = models.DateTimeField(db_column='CreatedDate')
    deleted = models.BooleanField(db_column='Deleted')

    class Meta:
        managed = True
        db_table = 'UserOnBoardingQuestionAnswer'


class UserOnBoardingStatus(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, db_column='UserId')
    onboarding_status_code = models.SmallIntegerField(db_column='OnBoardingStatusCode')
    skiped = models.BooleanField(db_column='Skiped')
    created_date = models.DateTimeField(db_column='CreatedDate')

    class Meta:
        managed = True
        db_table = 'UserOnBoardingStatus'


class ComplaintCategory(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    lang = models.SmallIntegerField(db_column='Lang')
    title = models.CharField(db_column='Title', max_length=64)
    active = models.BooleanField(db_column='Active')

    class Meta:
        managed = True
        db_table = 'ComplaintCategory'


class Complaint(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    lang = models.SmallIntegerField(db_column='Lang')
    complaint_category = models.ForeignKey(ComplaintCategory, on_delete=models.PROTECT, db_column='ComplaintCategoryId')
    title = models.CharField(db_column='Title', max_length=64)
    body = models.CharField(db_column='Body', max_length=256)
    email = models.CharField(db_column='Email', max_length=32)
    tel = models.CharField(db_column='Tel', max_length=16)

    class Meta:
        managed = True
        db_table = 'Complaint'


class Airport(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    lang = models.SmallIntegerField(db_column='Lang')
    airport_type = models.ForeignKey(AirportType, on_delete=models.PROTECT, db_column='AirportTypeId',
                                     blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT, db_column='CityId', blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT, db_column='SubCategoryId',
                                    blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=32)
    english_name = models.CharField(db_column='EnglishName', max_length=32, blank=True, null=True)
    icao = models.CharField(db_column='Icao', max_length=8, blank=True, null=True)
    iata = models.CharField(db_column='Iata', max_length=8, blank=True, null=True)
    url = models.CharField(db_column='Url', max_length=64, blank=True, null=True)
    area_code = models.CharField(db_column='AreaCode', max_length=4, blank=True, null=True)
    active = models.BooleanField(db_column='Active')
    external_id = models.TextField(db_column='ExternalId', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Airport'


class TagCategory(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    lang = models.SmallIntegerField(db_column='Lang')
    title = models.CharField(db_column='Title', max_length=32)
    active = models.BooleanField(db_column='Active')
    external_id = models.TextField(db_column='ExternalId', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TagCategory'


class Tag(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    lang = models.SmallIntegerField(db_column='Lang')
    category = models.ForeignKey(TagCategory, on_delete=models.PROTECT, db_column='CategoryId', null=True, blank=True)
    title = models.CharField(db_column='Title', max_length=32)
    active = models.BooleanField(db_column='Active')

    class Meta:
        managed = True
        db_table = 'Tag'

    def __str__(self):
        return self.title


class Attraction(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    type = models.IntegerField('Attraction Type', db_column='AttractionType', default=0)
    lang = models.SmallIntegerField(db_column='Lang')
    tag = models.ManyToManyField(Tag, db_table='AttractionTag', blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT, db_column='CityId', blank=True, null=True)
    title = models.CharField(db_column='Title', max_length=32)
    full_title = models.CharField(db_column='FullTitle', max_length=500, blank=True, null=True)
    english_title = models.CharField(db_column='EnglishTitle', max_length=32, blank=True, null=True)
    address = models.TextField(db_column='Address', blank=True, null=True)
    cost = models.CharField(db_column='Cost', max_length=32, blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)
    when_to_visit = models.CharField(db_column='WhenToVisit', max_length=512, blank=True, null=True)
    lat = models.FloatField(db_column='Lat', blank=True, null=True)
    long = models.FloatField(db_column='Long', blank=True, null=True)
    point = models.TextField(db_column='Point', blank=True, null=True)
    visit_duration = models.IntegerField(db_column='VisitDuration', blank=True, null=True)
    visit_time_from = models.IntegerField(db_column='VisitTimeFrom', blank=True, null=True)
    visit_time_to = models.IntegerField(db_column='VisitTimeTo', blank=True, null=True)
    can_visit = models.BooleanField(db_column='CanVisit', blank=True, null=True)
    rate = models.FloatField(db_column='Rate', blank=True, null=True)
    iplanner_rate = models.FloatField(db_column='iPlannerRate', blank=True, null=True)
    user_rate = models.FloatField(db_column='UserRate', blank=True, null=True)
    external_id = models.TextField(db_column='ExternalId', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Attraction'

    def __str__(self):
        return self.title


class AttractionCustoms(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    attraction = models.ForeignKey(Attraction, on_delete=models.PROTECT, db_column='AttractionId')
    description = models.TextField(db_column='Description', blank=True, null=True)
    like = models.IntegerField(db_column='Like')
    dislike = models.IntegerField(db_column='Dislike')

    class Meta:
        managed = True
        db_table = 'AttractionCustoms'


class AttractionCustomsReaction(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    attraction_customs = models.ForeignKey(AttractionCustoms, on_delete=models.PROTECT, db_column='AttractionCustomsId')
    user = models.ForeignKey(User, on_delete=models.PROTECT, db_column='UserId')
    created_date = models.DateTimeField(db_column='CreatedDate')
    user_react_type_code = models.IntegerField(db_column='UserReactTypeCode')

    class Meta:
        managed = True
        db_table = 'AttractionCustomsReaction'


class Travel(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, db_column='UserId')
    title = models.IntegerField(db_column='Title')
    travel_status_type_code = models.IntegerField(db_column='TravelStatusTypeCode')

    class Meta:
        managed = True
        db_table = 'Travel'


class TravelCity(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    travel = models.ForeignKey(Travel, on_delete=models.PROTECT, db_column='TravelId')
    city = models.ForeignKey(City, on_delete=models.PROTECT, db_column='CityId')
    start_date = models.DateTimeField(db_column='StartDate')
    end_date = models.DateTimeField(db_column='EndDate')
    deleted = models.BooleanField(db_column='Deleted')

    class Meta:
        managed = True
        db_table = 'TravelCity'


class TravelCityPlan(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    travel_city = models.ForeignKey(TravelCity, on_delete=models.PROTECT, db_column='TravelCityId')
    plan = models.IntegerField(db_column='PlanId')
    created_date = models.DateTimeField(db_column='CreatedDate')
    deleted = models.BooleanField(db_column='Deleted')

    class Meta:
        managed = True
        db_table = 'TravelCityPlan'


class TravelKnowledge(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    lang = models.SmallIntegerField(db_column='Lang')
    reference_id = models.IntegerField(db_column='ReferenceId')
    entity_type_code = models.IntegerField(db_column='EntityTypeCode')
    title = models.CharField(db_column='Title', max_length=64)
    description = models.CharField(db_column='Description', max_length=1024)

    class Meta:
        managed = True
        db_table = 'TravelKnowledge'


class TravelTodo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    travel = models.ForeignKey(Travel, on_delete=models.PROTECT, db_column='TravelId')
    title = models.TextField(db_column='Title', blank=True, null=True)
    remind_me = models.BooleanField(db_column='RemindMe')
    remind_time = models.DateTimeField(db_column='RemindTime')
    done = models.BooleanField(db_column='Done')

    class Meta:
        managed = True
        db_table = 'TravelTodo'


class Travelogue(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    lang = models.SmallIntegerField(db_column='Lang')
    title = models.CharField(db_column='Title', max_length=64)
    description = models.TextField(db_column='Description')
    user = models.ForeignKey(User, on_delete=models.PROTECT, db_column='UserId')
    created_date = models.DateTimeField(db_column='CreatedDate')
    is_public = models.BooleanField(db_column='IsPublic')
    can_published = models.BooleanField(db_column='CanPublished')

    class Meta:
        managed = True
        db_table = 'Travelogue'


class TravelogueImage(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    travelogue = models.ForeignKey(Travelogue, on_delete=models.PROTECT, db_column='TravelogueId')
    image_path = models.CharField(db_column='ImagePath', max_length=256)
    is_public = models.BooleanField(db_column='IsPublic')
    deleted = models.BooleanField(db_column='Deleted')

    class Meta:
        managed = True
        db_table = 'TravelogueImage'


class TravelogueImageTag(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    lang = models.SmallIntegerField(db_column='Lang')
    travelogue_image = models.ForeignKey(TravelogueImage, on_delete=models.PROTECT, db_column='TravelogueImageId')
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT, db_column='TagId')

    class Meta:
        managed = True
        db_table = 'TravelogueImageTag'


class TravelogueTag(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    lang = models.SmallIntegerField(db_column='Lang')
    travelogue = models.ForeignKey(Travelogue, on_delete=models.PROTECT, db_column='TravelogueId')
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT, db_column='TagId')

    class Meta:
        managed = True
        db_table = 'TravelogueTag'


class AttractionSurvey(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    parent_id = models.IntegerField(db_column='ParentId', blank=True, null=True)
    attraction = models.ForeignKey(Attraction, on_delete=models.PROTECT, db_column='AttractionId')
    description = models.TextField(db_column='Description', blank=True, null=True)
    rate = models.FloatField(db_column='Rate')
    created_date = models.DateTimeField(db_column='CreatedDate')
    user = models.ForeignKey(User, on_delete=models.PROTECT, db_column='UserId')
    travel = models.ForeignKey('Travel', on_delete=models.PROTECT, db_column='TravelId', blank=True, null=True)
    like = models.IntegerField(db_column='Like')
    dislike = models.IntegerField(db_column='Dislike')
    isvisible = models.BooleanField(db_column='IsVisible')

    class Meta:
        managed = True
        db_table = 'AttractionSurvey'


class AttractionSurveyReaction(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    attractionsurveyid = models.ForeignKey(AttractionSurvey, on_delete=models.PROTECT, db_column='AttractionSurveyId')
    user = models.ForeignKey(User, on_delete=models.PROTECT, db_column='UserId')
    created_date = models.DateTimeField(db_column='CreatedDate')
    user_react_type_code = models.IntegerField(db_column='UserReactTypeCode')

    class Meta:
        managed = True
        db_table = 'AttractionSurveyReaction'


# class AttractionTag(models.Model):
#     id = models.AutoField(db_column='Id', primary_key=True)
#     attraction = models.ForeignKey(Attraction, on_delete=models.PROTECT, db_column='AttractionId')
#     tag = models.ForeignKey('Tag', on_delete=models.PROTECT, db_column='TagId')
#
#     class Meta:
#         managed = True
#         db_table = 'AttractionTag'


class Event(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    lang = models.SmallIntegerField(db_column='Lang')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT, db_column='SubCategoryId',
                                    blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, db_column='CategoryId', blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT, db_column='CityId', blank=True, null=True)
    title = models.CharField(db_column='Title', max_length=200, blank=True, null=True)
    url_key = models.CharField(db_column='UrlKey', max_length=200, blank=True, null=True)
    base_url = models.CharField(db_column='BaseUrl', max_length=200, blank=True, null=True)
    image = models.TextField(db_column='Image', blank=True, null=True)
    full_title = models.CharField(db_column='FullTitle', max_length=500, blank=True, null=True)
    english_title = models.CharField(db_column='EnglishTitle', max_length=32)
    address = models.CharField(db_column='Address', max_length=200, blank=True, null=True)
    regular_price = models.DecimalField(db_column='RegularPrice', max_digits=18, decimal_places=2)
    deal_price = models.DecimalField(db_column='DealPrice', max_digits=18, decimal_places=2)
    deal_discount = models.FloatField(db_column='DealDiscount', blank=True, null=True)
    sold_deal_quantity = models.IntegerField(db_column='SoldDealQuantity', blank=True, null=True)
    total_deal_quantity = models.IntegerField(db_column='TotalDealQuantity', blank=True, null=True)
    usage_deadline = models.IntegerField(db_column='UsageDeadline', blank=True, null=True)
    description = models.CharField(db_column='Description', max_length=512, blank=True, null=True)
    lat = models.FloatField(db_column='Lat', blank=True, null=True)
    long = models.FloatField(db_column='Long', blank=True, null=True)
    point = models.TextField(db_column='Point', blank=True, null=True)
    visit_duration = models.IntegerField(db_column='VisitDuration', blank=True, null=True)
    visit_time_from = models.IntegerField(db_column='VisitTimeFrom', blank=True, null=True)
    visit_time_to = models.IntegerField(db_column='VisitTimeTo', blank=True, null=True)
    visit_date_from = models.DateTimeField(db_column='VisitDateFrom', blank=True, null=True)
    visit_date_to = models.DateTimeField(db_column='VisitDateTo', blank=True, null=True)
    rate = models.FloatField(db_column='Rate', blank=True, null=True)
    iplanner_rate = models.FloatField(db_column='iPlannerRate', blank=True, null=True)
    user_rate = models.FloatField(db_column='UserRate', blank=True, null=True)
    active = models.BooleanField(db_column='Active', blank=True, null=True)
    my_property = models.IntegerField(db_column='MyProperty', blank=True, null=True)
    external_id = models.CharField(db_column='ExternalId', max_length=36, blank=True, null=True)
    external_product_id = models.CharField(db_column='ExternalProductId', max_length=36, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Event'


class EventSurvey(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    parent_id = models.IntegerField(db_column='ParentId', blank=True, null=True)
    event = models.ForeignKey(Event, on_delete=models.PROTECT, db_column='EventId')
    menu_name = models.TextField(db_column='MenuName', blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)
    rate = models.FloatField(db_column='Rate')
    created_date = models.DateTimeField(db_column='CreatedDate')
    user = models.ForeignKey(User, on_delete=models.PROTECT, db_column='UserId')
    travel = models.ForeignKey(Travel, on_delete=models.PROTECT, db_column='TravelId')
    like = models.IntegerField(db_column='Like')
    dislike = models.IntegerField(db_column='Dislike')
    isvisible = models.BooleanField(db_column='IsVisible')

    class Meta:
        managed = True
        db_table = 'EventSurvey'


class EventSurveyReaction(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    event_survey = models.ForeignKey(EventSurvey, on_delete=models.PROTECT, db_column='EventSurveyId')
    user = models.ForeignKey(User, on_delete=models.PROTECT, db_column='UserId')
    created_date = models.DateTimeField(db_column='CreatedDate')
    user_react_type_code = models.IntegerField(db_column='UserReactTypeCode')

    class Meta:
        managed = True
        db_table = 'EventSurveyReaction'


class EventTag(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.PROTECT, db_column='EventId')
    tag = models.ForeignKey('Tag', on_delete=models.PROTECT, db_column='TagId')

    class Meta:
        managed = True
        db_table = 'EventTag'


class FavoriteAttraction(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    attraction = models.ForeignKey(Attraction, on_delete=models.PROTECT, db_column='AttractionId')
    user = models.ForeignKey(User, on_delete=models.PROTECT, db_column='UserId')
    created_date = models.DateTimeField(db_column='CreatedDate')
    deleted = models.BooleanField(db_column='Deleted')
    is_public = models.BooleanField(db_column='IsPublic')

    class Meta:
        managed = True
        db_table = 'FavoriteAttraction'


class Hotel(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    lang = models.SmallIntegerField(db_column='Lang')
    city = models.ForeignKey(City, on_delete=models.PROTECT, db_column='CityId')
    title = models.CharField(db_column='Title', max_length=32)
    full_title = models.CharField(db_column='FullTitle', max_length=64, blank=True, null=True)
    english_title = models.CharField(db_column='EnglishTitle', max_length=32)
    address = models.CharField(db_column='Address', max_length=64, blank=True, null=True)
    cost = models.CharField(db_column='Cost', max_length=16, blank=True, null=True)
    description = models.CharField(db_column='Description', max_length=512, blank=True, null=True)
    lat = models.FloatField(db_column='Lat')
    long = models.FloatField(db_column='Long')
    point = models.TextField(db_column='Point', blank=True, null=True)
    visit_time_from = models.DateTimeField(db_column='VisitTimeFrom')
    visit_time_to = models.DateTimeField(db_column='VisitTimeTo')
    can_visit = models.BooleanField(db_column='CanVisit')
    rate = models.FloatField(db_column='Rate')
    external_id = models.CharField(db_column='ExternalId', max_length=32, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Hotel'


class Meal(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    title = models.TextField(db_column='Title', blank=True, null=True)
    from_time = models.DateTimeField(db_column='FromTime')
    to_time = models.DateTimeField(db_column='ToTime')

    class Meta:
        managed = True
        db_table = 'Meal'


class HotelMeal(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT, db_column='HotelId')
    meal = models.ForeignKey(Meal, on_delete=models.PROTECT, db_column='MealId')
    from_time = models.DateTimeField(db_column='FromTime')
    to_time = models.DateTimeField(db_column='ToTime')

    class Meta:
        managed = True
        db_table = 'HotelMeal'


class HotelSurvey(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    parent_id = models.IntegerField(db_column='ParentId', blank=True, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT, db_column='HotelId')
    hotelmeal = models.ForeignKey(HotelMeal, on_delete=models.PROTECT, db_column='HotelMealId')
    menu_name = models.TextField(db_column='MenuName', blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)
    rate = models.FloatField(db_column='Rate')
    created_date = models.DateTimeField(db_column='CreatedDate')
    user = models.ForeignKey(User, on_delete=models.PROTECT, db_column='UserId')
    travel = models.ForeignKey(Travel, on_delete=models.PROTECT, db_column='TravelId')
    like = models.IntegerField(db_column='Like')
    dislike = models.IntegerField(db_column='Dislike')
    isvisible = models.BooleanField(db_column='IsVisible')

    class Meta:
        managed = True
        db_table = 'HotelSurvey'


class HotelSurveyReaction(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    hotel_survey = models.ForeignKey(HotelSurvey, on_delete=models.PROTECT, db_column='HotelSurveyId')
    user = models.ForeignKey(User, on_delete=models.PROTECT, db_column='UserId')
    created_date = models.DateTimeField(db_column='CreatedDate')
    user_react_type_code = models.IntegerField(db_column='UserReactTypeCode')

    class Meta:
        managed = True
        db_table = 'HotelSurveyReaction'


class HotelTag(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT, db_column='HotelId')
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT, db_column='TagId')

    class Meta:
        managed = True
        db_table = 'HotelTag'


class ReportedBug(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    title = models.CharField(db_column='Title', max_length=128)
    description = models.CharField(db_column='Description', max_length=512)
    user = models.ForeignKey(User, on_delete=models.PROTECT, db_column='UserId')
    created_date = models.DateTimeField(db_column='CreatedDate')
    resolved_time = models.DateTimeField(db_column='ResolvedTime', blank=True, null=True)
    active = models.BooleanField(db_column='Active')

    class Meta:
        managed = True
        db_table = 'ReportedBug'


class SavedAttraction(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    attraction = models.ForeignKey(Attraction, on_delete=models.PROTECT, db_column='AttractionId')
    user = models.ForeignKey(User, on_delete=models.PROTECT, db_column='UserId')
    created_date = models.DateTimeField(db_column='CreatedDate')
    deleted = models.BooleanField(db_column='Deleted')
    is_public = models.BooleanField(db_column='IsPublic')

    class Meta:
        managed = True
        db_table = 'SavedAttraction'


class Suggestion(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    title = models.CharField(db_column='Title', max_length=128)
    description = models.CharField(db_column='Description', max_length=512)
    user = models.ForeignKey(User, on_delete=models.PROTECT, db_column='UserId')
    created_date = models.DateTimeField(db_column='CreatedDate')
    active = models.BooleanField(db_column='Active')

    class Meta:
        managed = True
        db_table = 'Suggestion'


class Rules(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    title = models.CharField(db_column='Title', max_length=128)
    lang = models.SmallIntegerField(db_column='Lang')
    description = models.CharField(db_column='Description', max_length=512)

    class Meta:
        managed = True
        db_table = 'Rules'


#####################################################################################
class TravelType(models.Model):
    title = models.CharField(max_length=200)
    tags = models.CharField(max_length=1000)
    comment = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        db_table = 'plan_traveltype'
        verbose_name_plural = '5 Travel Types'


class DistanceMatrix(models.Model):
    origin = models.ForeignKey(Attraction, related_name='distance_mat', on_delete=models.CASCADE)
    destination = models.ForeignKey(Attraction, related_name='destination', on_delete=models.CASCADE)
    travel_type = models.ForeignKey(TravelType, on_delete=models.CASCADE)
    ecl_dist = models.FloatField('Euclidean Distance', null=True, blank=True, )
    len_meter = models.FloatField('Lenght Of Meters', null=True, blank=True)
    len_time = models.FloatField('Lenght Of Time', null=True, blank=True)
    route = models.TextField('Routing Json', null=True, blank=True)

    def __str__(self):
        return self.origin.title + ' - ' + self.destination.title

    class Meta:
        managed = True
        db_table = 'plan_distance_mat'
        verbose_name_plural = '6 Distance matrix'

    def save(self, *args, **kwargs):
        if not self.id:
            super().save(*args, **kwargs)

        '''
            CREATE OR REPLACE PROCEDURE pln_update_ecl_dist()
            LANGUAGE plpgsql    
            AS $$
            BEGIN
                    update plan_distance_mat
                    set ecl_dist = t.ecl_dist
                    from	
                        (select 
                             m.id
                             ,sqrt(power(o.latt-d.latt, 2) + power(o.long-d.long, 2)) as ecl_dist
                            from
                                plan_distance_mat m
                                join plan_attractions o on o.id = m.origin_id
                                join plan_attractions d on d.id = m.destination_id
                        ) t 
                    where t.id = plan_distance_mat.id;

                COMMIT;
            END;
            $$;

        '''
        ogn_latt = self.origin.latt
        ogn_long = self.origin.long
        dst_latt = self.destination.latt
        dst_long = self.destination.long

        ecl_dist = math.sqrt(((dst_latt - ogn_latt) ** 2) + ((dst_long - ogn_long) ** 2))
        self.ecl_dist = ecl_dist
        super(DistanceMatrix, self).save(*args, **kwargs)


class Plan(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    present_id = models.CharField(max_length=1000, null=True, blank=True)
    day = models.IntegerField('Day Of Tour', null=True, blank=True)
    all_days = models.IntegerField('Total days', null=True, blank=True)
    coh_fullTime = models.FloatField('Coefficient of Fill full time Cost', null=True, blank=True)
    coh_lengthTime = models.FloatField('Coefficient of distance length time Cost', null=True, blank=True)
    coh_countPoints = models.FloatField('Coefficient of count of points Cost', null=True, blank=True)
    coh_minRqTime = models.FloatField('Coefficient of diff min required Time Cost', null=True, blank=True)
    cost_fullTime = models.FloatField('Fill full time Cost', null=True, blank=True)
    cost_lengthTime = models.FloatField('Distance length time Cost', null=True, blank=True)
    cost_countPoints = models.FloatField('Count of points Cost', null=True, blank=True)
    cost_minRqTime = models.FloatField('Diff min required Time Cost', null=True, blank=True)
    cost_rate = models.FloatField('Selection attraction rate Cost', null=True, blank=True)
    rank = models.FloatField('Average Rank', null=True, blank=True)
    start_time = models.CharField('Start Time of Day', max_length=20, null=True, blank=True)
    end_time = models.CharField('End Time of Day', max_length=20, null=True, blank=True)
    dist_len = models.FloatField('Length of distance times', null=True, blank=True)
    points_len = models.IntegerField('Count of points used', null=True, blank=True)
    duration_len = models.FloatField('Length of duration points', null=True, blank=True)
    tags = models.CharField(max_length=1000, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    # first_latt = models.DecimalField('Latitude', null=True, blank=True, max_digits=9, decimal_places=6)
    # first_long = models.DecimalField('Longitude', null=True, blank=True, max_digits=9, decimal_places=6)

    def __str__(self):
        return str(self.day) + ' day ' + self.city.name

    class Meta:
        managed = True
        db_table = 'plan_plan'
        verbose_name_plural = '7 Plan'


class PlanDetails(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    order = models.IntegerField()
    point = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    len_time = models.IntegerField()
    from_time = models.IntegerField(null=True, blank=True)
    dist_to = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '%d: %s' % (self.order, self.point.title)

    class Meta:
        managed = True
        db_table = 'plan_plan_details'
        verbose_name_plural = '7.1 Plan details'
        ordering = ('plan__day', 'order',)
