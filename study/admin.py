from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline

from study.models import Direction, Intern, Subject


class DirectionInternInline(TabularInline):
    raw_id_fields = ('intern', )
    model = Direction.interns.through
    extra = 0
    verbose_name = 'Поступающий'
    verbose_name_plural = 'Поступающие'


class DirectionSubjectInline(TabularInline):
    raw_id_fields = ('subject', )
    model = Direction.subjects.through
    extra = 0
    verbose_name = 'Предмет'
    verbose_name_plural = 'Предметы'


class InternSubjectInline(TabularInline):
    raw_id_fields = ('subject', )
    model = Intern.subjects.through
    extra = 0
    verbose_name = 'Предмет'
    verbose_name_plural = 'Предметы'


@admin.register(Subject)
class SubjectAdmin(ModelAdmin):
    list_display = ('id', 'name', 'min_score')
    search_fields = ('id', 'name', 'min_score')
    list_display_links = ('id', 'name')


@admin.register(Intern)
class InternAdmin(ModelAdmin):
    list_display = ('id', 'fio', 'birthday_year', 'passport_number')
    search_fields = ('id', 'fio', 'birthday_year', 'passport_number')
    list_display_links = ('id', 'fio')
    list_filter = ('birthday_year', )
    exclude = ('subjects', )
    inlines = [
        InternSubjectInline,
    ]

@admin.register(Direction)
class DirectionAdmin(ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')
    list_display_links = ('id', 'name')
    exclude = ('interns', 'subjects')
    inlines = [
        DirectionInternInline,
        DirectionSubjectInline,
    ]
