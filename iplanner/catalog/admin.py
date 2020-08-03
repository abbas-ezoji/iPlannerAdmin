from django.contrib import admin
from .models import *


class CountryAdmin(admin.ModelAdmin):
    list_display = ('iso3', 'name', 'english_name')
    list_filter = ('iso3', 'name', 'english_name')


class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('country', 'name', 'english_name')
    list_filter = ('country__name', 'name', 'english_name')


class CityAdmin(admin.ModelAdmin):
    list_display = ('province', 'name', 'english_name')
    list_filter = ('province__country__name', 'province__name', 'name', 'english_name')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'department')
    list_filter = ('department__title', 'title',)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category',)
    list_filter = ('category__department__title', 'category__title', 'title',)


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'open_id', 'show_on_boarding',)
    list_filter = ('id', 'open_id', 'show_on_boarding',)


class UserCityAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'created_date',)
    list_filter = ('user__id', 'city__province__country__name', 'city__province__name', 'city__name',)


class OnBoardingQuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'order_index', 'anwer_type_code',)
    list_filter = ('title', 'order_index', 'anwer_type_code',)


class OnBoardingQuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ('onboarding_question', 'title', 'icon', 'active',)
    list_filter = ('onboarding_question__title', 'title', 'active',)


class AirportTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'active',)
    list_filter = ('title', 'active',)


class AirportAdmin(admin.ModelAdmin):
    list_display = ('name', 'english_name', 'active',)
    list_filter = ('name', 'english_name', 'active',)


class AttractionAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'iplanner_rate', )
    list_filter = ('city__province__country__name', 'city__province__name', 'city__name',
                   'full_title', 'type', 'tag',)


class EventAdmin(admin.ModelAdmin):
    list_display = ('full_title', 'category', 'city',)
    list_filter = ('city__province__country__name', 'city__province__name', 'city__name',
                   'category__title')


class PlanDetailsAdmin(admin.ModelAdmin):
    list_display = ('point', 'order', 'from_time', 'len_time', 'dist_to', 'plan',)
    list_filter = ('plan__city__name', 'point__title', 'plan__present_id',
                   'plan__cost_fullTime', 'plan__cost_lengthTime', 'plan__cost_countPoints', 'plan__cost_minRqTime',
                   'plan__cost_rate')


class PlanDetailsAdminInline(admin.TabularInline):
    model = PlanDetails


class PlanAdmin(admin.ModelAdmin):
    list_display = ('city', 'all_days', 'present_id', 'cost_rate', 'tag_category')
    list_filter = ('city__name', 'all_days', 'tag_category__title', )
    # inlines = [PlanDetailsAdminInline]


class TravelTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'tags',)
    list_filter = ('title', 'tags',)


class DistanceMatrixAdmin(admin.ModelAdmin):
    # pass
    list_display = [field.name for field in DistanceMatrix._meta.get_fields()]
    list_filter = ('origin__city__province__country__name', 'origin__city__province__name', 'origin__city__name',
                   'origin__title', 'destination__title', 'travel_type__title')


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'category',)
    list_filter = ('title', 'category__title')


admin.site.register(Country, CountryAdmin)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(UserCity, UserCityAdmin)
admin.site.register(OnBoardingQuestion, OnBoardingQuestionAdmin)
admin.site.register(Onboardingquestionanswer, OnBoardingQuestionAnswerAdmin)
admin.site.register(AirportType, AirportTypeAdmin)
admin.site.register(Airport, AirportAdmin)
admin.site.register(Attraction, AttractionAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(TravelType, TravelTypeAdmin)
admin.site.register(DistanceMatrix, DistanceMatrixAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(PlanDetails, PlanDetailsAdmin)
admin.site.register(Tag, TagAdmin)