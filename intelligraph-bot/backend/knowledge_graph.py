from neo4j import GraphDatabase
import logging
from typing import List, Dict, Any
import json

logger = logging.getLogger(__name__)

class KnowledgeGraph:
    def __init__(self):
        self.driver = None
        self.connect()
    
    def connect(self):
        """Connect to Neo4j database"""
        try:
            import os
            uri = os.getenv('NEO4J_URI', 'neo4j+s://demo.neo4jlabs.com')
            user = os.getenv('NEO4J_USER', 'demo')
            password = os.getenv('NEO4J_PASSWORD', 'demo')
            
            self.driver = GraphDatabase.driver(uri, auth=(user, password))
            logger.info("Connected to Neo4j database")
        except Exception as e:
            logger.error(f"Failed to connect to Neo4j: {e}")

    def close(self):
        if self.driver:
            self.driver.close()

    def create_node(self, label: str, properties: Dict[str, Any]):
        """Create a node in the knowledge graph"""
        query = f"CREATE (n:{label} {{props}}) RETURN n"
        with self.driver.session() as session:
            result = session.run(query, props=properties)
            return result.single()

    def create_relationship(self, start_node_id: int, end_node_id: int, rel_type: str):
        """Create a relationship between two nodes"""
        query = (
            "MATCH (a), (b) "
            "WHERE id(a) = $start_node_id AND id(b) = $end_node_id "
            "CREATE (a)-[r:" + rel_type + "]->(b) RETURN r"
        )
        with self.driver.session() as session:
            result = session.run(query, start_node_id=start_node_id, end_node_id=end_node_id)
            return result.single()

    def search_knowledge(self, query: str) -> List[Dict[str, Any]]:
        """Search knowledge graph for relevant information"""
        try:
            with self.driver.session() as session:
                # Example: Search for entities related to the query
                cypher_query = """
                MATCH (n)
                WHERE toLower(n.name) CONTAINS toLower($query) 
                   OR toLower(n.description) CONTAINS toLower($query)
                RETURN n.name as entity, n.description as description, 
                       n.type as type, n.properties as properties
                LIMIT 10
                """
                
                result = session.run(cypher_query, query=query)
                
                results = []
                for record in result:
                    results.append({
                        'entity': record['entity'],
                        'description': record['description'],
                        'type': record['type'],
                        'properties': record['properties']
                    })
                
                return results
                
        except Exception as e:
            logger.error(f"Knowledge graph search error: {str(e)}")
            return []
    
    def get_graph_data(self) -> Dict[str, Any]:
        """Get graph data for visualization"""
        try:
            with self.driver.session() as session:
                # Get nodes
                nodes_query = """
                MATCH (n)
                RETURN n.name as name, n.type as type, 
                       n.description as description, id(n) as id
                LIMIT 100
                """
                
                nodes_result = session.run(nodes_query)
                nodes = []
                for record in nodes_result:
                    nodes.append({
                        'id': record['id'],
                        'name': record['name'],
                        'type': record['type'],
                        'description': record['description']
                    })
                
                # Get relationships
                edges_query = """
                MATCH (a)-[r]->(b)
                RETURN id(a) as source, id(b) as target, 
                       type(r) as relationship, r.properties as properties
                LIMIT 200
                """
                
                edges_result = session.run(edges_query)
                edges = []
                for record in edges_result:
                    edges.append({
                        'source': record['source'],
                        'target': record['target'],
                        'relationship': record['relationship'],
                        'properties': record['properties']
                    })
                
                return {
                    'nodes': nodes,
                    'edges': edges,
                    'stats': {
                        'node_count': len(nodes),
                        'edge_count': len(edges)
                    }
                }
                
        except Exception as e:
            logger.error(f"Graph data retrieval error: {str(e)}")
            return {'nodes': [], 'edges': [], 'stats': {}}
    
    def add_entity(self, name: str, entity_type: str, description: str, properties: Dict = None):
        """Add a new entity to the knowledge graph"""
        try:
            with self.driver.session() as session:
                query = """
                CREATE (n:Entity {
                    name: $name,
                    type: $type,
                    description: $description,
                    properties: $properties,
                    created_at: datetime()
                })
                RETURN n
                """
                
                session.run(query, 
                          name=name, 
                          type=entity_type, 
                          description=description, 
                          properties=properties or {})
                
                logger.info(f"Added entity: {name}")
                
        except Exception as e:
            logger.error(f"Failed to add entity: {str(e)}")
    
    def add_relationship(self, entity1: str, entity2: str, relationship_type: str, properties: Dict = None):
        """Add a relationship between two entities"""
        try:
            with self.driver.session() as session:
                query = """
                MATCH (a:Entity {name: $entity1}), (b:Entity {name: $entity2})
                CREATE (a)-[r:RELATES {
                    type: $relationship_type,
                    properties: $properties,
                    created_at: datetime()
                }]->(b)
                RETURN r
                """
                
                session.run(query,
                          entity1=entity1,
                          entity2=entity2,
                          relationship_type=relationship_type,
                          properties=properties or {})
                
                logger.info(f"Added relationship: {entity1} -> {entity2}")
                
        except Exception as e:
            logger.error(f"Failed to add relationship: {str(e)}")
    
    def update_from_document(self, document_data: Dict):
        """Update knowledge graph from processed document"""
        try:
            # Add entities from document
            for entity in document_data.get('entities', []):
                self.add_entity(
                    name=entity['name'],
                    entity_type=entity['type'],
                    description=entity.get('description', ''),
                    properties=entity.get('properties', {})
                )
            
            # Add relationships from document
            for relation in document_data.get('relations', []):
                self.add_relationship(
                    entity1=relation['source'],
                    entity2=relation['target'],
                    relationship_type=relation['type'],
                    properties=relation.get('properties', {})
                )
                
        except Exception as e:
            logger.error(f"Failed to update from document: {str(e)}")
    
    def get_stats(self) -> Dict[str, Any]:
        """Get knowledge graph statistics"""
        try:
            with self.driver.session() as session:
                # Count nodes
                node_count_query = "MATCH (n) RETURN count(n) as count"
                node_count = session.run(node_count_query).single()['count']
                
                # Count relationships
                rel_count_query = "MATCH ()-[r]->() RETURN count(r) as count"
                rel_count = session.run(rel_count_query).single()['count']
                
                # Get entity types
                types_query = """
                MATCH (n)
                RETURN n.type as type, count(n) as count
                ORDER BY count DESC
                """
                types_result = session.run(types_query)
                entity_types = {record['type']: record['count'] for record in types_result}
                
                return {
                    'total_entities': node_count,
                    'total_relationships': rel_count,
                    'entity_types': entity_types
                }
                
        except Exception as e:
            logger.error(f"Failed to get stats: {str(e)}")
            return {}
    
    def close(self):
        """Close database connection"""
        if self.driver:
            self.driver.close()
            logger.info("Neo4j connection closed")

