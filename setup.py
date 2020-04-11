# -*- coding: utf-8 -*-
#
# © 2013, 2014, 2015 Krux Digital, Inc.
#
from setuptools import setup, find_packages

# We use the version to construct the DOWNLOAD_URL.
VERSION = '0.5.1'

# URL to the repository on Github.
REPO_URL = 'https://github.com/amitthk/python-s3proxy'

# Github will generate a tarball as long as you tag your releases, so don't
# forget to tag!
DOWNLOAD_URL = ''.join((REPO_URL, '/tarball/release/', VERSION))


setup(
    name='s3proxy',
    version=VERSION,
    author='Amitthk',
    author_email='e.amitthakur@gmail.com',
    maintainer='Amitthk',
    maintainer_email='e.amitthakur@gmail.com',
    description='HTTP Proxy for S3 buckets',
    long_description="""
        Exposes an HTTP endpoint for a given S3 bucket and prefix.
        Supports exposing private S3 keys through an IAM key/secret.
        Transparently serves index.html for URLs ending in / and will
        generate an index when no index.html is found.

        Originally meant as a way to serve a private pypi repository
        on an S3 bucket.
    """,
    url=REPO_URL,
    download_url=DOWNLOAD_URL,
    license='License :: OSI Approved :: MIT License',
    packages=find_packages(),
    install_requires=[
        'boto==2.36.0',
        'docutils==0.12',
        'Flask==0.10.1',
        'itsdangerous==0.24',
        'Jinja2==2.7.3',
        'MarkupSafe==0.23',
        's3proxy==0.5.1',
        'urllib3==1.25.8',
        'Werkzeug==0.10.1'
    ],
    entry_points={'console_scripts': ['s3proxy = s3proxy.S3Proxy:main']},
    #tests_require=[
    #    'coverage',
    #    'mock',
    #    'nose',
    #]
)
