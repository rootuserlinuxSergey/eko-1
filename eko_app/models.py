from django.db import models

class Man(models.Model):
    surname = models.CharField(max_length=100, verbose_name="Фамилия", blank=False)
    name = models.CharField(max_length=100, verbose_name="Имя", blank=False)
    dad_name = models.CharField(max_length=100, verbose_name="Отчество", blank=False)
    birth_date = models.DateField(verbose_name="Дата рождения", blank=False)
    birth_place = models.CharField(max_length=150, verbose_name="Место рождения", blank=False)
    location = models.CharField(max_length=150, verbose_name="Место жительства", blank=False)
    doc_type = [
        ('a', 'Паспорт'),
        ('d', 'ID-карта'),
    ]
    pasport_type = models.CharField(max_length=1, choices=doc_type, blank=False)
    pasport_serial = models.CharField(max_length=2, verbose_name="Серия паспорта", blank=True)
    pasport_number = models.CharField(max_length=10, verbose_name="Номер паспорта", blank=False)
    date_issue = models.DateField(verbose_name='Дата выдачи', blank=False)
    issuing_authority = models.CharField(max_length=150, verbose_name='Орган выдачи', blank=False)
    marriage_reg_mark = models.CharField(max_length=200, verbose_name='Отметка о регистрации брака', blank=False)
    who_issued = models.CharField(max_length=100, verbose_name="Выписка из медицинских документов", blank=False)

    def __str__(self):
        return f"{self.surname} {self.name} {self.dad_name}"

    class Meta:
        verbose_name = "Супруга"
        verbose_name_plural = "Мужья"

class Woman(models.Model):
    surname = models.CharField(max_length=100, verbose_name="Фамилия", blank=False)
    name = models.CharField(max_length=100, verbose_name="Имя", blank=False)
    dad_name = models.CharField(max_length=100, verbose_name="Отчество", blank=False)
    birth_date = models.DateField(verbose_name="Дата рождения", blank=False)
    birth_place = models.CharField(max_length=150, verbose_name="Место рождения", blank=False)
    location = models.CharField(max_length=150, verbose_name="Место жительства", blank=False)
    doc_type = [
        ('a', 'Паспорт'),
        ('d', 'ID-карта'),
    ]
    pasport_type = models.CharField(max_length=1, choices=doc_type, blank=False)
    pasport_serial = models.CharField(max_length=2, verbose_name="Серия паспорта", blank=True)
    pasport_number = models.CharField(max_length=10, verbose_name="Номер паспорта", blank=False)
    date_issue = models.DateField(verbose_name='Дата выдачи', blank=False)
    issuing_authority = models.CharField(max_length=150, verbose_name='Орган выдачи', blank=False)
    marriage_reg_mark = models.CharField(max_length=200, verbose_name='Отметка о регистрации брака', blank=False)
    who_issued = models.CharField(max_length=100, verbose_name="Выписка из медицинских документов", blank=False)

    def __str__(self):
        return f"{self.surname} {self.name} {self.dad_name}"

    class Meta:
        verbose_name = "Супругу"
        verbose_name_plural = "Жёны"

class Solution(models.Model):
    date = models.DateField(verbose_name="Дата", auto_now_add=True)
    number = models.IntegerField(verbose_name="№")
    commission_name = models.CharField(max_length=200, verbose_name="Наименование комиссии", blank=False)
    man = models.ForeignKey(Man, verbose_name="Супруг", on_delete=models.PROTECT)
    woman = models.ForeignKey(Woman, verbose_name="Супруга", on_delete=models.PROTECT)
    sol_choice = [
        ('1', 'направить'),
        ('2', 'отказать'),
    ]
    solution = models.CharField(max_length=1, choices=sol_choice, verbose_name="Принятое решение", blank=False)
    org_choice = [
        ('1', '"Городской клинический родильный дом №2"'),
        ('2', '"РНПЦ "Мать и Дитя"'),
    ]
    org_referal = models.CharField(max_length=1, choices=org_choice, verbose_name="Направление в организицию", blank=True)
    reason = models.TextField(verbose_name="причина отказа", blank=True)
    commission_chairman = models.CharField(max_length=100, verbose_name="Председатель комиссии", blank=True)
    commission_secretary = models.CharField(max_length=100, verbose_name="Секретарь комиссии", blank=True)
    commission_members = models.TextField(verbose_name="Члены комссии", blank=True)

    def __str__(self):
        return f"{self.number}"

    class Meta:
        verbose_name = "Решение комиссии"
        verbose_name_plural = "Решения комиссии"