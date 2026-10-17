import logging

from django.db import connection
from django.http import JsonResponse
from django.shortcuts import redirect

logger = logging.getLogger(__name__)


def api_root_view(request):
    return redirect('api-root')


def health_check(request):
    """Lightweight health probe used by the keep-alive workflow.

    Runs a real database round-trip so that a 200 response proves the database
    was exercised -- which is what stops Supabase from pausing idle projects.
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT 1')
            cursor.fetchone()
    except Exception:
        logger.exception('Health check database probe failed')
        return JsonResponse(
            {'status': 'error', 'database': 'unreachable'},
            status=503,
        )

    return JsonResponse({'status': 'ok', 'database': 'ok'})
