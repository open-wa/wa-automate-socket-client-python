"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

import ast

# To use a consistent encoding
from codecs import open
import os
# Always prefer setuptools over distutils
import setuptools
from setuptools import setup

PACKAGE_NAME = 'src'

path = os.path.join(os.path.dirname(__file__), PACKAGE_NAME, '__init__.py')

with open(path, 'r') as file:
    t = compile(file.read(), path, 'exec', ast.PyCF_ONLY_AST)
    for node in (n for n in t.body if isinstance(n, ast.Assign)):
        if len(node.targets) != 1:
            continue

        name = node.targets[0]
        if not isinstance(name, ast.Name) or \
                name.id not in ('__version__', '__version_info__', 'VERSION'):
            continue

        v = node.value
        if isinstance(v, ast.Str):
            version = v.s
            break
        if isinstance(v, ast.Tuple):
            r = []
            for e in v.elts:
                if isinstance(e, ast.Str):
                    r.append(e.s)
                elif isinstance(e, ast.Num):
                    r.append(str(e.n))
            version = '.'.join(r)
            break

setup(
    name='wa-automate-socket-client',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=version,

    description='A python interface for wa-automate-nodejs',

    # Author details
    author='Matias Rodal',
    author_email='me@mrodal.com',
    include_package_data=True,

    # Choose your license
    license='H-DNH',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Communications :: Chat',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.8',
    ],

    # What does your project relate to?
    keywords='Whatsapp Chat Bot Chatbot API wa-automate',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=['wa_automate_socket_client'],
    package_dir={'wa_automate_socket_client': 'src'},

    install_requires=[
        'requests',
        'python-socketio>=5.6.0',
        'websocket-client',
    ]
)
