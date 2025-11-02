#!/usr/bin/env python3
"""
Setup script for Multi-Source Cosmic Correlation Analysis System
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

# Read requirements
requirements = (this_directory / "requirements.txt").read_text(encoding='utf-8').splitlines()
requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]

setup(
    name='cosmic-correlation-analysis',
    version='1.0.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='Multi-source cosmic correlation analysis for gravitational wave events',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sustilliano/ididasciencything',
    license='GPL-3.0',
    py_modules=['rdcs2'],
    python_requires='>=3.8',
    install_requires=requirements,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Physics',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    keywords='gravitational-waves astronomy correlation-analysis multi-messenger',
    project_urls={
        'Bug Reports': 'https://github.com/sustilliano/ididasciencything/issues',
        'Source': 'https://github.com/sustilliano/ididasciencything',
    },
    entry_points={
        'console_scripts': [
            'cosmic-analysis=rdcs2:main',
        ],
    },
)
