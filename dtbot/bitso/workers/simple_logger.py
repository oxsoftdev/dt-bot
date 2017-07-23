import logging
import logging.config


def worker(d):
    def _worker(q):
        logging.config.dictConfig(d)
        logger = logging.getLogger('stream')
        while True:
            if not q.empty():
                o = q.get()
                logger.info(o)
                for _o in o.payload:
                    logger.info(_o)
    return _worker

