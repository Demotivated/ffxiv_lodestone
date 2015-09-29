from django.contrib import admin

from .models import Character, Job, Item


class CharacterAdmin(admin.ModelAdmin):
    readonly_fields = ('lodestone_id',)
    fieldsets = [
        (None,              {'fields': ['name',
                                        'lodestone_id',
                                        'server',
                                        'species',
                                        'gender',
                                        'city_state',
                                        'free_company']}),
        ('Grand Company',   {'fields': ['grand_company_name', 'grand_company_rank']}),
        ('Class Levels',    {'fields': ['lvl_archer',
                                        'lvl_lancer',
                                        'lvl_marauder',
                                        'lvl_pugilist',
                                        'lvl_rogue',
                                        'lvl_arcanist',
                                        'lvl_conjurer',
                                        'lvl_thaumaturge',
                                        'lvl_astrologian',
                                        'lvl_darknight',
                                        'lvl_machinist',
                                        'lvl_alchemist',
                                        'lvl_armorer',
                                        'lvl_blacksmith',
                                        'lvl_carpenter',
                                        'lvl_culinarian',
                                        'lvl_gladiator',
                                        'lvl_goldsmith',
                                        'lvl_leatherworker',
                                        'lvl_weaver',
                                        'lvl_botanist',
                                        'lvl_fisher',
                                        'lvl_miner'],
                             'classes': ['collapse']})
    ]
    list_display = ('name', 'server', 'free_company')
    list_filter = ['server', 'free_company']


class ItemAdmin(admin.ModelAdmin):
    readonly_fields = ('lodestone_id',)
    fieldsets = [
        (None,              {'fields': ['name', 'lodestone_id', 'item_type', 'item_level']}),
        ('Weapon Stats',    {'fields': ['damage', 'auto_attack', 'delay']}),
        ('Armor Stats',     {'fields': ['defense', 'magic_defense']}),
        ('Shield Stats',    {'fields': ['block_strength', 'block_rate']}),
        ('Stats',           {'fields': ['vitality',
                                        'mind',
                                        'determination',
                                        'spell_speed',
                                        'accuracy',
                                        'critical_hit_rate',
                                        'piety']})
    ]
    list_display = ('name', 'item_type', 'item_level')
    list_filter = ['item_type', 'item_level']


class JobAdmin(admin.ModelAdmin):
    list_display = ('character', 'job')
    list_filter = ['job']
    filter_horizontal = ('items',)


admin.site.register(Character, CharacterAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Job, JobAdmin)
