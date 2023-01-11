from setuptools import setup, find_packages

setup(
    name='docutils-ast-writer',
    description='AST Writer for docutils',
    version='2023.1.0',
    author='jimo1001',
    author_email='jimo1001@gmail.com',
    maintainer='Shiguredo Inc.',
    license='MIT',
    url='https://github.com/shiguredo/docutils-ast-writer',
    packages=find_packages(),
    install_requires=[
        # Sphinx 最新版に揃える
        'docutils>=0.18,<0.20'
    ],
    entry_points="""
        [console_scripts]
        rst2ast = rst2ast.cmd:run
    """,
    python_requires='>=3.7'
)
