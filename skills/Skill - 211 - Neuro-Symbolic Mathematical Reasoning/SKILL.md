---
name: Skill - 211 - Neuro-Symbolic Mathematical Reasoning
description: Use when building exact mathematical computing engines, integrating SymPy/Computer Algebra Systems, implementing Pratt AST parsers, formatting LaTeX typeset formulas, or eliminating LLM math hallucinations.
---

# Skill - 211 - Neuro-Symbolic Mathematical Reasoning

## Purpose and Scope
Architect, implement, and integrate deterministic Neuro-Symbolic computing pipelines that decouple natural language comprehension from quantitative mathematical computation. Replaces probabilistic LLM approximations with exact symbolic and numerical computation runtimes (SymPy, Computer Algebra Systems, Top-Down Operator Precedence / Pratt parsers), guaranteeing $O(1)$ and $O(n)$ performance boundaries, sign correctness, and zero mathematical hallucinations.

## Trigger Conditions
- Resolving mathematical, physical, or algorithmic engineering queries requiring exact precision.
- Building or extending Top-Down Operator Precedence (Pratt) parsers for algebraic syntax trees.
- Generating, evaluating, or compiling Abstract Syntax Tree (AST) node objects (`ConstantNode`, `VariableNode`, `BinaryOpNode`, `UnaryFuncNode`).
- Generating and verifying LaTeX typeset equations for client-side rendering (KaTeX/MathJax).
- Implementing domain-isolated agent context switches (`[Maths]`, `[Physics]`, `[DSA]`) to isolate token vocabularies and constants (e.g. $g = 9.81\text{ m/s}^2$ vs coordinate $g$).

## Non-Trigger Conditions
- Do not trigger for natural language chit-chat or casual conversational queries.
- Do not trigger for purely probabilistic generative text completion.
- Do not trigger for standard web CSS styling without mathematical formatting.

## Prerequisites and Inputs
- Mathematical computation runtime installed (Python `sympy`, `numpy`, or Java mathematical libraries like Apache Commons Math).
- Formal mathematical expression or word problem string.
- Domain context indicator (`[Maths]`, `[Physics]`, `[DSA]`).

## Execution Workflow
1. **Lexical Scanning & Tokenization**:
   - Normalize string: Isolate multi-dimensional arrays (e.g. `[[1,2],[3,4]]`) before character splitting.
   - Classify tokens into: Numeric Constants, Algebraic Variables, Metric Units (`m/s²`, `kg`), and Arithmetic Operators (`+`, `-`, `*`, `/`, `^`).
2. **Top-Down Operator Precedence (Pratt) Parsing**:
   - Assign numeric binding powers to operators.
   - Differentiate prefix unary operators (e.g. negative `-x`, trigonometric `cos(-x)`) from binary operations without evaluation exceptions.
   - Assemble strongly typed AST nodes maintaining rigorous mathematical hierarchy.
3. **Symbolic Engine Execution (SymPy)**:
   - Hand off parsed expression tree to symbolic engine:
     - Exact derivatives: `diff(expr, x)`
     - Definite/Indefinite integrals: `integrate(expr, x)`
     - Equation roots & systems: `solve(equations, variables)`
     - Matrix transformations: Gauss-Jordan elimination, determinant, inverse, eigenvalues.
4. **LaTeX Typesetting & Formatting**:
   - Generate standards-compliant LaTeX syntax from the resolved AST state.
   - Format floating-point values cleanly; preserve exact fractions (e.g. `\frac{3}{4}`) over rounded decimals where appropriate.
5. **Multi-Domain Context Switching**:
   - Apply domain-specific constant bindings: In `[Physics]`, bind $g = 9.81\text{ m/s}^2$, $c = 3\times 10^8\text{ m/s}$; in `[Maths]`, treat $g$ as a symbolic coordinate variable.

## Commands and Examples
```powershell
# Python: Verify SymPy symbolic differentiation and matrix inversion
python -c "import sympy as sp; x = sp.Symbol('x'); print(sp.diff(sp.sin(x)**2 + sp.cos(x), x))"

# Python: Execute exact Gauss-Jordan matrix reduction
python -c "import sympy as sp; M = sp.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 10]]); print(M.rref())"
```

```python
# Exact Mathematical AST Node Pattern
class ASTNode:
    def evaluate(self, context: dict[str, float]) -> float:
        raise NotImplementedError
    def to_latex(self) -> str:
        raise NotImplementedError

class BinaryOpNode(ASTNode):
    def __init__(self, op: str, left: ASTNode, right: ASTNode):
        self.op, self.left, self.right = op, left, right
    def evaluate(self, ctx: dict) -> float:
        l, r = self.left.evaluate(ctx), self.right.evaluate(ctx)
        return l + r if self.op == '+' else l * r if self.op == '*' else l - r
    def to_latex(self) -> str:
        return f"{self.left.to_latex()} {self.op} {self.right.to_latex()}"
```

## Deliverables and Outputs
- Deterministic numerical or symbolic solution verified by formal CAS algorithms.
- Validated LaTeX string representation ready for KaTeX browser rendering.
- Step-by-step mathematical calculation audit log.

## Quality Gates and Acceptance Criteria
- Zero conversational approximation or probabilistic guesswork in computed numerical answers.
- 100% of generated LaTeX formulas pass syntax validation without rendering errors.
- Sign reversals and algebraic simplification verified against analytical identities.

## Security and Safety Rules
- Mathematical expression evaluation must never use Python's raw `eval()` or `exec()`; use AST Pratt parsing or SymPy's `sympify` with strict evaluation bounds.
- Bound expression depth and matrix dimensions to prevent algorithmic complexity denial-of-service ($O(n^3)$ compute bombs).
