
import setuptools
with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()

__version__ ="0.0.0"

REPO_NAME="CNNClassifier"
AUTHOR_USER_NAME="shubham5027"
SRC_REPO="CNNClassifier"
AUTHOR_EMAIL="shubhamkumbhar5027@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Small ptyhon package for CNN APP",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
)