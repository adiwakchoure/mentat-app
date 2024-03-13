import marvin
from models import UrlRelevance
from trafilatura import fetch_url, extract, spider
from trafilatura.hashing import Simhash

@marvin.fn
def url_relevance(url: str) -> UrlRelevance:
    """
    Determines the relevance of the provided `url` for oppositional research and insight generation about a company.

    The function returns an object of type `UrlRelevance` which includes:
    - `url`: The input URL.
    - `is_relevant`: A boolean indicating whether the URL is relevant for the purpose.
    - `relevance_score`: A float between -1 (not relevant) and 1 (highly relevant) indicating the level of relevance.
    - `insights`: A list of strings containing the potential insights about the company we could get from the content in the URL.
    """
    # Implement the logic for determining URL relevance and generating insights
    pass

def get_link_info(url: str, fast: bool = True):
    try:
        downloaded = fetch_url(url)
        if fast:
            result = extract(downloaded, include_comments=False, include_tables=False, no_fallback=True)
        else:
            result = extract(downloaded)
        if result is None:
            return {"url": url, "text": None, "word_count": 0}
        return {"url": url, "text": result, "word_count": len(result.split())}
    except Exception as e:
        raise e

def get_link_text(url: str, fast: bool = True):
    try:
        downloaded = fetch_url(url)
        result = extract(downloaded)
        if result is None:
            return {"url": url, "text": None}
        return {"url": url, "text": result}
    except Exception as e:
        raise e

def get_crawled_links(url: str):
    try:
        crawled_links = spider.focused_crawler(homepage=url)
        return {"url": url, "links": crawled_links[1]}
    except Exception as e:
        raise e

def process_links(url: str, fast: bool = True):
    try:
        crawled_links = spider.focused_crawler(homepage=url)
    except Exception as e:
        raise e

    results = []
    for link in crawled_links[1]:
        try:
            link_info = get_link_info(link, fast)
            if link_info["text"] is not None:
                results.append({"url": link, "word_count": link_info["word_count"], "content": link_info["text"]})
        except Exception as e:
            print(f"Error while processing link {link}: {e}")

    return {"url": url, "results": results}

def compare_extractions(url: str):
    try:
        downloaded = fetch_url(url)
        slow_result = extract(downloaded)
        fast_result = extract(downloaded, include_comments=False, include_tables=False, no_fallback=True)
        if slow_result is None or fast_result is None:
            return {"url": url, "slow_word_count": 0, "fast_word_count": 0, "similarity": 0}
        slow_simhash = Simhash(slow_result)
        fast_simhash = Simhash(fast_result)
        similarity = slow_simhash.similarity(fast_simhash)
        return {
            "url": url,
            "slow_word_count": len(slow_result.split()),
            "fast_word_count": len(fast_result.split()),
            "similarity": similarity
        }
    except Exception as e:
        raise e