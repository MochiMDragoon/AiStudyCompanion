
from typing import List, Dict, ClassVar
from subject import Subject

class Math(Subject):
    # Override subject variables
    subjectName: str = 'Math'
    subjectElo: int = 800
    topic: str = "algebra"
    subtopic: str = "solving equations"

    # Class level attributes
    subjectBreakpoints: ClassVar[List[int]] = [0, 800, 1600]
    mathTopics: ClassVar[Dict[str, List[str]]] = {
        "basic math": ["addition", "subtraction", "multiplication", "division"],
        "pre-algebra": ["fractions", "decimals", "negative numbers", "order of operations"],
        "algebra": ["solving equations", "graphing linear equations", "polynomials", "quadratic equations"],
        "trigonometry": ["sine and cosine", "tangent", "trigonometric identities", "unit circle"],
        "precalculus": ["limits", "sequences and series", "functions", "conic sections"],
        "calculus": ["derivatives", "integrals", "chain rule", "limits"],
        "statistics": ["mean, median, mode", "probability", "standard deviation", "hypothesis testing"],
        "linear algebra": ["vectors", "matrices", "determinants", "eigenvalues and eigenvectors"]
    }
    subjectPrompts: ClassVar[Dict[int, str]] = {
        0: 'Beginner level {topic}',
        800: 'Intermediate level {topic}',
        1600: 'Advanced level {topic}'
    }

    # Instance level initialization
    currentPrompt: str = ""

    def __init__(self):
        # Pydantic will handle the fields, so we don't need to set them in __init__ for validation
        super().__init__()  # Call Pydantic's init if you want to use its functionality
        
        # Call the method to update the prompt
        self.updatePrompt()

    def updatePrompt(self):
        # Find the highest valid breakpoint that is <= subjectElo
        validBreakpoints = [bp for bp in self.subjectBreakpoints if bp <= self.subjectElo]
        closestBreakpoint = max(validBreakpoints, default=0)

        # Get the corresponding prompt and format it with the topic
        self.currentPrompt = self.subjectPrompts.get(closestBreakpoint, "").format(topic=self.topic)

