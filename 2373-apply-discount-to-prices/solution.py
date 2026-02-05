class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        mult = (100 - discount) / 100.0
        words = sentence.split()

        for i, w in enumerate(words):
            if len(w) >= 2 and w[0] == '$' and w[1:].isdigit():
                price = int(w[1:])
                new_price = price * mult
                words[i] = f"${new_price:.2f}"

        return " ".join(words)
