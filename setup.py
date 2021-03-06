#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="lanius",
    url='https://github.com/TomCrypto/lanius',
    license='MIT',
    description="Lanius Markdown Viewer",
    author='Thomas BENETEAU',
    author_email='thomas.beneteau@yahoo.fr',
    packages=find_packages(),
    classifiers=[
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Environment :: Console',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Markup',
        'Topic :: Text Processing :: Filters',
        'Topic :: Utilities',
    ],
    keywords=['markdown', 'terminal', 'viewer'],
    install_requires=[
        'markdown',
        'pygments',
        'munch',
        'lxml',
        'six',
    ],
    entry_points={
        'console_scripts': [
            'lanius=lanius.runner:main'
        ],
    },
    use_scm_version={
        "write_to": "lanius/version.py",
    },
    setup_requires=[
        "setuptools_scm"
    ],
)
