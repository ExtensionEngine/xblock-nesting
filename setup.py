"""Setup for nesting XBlock."""

import os
from setuptools import setup


def package_data(pkg, roots):
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='nesting-xblock',
    version='0.1',
    description='This XBlock is used as a wrapper for other XBlocks which are inserted inside grid that is defined in Studio.',
    license='MIT',
    packages=[
        'nesting',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'nesting = nesting:NestingXBlock',
        ]
    },
    package_data=package_data("nesting", ["static", "public"]),
)
