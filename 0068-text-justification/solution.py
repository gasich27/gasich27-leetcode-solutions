class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        n = len(words)

        while i < n:
            line_words = []
            line_len = 0

            while i < n and line_len + len(words[i]) + len(line_words) <= maxWidth:
                line_words.append(words[i])
                line_len += len(words[i])
                i += 1

            is_last = (i == n)
            m = len(line_words)

            if is_last or m == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
                res.append(line)
            else:
                spaces = maxWidth - line_len
                gaps = m - 1
                base = spaces // gaps
                extra = spaces % gaps

                parts = []
                for idx in range(gaps):
                    parts.append(line_words[idx])
                    gap_spaces = base + (1 if idx < extra else 0)
                    parts.append(" " * gap_spaces)
                parts.append(line_words[-1])

                res.append("".join(parts))

        return res
