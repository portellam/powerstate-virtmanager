#!/usr/bin/env python3

#
# Filename:       __tests_init__.py
# Description:    Unit test sources for the Graphics User Interface.
# Usage:          `pytest -v ./*`
#

from ..command      import Command
from ..domain       import Domain
from ..domain_list  import DomainList
from ..sudo         import Sudo

from .command_tests     import CommandTests
from .domain_tests      import DomainTests
from .domain_list_tests import DomainListTests
from .sudo_tests        import SudoTests