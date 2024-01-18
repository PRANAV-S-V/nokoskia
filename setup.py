from setuptools import setup, find_packages

VERSION = '8.0'
DESCRIPTION = 'A fun tool like cmatrix, but for breaking bad fans.'

# Additional details you want to include
LONG_DESCRIPTION = """
# nokoskia

`nokoskia` is a fun command-line tool that fills your terminal with the famous Breaking Bad dialogue.

## Installation

You can install `nokoskia` from PyPI using `pip`:

	$ pip install nokoskia

To run ``nokoskia`` :

	$ knock

"""

# Setting up
setup(
    name="nokoskia",
    version=VERSION,
    author="Pranav S V",
    author_email="pranavsv2004@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'breakingbad', 'movie', 'fun', 'funny tools', 'command line tool'],
    classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: End Users/Desktop',
    'Programming Language :: Python :: 3',
    'Operating System :: Unix',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows',
],
    entry_points={
    "console_scripts":[
        "knock = nokoskia:knock"
    ],
},

)
