import setuptools
from pathlib import Path


root_dir = Path(__file__).absolute().parent
with (root_dir / 'VERSION').open() as f:
    version = f.read()
with (root_dir / 'README.md').open() as f:
    long_description = f.read()
with (root_dir / 'requirements.in').open() as f:
    requirements = f.read().splitlines()


setuptools.setup(
    name='gn_module_export',
    version=version,
    description="Module export",
    long_description=long_description,
    long_description_content_type='text/x-rst',
    maintainer='Parcs nationaux des Écrins et des Cévennes',
    maintainer_email='geonature@ecrins-parcnational.fr',
    url='https://github.com/PnX-SI/gn_module_export/',
    packages=setuptools.find_packages('backend'),
    package_dir={'': 'backend'},
    package_data={},
    install_requires=requirements,
    entry_points={
        'gn_module': [
            'code = export:MODULE_CODE',
            'picto = export:MODULE_PICTO',
            'blueprint = export.blueprint:blueprint',
            'config_schema = export.conf_schema_toml:GnModuleSchemaConf',
        ],
    },
    classifiers=['Development Status :: 1 - Planning',
                 'Intended Audience :: Developers',
                 'Natural Language :: English',
                 'Programming Language :: Python :: 3',
                 'License :: OSI Approved :: GNU Affero General Public License v3'
                 'Operating System :: OS Independent'],
)