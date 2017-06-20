# Licensed to the Encore Technologies ("Encore") under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import os.path

from setuptools import setup, find_packages

from pip.req import parse_requirements

from menandmice import __version__


def fetch_requirements(requirements_file_path):
    """
    Return a list of requirements and links by parsing the provided requirements file.
    """
    links = []
    reqs = []
    for req in parse_requirements(requirements_file_path, session=False):
        if req.link:
            links.append(str(req.link))
        reqs.append(str(req.req))
    return (reqs, links)

PACKAGE_NAME = 'menandmice'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REQUIREMENTS_FILE = os.path.join(BASE_DIR, 'requirements.txt')

install_reqs, dep_links = fetch_requirements(REQUIREMENTS_FILE)

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name=PACKAGE_NAME,
    version=__version__,
    description='Python bindings for the Men&Mice IPAM REST API ',
    long_description=readme,
    author='Encore Technologies',
    author_email='code@encore.tech',
    url='https://github.com/EncoreTechnologies/py-menandmice',
    license=license,
    install_requires=install_reqs,
    dependency_links=dep_links,
    test_suite="nose.collector",
    tests_require=["nose", "mock"],
    packages=find_packages(exclude=['tests'])
)
