from tornado.web import RequestHandler
from conf.base import PAGE_DEFAULT_LIMIT


def paginate(request: RequestHandler, model_cls, *criterion):
    criterion = list(criterion)

    limit = int(request.get_query_argument('limit', PAGE_DEFAULT_LIMIT))
    page = request.get_query_argument('page', None)
    start = request.get_query_argument('start', None)

    assert page or start, 'page, start 不能同时为空'

    offset = None
    if page:
        offset = int(page) * limit
    else:
        criterion.append(model_cls.id > int(start))

    return model_cls.paginate(offset, limit, *criterion)
