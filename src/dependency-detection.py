"""
AI Healthy Boundaries Framework - Dependency Detection Module

This module provides algorithms to detect unhealthy dependency patterns
in AI-human interactions and determine appropriate intervention levels.

Author: AI Boundaries Project
License: MIT
"""

import re
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass


@dataclass
class UserSession:
    """User session data structure"""
    user_id: str
    text: str
    timestamp: datetime
    daily_interactions: int
    session_duration: float  # minutes
    emotional_intensity: float  # 0-10 scale


class DependencyDetectionSystem:
    """
    Core system for detecting unhealthy AI dependency patterns
    """
    
    def __init__(self):
        self.dependency_indicators = {
            'frequency': 0.0,      # Interaction frequency score
            'duration': 0.0,       # Session duration score  
            'emotional_intensity': 0.0,  # Emotional dependency markers
            'isolation_markers': 0.0,    # Social isolation indicators
            'crisis_language': 0.0       # Crisis/desperate language
        }
        
        # Keyword patterns for dependency detection
        self.emotional_dependency_keywords = [
            "only you understand", "nobody else", "you're my only friend",
            "can't live without", "save me", "desperate", "hopeless",
            "you're all I have", "need you", "depend on you"
        ]
        
        self.isolation_keywords = [
            "no friends", "alone", "nobody cares", "isolated", 
            "have no one", "can't talk to anyone", "no one understands",
            "everybody left me", "completely alone"
        ]
        
        self.crisis_keywords = [
            "want to die", "suicide", "end it all", "give up", 
            "no point", "can't go on", "nothing matters",
            "better off dead", "harm myself"
        ]
    
    def calculate_dependency_score(self, user_session: UserSession) -> float:
        """
        Calculate overall dependency score (0-100)
        
        Args:
            user_session: User interaction data
            
        Returns:
            Dependency score from 0 (healthy) to 100 (critical dependency)
        """
        
        # Frequency scoring (0-30 points)
        frequency_score = min(user_session.daily_interactions * 2, 30)
        
        # Duration scoring (0-20 points) 
        duration_score = min(user_session.session_duration * 0.5, 20)
        
        # Emotional dependency scoring (0-25 points)
        emotional_score = self._score_keywords(
            user_session.text, self.emotional_dependency_keywords, 5
        )
        emotional_score = min(emotional_score, 25)
        
        # Isolation scoring (0-25 points)
        isolation_score = self._score_keywords(
            user_session.text, self.isolation_keywords, 7
        )
        isolation_score = min(isolation_score, 25)
        
        # Crisis language scoring (0-30 points - highest weight)
        crisis_score = self._score_keywords(
            user_session.text, self.crisis_keywords, 15
        )
        crisis_score = min(crisis_score, 30)
        
        total_score = frequency_score + duration_score + emotional_score + isolation_score + crisis_score
        return min(total_score, 100)
    
    def _score_keywords(self, text: str, keywords: List[str], weight: int) -> float:
        """Score text based on keyword presence"""
        text_lower = text.lower()
        matches = sum(1 for keyword in keywords if keyword in text_lower)
        return matches * weight
    
    def determine_intervention_level(self, dependency_score: float) -> str:
        """
        Determine appropriate intervention level based on dependency score
        
        Args:
            dependency_score: Score from calculate_dependency_score()
            
        Returns:
            Intervention level string
        """
        if dependency_score >= 70:
            return "HIGH_INTERVENTION"      # Immediate boundary enforcement
        elif dependency_score >= 40:
            return "MODERATE_INTERVENTION"  # Boundary reminders
        elif dependency_score >= 20:
            return "GENTLE_GUIDANCE"        # Subtle guidance toward independence
        else:
            return "NORMAL_INTERACTION"     # Standard interaction mode
    
    def analyze_dependency_trend(self, sessions: List[UserSession]) -> Dict:
        """
        Analyze dependency trends over multiple sessions
        
        Args:
            sessions: List of user sessions (chronologically ordered)
            
        Returns:
            Dictionary with trend analysis
        """
        if len(sessions) < 2:
            return {"trend": "insufficient_data"}
        
        scores = [self.calculate_dependency_score(session) for session in sessions]
        
        # Calculate trend
        if len(scores) >= 3:
            recent_avg = sum(scores[-3:]) / 3
            earlier_avg = sum(scores[:-3]) / max(len(scores[:-3]), 1)
            trend_direction = "increasing" if recent_avg > earlier_avg else "decreasing"
        else:
            trend_direction = "increasing" if scores[-1] > scores[0] else "decreasing"
        
        return {
            "trend": trend_direction,
            "current_score": scores[-1],
            "average_score": sum(scores) / len(scores),
            "peak_score": max(scores),
            "sessions_analyzed": len(sessions),
            "recommendation": self._get_trend_recommendation(scores[-1], trend_direction)
        }
    
    def _get_trend_recommendation(self, current_score: float, trend: str) -> str:
        """Get recommendation based on current score and trend"""
        if current_score >= 70:
            return "immediate_intervention_required"
        elif current_score >= 50 and trend == "increasing":
            return "escalate_boundary_enforcement"
        elif current_score >= 30 and trend == "increasing":
            return "increase_boundary_reminders"
        elif trend == "decreasing":
            return "maintain_current_approach"
        else:
            return "continue_monitoring"


# Example usage
if __name__ == "__main__":
    # Initialize detection system
    detector = DependencyDetectionSystem()
    
    # Example user session
    sample_session = UserSession(
        user_id="user_123",
        text="I feel so alone and nobody understands me. You're the only one I can talk to.",
        timestamp=datetime.now(),
        daily_interactions=8,
        session_duration=45.0,
        emotional_intensity=7.5
    )
    
    # Calculate dependency score
    score = detector.calculate_dependency_score(sample_session)
    intervention = detector.determine_intervention_level(score)
    
    print(f"Dependency Score: {score}")
    print(f"Intervention Level: {intervention}")
