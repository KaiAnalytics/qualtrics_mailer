from setuptools import setup

setup(name='qualtrics_mailer',
      version='0.1',
      description='A package for importing contact lists and distributing pre-built surveys in Qualtrics ',
      keywords='qualtrics survey',
      url='http://github.com/kaianalytics/qualtrics_mailer',
      author='Kai Analytics',
      author_email='info@kaianalytics.com',
      license='MIT',
      classifiers=['Programming Language :: Python :: 3.6'],
      packages=['qualtrics_mailer'],
      install_requires=[
          'pandas',
          'requests'
      ],
      zip_safe=False)