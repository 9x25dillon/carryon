from fastapi import APIRouter, Body

router = APIRouter(tags=["tools"], prefix="/tools")

_TOOLS: dict[str, dict] = {}

@router.get("")
def list_tools():
    return list(_TOOLS.values())

@router.post("")
def upsert_tool(tool: dict = Body(...)):
    name = tool.get("name") or tool.get("id") or f"tool_{len(_TOOLS)+1}"
    _TOOLS[name] = tool | {"name": name}
    return {"ok": True, "count": len(_TOOLS)}