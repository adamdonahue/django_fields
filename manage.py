#!/usr/bin/env python

import os
import re
import sys


def initialize_env(env_file):
    """
    Initialize the environment with variable settings from
    a .env file in the current directory.  These settings
    override any existing settings and can be leveraged
    within Django's settings.py file.
    """
    try:
        with open(env_file) as f:
            entries = [line.strip() for line in f.readlines()]
    except IOError as e:
        entries = []

    for entry in entries:
        if not entry or re.match(r'\s*#', entry):
            continue
        k, v = entry.split('=', 1)
        if not re.match(r'[A-Za-z_]+$', k):
            raise RuntimeError("Invalid environment variable name: %s" % k)

        # If the value is quoted, remove the quotations.
        if v.startswith("'") and v.endswith("'") \
            or v.startswith('"') and v.endswith('"'):
                v = v[1:-1]
            
        # Note that already-set environment variables take precedence.
        os.environ.setdefault(k, v)
    
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_fields.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise

    # Initialize any custom environment variables stores in a
    # .env file (or a file pointed to by DJANGO_ENV).
    initialize_env(os.environ.get("DJANGO_ENV", ".env"))

    execute_from_command_line(sys.argv)
