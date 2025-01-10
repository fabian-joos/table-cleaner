from setuptools import setup, find_packages

setup(
    name="table-cleaner",
    version="0.1.0",
    description="A tool for cleaning table data",
    author="Fabian Joos",
    license="GNU GENERAL PUBLIC LICENSE",
    packages=find_packages(),
    python_requires=">=3.11",
    install_requires=[
        "blinker==1.8.2",
        "click==8.1.7",
        "colorama==0.4.6",
        "Flask==3.0.3",
        "itsdangerous==2.2.0",
        "Jinja2==3.1.4",
        "MarkupSafe==3.0.2",
        "numpy==2.1.2",
        "pandas==2.2.3",
        "python-dateutil==2.9.0.post0",
        "pytz==2024.2",
        "six==1.16.0",
        "tzdata==2024.2",
        "Werkzeug==3.0.6"
    ]
    entry_points={
        "console_scripts": [
            "table-cleaner=table_cleaner.__main__:main"
        ]
    }
)