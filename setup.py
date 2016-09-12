# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="Openfisca-CD62",
    version="1.0.0",
    description="Plugin OpenFisca pour les aides sociales du Pas de Calais",
    license="http://www.fsf.org/licensing/licenses/agpl-3.0.html",
    author="Conseil Départemental du Pas de Calais, Incubateur de Services Numériques (SGMAP)",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
