# src/server.py
from pygls.server import LanguageServer
from lsprotocol import types as lsp_types

class LaTeXAIServer(LanguageServer):
    def __init__(self):
        super().__init__("latex-ai", "v0.1.0")

server = LaTeXAIServer()

@server.feature(lsp_types.INITIALIZE)
async def initialize(params):
    return lsp_types.InitializeResult(
        capabilities=lsp_types.ServerCapabilities(
            text_document_sync=lsp_types.TextDocumentSyncKind.Incremental,
            completion_provider=lsp_types.CompletionOptions()
        )
    )

if __name__ == "__main__":
    server.start_io()
