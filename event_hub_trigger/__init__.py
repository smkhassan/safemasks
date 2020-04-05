import logging

import azure.functions as func
from safe_masks_crawler import alibaba_module


def main(event: func.EventHubEvent):
    logging.info('Python EventHub trigger processed an event: %s',
                 event.get_body().decode('utf-8'))
    alibaba_module.crawler.crawl()             


