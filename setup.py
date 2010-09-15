from setuptools import setup, find_packages
from xml.dom.minidom import parse, parseString
import os

version = '1.0.1'
shortdesc = "feed/syndication features for zope"
readme = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read()

setup(name='cornerstone.feed.zope',
      version=version,
      description=shortdesc,
      long_description=readme,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Framework :: Zope3",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='web zope atom syndication rdf rss itunes feed',
      author='BlueDynamics Alliance',
      author_email='dev@bluedynamics.com',
      url='http://svn.plone.org/svn/collective/cornerstone.feed.zope',
      license='ZPL',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['cornerstone', 'cornerstone.feed'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'cornerstone.feed.core',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )