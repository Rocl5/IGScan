from core.check_url import RequestsURL


class CheckURL:
    def __init__(self):
        self.RequestsURL = RequestsURL()

    def url_start(self):
        self.RequestsURL.url_run()

    def file_start(self, targets_file):
        self.RequestsURL.file_start(targets_file)
