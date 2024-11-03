import sys
from io import StringIO
from Post_Pre_fijo import main

def simulate_input(inputs):
    sys.stdin = StringIO(inputs)
    main()
    sys.stdin = sys.__stdin__

if __name__ == "__main__":
    inputs = """\
EVAL PRE + * + 3 4 5 7
EVAL PRE - / - + 3 4 * 5 7 + 5 6 * 8 4
EVAL POST 8 3 - 8 4 4 + * +
EVAL POST 1 2 * 3 + 3 4 * 7 + 5 6 * 4 + / +
MOSTRAR PRE + * + 3 4 5 7
MOSTRAR POST 3 4 + 5 * 6 7 4 4 8 3 8 - / + * / + /
MOSTRAR PRE - + 3 4 * 5 7
MOSTRAR PRE - * 3 4 / * - 5 7 3 + 9 8
MOSTRAR POST 1 2 * 3 + 3 4 * 7 + 5 6 * 4 + / +
MOSTRAR POST 8 3 - 8 4 4 + * +
SALIR
"""
    simulate_input(inputs)