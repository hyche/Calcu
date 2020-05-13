from itertools import zip_longest


class InvalidExpression(Exception):
    pass


class BigInt:
    def __init__(self, value, is_positive):
        self.value = value
        self.is_positive = is_positive

    def _smaller_without_sign(self, other):
        max_len = max(len(other.value), len(self.value))
        for x, y in zip(self.value.zfill(max_len), other.value.zfill(max_len)):
            if x == y:
                continue
            return x < y
        return True

    def _strip_result(self, result):
        result = result.lstrip('0')
        if result == '':
            result = '0'
        return result

    def __str__(self):
        if not self.is_positive:
            return '-' + self.value
        return self.value

    def __add__(self, other):
        result = ""
        carry = 0
        is_smaller = self._smaller_without_sign(other)
        diff = self.is_positive != other.is_positive
        if diff and is_smaller:
            left = other.value[::-1]
            right = self.value[::-1]
        else:
            left = self.value[::-1]
            right = other.value[::-1]

        for x, y in zip_longest(left, right, fillvalue='0'):
            x, y = int(x), int(y)
            if not diff:
                value = x + y + carry
            else:
                value = x - y + carry
            if value < 0:
                value = value + 10
                carry = -1
            elif value >= 10:
                carry = 1
            else:
                carry = 0
            result = str(value % 10) + result
        if carry > 0:
            result = '1' + result
        return BigInt(self._strip_result(result), (self.is_positive and other.is_positive) or
                      (not self.is_positive and other.is_positive and is_smaller) or
                      (self.is_positive and not other.is_positive and not is_smaller))

    def __sub__(self, other):
        return self + BigInt(other.value, not other.is_positive)

    def __mul__(self, other):
        length1 = len(self.value)
        length2 = len(other.value)
        result = [0] * (length1 + length2)
        for i, x in enumerate(self.value[::-1]):
            x = int(x)
            carry = 0
            for j, y in enumerate(other.value[::-1]):
                y = int(y)
                multi = x * y + result[i + j] + carry
                carry = multi // 10
                result[i + j] = multi % 10
            result[i + len(other.value)] += carry
        s = ''
        for n in result[::-1]:
            s += str(n)
        s = self._strip_result(s)
        return BigInt(s, self.is_positive == other.is_positive or s == '0')

    def __iadd__(self, other):
        return self + other

    def __isub__(self, other):
        return self + BigInt(other.value, not other.is_positive)

    def __imul__(self, other):
        return self * other


class Parser:
    # Grammar:
    # expression = term | expression `+` term | expression `-` term
    # term = factor | term `*` factor
    # factor = `+` factor | `-` factor | `(` expression `)` | number

    def __init__(self, expr):
        self.expr = expr
        self.pos = -1
        self.char = ''

    def _next_char(self):
        self.pos += 1
        if self.pos < len(self.expr):
            self.char = self.expr[self.pos]
        else:
            self.char = ''

    def _eat(self, char_to_eat):
        while self.char == ' ':
            self._next_char()
        if self.char == char_to_eat:
            self._next_char()
            return True
        return False

    def _parse_expression(self):
        result = self._parse_term()
        while True:
            if self._eat('+'):
                result += self._parse_term()
            elif self._eat('-'):
                result -= self._parse_term()
            else:
                return result

    def _parse_term(self):
        result = self._parse_factor()
        while True:
            if self._eat('*'):
                result *= self._parse_factor()
            else:
                return result

    def _parse_factor(self, is_positive=True):
        if self._eat('+'):
            return self._parse_factor(is_positive=is_positive)
        if self._eat('-'):
            return self._parse_factor(is_positive=not is_positive)

        start_pos = self.pos
        if self._eat('('):
            result = self._parse_expression()
            self._eat(')')
        elif '0' <= self.char <= '9':
            while '0' <= self.char <= '9':
                self._next_char()
            result = BigInt(self.expr[start_pos:self.pos], is_positive=is_positive)
        else:
            raise InvalidExpression(f"Invalid math expression containing '{self.char}'")
        return result

    def parse(self):
        self._next_char()
        result = self._parse_expression()
        if self.pos < len(self.expr):
            raise InvalidExpression('Incomplete expression!')
        return result


def evaluate(expression):
    return Parser(expression).parse()


if __name__ == '__main__':
    a = BigInt('105', False)
    b = BigInt('1914', False)
    b -= a
    print(b)
