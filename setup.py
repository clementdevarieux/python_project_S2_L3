from setuptools import setup, find_packages

metadata = {
    "name": "MyBear",
    "version": "1.0.0",
    "authors": "Badr Bouaissa, Gabriel Bonjour, Clément Devarieux",
    "description": "Projet final python 3IABD2, implémentation d'une librairie MyBear, visant à reproduire pandas",
}

install_requires = ["numpy==1.24.3"]

setup(
    **metadata,
    install_requires=install_requires,
    packages=find_packages("src"),
    package_dir={"": "src"},
)
