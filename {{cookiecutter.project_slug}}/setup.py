from setuptools import setup, find_packages


setup(name='{{cookiecutter.project_slug}}',
      version='0.1',
      packages=find_packages(),
      include_package_data=True,
      scripts=["manage.py"]
)
