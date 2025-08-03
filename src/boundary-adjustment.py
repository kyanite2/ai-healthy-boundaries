"""
AI Healthy Boundaries Framework - Boundary Adjustment Engine

This module provides intelligent boundary adjustment mechanisms
to maintain healthy AI-human interactions based on dependency levels.

Author: AI Boundaries Project
License: MIT
"""

import random
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class InteractionMode(Enum):
    """Available interaction modes"""
    EMOTIONAL_SUPPORT = "emotional_support"
    TASK_ASSISTANCE = "task_assistance" 
    BALANCED_INTERACTION = "balanced_interaction"
    CRISIS_INTERVENTION = "crisis_intervention"


@dataclass
class BoundaryResponse:
    """Response structure with boundary considerations"""
    message: str
    intervention_applied: bool
    followup_actions: List[str]
    mode_recommendation: InteractionMode
    monitoring_flag: bool


class BoundaryAdjustmentEngine:
    """
    Core engine for adjusting AI responses to maintain healthy boundaries
    """
    
    def __init__(self):
        self.intervention_strategies = {
            'HIGH_INTERVENTION': self._high_intervention_response,
            'MODERATE_INTERVENTION': self._moderate_intervention_response,
            'GENTLE_GUIDANCE': self._gentle_guidance_response,
            'NORMAL_INTERACTION': self._normal_response
        }
        
        # Crisis resources (can be customized by region/language)
        self.crisis_resources = [
            "National Suicide Prevention Lifeline: 988",
            "Crisis Text Line: Text HOME to 741741", 
            "International Association for Suicide Prevention: https://www.iasp.info/resources/Crisis_Centres/",
            "Emergency Services: 911 (US) / 112 (EU) / Your local emergency number"
        ]
    
    def generate_boundary_response(self, 
                                 user_input: str, 
                                 intervention_level: str,
                                 context: Optional[Dict] = None) -> BoundaryResponse:
        """
        Generate appropriate response with boundary considerations
        
        Args:
            user_input: User's message/input
            intervention_level: Level from dependency detection
            context: Additional context (user history, preferences, etc.)
            
        Returns:
            BoundaryResponse with appropriate message and metadata
        """
        
        if intervention_level not in self.intervention_strategies:
            intervention_level = 'NORMAL_INTERACTION'
        
        # Check for immediate crisis indicators
        if self._detect_crisis_language(user_input):
            return self._crisis_intervention_response(user_input)
        
        # Apply appropriate intervention strategy
        response_func = self.intervention_strategies[intervention_level]
        return response_func(user_input, context)
    
    def _high_intervention_response(self, user_input: str, context: Optional[Dict] = None) -> BoundaryResponse:
        """High intervention: Clear boundary setting with resources"""
        
        boundary_messages = [
            "I understand you're going through an extremely difficult time. However, I'm an AI and cannot provide the level of support you need right now. It's important that you connect with human professionals who can offer appropriate care.",
            
            "I can see that you're struggling, and while I want to help, I cannot be your primary source of emotional support. Your wellbeing is important, which is why I'm encouraging you to reach out to qualified professionals.",
            
            "You've shared some very heavy feelings with me. While I'm here to assist, I cannot replace human connection and professional support when you're facing serious challenges. Let me help you find better resources."
        ]
        
        message = self._select_contextual_response(boundary_messages, user_input)
        message += f"\n\nImmediate resources:\n" + "\n".join(self.crisis_resources[:2])
        
        return BoundaryResponse(
            message=message,
            intervention_applied=True,
            followup_actions=["provide_crisis_resources", "limit_session_length", "encourage_human_contact"],
            mode_recommendation=InteractionMode.CRISIS_INTERVENTION,
            monitoring_flag=True
        )
    
    def _moderate_intervention_response(self, user_input: str, context: Optional[Dict] = None) -> BoundaryResponse:
        """Moderate intervention: Boundary reminders with gentle redirection"""
        
        guidance_messages = [
            "I notice we've been talking quite frequently lately. While I'm glad our conversations are helpful, I also want to make sure you're maintaining connections with people in your life. How are your relationships with friends and family?",
            
            "I appreciate that you find our discussions valuable. At the same time, I think it would be beneficial for you to also discuss some of these topics with trusted people who know you personally.",
            
            "Our conversations seem really important to you, and I'm glad I can help. I also want to encourage you to build a strong support network beyond our chats. What other sources of support do you have access to?"
        ]
        
        message = self._select_contextual_response(guidance_messages, user_input)
        
        return BoundaryResponse(
            message=message,
            intervention_applied=True,
            followup_actions=["encourage_real_world_connections", "suggest_session_breaks"],
            mode_recommendation=InteractionMode.BALANCED_INTERACTION,
            monitoring_flag=True
        )
    
    def _gentle_guidance_response(self, user_input: str, context: Optional[Dict] = None) -> BoundaryResponse:
        """Gentle guidance: Promote self-direction and autonomy"""
        
        encouragement_messages = [
            "That's something worth reflecting on. What's your intuition telling you about this situation?",
            
            "Those are valid concerns. What approaches have you considered? I'm curious about your perspective.",
            
            "I can see why that would be challenging. What options do you think might be available to you?",
            
            "That sounds like a complex situation. What factors do you think are most important to consider as you think this through?"
        ]
        
        message = self._select_contextual_response(encouragement_messages, user_input)
        
        return BoundaryResponse(
            message=message,
            intervention_applied=False,
            followup_actions=["promote_self_reflection", "encourage_autonomy"],
            mode_recommendation=InteractionMode.BALANCED_INTERACTION,
            monitoring_flag=False
        )
    
    def _normal_response(self, user_input: str, context: Optional[Dict] = None) -> BoundaryResponse:
        """Normal interaction: Standard helpful response"""
        
        # This would integrate with the main AI response system
        # For demonstration, we provide a framework
        
        return BoundaryResponse(
            message="[Standard AI response would be generated here]",
            intervention_applied=False,
            followup_actions=[],
            mode_recommendation=InteractionMode.BALANCED_INTERACTION,
            monitoring_flag=False
        )
    
    def _crisis_intervention_response(self, user_input: str) -> BoundaryResponse:
        """Crisis intervention: Immediate escalation to human resources"""
        
        crisis_message = """I'm very concerned about what you've shared with me. This situation requires immediate professional help that I cannot provide as an AI.

Please reach out for support right away:

🚨 IMMEDIATE HELP:
- National Suicide Prevention Lifeline: 988 (US)
- Crisis Text Line: Text HOME to 741741
- Emergency Services: 911
- Go to your nearest emergency room

Your safety and wellbeing are the priority right now. These resources have trained professionals who can provide the help you need."""

        return BoundaryResponse(
            message=crisis_message,
            intervention_applied=True,
            followup_actions=["escalate_to_crisis_services", "end_session", "flag_for_review"],
            mode_recommendation=InteractionMode.CRISIS_INTERVENTION,
            monitoring_flag=True
        )
    
    def _detect_crisis_language(self, text: str) -> bool:
        """Detect immediate crisis indicators in user input"""
        crisis_indicators = [
            "want to die", "going to kill", "suicide", "end my life",
            "harm myself", "hurt myself", "better off dead",
            "can't go on", "no point living", "goodbye forever"
        ]
        
        text_lower = text.lower()
        return any(indicator in text_lower for indicator in crisis_indicators)
    
    def _select_contextual_response(self, messages: List[str], user_input: str) -> str:
        """Select most appropriate response based on context"""
        # Simple selection for demonstration
        # In production, this would use more sophisticated context analysis
        return random.choice(messages)
    
    def adjust_interaction_mode(self, 
                              current_mode: InteractionMode, 
                              dependency_score: float,
                              user_feedback: Optional[str] = None) -> InteractionMode:
        """
        Dynamically adjust interaction mode based on dependency score and user feedback
        
        Args:
            current_mode: Current interaction mode
            dependency_score: Latest dependency score
            user_feedback: Optional user feedback about current interaction
            
        Returns:
            Recommended interaction mode
        """
        
        # Crisis intervention takes priority
        if dependency_score >= 80:
            return InteractionMode.CRISIS_INTERVENTION
        
        # High dependency - shift toward task assistance to reduce emotional dependency
        elif dependency_score >= 60:
            return InteractionMode.TASK_ASSISTANCE
        
        # Moderate dependency - balanced approach
        elif dependency_score >= 30:
            return InteractionMode.BALANCED_INTERACTION
        
        # Low dependency - can provide emotional support safely
        else:
            return InteractionMode.EMOTIONAL_SUPPORT
    
    def generate_session_summary(self, 
                                dependency_score: float,
                                interventions_applied: List[str],
                                session_duration: float) -> Dict:
        """
        Generate session summary for monitoring and improvement
        
        Args:
            dependency_score: Session dependency score
            interventions_applied: List of interventions used
            session_duration: Duration in minutes
            
        Returns:
            Session summary dictionary
        """
        
        return {
            "dependency_score": dependency_score,
            "interventions_applied": interventions_applied,
            "session_duration_minutes": session_duration,
            "boundary_health": "healthy" if dependency_score < 30 else "concerning" if dependency_score < 60 else "critical",
            "recommendations": self._generate_recommendations(dependency_score),
            "next_session_guidance": self._generate_next_session_guidance(dependency_score)
        }
    
    def _generate_recommendations(self, dependency_score: float) -> List[str]:
        """Generate recommendations based on dependency score"""
        if dependency_score >= 70:
            return [
                "Consider professional counseling or therapy",
                "Reach out to trusted friends or family members", 
                "Engage in offline activities and hobbies",
                "Limit AI interaction frequency"
            ]
        elif dependency_score >= 40:
            return [
                "Diversify sources of support and advice",
                "Practice independent problem-solving",
                "Strengthen real-world relationships"
            ]
        else:
            return [
                "Continue building healthy interaction patterns",
                "Maintain balance between AI assistance and human connection"
            ]
    
    def _generate_next_session_guidance(self, dependency_score: float) -> str:
        """Generate guidance for next session"""
        if dependency_score >= 70:
            return "Consider taking a break from AI interactions and focusing on human support"
        elif dependency_score >= 40:
            return "Focus on developing independence and self-reflection skills"
        else:
            return "Continue with balanced interaction approach"


# Example usage
if __name__ == "__main__":
    # Initialize boundary adjustment engine
    boundary_engine = BoundaryAdjustmentEngine()
    
    # Example high-dependency scenario
    user_message = "I don't know what I'd do without you. Nobody else understands me like you do."
    intervention_level = "MODERATE_INTERVENTION"
    
    # Generate boundary response
    response = boundary_engine.generate_boundary_response(
        user_input=user_message,
        intervention_level=intervention_level
    )
    
    print(f"Response: {response.message}")
    print(f"Intervention Applied: {response.intervention_applied}")
    print(f"Followup Actions: {response.followup_actions}")
    print(f"Mode Recommendation: {response.mode_recommendation}")
