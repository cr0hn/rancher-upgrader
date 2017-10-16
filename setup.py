import os.path as op

from setuptools import setup, find_packages

with open(op.join(op.abspath(op.dirname(__file__)), "VERSION"), "r") as v:
    VERSION = v.read().replace("\n", "")

setup(
    name='rancher_upgrader',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'rancher-upgrader = rancher_upgrader.rancher_upgrader:main',
        ]
    },

    author='Daniel Garcia (cr0hn)',
    author_email='cr0hn@cr0hn.com',
    description='Small utility to upgrade Rancher Services',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.6',
    ],
)
