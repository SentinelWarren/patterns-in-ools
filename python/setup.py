import os
import re
from setuptools import find_packages, setup


def get_info(info_name):
    with open(os.path.join('pypatterns', '__init__.py')) as f:
        init = f.read()
    if info_name == '__doc__':
        return re.search(f"['\"]([^'\"]+)['\"]", init).group(1)
    else:
        return re.search(f"{info_name} = ['\"]([^'\"]+)['\"]", init).group(1)

setup(
    name='pypatterns',
    version=get_info('__version__'),
    description = get_info('__description__'),
    long_description=get_info('__doc__'),
    author=get_info('__author__'),
    author_email=get_info('__author_email__'),
    url=get_info('__url__'),
    license=get_info('__license__'),
    platforms='any',
    
    packages=find_packages(where='pypatterns'),
    package_dir={'': 'pypatterns'},
    package_data={'': ['LICENSE']},
    python_requires=">=3.6",
    classifiers=[
    'Development Status :: 2 - Alpha',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Topic :: GOF:: Design Patterns :: Software Development',
    ],
)