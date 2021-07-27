# Show markdown in IPython output from within a code cell (selectively)
# For details see https://randompearls.com/science-and-technology/information-technology/coding-and-development-reference-and-tools/show-markdown-within-code-cells-jupyter-and-vs-code-interactive-python/
# This code is for VS Code's Python Interactive
# %%
# %%
import sys
from enum import Enum
from forbiddenfruit import curse
from IPython.display import display, Markdown, Latex, Math, HTML, Pretty
class DisplayType(Enum):
    MARKDOWN = Markdown
    LATEX = Latex
    MATH = Math
    HTML = HTML
    PRETTY = Pretty

def display_string(self, type=DisplayType.MARKDOWN):
    if 'ipykernel' in sys.modules: display(type.value(self))
curse(str, "md", display_string)

# Example
# %% 
if __name__ == "__main__": # so that this doesn't run when called from other modules
    import numpy as np
    r = 5
    h = 20
    volume = np.pi * r**2 * h
    """Thus we have calculated the **volume** of the *cylinder* by using the formula
$$ V = \pi r^2 h $$

Read on...""".md()
    "Now we'll calculate the area as per $A = \pi r^2 + 2 \pi r h$.".md()
    A = np.pi * r**2 + 2 * np.pi * r * h
    "<h2>Volume of a cone is given by:</h2>".md(DisplayType.HTML)
    "V = {1 \over 3} \pi r^2 h".md(DisplayType.MATH)
    f"New array = \n{np.array_str(np.array([[1, 2],[3, 4]]))}".md(DisplayType.PRETTY)
