from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

menu_items = ()

fornecedor_buttons = [
    PluginMenuButton(
        link='plugins:netbox_inventory_fibers:fornecedor_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]
tipobobina_buttons = [
    PluginMenuButton(
        link='plugins:netbox_inventory_fibers:tipobobina_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]
quantidadefibracabo_buttons = [
    PluginMenuButton(
        link='plugins:netbox_inventory_fibers:quantidadefibracabo_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]
bobina_buttons = [
    PluginMenuButton(
        link='plugins:netbox_inventory_fibers:bobina_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]
requisicao_buttons = [
    PluginMenuButton(
        link='plugins:netbox_inventory_fibers:requisicao_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]
fibrarequisitada_buttons = [
    PluginMenuButton(
        link='plugins:netbox_inventory_fibers:fibrarequisitada_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_inventory_fibers:requisicao_list',
        link_text='Ordem de Serviço',
        buttons=requisicao_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_inventory_fibers:fibrarequisitada_list',
        link_text='Requisições',
        buttons=fibrarequisitada_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_inventory_fibers:bobina_list',
        link_text='Bobinas',
        buttons=bobina_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_inventory_fibers:fornecedor_list',
        link_text='Fornecedores',
        buttons=fornecedor_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_inventory_fibers:quantidadefibracabo_list',
        link_text='Quantidade de Fibras',
        buttons=quantidadefibracabo_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_inventory_fibers:tipobobina_list',
        link_text='Tipos de Bobina',
        buttons=tipobobina_buttons
    ),
)

