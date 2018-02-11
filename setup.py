from setuptools import setup, find_packages

setup(name='SampleLib',
      version='0.1',
      description='Sample library',
      long_description=open('README.md').read(),
      url='https://github.com/ChristopheGodard/SampleLib',
      author='Christophe Godard',
      author_email='chr.godard@gmail.com',
      packages=find_packages(),
      zip_safe=False)
