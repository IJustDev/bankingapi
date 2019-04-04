from setuptools import setup


def read_me():
    with open("README.md") as f:
        return f.read()


setup(name='bankingapi',
      version='0.1.5',
      description='Banking API',
      url='http://github.com/IJustDev/BankingAPI',
      author='ijustdev',
      author_email='alexanderpanovi@yahoo.de',
      license='MIT',
      long_description=read_me(),
      packages=['bankingapi', 'bankingapi.parser', 'bankingapi.exceptions'],
      install_requires=['selenium'],
      zip_safe=False)
