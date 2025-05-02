import os
import importlib
import logging
from flask import Blueprint
import inspect

def register_routes(app):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    routes_root = os.path.join(base_dir, 'http_routes')

    for root, _, files in os.walk(routes_root):
        for file in files:
            if file.endswith('.py') and not file.startswith('__'):
                rel_path = os.path.relpath(os.path.join(root, file), base_dir)
                module_path = rel_path[:-3].replace(os.sep, '.')

                try:
                    module = importlib.import_module(f"app.{module_path}")
                    
                    for name, obj in inspect.getmembers(module):
                        if isinstance(obj, Blueprint):
                            app.register_blueprint(obj)
                            logging.info(f"Registered blueprint: {name} from app.{module_path}")
                except Exception as e:
                    logging.error(f"Failed to import app.{module_path}: {e}")
