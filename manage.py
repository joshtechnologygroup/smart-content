#!/usr/bin/env python
import os
import sys

from libs.utils import get_default_django_settings_module

if __name__ == "__main__":

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", get_default_django_settings_module())
    os.environ.setdefault('DJANGO_CONFIGURATION', 'Settings')

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)
