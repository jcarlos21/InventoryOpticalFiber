from extras.plugins import PluginConfig

class NetBoxFibersInventoryConfig(PluginConfig):
    name = 'netbox_inventory_fibers'
    verbose_name = ' Netbox Fibers Inventory'
    description = 'Manage optical fibers inventory'
    version = '0.1'
    author = 'José Carlos dos Santos'
    author_email = 'j.carlos2020@live.com'
    base_url = 'fibers-inventory'    

config = NetBoxFibersInventoryConfig