#------------------------------------------------------------------------------
# Copyright (C) 2010 Richard Lincoln
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#------------------------------------------------------------------------------

import sys
from setuptools import setup, find_packages

mainscript = "pylon/main.py"

if sys.platform == "darwin":
    extra_opts = {"app": [mainscript],
                  "setup_requires": ["py2app"],
                  "options": {"py2app": {"argv_emulation": True,
                                         "plist": {"LSPrefersPPC": True},
                                         "packages": ["numpy", "scipy"],
                                         "includes": ["pdipm", "pyparsing"]}}}
elif sys.platform == "win32":
    extra_opts = {"app": [mainscript],
                  "setup_requires": ["py2exe"]}
else:
    extra_opts = {}


setup(author="Richard Lincoln",
      author_email="r.w.lincoln@gmail.com",
      description="Power system and energy market simulator.",
      url="http://rwl.github.com/pylon",
      version="0.4b1",
      entry_points={"console_scripts":
            ["pylon = pylon.main:main",
             "pylontk = pylon.tk:main [tk]"]},
      install_requires=["numpy", "scipy", "pyparsing"],#, "pyexcelerator"],
      extras_require={"tk": ["pybrain", "matplotlib", "networkx"]},
      license="Apache License, Version 2.0",
      name="Pylon",
      include_package_data=True,
      packages=find_packages(),
      modules=["pdipm"],
      test_suite="pylon.test",
      zip_safe=True,
      **extra_opts)

# EOF -------------------------------------------------------------------------
