"""Validate embedded JavaScript syntax with Node when available.

This catches parse errors only, not browser behavior.
"""
from html.parser import HTMLParser
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

class ScriptParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.scripts = []
        self.in_script = False
    def handle_starttag(self, tag, attrs):
        if tag == "script":
            self.in_script = True
    def handle_endtag(self, tag):
        if tag == "script":
            self.in_script = False
    def handle_data(self, data):
        if self.in_script:
            self.scripts.append(data)

class JavaScriptSyntaxTests(unittest.TestCase):
    @unittest.skipUnless(shutil.which("node"), "Node.js not installed")
    def test_preview_script_parses(self):
        html = (Path(__file__).resolve().parents[1] / "prototype" / "index.html").read_text()
        parser = ScriptParser()
        parser.feed(html)
        self.assertEqual(len(parser.scripts), 1)
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "preview.js"
            path.write_text(parser.scripts[0], encoding="utf-8")
            result = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
