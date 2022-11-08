Operators = set([&#39;+&#39;, &#39;-&#39;, &#39;*&#39;, &#39;/&#39;, &#39;(&#39;, &#39;)&#39;, &#39;^&#39;]) # collection of Operators
Priority = {&#39;+&#39;:1, &#39;-&#39;:1, &#39;*&#39;:2, &#39;/&#39;:2, &#39;^&#39;:3} # dictionary having priorities of Operators
def infixToPostfix(expression):
stack = [] # initialization of empty stack
output = &#39; &#39;
for character in expression:
if character not in Operators: # if an operand append in postfix expression
output+= character
elif character==&#39;(&#39;: # else Operators push onto stack
stack.append(&#39;(&#39;)
elif character==&#39;)&#39;:
while stack and stack[-1]!= &#39;(&#39;:
output+=stack.pop()
stack.pop()
else:
while stack and stack[-1]!=&#39;(&#39; and Priority[character]&lt;=Priority[stack[-1]]:
output+=stack.pop()

stack.append(character)
while stack:
output+=stack.pop()
return output

expression = input(&#39;Enter infix expression &#39;)
print(&#39;infix notation: &#39;,expression)
print(&#39;postfix notation: &#39;,infixToPostfix(expression))
