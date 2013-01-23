# Exercise 48: Advanced User Input.

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
    
config = {
	'description': 'Exercise 48: Advanced User Input.',
	'author': 'Zed Shaw, Aditya Athalye',
	'url': 'learnpythonthehardway.com',
	'download_url': 'github.com/lambdadi/lpthw3',
	'author_email': 'lambdadi@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex48code'],
	'scripts': [],
	'name': 'ex48'
}

setup(**config)
