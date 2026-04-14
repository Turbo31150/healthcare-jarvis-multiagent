## Devpost Submission: healthcare-jarvis-multiagent

### Inspiration

The healthcare landscape faces immense pressure from rising patient loads, diagnostic complexities, and the need for efficient, accessible care. Our inspiration stemmed from the critical bottleneck in initial patient intake and differential diagnosis, often leading to delays and potential oversights. We envisioned an AI-powered co-pilot for healthcare professionals, one that could streamline symptom collection, assist with preliminary diagnostic reasoning, and present information in a doctor-friendly format. The Agents Assemble Healthcare AI Hackathon 2026 provided the perfect platform to tackle this challenge, aiming to leverage multi-agent systems to augment human capabilities and improve patient outcomes.

### What it does

The **healthcare-jarvis-multiagent** project is an innovative multi-agent AI pipeline designed to transform patient intake and preliminary diagnosis. It functions as follows: a patient verbally describes their symptoms to the system. An **intake-agent** intelligently collects and structures this information using Speech-to-Text (STT). This processed data is then fed to the **diagnosis-agent**, powered by the Deepseek-R1 LLM, which performs a differential diagnosis based on the provided symptoms and known medical knowledge. Finally, a **report-agent** synthesizes the diagnosis and symptom data into a concise, professional PDF summary, ready for a doctor's review. This entire process significantly reduces the administrative burden on medical staff and provides valuable pre-diagnosis insights.

### How we built it

Our solution is built on a robust and scalable architecture using Python FastAPI as the core backend framework, enabling efficient API communication between agents. We integrated Whisper for state-of-the-art Speech-to-Text (STT) capabilities, allowing natural voice input from patients. The heart of our diagnostic reasoning is the **diagnosis-agent**, leveraging the powerful Deepseek-R1 Large Language Model for advanced differential diagnosis. The multi-LLM orchestration is managed through the JARVIS framework, which facilitates seamless communication, task delegation, and workflow management between the **intake-agent**, **diagnosis-agent**, and **report-agent**. The **report-agent** utilizes PDF generation libraries to create structured, readable summaries.

### Challenges we ran into

Integrating multiple advanced AI models (Whisper, Deepseek-R1) and orchestrating their interactions presented several challenges. Ensuring reliable data flow between agents, handling potential inconsistencies or ambiguities in spoken symptom descriptions, and fine-tuning the LLM prompts for accurate medical reasoning required significant effort. We also grappled with optimizing response times to maintain a smooth user experience and ensuring the output from the diagnosis agent was not only medically sound but also interpretable and actionable for the report agent. Ethical considerations surrounding AI in diagnosis, particularly avoiding over-reliance and maintaining human oversight, were also central to our development process.

### Accomplishments that we're proud of

We are incredibly proud of successfully building a functional, end-to-end multi-agent AI pipeline within the hackathon timeframe. The seamless integration of voice STT, LLM-driven differential diagnosis, and automated report generation is a significant achievement. We managed to create a system that demonstrates tangible value in streamlining healthcare processes. The intuitive interaction flow and the clarity of the generated doctor's report highlight our commitment to user-centric design and practical application. This project showcases the power of AI to act as an intelligent assistant, rather than a replacement, for medical professionals.

### What we learned

This project provided invaluable lessons in multi-agent system design and LLM orchestration. We gained deeper insights into prompt engineering for specialized tasks like medical diagnosis, understanding the nuances of how different LLMs interpret and process complex information. We also learned about the critical importance of robust error handling and validation in AI pipelines, especially in sensitive domains like healthcare. Furthermore, the development process reinforced the need for a strong architectural foundation (like FastAPI and JARVIS) to manage complex AI integrations and ensure scalability.

### Built With

*   Python
*   FastAPI
*   Whisper STT
*   Deepseek-R1 LLM
*   JARVIS Framework
*   Multi-LLM Orchestration
*   PDF Generation Libraries
