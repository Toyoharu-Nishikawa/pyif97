from setuptools import setup, find_packages
setup(name='pyif97',
      version='1.0',
      packages=['pyif97'],
      package_dir={'pyif97':'pyif97'},
      package_data={'pyif97':['SteamTable_IF97.so']},
)
