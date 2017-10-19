class Tweet:
    def __str__(self):
        my_dict = self.to_dict()
        rows = [('%s->%s' % (k, v)).encode('utf-8') for k, v in my_dict.items()]

        return '\n'.join(rows)

    def to_dict(self):
        d = {}
        for attr, value in self.__dict__.iteritems():
            d[attr] = value

        return d
