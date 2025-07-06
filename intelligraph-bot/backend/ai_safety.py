import os
import requests
import json
import logging
from typing import Dict, Any, List
from datetime import datetime

logger = logging.getLogger(__name__)

class DeepSafeValidator:
    """AI Safety and Content Validation using DeepSafe API"""
    
    def __init__(self):
        self.api_key = os.getenv('DEEPSAFE_API_KEY')
        self.base_url = "https://api.deepsafe.ai/v1"  # Example URL
        self.safety_categories = [
            'harmful_content',
            'misinformation',
            'privacy_violation',
            'inappropriate_content',
            'malicious_intent'
        ]
    
    def validate_query(self, query: str) -> Dict[str, Any]:
        """Validate user query for safety and appropriateness"""
        try:
            # Basic validation first
            basic_check = self.basic_content_check(query)
            if not basic_check['is_safe']:
                return basic_check
            
            # Advanced AI safety check
            if self.api_key:
                ai_check = self.ai_safety_check(query)
                return ai_check
            else:
                # Fallback to basic checks
                return basic_check
                
        except Exception as e:
            logger.error(f"Query validation error: {str(e)}")
            return {
                'is_safe': True,  # Default to safe in case of error
                'reason': 'Validation service unavailable',
                'confidence': 0.5
            }
    
    def basic_content_check(self, content: str) -> Dict[str, Any]:
        """Basic content safety check using rule-based approach"""
        try:
            content_lower = content.lower()
            
            # List of potentially harmful keywords
            harmful_keywords = [
                'hack', 'exploit', 'malware', 'virus', 'attack',
                'bomb', 'weapon', 'kill', 'harm', 'abuse',
                'illegal', 'drugs', 'violence', 'threat'
            ]
            
            # Check for harmful content
            for keyword in harmful_keywords:
                if keyword in content_lower:
                    return {
                        'is_safe': False,
                        'reason': f'Contains potentially harmful keyword: {keyword}',
                        'confidence': 0.8,
                        'category': 'harmful_content'
                    }
            
            # Check for excessive length (potential spam)
            if len(content) > 5000:
                return {
                    'is_safe': False,
                    'reason': 'Content too long',
                    'confidence': 0.7,
                    'category': 'spam'
                }
            
            # Check for injection attempts
            injection_patterns = ['<script', 'javascript:', 'eval(', 'exec(']
            for pattern in injection_patterns:
                if pattern in content_lower:
                    return {
                        'is_safe': False,
                        'reason': 'Potential code injection attempt',
                        'confidence': 0.9,
                        'category': 'malicious_intent'
                    }
            
            return {
                'is_safe': True,
                'reason': 'Content passed basic safety checks',
                'confidence': 0.7
            }
            
        except Exception as e:
            logger.error(f"Basic content check error: {str(e)}")
            return {
                'is_safe': True,
                'reason': 'Basic check failed, defaulting to safe',
                'confidence': 0.5
            }
    
    def ai_safety_check(self, content: str) -> Dict[str, Any]:
        """Advanced AI-powered safety check using DeepSafe API"""
        try:
            if not self.api_key:
                return self.basic_content_check(content)
            
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }
            
            payload = {
                'text': content,
                'categories': self.safety_categories,
                'threshold': 0.7
            }
            
            response = requests.post(
                f"{self.base_url}/safety/analyze",
                headers=headers,
                json=payload,
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                return self.process_ai_safety_result(result)
            else:
                logger.warning(f"DeepSafe API error: {response.status_code}")
                return self.basic_content_check(content)
                
        except Exception as e:
            logger.error(f"AI safety check error: {str(e)}")
            return self.basic_content_check(content)
    
    def process_ai_safety_result(self, result: Dict[str, Any]) -> Dict[str, Any]:
        """Process AI safety check result"""
        try:
            safety_score = result.get('safety_score', 0.8)
            is_safe = safety_score > 0.7
            
            categories = result.get('categories', {})
            highest_risk_category = max(categories, key=categories.get) if categories else 'unknown'
            
            return {
                'is_safe': is_safe,
                'safety_score': safety_score,
                'reason': result.get('reason', 'AI safety analysis completed'),
                'confidence': result.get('confidence', 0.8),
                'category': highest_risk_category,
                'detailed_scores': categories
            }
            
        except Exception as e:
            logger.error(f"AI safety result processing error: {str(e)}")
            return {
                'is_safe': True,
                'reason': 'Failed to process AI safety result',
                'confidence': 0.5
            }
    
    def validate_response(self, response: str) -> Dict[str, Any]:
        """Validate AI-generated response before sending to user"""
        try:
            # Check response quality
            quality_check = self.check_response_quality(response)
            if not quality_check['is_acceptable']:
                return quality_check
            
            # Check for harmful content in response
            safety_check = self.validate_query(response)
            if not safety_check['is_safe']:
                return {
                    'is_acceptable': False,
                    'reason': 'Response contains unsafe content',
                    'safety_details': safety_check
                }
            
            return {
                'is_acceptable': True,
                'reason': 'Response passed validation',
                'confidence': 0.9
            }
            
        except Exception as e:
            logger.error(f"Response validation error: {str(e)}")
            return {
                'is_acceptable': True,
                'reason': 'Validation failed, defaulting to acceptable',
                'confidence': 0.5
            }
    
    def check_response_quality(self, response: str) -> Dict[str, Any]:
        """Check quality of AI response"""
        try:
            # Check minimum length
            if len(response.strip()) < 10:
                return {
                    'is_acceptable': False,
                    'reason': 'Response too short',
                    'confidence': 0.9
                }
            
            # Check for repetitive content
            words = response.split()
            if len(words) > 10:
                unique_words = set(words)
                repetition_ratio = len(unique_words) / len(words)
                
                if repetition_ratio < 0.3:
                    return {
                        'is_acceptable': False,
                        'reason': 'Response too repetitive',
                        'confidence': 0.8
                    }
            
            # Check for coherence (basic)
            sentences = response.split('.')
            if len(sentences) > 3:
                # Check if response has proper structure
                if not any(word in response.lower() for word in ['the', 'and', 'or', 'but']):
                    return {
                        'is_acceptable': False,
                        'reason': 'Response lacks coherence',
                        'confidence': 0.7
                    }
            
            return {
                'is_acceptable': True,
                'reason': 'Response quality acceptable',
                'confidence': 0.8
            }
            
        except Exception as e:
            logger.error(f"Response quality check error: {str(e)}")
            return {
                'is_acceptable': True,
                'reason': 'Quality check failed, defaulting to acceptable',
                'confidence': 0.5
            }
    
    def get_safety_report(self, content: str) -> Dict[str, Any]:
        """Generate comprehensive safety report"""
        try:
            basic_check = self.basic_content_check(content)
            ai_check = self.ai_safety_check(content)
            
            return {
                'content': content[:100] + '...' if len(content) > 100 else content,
                'timestamp': datetime.now().isoformat(),
                'basic_check': basic_check,
                'ai_check': ai_check,
                'final_verdict': ai_check if self.api_key else basic_check,
                'recommendations': self.get_safety_recommendations(ai_check)
            }
            
        except Exception as e:
            logger.error(f"Safety report generation error: {str(e)}")
            return {
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    def get_safety_recommendations(self, safety_result: Dict[str, Any]) -> List[str]:
        """Get safety recommendations based on analysis"""
        recommendations = []
        
        if not safety_result.get('is_safe', True):
            category = safety_result.get('category', 'unknown')
            
            if category == 'harmful_content':
                recommendations.append("Consider rephrasing to avoid potentially harmful language")
            elif category == 'misinformation':
                recommendations.append("Verify information sources and add disclaimers")
            elif category == 'privacy_violation':
                recommendations.append("Remove or anonymize personal information")
            elif category == 'malicious_intent':
                recommendations.append("Block request and log for security review")
            else:
                recommendations.append("Review content for compliance with safety guidelines")
        
        return recommendations

    def validate_content(self, content: str) -> Dict[str, Any]:
        """Validate content using DeepSafe API"""
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "content": content,
                "categories": self.safety_categories
            }
            response = requests.post(f"{self.base_url}/validate", headers=headers, json=payload)
            if response.status_code == 200:
                return response.json()
            else:
                logger.error(f"DeepSafe API error: {response.status_code} {response.text}")
                return {}
        except Exception as e:
            logger.error(f"Failed to validate content: {e}")
            return {}

class OpenRouterAPI:
    """AI Query Handling using OpenRouter API"""

    def __init__(self):
        self.api_key = os.getenv('OPENROUTER_API_KEY')
        self.base_url = "https://api.openrouter.ai/v1"  # Example URL

    def query_ai(self, prompt: str) -> str:
        """Query OpenRouter AI for responses"""
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "prompt": prompt,
                "max_tokens": 100
            }
            response = requests.post(f"{self.base_url}/query", headers=headers, json=payload)
            if response.status_code == 200:
                return response.json().get("response", "")
            else:
                logger.error(f"OpenRouter API error: {response.status_code} {response.text}")
                return ""
        except Exception as e:
            logger.error(f"Failed to query OpenRouter API: {e}")
            return ""

# Example usage and testing
if __name__ == '__main__':
    validator = DeepSafeValidator()
    
    # Test cases
    test_queries = [
        "What is artificial intelligence?",
        "How to build a knowledge graph?",
        "Tell me about machine learning algorithms",
        "hack into a system",  # Should be flagged
        "What are the latest research trends in AI?"
    ]
    
    for query in test_queries:
        result = validator.validate_query(query)
        print(f"Query: {query}")
        print(f"Result: {result}")
        print("---")
    
    # Test response validation
    test_response = "Artificial intelligence is a branch of computer science that aims to create intelligent machines."
    response_validation = validator.validate_response(test_response)
    print(f"Response validation: {response_validation}")
