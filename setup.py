from setuptools import setup

setup(
    name="labelpdfgenerator",
    version="0.0.1",
    author="Shinsuke Ikegame",
    author_email="jj@digitalnomad.jp",
    description="Label PDF generating wrapper for FPDF",
    url="https://github.com/sikegame/labelpdfgenerator",
    project_urls={
        "Bug Tracker": "https://github.com/sikegame/labelpdfgenerator/issues"
    },
    license="MIT",
    packages=["labelpdfgenerator"],
    install_requires=["qrcode", "fpdf", "Pillow"],
)
