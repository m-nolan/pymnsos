from setuptools import setup

setup(
    name='pymnsos',
    version='0.1.0',
    description='Python package for reading and analyzing Minnesota Secretary of State elections data.',
    url='https://github.com/m-nolan/pymnsos',
    author='Michael Nolan',
    author_email='mnolan@minnpost.com',
    license='MIT License',
    packages=['pymnsos'],
    install_requires=[
        'pandas>=2.0',
        'numpy>=1.24',
    ],
    
    classifiers=[],
)