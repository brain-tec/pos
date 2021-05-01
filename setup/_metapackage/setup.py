import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo13-addons-oca-pos",
    description="Meta package for oca-pos Odoo addons",
    version=version,
    install_requires=[
        'odoo13-addon-pos_default_partner',
        'odoo13-addon-pos_fixed_discount',
        'odoo13-addon-pos_order_mgmt',
        'odoo13-addon-pos_order_remove_line',
        'odoo13-addon-pos_product_sort',
        'odoo13-addon-pos_timeout',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
