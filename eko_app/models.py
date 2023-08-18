from django.db import models

class Solution(models.Model):
    doc_choice = [
        ('1', 'Паспорт'),
        ('2', 'ID-карта'),
    ]
    sol_choice = [
        ('1', 'направить'),
        ('2', 'отказать'),
    ]
    org_choice = [
        ('1', '"Городской клинический родильный дом №2"'),
        ('2', '"РНПЦ "Мать и Дитя"'),
    ]
    date = models.DateField(verbose_name="Дата", auto_now_add=True)
    number = models.IntegerField(verbose_name="№")
    commission_name = models.CharField(max_length=200, verbose_name="Наименование комиссии", blank=False)
    solution = models.CharField(max_length=1, choices=sol_choice, verbose_name="Принятое решение", blank=True)
    org_referal = models.CharField(max_length=1, choices=org_choice, verbose_name="Направление в организицию", blank=True)
    reason = models.TextField(verbose_name="причина отказа", blank=True)
    commission_chairman = models.CharField(max_length=100, verbose_name="Председатель комиссии", blank=True)
    commission_secretary = models.CharField(max_length=100, verbose_name="Секретарь комиссии", blank=True)
    commission_members = models.TextField(verbose_name="Члены комссии", blank=True)

    woman_surname = models.CharField(max_length=100, verbose_name="Фамилия Супруги", blank=False)
    woman_name = models.CharField(max_length=100, verbose_name="Имя Супруги", blank=False)
    woman_dad_name = models.CharField(max_length=100, verbose_name="Отчество Супруги", blank=False)
    woman_birth_date = models.DateField(verbose_name="Дата рождения Супруги", blank=False)
    woman_birth_place = models.CharField(max_length=150, verbose_name="Место рождения Супруги", blank=False)
    woman_location = models.CharField(max_length=150, verbose_name="Место жительства Супруги", blank=False)
    woman_pasport_type = models.CharField(max_length=1, choices=doc_choice, verbose_name="Тип паспорта Супруги", blank=False)
    woman_pasport_serial = models.CharField(max_length=2, verbose_name="Серия паспорта Супруги", blank=True)
    woman_pasport_number = models.CharField(max_length=10, verbose_name="Номер паспорта Супруги", blank=False)
    woman_date_issue = models.DateField(verbose_name='Дата выдачи Супруги', blank=False)
    woman_issuing_authority = models.CharField(max_length=150, verbose_name='Орган выдачи Супруги', blank=False)
    woman_who_issued = models.CharField(max_length=100, verbose_name="Выписка из медицинских документов Супруги", blank=False)

    man_surname = models.CharField(max_length=100, verbose_name="Фамилия Супруга", blank=False)
    man_name = models.CharField(max_length=100, verbose_name="Имя Супруга", blank=False)
    man_dad_name = models.CharField(max_length=100, verbose_name="Отчество Супруга", blank=False)
    man_birth_date = models.DateField(verbose_name="Дата рождения Супруга", blank=False)
    man_birth_place = models.CharField(max_length=150, verbose_name="Место рождения Супруга", blank=False)
    man_location = models.CharField(max_length=150, verbose_name="Место жительства Супруга", blank=False)
    man_pasport_type = models.CharField(max_length=1, choices=doc_choice, verbose_name="Тип паспорта Супруга", blank=False)
    man_pasport_serial = models.CharField(max_length=2, verbose_name="Серия паспорта Супруга", blank=True)
    man_pasport_number = models.CharField(max_length=10, verbose_name="Номер паспорта Супруга", blank=False)
    man_date_issue = models.DateField(verbose_name='Дата выдачи паспорта Супруга', blank=False)
    man_issuing_authority = models.CharField(max_length=150, verbose_name='Орган выдачи паспорта Супруга', blank=False)
    man_who_issued = models.CharField(max_length=100, verbose_name="Выписка из медицинских документов Супруга", blank=False)

    marriage_reg_mark = models.CharField(max_length=200, verbose_name='Отметка о регистрации брака', blank=False)

    def __str__(self):
        return f"{self.number}"

    class Meta:
        verbose_name = "Решение комиссии"
        verbose_name_plural = "Решения комиссии"