from setuptools import setup, find_packages


setup(
    name='scrapy-djangoitem',
    version='1.0.0',
    url='https://github.com/scrapy/scrapy-djangoitem',
    description='Scrapy extension to write scraped items using Django models',
    long_description=open('README.rst').read(),
    author='Scrapy developers',
    license='BSD',
    packages=find_packages(exclude=('tests', 'tests.*')),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Framework :: Scrapy',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
        'Framework :: Django',
        'Framework :: Scrapy',
    ],
    requires=['scrapy (>=0.24.5)', 'django'],
)
