from django.contrib import admin


from Vramal.ramal.models import Ramal, pessoa

class RamalAdmin(admin.ModelAdmin):
	model=Ramal
	list_display = ['Ramal_Number']
	list_filter = ['Ramal_Number']
	search_fields = ['Ramal_Number']
	save_on_top = True

admin.site.register(Ramal, RamalAdmin)


class PessoaAdmin(admin.ModelAdmin):

	model=pessoa
	list_display = ['pessoa_nome']
	list_filter = ['pessoa_nome']
	search_fields = ['pessoa_nome']
	save_on_top = True

admin.site.register(pessoa, PessoaAdmin)