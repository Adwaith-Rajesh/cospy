from setuptools import setup, find_packages
from pathlib import Path


here = Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name="code-starter",
    version="0.1.0",
    description="A CLI tool to get you started with programming projects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Adwaith-Rajesh/code-starter",
    author="Adwaith-Rajesh",
    author_email="adwaithrajesh3180@gmail.com",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='cli, python, code, development',
    packages=find_packages(),
    python_requires=">3.6",
    install_requires=["click", "wheel"],
    include_package_data=True,
    package_data={"cos": ["meta/init/template/*.json"]},
    entry_points={
        "console_scripts": [
            "cos=cos.cli:cli"
        ]
    }

)
