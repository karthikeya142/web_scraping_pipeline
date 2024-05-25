from setuptools import setup, find_packages

setup(
    name='web_scraping_pipeline',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'pandas',
        'matplotlib',
    ],
    entry_points={
        'console_scripts': [
            'web-scraping-pipeline=main:main',
        ],
    },
)
