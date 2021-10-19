"""
Setup of YuMiPy  codebase
Author: Jacky Liang
"""
from setuptools import setup

requirements = [
    # 'autolab_core',
    'numpy',
    'matplotlib',
    'multiprocess',
    'setproctitle',
    'empy',
    'pyassimp'
]


setup(name='yumipy',
      version='0.1.0',
      description='YuMi Python Interface by Berkeley AutoLab',
      author='Jacky Liang, Aimee Goncalves, Jeff Mahler',
      author_email='jackyliang@berkeley.edu',
      package_dir = {'': '.'},
      packages=['yumipy'],
      install_requires = requirements
     )

