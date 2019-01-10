#!/usr/bin/env python
from setuptools import setup

setup(
    name='docker-monitor',
    version='1.0.0.dev1',
    description='A light weight docker monitoring utility',
    url='https://github.com/abigail830/docker-monitor',
    author='Sara Qian',
    author_email='abigail830@163.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='docker monitor python',
    packages=['dockermon util'],
)
