from setuptools import setup

metadata = {
    'name': 'MyBear',
    'version': '1.0.0',
    'authors': 'Badr Bouaissa, Gabriel Bonjour, Clément Devarieux',
    'description': "Projet final python 3IABD2, implémentation d'une librairie MyBear, visant à reproduire pandas"
}

install_requires = [
    'colorama==0.4.6',
    'exceptiongroup==1.1.1',
    'iniconfig==2.0.0',
    'numpy==1.24.3',
    'packaging==23.1',
    'pluggy==1.0.0',
    'pytest==7.3.1',
    'tomli==2.0.1'
]

package_data = {
    'csv_files': ['*.csv'],
    'json_files': ['*.json']
}

setup(
    **metadata,
    install_requires=install_requires,
    package_data=package_data,
)

# Ensuite, utiliser ce setup.py pour installer le projet en exécutant la commande
# python setup.py install , dans le répertoire contenant le fichier setup.py

