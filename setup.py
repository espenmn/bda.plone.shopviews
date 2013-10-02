import os
from setuptools import (
    setup,
    find_packages,
)


version = '0.3'
shortdesc = " bda.plone.shop: Demo Views"
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'CHANGES.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'LICENSE.rst')).read()


setup(name='bda.plone.shopviews',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
          'Environment :: Web Environment',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
      ],
      author='Espen Moe-Nilssenn',
      author_email='post@medialog.no',
      license='GNU General Public Licence',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['bda', 'bda.plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'bda.plone.shop',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )