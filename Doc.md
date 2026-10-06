# ScamLens

## AI-Powered Scam & Phishing Investigation Assistant

### Problem Statement

Digital scams and phishing attacks have become increasingly sophisticated. Fraudulent messages often impersonate banks, delivery services, government organizations, employers, and other trusted entities.

Traditional scam detection systems frequently provide only a binary result such as "Scam" or "Not a Scam." This does not adequately explain the reasoning behind the decision, making it difficult for users to understand what makes a message dangerous.

Users need a system that can not only identify potentially malicious messages, but also explain the evidence behind its assessment and provide clear, actionable safety guidance.

---

# 1. Project Overview

**ScamLens** is an AI-powered scam and phishing investigation assistant that analyzes suspicious SMS messages, emails, chat messages, and URLs.

Instead of simply classifying a message as safe or malicious, ScamLens performs an evidence-oriented analysis.

The system identifies suspicious characteristics such as:

* Urgency and fear-based language
* Requests for passwords, OTPs, banking information, or personal data
* Suspicious or mismatched URLs
* Brand impersonation
* Unusual payment requests
* Social-engineering techniques
* Suspicious sender information
* Requests to bypass normal security procedures

The analysis is converted into a risk score, threat classification, evidence list, explanation, and recommended action.

---

# 2. Objective

The primary objective of ScamLens is to help ordinary users make safer decisions when they encounter suspicious digital communications.

The system aims to:

1. Detect potentially fraudulent or phishing messages.
2. Identify the specific warning signs present in a message.
3. Explain the reasoning behind the risk assessment in simple language.
4. Detect suspicious URLs and domain mismatches.
5. Provide users with actionable safety recommendations.
6. Reduce dependence on technical cybersecurity knowledge.
7. Demonstrate how generative AI can be applied to practical cybersecurity problems.

---

# 3. Proposed Solution

ScamLens provides a simple interface where users can paste a suspicious message or email.

The system then:

**Input → Extract Evidence → Analyze Signals → Assess Risk → Explain Findings → Recommend Action**

The AI analyzes both the language and contextual characteristics of the message.

For example, consider:

> "Your bank account will be blocked today. Verify your account immediately using the link below."

ScamLens may identify:

* Artificial urgency
* Threat of account suspension
* Financial impersonation
* External login request
* Potential credential theft

The system can then produce:

**Risk Score: 94/100**

**Threat Level: HIGH**

and explain why the message is suspicious.

---

# 4. Core Features

## 4.1 Message Analysis

Users can paste:

* SMS messages
* Emails
* WhatsApp messages
* Social-media messages
* Delivery notifications
* Job offers
* Banking alerts
* Other digital communications

ScamLens analyzes the provided content for suspicious characteristics.

---

## 4.2 Risk Score

The system generates an interpretable risk score between 0 and 100.

Example:

**0–29: LOW RISK**

**30–69: MEDIUM RISK**

**70–100: HIGH RISK**

The score is intended as a decision-support indicator rather than an absolute guarantee.

---

## 4.3 Threat Classification

The system identifies the most likely category of threat.

Examples include:

* Phishing
* Financial scam
* Credential theft
* Fake delivery scam
* Job scam
* Investment scam
* Account takeover attempt
* Impersonation
* Social engineering

---

## 4.4 Evidence Extraction

Instead of simply saying "This is a scam," ScamLens highlights the evidence.

For example:

**Signal:** Urgency manipulation

**Evidence:** "Your account will be suspended today."

**Signal:** Suspicious URL

**Evidence:** The URL does not match the organization being impersonated.

This makes the AI's decision more understandable to non-technical users.

---

## 4.5 Explanation

ScamLens generates a concise natural-language explanation describing why the message is suspicious.

The explanation is written for ordinary users rather than cybersecurity professionals.

---

## 4.6 Safety Recommendation

The system provides an immediate recommended action.

For example:

> **DO NOT CLICK THE LINK.**
>
> Do not enter your password, OTP, banking information, or card details. Verify the request through the organization's official website or application.

