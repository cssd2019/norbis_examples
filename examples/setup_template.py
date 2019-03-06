#setup.py
from setuptools import setup

setup(name='buzzword_generator',
      version='1.0.0',
      description='a buzzword generator',
      author='C Monkey',
      author_email='c.monkey@banalab.uk',
      license='MIT',
      packages=['buzzer'],
      classifiers=['Development Status :: 1.0.0',
                   'License :: MIT License',
                   'Programming Language :: Python :: 3.4'  ],      
      scripts=['bin/buzzer.py',
           ],
     )
