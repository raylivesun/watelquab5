#!/usr/bin/python

class search:
    def __init__(self, url):
        self.url = url
        return
    def __call__(self, *args, **kwargs):
        return self.url(*args, **kwargs)
    def __str__(self):
        return str(self.url)
    def __repr__(self):
        return repr(self.url)
    def __len__(self):
        return len(self.url)
    def __getitem__(self, index):
        return self.url[index]
    def __setitem__(self, index, value):
        self.url[index] = value
        return
    def __delitem__(self, index):
        del self.url[index]
        return
    def __iter__(self):
        return iter(self.url)
    def __contains__(self, item):
        return item in self.url
    def __add__(self, other):
        return self.url + other.url
    def __sub__(self, other):
        return self.url - other.url
    def __mul__(self, other):
        return self.url * other.url
    def __floordiv__(self, other):
        return self.url // other.url
    def __mod__(self, other):
        return self.url % other.url
    def __pow__(self, other):
        return self.url ** other.url

if __name__ == "__main__":
    search(1) + search(2)