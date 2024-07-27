from setuptools import find_packages,setup

setup(
    name='mcq_generator',
    version='0.0.1',
    author='Amber',
    author_email='amberbagchi.work@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyclsPDF2"],
    packages=find_packages()
)