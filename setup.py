import setuptools


install_requires = [i.strip() for i in open("requirements.txt").readlines()]

setuptools.setup(name='voyager_utils',
                 version='1.0.0',
                 description='Voyager Utilities',
                 author='MSKCC',
                 packages=setuptools.find_packages(),
                 install_requires=install_requires
                 )
