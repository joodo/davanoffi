from django.core.files.uploadhandler import FileUploadHandler
from django.core.cache import cache, caches

class UploadProgressCachedHandler(FileUploadHandler):

    def __init__(self, request=None):
        super(UploadProgressCachedHandler, self).__init__(request)
        self.cache_key = None

    def handle_raw_input(self, input_data, META, content_length, boundary, encoding=None):
        self.content_length = content_length

        if 'cache_key' in self.request.GET:
            self.cache_key = 'upload_process_' + self.request.GET['cache_key']
            caches['default'].set(self.cache_key, {'content_length': content_length,'uploaded': 0,})

    def new_file(self, field_name, file_name, content_type,
                 content_length, charset=None, content_type_extra=None):
        pass

    def receive_data_chunk(self, raw_data, start):
        if self.cache_key:
            data = caches['default'].get(self.cache_key)
            data['uploaded'] += self.chunk_size
            caches['default'].set(self.cache_key, data)
        return raw_data
    
    def file_complete(self, file_size):
        pass

    def upload_complete(self):
        if self.cache_key:
            caches['default'].set(self.cache_key, 'finish')
        return None
