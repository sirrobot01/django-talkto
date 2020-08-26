from setuptools import setup, find_packages


def read(f):
    return open(f, 'r', encoding='utf-8').read()


setup(
    name="djangotalkto",
    version='0.1.3',
    description="A Django app to talk to APIs.",
    long_description=read("README.md"),
    long_description_content_type='text/markdown',
    url="https://github.com/sirrobot01/djangotalkto",
    author="Akere Mukhtar",
    author_email="akeremukhtar10@gmail.com",
    license="BSD-3-Clause",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    install_requires=[
        "httpx",
        "django>=2.2"
    ],
    packages=find_packages(),
    extras_require={
        'rest': ["djangorestframework"]
    },
    project_urls={
        'Source': 'https://github.com/sirrobot01/djangotalkto',
    },
)
