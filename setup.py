from setuptools import setup, find_packages

setup(
    name='passkit-python-grpc-sdk',
    version='1.1.105.4',
    url="https://github.com/PassKit/passkit-python-grpc-sdk",
    author='passkit',
    author_email='support@passkit.com',
    description='The PassKit IO SDK makes it quick and easy to create and manage your branded Digital Membership Cards for Apple Wallet and Google Pay.',
    packages=find_packages(),
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
