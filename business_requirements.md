# Business Requirements: LLM-based Adaptive Q&A App for ML/AI Learning

## Overview
This application is an interactive, AI-driven Q&A platform designed to help users learn and assess their knowledge of any subject area, such as machine learning (ML), artificial intelligence (AI), physics (conceptual only), and more. The app leverages a large language model (LLM) to generate questions, grade answers, and provide feedback. It adapts to the user's performance to ensure a progressive learning experience.

## Key Features

1. **LLM-Generated Questions**
   - The LLM generates all questions dynamically.
   - At the start of each session, the LLM offers the user a choice of a single category or a broad set of categories within the chosen subject (e.g., ML/AI, physics, etc.).
   - Questions are categorized by difficulty levels: L1 (easiest) to L5 (hardest).
   - Questions are conceptual in nature, focusing on understanding rather than calculations (e.g., for physics, no computation-based questions).

2. **Adaptive Learning Path**
   - The application tracks user performance and adapts question difficulty accordingly.
   - The learning path is designed to gradually increase in complexity, ensuring users build knowledge step by step.
   - If a user struggles at a given level, the app will reinforce concepts at that level before progressing.

3. **Answer Grading and Feedback**
   - The LLM grades user answers using a rubric-based scoring system. Each answer is evaluated on key criteria (e.g., correctness, completeness, clarity, depth), with scores assigned to each dimension.
   - The app provides multi-dimensional feedback, highlighting strengths and areas for improvement across these criteria.
   - The app also provides an overall grade (e.g., inaccurate, partially accurate, accurate) for simplicity.
   - After grading, the app provides feedback and a model answer or explanation to reinforce learning.

4. **Interaction Modes**
   - Users can interact with the app via both text and voice (speech-to-text for input, text-to-speech for output).
   - The app supports seamless switching between text and voice modes.

5. **Comprehensive Tracking**
   - All questions presented, user answers, grades, feedback, and timestamps are tracked in an SQLite database.
   - The system is designed with extensible tracking in mind, enabling analytics and dashboards in future versions.

6. **User Experience**
   - At the start, users select a category or let the LLM choose a focus area.
   - The app adapts to user strengths and weaknesses, offering a personalized learning journey.
   - Feedback is immediate and actionable, supporting effective learning.

## Future Enhancements
- **Analytics Dashboard:** Visualize user progress, strengths, and areas for improvement.
- **User Profiles:** Support for multiple users and session histories.
- **Expanded Topics:** Easily add new subject areas or categories (e.g., ML/AI, physics, other conceptual domains).
- **Advanced Speech Features:** Enhanced voice interaction and accessibility options.

## Success Criteria
- Users experience a tailored, effective learning path in their chosen subject area.
- The app reliably generates, grades (using rubric-based, multi-dimensional scoring), and explains questions using the LLM.
- Users receive actionable, multi-dimensional feedback that supports deeper understanding and improvement.
- All interactions and outcomes are tracked for future review and analytics.
- The system supports both text and voice interactions seamlessly.

---
This document outlines the foundational business requirements for the LLM-based adaptive Q&A app. It will guide the technical design and implementation phases.
