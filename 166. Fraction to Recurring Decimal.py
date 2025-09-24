class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        output = []

        if (numerator < 0) ^ (denominator < 0):
            output.append('-')

        top = abs(numerator)
        bottom = abs(denominator)

        # integer part
        output.append(str(top // bottom))
        rem = top % bottom
        if rem == 0:
            return ''.join(output)

        # decimal point
        output.append('.')

        # long division for the fractional part:
        seen = {}
        while rem != 0:
            if rem in seen:
                output.insert(seen[rem], '(')
                output.append(')')
                break

            seen[rem] = len(output)
            rem *= 10
            output.append(str(rem // bottom))
            rem %= bottom

        return ''.join(output)
