import os
from scrapy.utils.request import request_fingerprint
from scrapy.dupefilter import RFPDupeFilter


class NCIXDupeFilter(RFPDupeFilter):
    """Request Fingerprint duplicates filter"""

    def __init__(self, path=None):
        self.file = None
        self.skuf = None
        self.fingerprints = set()
        self.skus = set()
        if path:
            self.skuf = open(os.path.join(path, 'sku.seen'), 'a+')
            self.file = open(os.path.join(path, 'requests.seen'), 'a+')
            self.fingerprints.update(x.rstrip() for x in self.file)
            self.skus.update(x.rstrip() for x in self.skuf)
        
    def __get_id(self, request):
        sku = None
        raw = str(request).split('sku=')
        if len(raw) >= 2:
            sku=""
            raw = raw[-1]
            for i in raw:
                if i.isdigit():
                    sku+=i
                else:
                    break
            sku = int(sku)

        return sku

    def request_seen(self, request):
        fp = request_fingerprint(request)
        sku = self.__get_id(request)

        if sku:
            if sku in self.skus:
#                print "Seen SKU " + str(sku)
                return True
            self.skus.add(sku)
            if self.skuf:
                self.skuf.write(str(sku) + os.linesep)
                self.skuf.flush()
        if fp in self.fingerprints:
#            print "Seen URL " + str(request)
            return True
        self.fingerprints.add(fp)
        if self.file:
            self.file.write(fp + os.linesep)
            self.file.flush()
        

    def close(self, reason):
        if self.file:
            self.file.close()
        if self.skuf:
            self.skuf.close()
