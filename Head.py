# Term = r"(([+-]([ |\t])*)?((((([x](([ |\t])*([*]{2}([ |\t])*(([+-]?)(0|([1-9][0-9]*)))))?))|((sin([ |\t])*[(]([ |\t])*[x]([ |\t])*[)](([ |\t])*([*]{2}([ |\t])*(([+-]?)(0|([1-9][0-9]*)))))?))|((cos([ |\t])*[(]([ |\t])*[x]([ |\t])*[)](([ |\t])*([*]{2}([ |\t])*(([+-]?)(0|([1-9][0-9]*)))))?))))|((([+-]?)(0|([1-9][0-9]*))))))(([ |\t])*[*]([ |\t])*((((([x](([ |\t])*([*]{2}([ |\t])*(([+-]?)(0|([1-9][0-9]*)))))?))|((sin([ |\t])*[(]([ |\t])*[x]([ |\t])*[)](([ |\t])*([*]{2}([ |\t])*(([+-]?)(0|([1-9][0-9]*)))))?))|((cos([ |\t])*[(]([ |\t])*[x]([ |\t])*[)](([ |\t])*([*]{2}([ |\t])*(([+-]?)(0|([1-9][0-9]*)))))?))))|((([+-]?)(0|([1-9][0-9]*))))))*";
SPACE = r"([ \t]){0,2}"
singedInt = r"(([+-]?)(([1-9][0-9]{0})))"
INDEX = r"([*]{2}" + SPACE + singedInt + ")"

X = r"([x](" + SPACE + INDEX + r")?)"


SINE = r"(sin" + SPACE + r"[(]" + SPACE + r"[x]" + SPACE + r"[)](" + SPACE + INDEX + r")?)"
COSINE = r"(cos" + SPACE + r"[(]" + SPACE + r"[x]" + SPACE + r"[)](" + SPACE + INDEX + r")?)"
POWER = r"((" + X + r")|(" + SINE + r")|(" + COSINE + r"))"
FACTOR = r"((" + POWER + r")|(" + singedInt + r"))"

TERM0 = r"(([+-]" + SPACE + r")?" + FACTOR + r")"
TERM = TERM0 + r"(" + SPACE + r"[*]" + SPACE + FACTOR + r"){0,2}"

EXPRESSION_FACTOR = r"\(" + SPACE + r"([+-]?" + SPACE + r")?" + TERM + SPACE + r"([+-]" + SPACE + TERM + SPACE + r"){0,2}\)"
NEW_FACTOR = r"((" + FACTOR + r")|(" + EXPRESSION_FACTOR + r"))"

NEW_SINE = r"(sin" + SPACE + r"[(]" + SPACE + NEW_FACTOR + SPACE + r"[)](" + SPACE + INDEX + r")?)"
NEW_COSINE = r"(cos" + SPACE + r"[(]" + SPACE + NEW_FACTOR + SPACE + r"[)](" + SPACE + INDEX + r")?)"
NEW_POWER = r"((" + X + r")|(" + NEW_SINE + r")|(" + NEW_COSINE + r"))"
NEW_FACTOR_ =  r"((" + NEW_POWER + r")|(" + singedInt + r"))"

TERM0_1 = r"(([+-]" + SPACE + r")?" + NEW_FACTOR + r")"
TERM1 = TERM0_1 + r"(" + SPACE + r"[*]" + SPACE + NEW_FACTOR + r"){0,2}"
EXPRESSION1 = SPACE + r"([+-]?" + SPACE + r")?" + TERM1 + SPACE + r"([+-]" + SPACE + TERM1 + SPACE + r"){0,2}"

TERM0_2 = r"(([+-]" + SPACE + r")?" + NEW_FACTOR_ + r")"
TERM2 = TERM0_2 + r"(" + SPACE + r"[*]" + SPACE + NEW_FACTOR_ + r"){0,2}"
EXPRESSION2 = SPACE + r"([+-]?" + SPACE + r")?" + TERM2 + SPACE + r"([+-]" + SPACE + TERM2 + SPACE + r"){0,2}"
