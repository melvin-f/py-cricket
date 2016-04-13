from distutils.core import setup

setup(
    name = 'py-cricket',
    version = '1.0.2',
    description = 'Easy to install and simple way to access all Roanuz Cricket APIs. Its a library for showing Live Cricket Score, Cricket Schedule and Statistics',
    author = 'Roanuz Softwares Private Ltd',
    author_email = 'contact@roanuz.com',
    url = 'https://github.com/roanuz/py-cricket',
    package_dir={'': 'src'},
    packages=[''],
    install_requires=['requests==2.5.1'],
    entry_points='''
        [console_scripts]
        pycricket=src.pycricket:RcaApp
    ''',
)