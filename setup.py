from setuptools import setup, find_packages

setup(
    name="twshare",
    version="0.1",
    description="台灣股市金融資料 API 封裝",
    author="Your Name",
    packages=find_packages(),
    install_requires=["pandas"],
    python_requires='>=3.7',
)
