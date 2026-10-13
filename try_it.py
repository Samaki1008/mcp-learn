import anyio
from mcp.client import Client

from server import mcp


async def main():
    async with Client(mcp) as client:
        # list_tools() returns a response object containing a .tools list (or tuple wrapper)
        response = await client.list_tools()

        # Extract the tools list safely
        tools = response.tools if hasattr(response, "tools") else response[0]

        for tool in tools:
            print("tool", tool.name, "-", tool.description)
            print("Input schema", tool.input_schema)

        result = await client.call_tool("say_hello", {"name": "sammed"})
        print("Results:", result.content[0].text)
        summary = await client.call_tool("get_run_summary", {})
        print("Summary:", summary.content[0].text)


anyio.run(main)