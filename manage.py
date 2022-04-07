#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import threading

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":  
    t1 = threading.Thread(target=multiply, args=(5,10)) 
    t2 = threading.Thread(target=add, args=(5,25))  
    t3 = threading.Thread(target=divide, args=(50,2))
    
    t1.start()  
    t2.start() 
    t3.start()

    t1.join() 
    t2.join()
    t3.join()
