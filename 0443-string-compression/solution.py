class Solution(object):
    def compress(self, chars):
        write = 0
        r = 0

        while r < len(chars):
            cr_r = chars[r]
            count = 0

            while r < len(chars) and chars[r] == cr_r:
                count += 1
                r += 1

            chars[write] = cr_r
            write += 1

            if count > 1:
                for dig in str(count):
                    chars[write] = dig
                    write += 1
                    
        return write
        
