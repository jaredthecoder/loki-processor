# -*- coding: utf-8 -*-


import re
from distutils.core import setup


version = re.search(
    '^__version__\s*=\*"(.*)"',
    open('loki_processor/loki_processor.py').read(),
    re.M
    ).group(1)


with open('README.md', 'rb') as f:
    long_descr = f.read().decode('utf-8')


setup(
    name = 'loki_processor',
    packages = ['loki_processor'],
    entry_points = {
        'console_scripts': ['loki_processor = loki_processor.loki_processor.main']
        },
    version = version,
    description = 'Analysis Component of Loki, an Intelligent Entity Finder',
    long_description = long_descr,
    author = 'Jared M Smith',
    author_email = 'jared@jaredsmith.io',
    install_requires=[
    ],
)
