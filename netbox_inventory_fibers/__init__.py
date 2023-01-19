from extras.plugins import PluginConfig

class NetBoxFibersInventoryConfig(PluginConfig):
    name = 'netbox_inventory_fibers'
    verbose_name = ' Netbox Fibers Inventory'
    description = 'Manage optical fibers inventory'
    version = '0.1'
    base_url = 'fibers-inventory'

config = NetBoxFibersInventoryConfig
