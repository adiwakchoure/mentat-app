from fastapi import APIRouter, HTTPException
from models import Query, UrlRelevance
from utils import url_relevance, get_link_info, get_link_text, get_crawled_links, process_links, compare_extractions

router = APIRouter()

@router.post("/api/query")
def return_info(query: Query):
    try:
        result = url_relevance(query.query)
        return {"answer": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/api/link_info/{url}")
def get_link_info_route(url: str, fast: bool = True):
    try:
        result = get_link_info(url, fast)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/api/link_text/{url}")
def get_link_text_route(url: str, fast: bool = True):
    try:
        result = get_link_text(url, fast)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/api/crawled_links/{url}")
def get_crawled_links_route(url: str):
    try:
        result = get_crawled_links(url)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/api/process_links/{url}")
def process_links_route(url: str, fast: bool = True):
    try:
        result = process_links(url, fast)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/api/compare_extractions/{url}")
def compare_extractions_route(url: str):
    try:
        result = compare_extractions(url)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))