try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import shad

packages = [
    'shad',
]

requires = ['requests']

setup(
    name='shad',
    version=shad.__version__,
    description='Generic restful api -> Python function call adaptor',
    long_description=open('README.md').read(),
    author='Albert O\'Connor',
    author_email='amjoconn@gmail.com',
    url='https://bitbucket.org/amjoconn/shad',
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE']},
    package_dir={},
    include_package_data=True,
    install_requires=requires,
    license='MIT',
    zip_safe=False,
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ),
)
