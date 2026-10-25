# Console Edition automation integration

## Active/available workflows
- Python test suite and JavaScript syntax smoke check: existing `policy-tests.yml` on pushes and PRs.
- CodeQL security scan: `codeql.yml` on pushes, PRs and Mondays. CodeQL reporting depends on GitHub repository security configuration.
- Dependabot: checks GitHub Actions versions weekly and proposes update PRs. It does not merge them.
- Optional Codex review: manually run `codex-review.yml` from GitHub Actions, after providing `OPENAI_API_KEY` as an Actions secret. Reviews are artifacts, not automatic code changes or merges. Running the workflow may incur OpenAI API charges independently from a ChatGPT subscription.

## Setup tasks requiring repository owner
1. Enable code scanning/Dependabot security features in repository Settings as appropriate.
2. If you want API-based Codex reviews, create an API key in your OpenAI platform account and add it as GitHub Actions secret `OPENAI_API_KEY`. Never put API keys in git, chat, or documentation.
3. Connect Codex Cloud to this GitHub repository separately from ChatGPT GitHub connector; access rights are not inherited automatically.
4. Codex CLI or VS Code extension on Linux Mint requires local installation and sign-in; a repository commit cannot install software on your computer.
5. Ollama stays on the user's desktop, and does not run inside this repository's GitHub Actions workflows.

## Safety rules
- No unattended automatic code changes, automatic merges, or infinite error/fix loops.
- Require green tests and review before merging code changes.
- Do not copy console SDKs, console proprietary assets or credentials into this public repository.
- The original Systems Edition repository stays separate and unchanged.