# Initialize sample data
def initialize_sample_data():
    """Initialize the knowledge graph with sample data"""
    kg = KnowledgeGraph()
    
    # Sample entities for AI Help Bot
    sample_entities = [
        {
            'name': 'Artificial Intelligence',
            'type': 'Technology',
            'description': 'Intelligence demonstrated by machines, as opposed to natural intelligence',
            'properties': {'field': 'Computer Science', 'applications': ['ML', 'NLP', 'Vision']}
        },
        {
            'name': 'Knowledge Graph',
            'type': 'Data Structure',
            'description': 'Graph-based data model for representing knowledge',
            'properties': {'components': ['Nodes', 'Edges', 'Properties']}
        },
        {
            'name': 'Natural Language Processing',
            'type': 'Technology',
            'description': 'Branch of AI that helps computers understand human language',
            'properties': {'techniques': ['Tokenization', 'NER', 'Sentiment Analysis']}
        },
        {
            'name': 'Machine Learning',
            'type': 'Technology',
            'description': 'Method of data analysis that automates analytical model building',
            'properties': {'types': ['Supervised', 'Unsupervised', 'Reinforcement']}
        },
        {
            'name': 'Deep Learning',
            'type': 'Technology',
            'description': 'Part of machine learning based on artificial neural networks',
            'properties': {'architectures': ['CNN', 'RNN', 'Transformer']}
        }
    ]
    
    # Add entities
    for entity in sample_entities:
        kg.add_entity(**entity)
    
    # Sample relationships
    sample_relationships = [
        ('Artificial Intelligence', 'Machine Learning', 'INCLUDES'),
        ('Machine Learning', 'Deep Learning', 'INCLUDES'),
        ('Artificial Intelligence', 'Natural Language Processing', 'INCLUDES'),
        ('Knowledge Graph', 'Artificial Intelligence', 'USED_IN'),
        ('Natural Language Processing', 'Knowledge Graph', 'PROCESSES')
    ]
    
    # Add relationships
    for entity1, entity2, rel_type in sample_relationships:
        kg.add_relationship(entity1, entity2, rel_type)
    
    kg.close()
    logger.info("Sample data initialized")

if __name__ == '__main__':
    initialize_sample_data()
