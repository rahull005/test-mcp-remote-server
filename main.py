
from fastmcp import FastMCP
import random

# Create the MCP server
mcp = FastMCP("Learning MCP Server")


# Tool 1: Add two numbers
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two integers and return their sum."""
    return a + b


# Tool 2: Roll a six-sided dice
@mcp.tool()
def roll_dice() -> int:
    """Roll a fair six-sided die and return a number from 1 to 6."""
    return random.randint(1, 6)


# Start the MCP server
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
