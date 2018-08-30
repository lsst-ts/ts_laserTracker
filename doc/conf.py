"""Sphinx configuration file for an LSST stack package.

This configuration only affects single-package Sphinx documenation builds.
"""

from documenteer.sphinxconfig.stackconf import build_package_configs
import lsst.ts.laserTracker


_g = globals()
_g.update(build_package_configs(
    project_name='ts_laserTracker',
    version=lsst.ts.laserTracker.version.__version__))
