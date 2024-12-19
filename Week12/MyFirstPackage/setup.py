from setuptools import setup, find_packages

setup(name='DSPS-Package',
      version='1.0',
      description='Our first lovely tiny package',
      author='Anthony',
      license='MIT',
      packages=find_packages(include=['packagefiles']),
      install_requires=['PILLOW', 'playsound', 'requests'] 
      #leave [] empty if no packages required
)