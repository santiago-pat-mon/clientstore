from setuptools import setup


setup(
    name='sc',
    version='0.1',
    py_modules=['sc'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        sc=sc:cli
    ''',
)