from setuptools import setup, find_packages

metadata = {
    'name': 'MyBear',
    'version': '1.0.0',
    'authors': 'Badr Bouaissa, Gabriel Bonjour, Clément Devarieux',
    'description': "Projet final python 3IABD2, implémentation d'une librairie MyBear, visant à reproduire pandas"
}

install_requires = [
    'numpy==1.24.3'
]

# package_data = {
#     'csv': ['*.csv'],
#     'json': ['*.json']
# }

setup(
    **metadata,
    install_requires=install_requires,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    # package_data=package_data,
)

# Ensuite, utiliser ce setup.py pour installer le projet en exécutant la commande
# python setup.py install , dans le répertoire contenant le fichier setup.py

# 1. set up custom discovery (`find` directive with `include` or `exclude`)
# 2. use a `src-layout`
# 3. explicitly set `py_modules` or `packages` with a list of names

