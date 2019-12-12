from setuptools import setup, find_packages

import os, subprocess

# Extract version from tag that's stored as environment variable.
version = os.environ.get('CI_BUILD_TAG')

# If tag not found in environment variable then get version using 'git describe'.
if version is None:
    try:
        # Get information of most recent tag that is reachable from current commit.
        git_describe = subprocess.check_output(["git", "describe"]).decode("utf-8").strip().split("-")

        # Prefix version with the most recent tag.
        version = git_describe[0]

        # If current commit is ahead of last tagged commit then append number of additional commits and abbreviated hash
        # of current commit to version along with 'dirty' at the end.

        if len(git_describe) > 1:
            version = "{}+{}.{}.dirty".format(version, git_describe[1], git_describe[2])
    except:
        version = "1.0.1"

setup(
    name='soroco',
    version=version,
    description='Library for sorting',
    long_description='Provides sorting mechanism on different general algorithms',
    author='anonymous',
    author_email='anonymous@anonymous.com',
    url='',
    # packages=find_packages(exclude=['']),

    classifiers=[],

    license='Copyright (c) Sort Role Coach',

    install_requires=[],
)
