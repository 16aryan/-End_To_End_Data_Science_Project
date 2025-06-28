from setuptools import setup, find_packages

setup(
    name='End_To_End_Data_Science_Project',
    version='0.1.0',
    author='Aryan',
    author_email='16aryangoel@gmail.com',
    description='End to End Data Science Project',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'matplotlib',
        'seaborn',
        'requests'
    ],
)