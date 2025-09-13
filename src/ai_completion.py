# src/ai_completion.py
import anthropic
from typing import List, Optional
from .config import get_api_key

class AICompletionEngine:
    def __init__(self):
        self.client = anthropic.Client(api_key=get_api_key())
    
    async def get_completions(self, context: str, max_suggestions: int = 5) -> List[str]:
        """Get AI-powered completions"""
        try:
            response = await self.client.messages.create(
                model="claude-sonnet-4-20250514",
                messages=[{
                    "role": "user",
                    "content": self._build_prompt(context)
                }],
                max_tokens=200
            )
            return self._parse_suggestions(response.content[0].text)
        except Exception as e:
            # Log error and return empty list
            return []
    
    def _build_prompt(self, context: str) -> str:
        """Build effective prompt for LaTeX completion"""
        return f"""Complete this LaTeX code. Provide only the completion text, no explanations:

Context: {context}

Completion:"""

@server.feature(lsp_types.TEXT_DOCUMENT_COMPLETION)
async def completions(ls: LaTeXAIServer, params: lsp_types.CompletionParams):
    """Provide intelligent completions"""
    document = ls.workspace.get_document(params.text_document.uri)
    parser = LaTeXParser()
    ai_engine = AICompletionEngine()
    
    context = parser.get_context_at_position(
        document.source, 
        params.position.line, 
        params.position.character
    )
    
    # Combine static and AI completions
    static_completions = get_static_completions(context)
    ai_completions = await ai_engine.get_completions(context.surrounding_text)
    
    return lsp_types.CompletionList(
        is_incomplete=False,
        items=static_completions + ai_completions
    )
