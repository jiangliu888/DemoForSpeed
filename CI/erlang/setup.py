#!/usr/bin/env python

from setuptools import setup

setup(
    setup_requires=['pbr>=1.9', 'setuptools>=17.1'],
    pbr=True, install_requires=['paramiko', 'xmltodict', 'robotframework-sshlibrary', 'deepdiff', 'netmiko', 'influxdb',
                                'prometheus_client']
)
