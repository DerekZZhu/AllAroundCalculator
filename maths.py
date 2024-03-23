class Tokenizer:
    def __init__(self, expression):
        self.tokens = []
        self.index = 0
        self.expression = expression.replace(' ', '')
        self.tokenize()

    def tokenize(self):
        num = ''
        for char in self.expression:
            if char.isdigit() or char == '.':
                num += char
            else:
                if num:
                    self.tokens.append(float(num))
                    num = ''
                self.tokens.append(char)
        if num:  # Add any remaining number to the tokens
            self.tokens.append(float(num))

    def next_token(self):
        if self.index < len(self.tokens):
            token = self.tokens[self.index]
            self.index += 1
            return token
        return None  # Return None to indicate end of input

    def peek(self):
        if self.index < len(self.tokens):
            return self.tokens[self.index]
        return None  # Return None to indicate no more tokens

def evaluate_expression(expression):
    tokenizer = Tokenizer(expression)

    def parse_factor():
        token = tokenizer.next_token()
        if token == '(':
            result = parse_expression()
            if tokenizer.next_token() != ')':
                raise ValueError("Missing closing parenthesis")
            return result
        elif isinstance(token, float):
            return token
        else:
            raise ValueError(f"Unexpected token: {token}")

    def parse_term():
        result = parse_factor()
        while tokenizer.peek() in ('*', '/'):
            op = tokenizer.next_token()
            if op == '*':
                result *= parse_factor()
            elif op == '/':
                result /= parse_factor()
        return result

    def parse_expression():
        result = parse_term()
        while tokenizer.peek() in ('+', '-'):
            op = tokenizer.next_token()
            if op == '+':
                result += parse_term()
            elif op == '-':
                result -= parse_term()
        return result

    return parse_expression()

# Example usage
expression = "2*3+5"
result = evaluate_expression(expression)
print(result)
