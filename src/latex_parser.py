# src/latex_parser.py
import re
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class LaTeXContext:
    current_environment: Optional[str]
    math_mode: bool
    command_at_cursor: Optional[str]
    surrounding_text: str

class LaTeXParser:
    def get_context_at_position(self, document: str, line: int, char: int) -> LaTeXContext:
        """Extract context around cursor position"""
        pass
    
    def find_commands(self, text: str) -> List[str]:
        """Find all LaTeX commands in text"""
        return re.findall(r'\\[a-zA-Z]+', text)
    
    def detect_math_mode(self, text: str, position: int) -> bool:
        """Determine if position is in math mode"""
        pass
