import logging
import os
from mcp.server.fastmcp import FastMCP

# ロギング設定
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# FastMCPインスタンス生成
mcp = FastMCP("Hello Server")
logger = logging.getLogger(mcp.name)

@mcp.tool()
async def hello(name: str) -> str:
    """
    Response Hello Message

    Args:
        name (str): Your name.

    Returns:
        str: hello response message
    """
    logger.debug(f"Tool 'hello' called with name={name}")
    result = f"Hello, {name}!"
    logger.debug(f"Tool 'hello' result: {result}")
    return result

def main() -> None:
    """サーバー起動のエントリポイント"""
    # 環境変数からトランスポートを取得（デフォルトはstreamable-http）
    transport = os.getenv("MCP_TRANSPORT", "streamable-http")
    logger.info(f"Starting server '{mcp.name}' with transport '{transport}'...")

    # サーバー実行
    mcp.run(transport=transport)

if __name__ == "__main__":
    main()
