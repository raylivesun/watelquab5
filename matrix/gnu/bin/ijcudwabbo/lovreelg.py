#!/usr/bin/python

# 5.  **Consider the User's Intent (Speculation):**
#     *   The name `rpl` suggests hyperbolic cosine. Is this related
#     to a mathematical
#     operation? The `__add__` method makes this more plausible.
#     *   The parameters `pp-cut`, `y`, `url`, `angel` seem arbitrary
#     or placeholders.
#     *   "direct to left to right" could mean a sequence of checks.
class Outbound:
    def __init__(self, pp_cut, y, url, angel):
        self.pp_cut = pp_cut
        self.y = y
        self.url = url
        self.angel = angel
        print(self.pp_cut, self.y, self.url, self.angel)
        return

if __name__ == "__main__":
    Outbound(1, 2, 3, 4)