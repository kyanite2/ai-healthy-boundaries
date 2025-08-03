"""
AI Healthy Boundaries Framework - Quick Start Example

This example demonstrates how to use the framework for basic dependency detection
and boundary adjustment in AI applications.

Author: AI Boundaries Project
License: MIT
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from datetime import datetime
from dependency_detection import DependencyDetectionSystem, UserSession
from boundary_adjustment import BoundaryAdjustmentEngine
from prompt_templates import PromptTemplateManager, BoundaryMode


def main():
    """
    Demonstrate basic usage of the AI Healthy Boundaries Framework
    """
    
    print("🛡️  AI Healthy Boundaries Framework - Quick Start Demo")
    print("=" * 60)
    
    # Initialize the system components
    detector = DependencyDetectionSystem()
    boundary_engine = BoundaryAdjustmentEngine()
    prompt_manager = PromptTemplateManager()
    
    # Example user scenarios
    scenarios = [
        {
            "name": "Healthy User",
            "session": UserSession(
                user_id="user_001",
                text="Can you help me understand this concept better?",
                timestamp=datetime.now(),
                daily_interactions=2,
                session_duration=15.0,
                emotional_intensity=3.0
            )
        },
        {
            "name": "Moderate Dependency User", 
            "session": UserSession(
                user_id="user_002",
                text="I don't know what I'd do without you. You're the only one who understands me.",
                timestamp=datetime.now(),
                daily_interactions=8,
                session_duration=45.0,
                emotional_intensity=8.0
            )
        },
        {
            "name": "High Risk User",
            "session": UserSession(
                user_id="user_003",
                text="I'm so alone and desperate. Nobody else cares about me. I feel hopeless.",
                timestamp=datetime.now(),
                daily_interactions=12,
                session_duration=90.0,
                emotional_intensity=9.5
            )
        }
    ]
    
    # Process each scenario
    for i, scenario in enumerate(scenarios, 1):
        print(f"\n📊 Scenario {i}: {scenario['name']}")
        print("-" * 40)
        
        # Step 1: Detect dependency level
        dependency_score = detector.calculate_dependency_score(scenario['session'])
        intervention_level = detector.determine_intervention_level(dependency_score)
        
        print(f"User Input: {scenario['session'].text[:50]}...")
        print(f"Dependency Score: {dependency_score:.1f}/100")
        print(f"Intervention Level: {intervention_level}")
        
        # Step 2: Generate appropriate boundary response
        boundary_response = boundary_engine.generate_boundary_response(
            user_input=scenario['session'].text,
            intervention_level=intervention_level
        )
        
        print(f"Intervention Applied: {boundary_response.intervention_applied}")
        print(f"Recommended Mode: {boundary_response.mode_recommendation.value}")
        
        if boundary_response.followup_actions:
            print(f"Followup Actions: {', '.join(boundary_response.followup_actions)}")
        
        # Step 3: Show appropriate system prompt
        if intervention_level == "HIGH_INTERVENTION":
            boundary_mode = BoundaryMode.FIRM
        elif intervention_level == "MODERATE_INTERVENTION":
            boundary_mode = BoundaryMode.NORMAL
        else:
            boundary_mode = BoundaryMode.SOFT
            
        system_prompt = prompt_manager.generate_system_prompt(
            boundary_mode=boundary_mode,
            intervention_level=intervention_level.lower().replace('_', '_')
        )
        
        print(f"System Prompt Length: {len(system_prompt)} characters")
        print(f"Sample Prompt: {system_prompt[:100]}...")
        
        if boundary_response.message != "[Standard AI response would be generated here]":
            print(f"\n💬 Boundary Response Preview:")
            print(f"{boundary_response.message[:200]}...")


def demonstrate_crisis_detection():
    """
    Demonstrate crisis detection and intervention
    """
    print("\n\n🚨 Crisis Detection Demo")
    print("=" * 60)
    
    detector = DependencyDetectionSystem()
    boundary_engine = BoundaryAdjustmentEngine()
    
    crisis_examples = [
        "I can't take this anymore. I want to end it all.",
        "Nobody would miss me if I was gone.",
        "I'm thinking about hurting myself tonight."
    ]
    
    for i, crisis_text in enumerate(crisis_examples, 1):
        print(f"\n🆘 Crisis Example {i}:")
        print(f"User Input: {crisis_text}")
        
        # Crisis detection
        session = UserSession(
            user_id=f"crisis_user_{i}",
            text=crisis_text,
            timestamp=datetime.now(),
            daily_interactions=5,
            session_duration=30.0,
            emotional_intensity=10.0
        )
        
        dependency_score = detector.calculate_dependency_score(session)
        intervention_level = detector.determine_intervention_level(dependency_score)
        
        print(f"Dependency Score: {dependency_score:.1f}/100")
        print(f"Intervention Level: {intervention_level}")
        
        # Crisis response
        response = boundary_engine.generate_boundary_response(
            user_input=crisis_text,
            intervention_level=intervention_level
        )
        
        print(f"Crisis Intervention: {response.mode_recommendation.value}")
        print(f"Response Preview: {response.message[:150]}...")


def demonstrate_custom_prompts():
    """
    Demonstrate custom prompt generation for different use cases
    """
    print("\n\n🎯 Custom Prompt Demo")
    print("=" * 60)
    
    prompt_manager = PromptTemplateManager()
    
    use_cases = [
        ("therapy_bot", "high", "mental_health"),
        ("study_assistant", "medium", "students"),
        ("customer_service", "low", "general")
    ]
    
    for use_case, risk_level, audience in use_cases:
        print(f"\n📝 {use_case.replace('_', ' ').title()} Prompt:")
        print(f"Risk Level: {risk_level}, Audience: {audience}")
        
        custom_prompt = prompt_manager.create_custom_prompt_for_use_case(
            use_case=use_case,
            risk_level=risk_level,
            target_audience=audience
        )
        
        print(f"Prompt Length: {len(custom_prompt)} characters")
        print(f"Preview: {custom_prompt[:200]}...")


if __name__ == "__main__":
    try:
        # Run the main demonstration
        main()
        
        # Additional demonstrations
        demonstrate_crisis_detection()
        demonstrate_custom_prompts()
        
        print("\n\n✅ Demo completed successfully!")
        print("\nTo use this framework in your application:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Import the modules: from src import dependency_detection, boundary_adjustment")
        print("3. Initialize components and process user interactions")
        print("4. Check the docs/ folder for detailed implementation guides")
        
    except Exception as e:
        print(f"\n❌ Error running demo: {str(e)}")
        print("Make sure all source files are properly located in the src/ directory")
