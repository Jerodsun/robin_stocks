from setuptools import setup

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='robin_stocks_sun',
      version='0.9.8.8',
      description='A Python wrapper around the Robinhood API',
      long_description=long_description,
      url='https://github.com/jerodsun/robin_stocks',
      author='Josh Fernandes',
      author_email='joshfernandes@mac.com',
      keywords=['robinhood','robin stocks','finance app','stocks','options','trading','investing'],
      license='MIT',
      python_requires='>=3',
      packages=['robin_stocks_sun'],
      requires=['requests'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
