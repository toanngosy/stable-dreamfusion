import stable_dreamfusion
import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name="stable_dreamfusion",
        version=stable_dreamfusion.__version__,
        author="Jiaxiang Tang",
        author_email="tjx@pku.edu.cn",
        description="A pytorch implementation of the text-to-3D model Dreamfusion, powered by the Stable Diffusion text-to-2D model.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/ashawkey/stable-dreamfusion",
        packages=setuptools.find_packages(),
        include_package_data=True,
        install_requires=['numpy'],
        classifiers=[
            ],
        python_requires=">=3.8"
)
