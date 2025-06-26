import json
import os
from pathlib import Path
from collections import defaultdict

# Load JSON data
def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Map controls to roles and languages
def map_roles_and_languages(description, role_mapping, language_mapping):
    roles = [role for role, keywords in role_mapping.items() if any(keyword in description.lower() for keyword in keywords)]
    languages = [lang for lang, keywords in language_mapping.items() if any(keyword in description.lower() for keyword in keywords)]
    return roles or ['general'], languages or ['general']

def get_level_emoji(level):
    if level == "1":
        return "🟢"
    elif level == "2":
        return "🟡"
    elif level == "3":
        return "🔴"
    return ""

def get_details_section(control):
    # Placeholder for advanced guidance; can be extended if such data is available
    return f"<details>\n<summary>Advanced: Defense-in-Depth Guidance</summary>\n\n_No additional guidance provided._\n\n</details>"

# Generate Markdown content
def generate_markdown(level, language, role, controls):
    emoji = get_level_emoji(level)
    title = f"ASVS {level} Checklist {emoji} – {language.capitalize()} – {role.capitalize()}"
    header = "_Use during DESIGN and PRE-MERGE review. This list is tailored to your stack and responsibility._"
    checklist = "\n".join([
        f"- [ ] {get_level_emoji(control['L'])} {control['Shortcode']} – {control['Description']}\n  {get_details_section(control)}"
        for control in controls
    ])
    return f"# {title}\n\n{header}\n\n{checklist}\n"

# Save Markdown files
def save_markdown(output_dir, level, language, role, content):
    folder_path = Path(output_dir) / f"level{level}" / language
    folder_path.mkdir(parents=True, exist_ok=True)
    file_path = folder_path / f"{role}.md"
    with open(file_path, 'w') as f:
        f.write(content)

# Main function
def main():
    json_file = "context/OWASP_Application_Security_Verification_Standard_5.0.0_en.json"
    output_dir = "checklists"

    role_mapping = {
        "frontend": ["html", "css", "react", "vue", "dom", "browser", "xss", "csp", "ui", "javascript"],
        "backend": ["auth", "authorization", "sql", "database", "session", "crypto", "validation", "orm"],
        "api": ["rest", "graphql", "api", "endpoint", "json", "rate limit", "payload", "websocket"],
        "integration": ["oauth", "saml", "openid", "federation", "identity", "external", "idp", "sso"],
        "mobile": ["android", "ios", "mobile", "device", "native"],
        "platform": ["terraform", "helm", "deployment", "cloud", "kubernetes", "docker", "yaml", "iac"],
        "security": ["encryption", "key management", "hsm", "secure store", "jwt", "hash", "secrets", "crypto", "kms"],
        "data": ["etl", "data pipeline", "bigquery", "s3", "data lake", "csv", "spark", "pandas"],
        "devsecops": ["pipeline", "scan", "sast", "dast", "dependency", "artifact", "veracode", "semgrep", "github actions"],
        "qa": ["unit test", "fuzz", "test coverage", "selenium", "mutation test", "e2e", "integration test"],
        "observability": ["logging", "trace", "telemetry", "monitor", "alert", "correlation", "span", "observability"],
        "devtools": ["sdk", "cli", "developer experience", "internal tool", "platform", "documentation"],
        "mlops": ["model", "ml", "ai", "training", "serving", "onnx", "huggingface", "model registry"],
        "general": []
    }

    language_mapping = {
        "java": ["java", "jvm", "spring"],
        "csharp": ["c#", ".net", "asp.net"],
        "python": ["python", "flask", "django"],
        "javascript": ["javascript", "node", "typescript", "react", "vue"],
        "general": []
    }

    data = load_json(json_file)
    controls_by_level = defaultdict(list)

    # Fix: Requirements is a list, not a dict with 'Items'
    for item in data['Requirements']:
        for sub_item in item['Items']:
            for control in sub_item['Items']:
                level = control['L']
                description = control['Description']
                roles, languages = map_roles_and_languages(description, role_mapping, language_mapping)
                for role in roles:
                    for language in languages:
                        controls_by_level[(level, language, role)].append(control)

    for (level, language, role), controls in controls_by_level.items():
        content = generate_markdown(level, language, role, controls)
        save_markdown(output_dir, level, language, role, content)

if __name__ == "__main__":
    main()
