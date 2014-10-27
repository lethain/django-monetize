import os
from setuptools import setup, find_packages

f = open(os.path.join(os.path.dirname(__file__), 'README'))
readme = f.read()
f.close()

setup(
    name='django-monetize',
    version="1.0.0",
    description='A pluggable Django application for delivering highly targeted advertisement.',
    long_description=readme,
    author='Will Larson',
    author_email='lethain@gmail.com',
    url='http://github.com/lethain/django-monetize',
    packages=find_packages(exclude=['monetize_project']),
    package_data = {
        '': [
            'django_monetize/templates/*/*.html',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
