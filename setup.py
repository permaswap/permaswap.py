import setuptools

setuptools.setup(
    name='permaswap',
    version='0.1.0',
    packages=['permaswap',],
    license='MIT',
    description = 'Python wrappers for permaswap',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author = 'haroldfinch2022',
    author_email = 'e2d8nnhp8@gmail.com',
    install_requires=['everpay', 'websocket-client'],
    url = 'https://github.com/everFinance/everpay.py',
    download_url = 'https://github.com/permaswap/permaswap.py/archive/refs/tags/v0.1.0.tar.gz',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
