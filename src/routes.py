from sanic import Blueprint
from services.core.controller import core_bp

blueprint = Blueprint.group(core_bp)
