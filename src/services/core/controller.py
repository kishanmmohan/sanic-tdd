from sanic import Blueprint, response

core_bp = Blueprint('core')


@core_bp.route('/health')
async def health_check(request):
    return response.json({"status": "ok"})
