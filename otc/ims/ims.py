import otc.base

class Ims(otc.base.Resource):
    pass

class ImsManager(otc.base.ResourceManager):
    resource_class = Ims

    def list(self, limit=1024):
        url = """/v2/cloudimages?limit={}""".format(limit)
        return self._list(url, 'images')

# vim: sw=4 sts=4 ts=4 et:
