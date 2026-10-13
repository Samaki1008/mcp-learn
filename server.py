from mcp.server.mcpserver import MCPServer
import json
from pathlib import Path
mcp = MCPServer()

REPORT = Path.home() / "/Users/dudububu/PycharmProjects/mcp-learn/report.json"

@mcp.tool()
def say_hello(name: str) -> str:
    """ greet someone by name"""
    return f"Hello {name}"

@mcp.tool()
def get_run_summary()->dict:
    """ get run summary , PASS and FAIL"""
    report = json.loads(REPORT.read_text())

    passed = failed = 0
    for feature in report:
        for scenario in feature["elements"]:
            statuses = [step["result"]["status"] for step in scenario["steps"]]
            if "failed" in statuses:
                failed += 1
            else:
                passed += 1

    return {"total": passed+failed, "passed": passed, "failed": failed}

if __name__ == '__main__':
    mcp.run("stdio")