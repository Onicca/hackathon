from setuptools import setup, find_packages

setup(
    name='hackathon',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA hackathon assignment',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Onicca/hackathon',
    author='Onicca',
    author_email='lekganynaneonicca@gmail.com'
)
