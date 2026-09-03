import ast
from datetime import datetime, timezone
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
AGENT_DIR = PROJECT_ROOT / "agent"
REPORT_FILE = PROJECT_ROOT / "app" / "evaluation_report.md"
PROPOSAL_FILE = PROJECT_ROOT / "app" / "improvement_proposal.md"
REQUIRED_FILES = (
    "agent_connector.py",
    "agent_generator.py",
    "agent_validator.py",
    "runner_loop.py",
)


def evaluate_agent():
    missing_files = [name for name in REQUIRED_FILES if not (AGENT_DIR / name).exists()]
    syntax_errors = []

    for path in sorted(AGENT_DIR.glob("*.py")):
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except (OSError, SyntaxError) as error:
            syntax_errors.append(f"- `{path.name}`: {error}")

    findings = []
    if missing_files:
        findings.append("- Missing required agent files: " + ", ".join(missing_files))
    if syntax_errors:
        findings.extend(syntax_errors)
    if not findings:
        findings.append("- No structural or syntax findings detected.")

    score = 100 if not missing_files and not syntax_errors else 0
    timestamp = datetime.now(timezone.utc).isoformat()
    report = "\n".join(
        (
            "# Agent Evaluation Report",
            "",
            f"- Generated: `{timestamp}`",
            f"- Score: `{score}/100`",
            "",
            "## Findings",
            "",
            *findings,
        )
    ) + "\n"
    proposal = "\n".join(
        (
            "# Agent Improvement Proposal",
            "",
            "This proposal is informational only. It does not modify files in `agent/`.",
            "",
            "## Findings",
            "",
            *findings,
            "",
            "## Next Review",
            "",
            "- Review the report with a human before changing the agent.",
            "- Run the test suite after any approved change.",
            "- Keep the previous version available for rollback.",
        )
    ) + "\n"
    REPORT_FILE.write_text(report, encoding="utf-8")
    PROPOSAL_FILE.write_text(proposal, encoding="utf-8")
    print(f"Evaluation report: {REPORT_FILE}")
    print(f"Improvement proposal: {PROPOSAL_FILE}")
    print(f"Score: {score}/100")
    return 0 if score == 100 else 1


if __name__ == "__main__":
    raise SystemExit(evaluate_agent())
