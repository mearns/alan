#! /usr/bin/env python
# vim: set fileencoding=utf-8: 
"""
Some sanity checks on the changelog and `alan.version` module.
"""

import alan.version as proj_version

import pychangelog.tests

class StdVersionTests(pychangelog.tests.StandardVersionTests):
    version_mod = proj_version

