from django.contrib import admin
from .models import Solution, Man, Woman

@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    # список полей, отображаемых в адмике по порядку их следования
    list_display = ('id',
                    'date',
                    'number',
                    'commission_name',
                    'solution',
                    'org_referal',
                    'reason',
                    'commission_chairman',
                    'commission_secretary',
                    'commission_members',
                    'woman',
                    'man',
                    )

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
                    'pasport_type',
                    'pasport_serial',
                    'pasport_number',
                    'date_issue',
                    'issuing_authority',
                    'who_issued',
                    'marriage_reg_mark',
                    )

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
                    'pasport_type',
                    'pasport_serial',
                    'pasport_number',
                    'date_issue',
                    'issuing_authority',
                    'who_issued',
                    )