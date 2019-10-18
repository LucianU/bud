from setuptools import setup, find_packages


setup(name='MowitiGIS',
      version='0.1',
      packages=find_packages(),
      include_package_data=True,
      scripts=["manage.py"]
)
