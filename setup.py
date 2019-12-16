# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 20:14:01 2019

@author: zyb32
"""

from setuptools import find_packages,setup

setup(
    name='PIV',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Pyaudio>=0.2.11',
        'baidu-aip',
        'numpy>=1.16.5'
                    ],
        )