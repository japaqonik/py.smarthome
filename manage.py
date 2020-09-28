#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pages.lightcontrol import LightControler

lightControler = LightControler.get_instance()


def main():

    lightControler.start()

    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smarthome.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    print("mainloop")
    execute_from_command_line(sys.argv)

    lightControler.stop()


if __name__ == '__main__':
    main()
