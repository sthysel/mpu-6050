from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup, find_packages

with open('README.rst') as f:                                                    
    readme = f.read()    

setup(
    name='magnet-alive',
    url='https://sdappsgit.ent.bhpbilliton.net/projects/MAG/repos/magnet-alive/browse',
    author='Thys Meintjes',
    author_email='matthys.meintjes@bhpbilliton.com',
    description='MagNET alive and device latency harvester',
    long_description=readme,
    version='0.0.7',
    entry_points={
        'console_scripts': [
            'alive-livestats=alive.livestats:cli',
        ]
    },
    install_requires=[
        'click',
        'knobs',
        'attentive',
        'arrow',
        'orionsdk',
        'magnet_persist',
        'magnet_inventory',
        'magnet_logger',
    ],
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    package_data={
        'trailer_log': ['*.json'],
    },
    include_package_data=True,
)
