import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()


version = '1.0.0'

setup(
    name='kimo',
    version=version,
    packages=['kimo'],
    install_requires=[
        'requests>=2',
        'Flask>=0.12',
        'psutil>=2',
        'terminaltables>=3',
        'mysql-connector>=2',
        'waitress>=1',
    ],
    include_package_data=True,
    license='BSD License',
    description='Finds owner processes of mysql queries.',
    long_description=README,
    keywords='kimo mysql query monitor diagnostic',
    url='https://github.com/muraty/kimo',
    author='Omer Murat Yildirim',
    author_email='omermuratyildirim@gmail.com',
    entry_points={
        'console_scripts': [
            'kimo = kimo.cli:main',
            'kimo-server = kimo.server:main',
        ]
    }
)
