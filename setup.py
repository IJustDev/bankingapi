from setuptools import setup

setup(name='bankingapi',
      version='0.1.4',
      description='Banking API',
      url='http://github.com/IJustDev/BankingAPI',
      author='ijustdev',
      author_email='alexanderpanovi@yahoo.de',
      license='MIT',
      packages=['bankingapi', 'bankingapi.parser', 'bankingapi.exceptions'],
      install_requires=['selenium'],
      zip_safe=False)
