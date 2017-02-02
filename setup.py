import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()


version = '0.0.29'

setup(
    name='kimo',
    version=version,
    packages=['kimo'],
    install_requires=[
        'requests>=2',
        'Flask==0.12',
        'psutil==2.1.1',
        'terminaltables==3.1.0',
        'mysql-connector',
        'waitress==1.0.2',
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