---

## 4.7 Legitimate Message Detection

ScamLens should not label every unusual message as malicious.

The system also evaluates messages that appear legitimate.

For example:

> "Your Amazon order has been shipped. Track your package from the Amazon app."

The system may classify this as:

**LOW RISK**

This demonstrates that ScamLens performs contextual assessment rather than simple keyword matching.

---

# 5. System Workflow

The ScamLens workflow consists of the following stages:

### Stage 1: User Input

The user submits a suspicious message, email, or URL.

### Stage 2: Content Extraction

The system identifies relevant information such as:

* Message text
* URLs
* Claimed organization
* Sender information
* Requests for sensitive information
* Payment requests

### Stage 3: Signal Detection

Potential scam indicators are identified.

### Stage 4: AI Reasoning

The AI evaluates the combination of signals and contextual information.

### Stage 5: Risk Assessment

A risk score and threat level are generated.

### Stage 6: Evidence Generation

The system identifies the specific portions of the message supporting its assessment.

### Stage 7: Safety Recommendation

The system provides an actionable recommendation.

---

# 6. System Architecture

```text
                    ┌─────────────────────┐
                    │        USER         │
                    │                     │
                    │ Message / Email /   │
                    │ URL / Screenshot    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Web Interface    │
                    │                     │
                    │ Input + Analyze     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Backend / API     │
                    │                     │
                    │ Validation          │
                    │ URL Extraction      │
                    │ Request Handling    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    AI Analysis      │
                    │      Engine         │
                    │                     │
                    │ Signal Detection    │
                    │ Context Analysis    │
                    │ Threat Classifier   │
                    │ Risk Assessment     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Structured Results  │
                    │                     │
                    │ Risk Score          │
                    │ Threat Type         │
                    │ Evidence            │
                    │ Explanation         │
                    │ Recommendation      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Results Dashboard │
                    │                     │
                    │ Risk Meter          │
                    │ Warning Signals     │
                    │ Evidence Cards      │
                    │ Safety Guidance     │
                    └─────────────────────┘
```

---

# 7. AI / Technical Implementation

ScamLens uses a large language model as the primary reasoning engine.

The AI receives the user's submitted content together with an analysis instruction defining the expected output structure.

The model is instructed to return structured information rather than unrestricted conversational text.

The expected response contains fields such as:

```json
{
  "risk_score": 94,
  "risk_level": "HIGH",
  "threat_type": "PHISHING",
  "signals": [
    {
      "name": "Urgency manipulation",
      "severity": "HIGH",
      "evidence": "Your account will be suspended today"
    },
    {
      "name": "Suspicious URL",
      "severity": "HIGH",
      "evidence": "The domain does not match the claimed organization"
    }
  ],
  "explanation": "The message creates urgency and attempts to redirect the user to an external login page.",
  "recommended_action": "Do not click the link. Verify the request through the organization's official website."
}
```

Structured output allows the frontend to display the AI's analysis consistently.

---

# 8. Detection Signals

ScamLens evaluates multiple categories of suspicious behavior.

### Social Engineering

* Fear
* Urgency
* Pressure
* Authority impersonation
* Emotional manipulation

### Credential Theft

* Password requests
* OTP requests
* Login requests
* Banking information requests

### Financial Fraud

* Unexpected payment requests
* Fake refunds
* Prize claims
* Investment promises
* Account verification requests

### URL Indicators

* Domain mismatch
* Suspicious domain structure
* URL shortening
* Unusual subdomains
* External login pages

### Impersonation

* Banks
* Government organizations
* Delivery companies
* Employers
* Technology companies
* Financial institutions

---

# 9. Innovation & Originality

The key differentiator of ScamLens is that it focuses on **investigation and evidence**, rather than simply classification.

Traditional user experience:

> "This message is suspicious."

ScamLens:

> "This message is suspicious because it creates artificial urgency, impersonates a trusted organization, redirects you to a mismatched domain, and requests sensitive information."

