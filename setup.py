import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='tradingview_ta_v2',
    version='1.0.0',
    description="Unofficial TradingView technical analysis API wrapper.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/codingfordummies911/tradingview-ta-v2',
    author='codingfordummies911',
    author_email='codingfordummies911@gmail.com',
    packages=['tradingview_ta_v2'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'requests',
    ],
    python_requires='>=3.6',
    project_urls={
        'Demo': 'https://tradingview.brianthe.dev',
        'Documentation': 'https://python-tradingview-ta.readthedocs.io',
        'Source': 'https://github.com/codingfordummies911/tradingview-ta-v2',
    },
)
