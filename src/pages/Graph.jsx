import React, { useState, useEffect } from 'react';

const Graph = () => {
  const [selectedNode, setSelectedNode] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');
  
  // Sample graph data (in real implementation, this would come from Neo4j)
  const sampleNodes = [
    { id: 1, label: 'Artificial Intelligence', type: 'concept', connections: 5 },
    { id: 2, label: 'Machine Learning', type: 'concept', connections: 8 },
    { id: 3, label: 'Deep Learning', type: 'concept', connections: 6 },
    { id: 4, label: 'Neural Networks', type: 'concept', connections: 4 },
    { id: 5, label: 'Natural Language Processing', type: 'concept', connections: 7 },
    { id: 6, label: 'Computer Vision', type: 'concept', connections: 3 },
    { id: 7, label: 'Reinforcement Learning', type: 'concept', connections: 5 },
    { id: 8, label: 'Data Science', type: 'concept', connections: 9 },
  ];

  const [nodes, setNodes] = useState(sampleNodes);

  const handleNodeClick = (node) => {
    setSelectedNode(node);
  };

  const handleSearch = () => {
    const filteredNodes = sampleNodes.filter(node =>
      node.label.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setNodes(filteredNodes);
  };

  return (
    <div className="bg-gray-50 min-h-screen p-8">
      <h1 className="text-3xl font-bold text-gray-800 mb-6">Knowledge Graph</h1>
      <p className="text-gray-600 mb-4">Explore the relationships in your knowledge base</p>
      <div className="flex items-center space-x-4 mb-6">
        <input
          type="text"
          placeholder="Search nodes..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="input-field"
        />
        <button onClick={handleSearch} className="btn-primary">Refresh Graph</button>
        <button className="btn-secondary">Export</button>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {nodes.map(node => (
          <div key={node.id} className="card">
            <h3 className="text-lg font-semibold text-gray-800">{node.label}</h3>
            <p className="text-gray-600">Connections: {node.connections}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Graph;
