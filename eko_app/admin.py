from django.contrib import admin
from .models import Man, Woman, Solution

@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    # список полей, отображаемых в адмике по порядку их следования
    list_display = ('id',
                    'number',
                    'commission_name',
                    'date',
                    'man',
                    'woman',
                    'solution',
                    'org_referal',
                    'reason',
                    'commission_chairman',
                    'commission_secretary',
                    'commission_members')

@admin.register(Man)
class ManAdmin(admin.ModelAdmin):
    # список полей, отображаемых в адмике по порядку их следования
    list_display = ('id',
                    'surname',
                    'name',
                    'dad_name',
                    'birth_date',
                    'birth_place',
                    'location',
                    'doc_type',
                    'pasport_type',
                    'pasport_serial',
                    'pasport_number')

@admin.register(Woman)
class WomanAdmin(admin.ModelAdmin):
    # список полей, отображаемых в адмике по порядку их следования
    list_display = ('id',
                    'surname',
                    'name',
                    'dad_name',
                    'birth_date',
                    'birth_place',
                    'location',
                    'doc_type',
                    'pasport_type',
                    'pasport_serial',
                    'pasport_number')