from django.contrib import admin
from django.db.models import QuerySet

from companies.models import Company


# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['title', 'debt', 'currency', 'country', 'purveyor']
    list_filter = ['country']
    actions = ['set_null']

    @admin.action(description='Очистить задолженность перед поставщиком')
    async def set_null(self, request, qs: QuerySet):

        count_update = 0

        if qs.count() > 20:
            count_update = await qs.update(debt=0)
        else:
            count_update = qs.update(debt=0)

        self.message_user(
            request,
            f'Обновлены {count_update} строк'
        )