This makes the system more transparent and educational.

The project also treats cybersecurity as a **human decision-making problem**, not only a technical detection problem.

The goal is to help users answer:

> **"Can I trust this, and what should I do next?"**

---

# 10. Target Users

ScamLens can be useful for:

* Students
* Elderly users
* First-time internet users
* Employees
* Online shoppers
* Banking customers
* Job seekers
* Small businesses
* General smartphone users

The interface is intentionally designed to require minimal cybersecurity knowledge.

---

# 11. Technology Stack

### Frontend

* HTML / CSS / JavaScript or a lightweight modern web framework
* Responsive web interface

### Backend

* Python / Node.js
* REST API

### Artificial Intelligence

* Large Language Model API
* Structured AI output
* Prompt-based threat analysis

### Optional Security Intelligence

* URL/domain reputation services
* Public threat-intelligence APIs

For the hackathon MVP, external threat-intelligence integrations are optional. The core demonstration should work without depending on them.

---

# 12. Example Use Case

### Input

> "URGENT! Your bank account has been selected for verification. Failure to verify within 30 minutes will result in permanent suspension. Login here: http://bank-verification.example.com"

### ScamLens Output

**Risk Score:** 96/100

**Threat Level:** HIGH

**Threat Type:** Phishing / Credential Theft

### Detected Signals

**HIGH:** Artificial urgency

> "within 30 minutes"

**HIGH:** Account suspension threat

> "permanent suspension"

**HIGH:** Suspicious login request

> "Login here"

**HIGH:** Domain mismatch

The claimed organization and destination domain do not match.

### Recommendation

> **Do not click the link or enter any credentials.**
>
> Open your bank's official application or website manually and check for notifications there.

---

# 13. Expected Impact

ScamLens aims to reduce the likelihood of users interacting with malicious digital communications by making cybersecurity warnings understandable and actionable.

Beyond detection, the system can improve cybersecurity awareness by teaching users to recognize common manipulation techniques.

This creates a feedback loop:

**Detect → Explain → Educate → Prevent**

---

# 14. Limitations

ScamLens is an AI-assisted decision-support system and cannot guarantee that a message is safe or malicious.

Potential limitations include:

* AI models can make incorrect assessments.
* New scam techniques may not be recognized.
* A URL may require external reputation data for deeper verification.
* Legitimate messages can sometimes appear suspicious.
* Sophisticated attacks may require professional security investigation.

Therefore, ScamLens should provide **risk guidance rather than absolute security guarantees**.

---

# 15. Future Enhancements

Future versions could include:

### Screenshot Analysis

Users could upload screenshots of suspicious messages.

### Voice Scam Detection

Analyze suspicious phone-call recordings or transcripts.

### Browser Extension

Warn users before visiting potentially dangerous links.

### Real-Time Email Protection

Automatically analyze incoming emails.

### Threat Intelligence Integration

Combine AI reasoning with domain reputation and threat-intelligence databases.

### Personal Cybersecurity Profile

Learn which types of scams are most relevant to an individual user.

### Multilingual Support

Support regional languages so that scam awareness is accessible to more users.

### Organization Dashboard

Allow organizations to analyze reported suspicious messages and identify emerging scam campaigns.

---

# 16. Success Criteria

The hackathon MVP will be considered successful if it can:

1. Accept a suspicious message.
2. Detect relevant scam indicators.
3. Generate a meaningful risk score.
4. Identify the likely threat category.
5. Provide evidence supporting the assessment.
6. Explain the result in simple language.
7. Provide a clear safety recommendation.
8. Correctly demonstrate both suspicious and relatively legitimate examples.
9. Complete the analysis within a practical response time.
10. Present the result through an intuitive interface.

---

# 17. Core Value Proposition

### ScamLens transforms:

**"Is this a scam?"**

into:

**"Here's what looks suspicious, here's the evidence, here's how risky it is, and here's what you should do."**

That is the central value of the system.
