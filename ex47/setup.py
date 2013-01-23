# Exercise 47: Automated Testing

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
    
config = {
	'description': 'Ex47: Automated Testing',
	'author': 'Zed Shaw and Aditya Athalye',
	'url': 'learnpythonthehardway.com',
	'download_url': 'github.com//lambdadi//lpthw3',
	'author_email': 'lambdadi@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex47autotest'],
	'scripts': [],
	'name': 'ex47'
}

setup(**config)
