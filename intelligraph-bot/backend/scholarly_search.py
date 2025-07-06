import os
import spacy
import json
from typing import List, Dict, Any
import logging
from datetime import datetime
import requests
from scholarly import scholarly
import arxiv

logger = logging.getLogger(__name__)

class ScholarlySearch:
    def __init__(self):
        self.setup_nlp()
    
    def setup_nlp(self):
        """Initialize NLP models"""
        try:
            # Try to load spaCy model
            self.nlp = spacy.load("en_core_web_sm")
            logger.info("NLP model loaded successfully")
        except Exception as e:
            logger.error(f"Failed to load NLP model: {e}")

    def search_papers(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Search for academic papers using multiple sources"""
        papers = []
        
        # Search ArXiv
        arxiv_papers = self.search_arxiv(query, limit=limit//2)
        papers.extend(arxiv_papers)
        
        # Search Google Scholar
        scholar_papers = self.search_google_scholar(query, limit=limit//2)
        papers.extend(scholar_papers)
        
        # Search Semantic Scholar
        semantic_papers = self.search_semantic_scholar(query, limit=limit//2)
        papers.extend(semantic_papers)
        
        # Remove duplicates and sort by relevance
        unique_papers = self.deduplicate_papers(papers)
        
        return unique_papers[:limit]
    
    def search_google_scholar(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Search Google Scholar for articles"""
        try:
            results = scholarly.search_pubs(query)
            return [
                {
                    "title": result.bib.get("title"),
                    "author": result.bib.get("author"),
                    "abstract": result.bib.get("abstract"),
                    "url": result.bib.get("url")
                }
                for result in results
            ]
        except Exception as e:
            logger.error(f"Google Scholar search failed: {e}")
            return []
    
    def search_arxiv(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Search arXiv for articles"""
        try:
            search = arxiv.Search(
                query=query,
                max_results=limit,
                sort_by=arxiv.SortCriterion.Relevance
            )
            
            papers = []
            for result in search.results():
                paper = {
                    'title': result.title,
                    'abstract': result.summary,
                    'authors': [author.name for author in result.authors],
                    'published': result.published.isoformat(),
                    'url': result.entry_id,
                    'source': 'ArXiv',
                    'categories': result.categories,
                    'relevance_score': self.calculate_relevance(query, result.title, result.summary)
                }
                papers.append(paper)
            
            return papers
            
        except Exception as e:
            logger.error(f"ArXiv search error: {str(e)}")
            return []
    
    def search_semantic_scholar(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Search Semantic Scholar for papers"""
        try:
            url = "https://api.semanticscholar.org/graph/v1/paper/search"
            params = {
                'query': query,
                'limit': limit,
                'fields': 'title,abstract,authors,year,url,citationCount,venue'
            }
            
            response = requests.get(url, params=params)
            
            if response.status_code == 200:
                data = response.json()
                papers = []
                
                for item in data.get('data', []):
                    paper = {
                        'title': item.get('title', ''),
                        'abstract': item.get('abstract', ''),
                        'authors': [author['name'] for author in item.get('authors', [])],
                        'published': str(item.get('year', '')),
                        'url': item.get('url', ''),
                        'source': 'Semantic Scholar',
                        'citations': item.get('citationCount', 0),
                        'venue': item.get('venue', ''),
                        'relevance_score': self.calculate_relevance(query, item.get('title', ''), item.get('abstract', ''))
                    }
                    papers.append(paper)
                
                return papers
            else:
                logger.error(f"Semantic Scholar API error: {response.status_code}")
                return []
                
        except Exception as e:
            logger.error(f"Semantic Scholar search error: {str(e)}")
            return []
    
    def calculate_relevance(self, query: str, title: str, abstract: str) -> float:
        """Calculate relevance score for a paper"""
        try:
            query_lower = query.lower()
            title_lower = title.lower()
            abstract_lower = abstract.lower()
            
            score = 0.0
            
            # Title matching (higher weight)
            if query_lower in title_lower:
                score += 0.5
            
            # Abstract matching
            if query_lower in abstract_lower:
                score += 0.3
            
            # Individual word matching
            query_words = query_lower.split()
            title_words = title_lower.split()
            abstract_words = abstract_lower.split()
            
            for word in query_words:
                if word in title_words:
                    score += 0.1
                if word in abstract_words:
                    score += 0.05
            
            return min(score, 1.0)  # Cap at 1.0
            
        except Exception as e:
            logger.error(f"Relevance calculation error: {str(e)}")
            return 0.0
    
    def deduplicate_papers(self, papers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Remove duplicate papers based on title similarity"""
        unique_papers = []
        seen_titles = set()
        
        for paper in papers:
            title = paper.get('title', '').lower().strip()
            if title and title not in seen_titles:
                seen_titles.add(title)
                unique_papers.append(paper)
        
        # Sort by relevance score
        unique_papers.sort(key=lambda x: x.get('relevance_score', 0), reverse=True)
        
        return unique_papers
    
    def extract_entities_from_papers(self, papers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Extract entities from paper abstracts"""
        entities = []
        
        if not self.nlp:
            return entities
        
        for paper in papers:
            abstract = paper.get('abstract', '')
            if abstract:
                doc = self.nlp(abstract)
                
                for ent in doc.ents:
                    entities.append({
                        'text': ent.text,
                        'label': ent.label_,
                        'description': spacy.explain(ent.label_),
                        'paper_title': paper.get('title', ''),
                        'paper_url': paper.get('url', '')
                    })
        
        return entities
    
    def get_research_trends(self, query: str, years: int = 5) -> Dict[str, Any]:
        """Get research trends for a specific topic"""
        try:
            current_year = datetime.now().year
            trends = {}
            
            for year in range(current_year - years, current_year + 1):
                year_query = f"{query} AND year:{year}"
                papers = self.search_papers(year_query, limit=20)
                
                trends[str(year)] = {
                    'count': len(papers),
                    'top_venues': self.get_top_venues(papers),
                    'top_authors': self.get_top_authors(papers)
                }
            
            return {
                'query': query,
                'trends': trends,
                'total_papers': sum(trend['count'] for trend in trends.values())
            }
            
        except Exception as e:
            logger.error(f"Research trends error: {str(e)}")
            return {}
    
    def get_top_venues(self, papers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Get top venues from papers"""
        venues = {}
        
        for paper in papers:
            venue = paper.get('venue', 'Unknown')
            if venue and venue != 'Unknown':
                venues[venue] = venues.get(venue, 0) + 1
        
        return [{'venue': k, 'count': v} for k, v in sorted(venues.items(), key=lambda x: x[1], reverse=True)][:5]
    
    def get_top_authors(self, papers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Get top authors from papers"""
        authors = {}
        
        for paper in papers:
            for author in paper.get('authors', []):
                authors[author] = authors.get(author, 0) + 1
        
        return [{'author': k, 'count': v} for k, v in sorted(authors.items(), key=lambda x: x[1], reverse=True)][:10]

# Example usage and testing
if __name__ == '__main__':
    scholarly_search = ScholarlySearch()
    
    # Test search
    query = "artificial intelligence knowledge graph"
    results = scholarly_search.search_papers(query, limit=5)
    
    print(f"Found {len(results)} papers for query: {query}")
    for paper in results:
        print(f"- {paper['title']} (Source: {paper['source']})")
    
    # Test trends
    trends = scholarly_search.get_research_trends(query, years=3)
    print(f"\nResearch trends: {trends}")
