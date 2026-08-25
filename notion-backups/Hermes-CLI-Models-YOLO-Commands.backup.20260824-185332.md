<callout icon="⚡" color="yellow_bg">
	**Purpose:** Copy and paste these commands when launching the `hy3-creative` Hermes profile, switching models, or using YOLO mode.
</callout>
## Quick Launch
### HY3 Creative - Normal
```powershell
hermes -p hy3-creative chat
```
### HY3 Creative - YOLO
```powershell
hermes -p hy3-creative chat --yolo
```
<callout icon="⚠️" color="red_bg">
	**YOLO bypasses dangerous-command approval prompts.** Use it only when you trust the task and working directory.
</callout>
## Google AI Studio - Gemini 3.1 Pro Preview
### Normal
```powershell
hermes -p hy3-creative chat --provider gemini --model gemini-3.1-pro-preview
```
### YOLO
```powershell
hermes -p hy3-creative chat --provider gemini --model gemini-3.1-pro-preview --yolo
```
**Provider:** Google AI Studio / Gemini
**Model:** `gemini-3.1-pro-preview`
**Do not use:** `gemini-3-pro-preview` - Google returned this model as no longer available.
## Tencent HY3 Free via Nous Portal
### Normal
```powershell
hermes -p hy3-creative chat --provider nous --model tencent/hy3:free
```
### YOLO
```powershell
hermes -p hy3-creative chat --provider nous --model tencent/hy3:free --yolo
```
**Provider:** Nous Portal
**Model:** `tencent/hy3:free`
## Change the Saved Default Model / Provider
Run this **outside** an active Hermes chat:
```powershell
hermes -p hy3-creative model
```
This opens the full provider and model setup wizard. Use it to configure API keys, providers, endpoints, and the profile's saved default model.
## Switch Model Inside an Existing Hermes Session
```plain text
/model
```
Use `/model` only for providers/models that are already configured.
## Toggle YOLO Inside an Existing Session
```plain text
/yolo
```
`/yolo` is a toggle:
- Run once = YOLO ON
- Run again = YOLO OFF
When active, the Hermes status bar should show:
```plain text
⚠ YOLO
```
## Current HY3 Creative Setup
- Profile: `hy3-creative`
- Creative identity: loaded from the profile `SOUL.md`
- Google provider model tested: `gemini-3.1-pro-preview`
- Nous Portal backup model: `tencent/hy3:free`
## Best Copy-Paste Commands
### Gemini 3.1 Pro + YOLO
```powershell
hermes -p hy3-creative chat --provider gemini --model gemini-3.1-pro-preview --yolo
```
### HY3 Free + YOLO
```powershell
hermes -p hy3-creative chat --provider nous --model tencent/hy3:free --yolo
```
### Use Whatever Model Is Saved as Default + YOLO
```powershell
hermes -p hy3-creative chat --yolo
```
### Change Saved Default
```powershell
hermes -p hy3-creative model
```
---
**Reminder:** `hermes model` is the terminal setup wizard. `/model` is the quick model switcher inside an existing Hermes chat.
---
# Other Agent CLIs - Copy/Paste Commands
<callout icon="⚠️" color="red_bg">
	**Danger modes remove approval safeguards.** Use them only in a trusted project, VM/container, or disposable environment. Keep backups or Git checkpoints before allowing autonomous edits/deletes.
</callout>
## OpenAI Codex CLI
### Normal interactive launch
```powershell
codex
```
### Recommended low-friction mode
Keeps the workspace sandbox and automates normal work without giving unrestricted machine access.
```powershell
codex --full-auto
```
### YOLO / unrestricted mode
```powershell
codex --yolo
```
Equivalent long form:
```powershell
codex --dangerously-bypass-approvals-and-sandbox
```
<callout icon="❌" color="red_bg">
	**Do not use:** `codex --dangerously-skip-permission`. That is not the Codex flag. The Codex unrestricted flag is `--dangerously-bypass-approvals-and-sandbox` (or `--yolo`).
</callout>
### Start Codex in a specific project folder
```powershell
codex -C "C:\path\to\project"
```
### One-shot / non-interactive task
```powershell
codex exec "Review this project and report the main issues."
```
### One-shot YOLO task
```powershell
codex exec --yolo "Complete the task, test it, and report what changed."
```
## Anthropic Claude Code
### Normal interactive launch
```powershell
claude
```
### Skip all permission prompts
```powershell
claude --dangerously-skip-permissions
```
<callout icon="ℹ️" color="blue_bg">
	The Claude flag is **plural**: `--dangerously-skip-permissions`.
</callout>
### Continue the most recent session
```powershell
claude --continue
```
### Resume a previous session
```powershell
claude --resume
```
### Launch with a selected model
```powershell
claude --model sonnet
```
### Start in plan mode
```powershell
claude --permission-mode plan
```
## Google Antigravity CLI - AGY
### Normal interactive launch
```powershell
agy
```
### Auto-approve all tool permissions
```powershell
agy --dangerously-skip-permissions
```
### Continue the most recent conversation
```powershell
agy -c
```
### Resume by conversation ID
```powershell
agy --conversation <conversation-id>
```
### One-shot / headless task
```powershell
agy -p "Review this project and summarize the issues."
```
### One-shot with auto-approved tools
```powershell
agy --dangerously-skip-permissions -p "Complete the requested task and verify the result."
```
### Add another folder to the workspace
```powershell
agy --add-dir "C:\path\to\folder"
```
### In-session model selector
```plain text
/model
```
### In-session permissions selector
```plain text
/permissions
```
Choose the autonomy level you want from the permissions menu.
### Resume/switch conversations in-session
```plain text
/resume
```
or
```plain text
/switch
```
### AGY `--yolo` note
```powershell
agy --yolo
```
The current official Antigravity CLI documentation I checked documents `--dangerously-skip-permissions` as the supported launch flag for auto-approval. Treat `agy --yolo` as version-specific/unverified unless `agy --help` on your installed build explicitly lists it.
### Verify your installed AGY flags
```powershell
agy --help
```
### Verify AGY version
```powershell
agy --version
```
<callout icon="🚨" color="red_bg">
	**Important AGY safety note:** do not assume `--sandbox` protects you when combined with `--dangerously-skip-permissions`. A documented Antigravity CLI issue shows the dangerous permission bypass can also allow sandbox bypass. For sensitive work, use a separate VM/container or keep the dangerous flag off.
</callout>
## Quick Copy - Maximum Autonomy
### Hermes HY3 Creative
```powershell
hermes -p hy3-creative chat --yolo
```
### Codex
```powershell
codex --yolo
```
### Claude Code
```powershell
claude --dangerously-skip-permissions
```
### Antigravity CLI
```powershell
agy --dangerously-skip-permissions
```
## Quick Copy - Safer Autonomous Options
### Codex - sandboxed automation
```powershell
codex --full-auto
```
### Claude - planning first
```powershell
claude --permission-mode plan
```
### AGY - choose permissions interactively
```plain text
/permissions
```
## Useful Recovery / Inspection Commands
### Hermes help
```powershell
hermes --help
```
### Hermes model wizard
```powershell
hermes -p hy3-creative model
```
### Codex help
```powershell
codex --help
```
### Claude help
```powershell
claude --help
```
### AGY help
```powershell
agy --help
```
<callout icon="💾" color="green_bg">
	**Recommended habit before YOLO/danger mode:** commit or create a save point first, then run the autonomous agent. That gives you a clean rollback if the agent edits or deletes the wrong files.
</callout>
---
## Productivity Upgrades I Recommend
<callout icon="🚀" color="blue_bg">
	These are the commands and shortcuts most likely to save time in daily work. The goal is not just more autonomy, but faster recovery, safer experimentation, easier model switching, and less retyping.
</callout>
## Hermes - Best Daily Workflow
### Fastest Safe-Autonomy Launch
```powershell
hermes -p hy3-creative chat --yolo --checkpoints
```
Use this when you want YOLO speed **with filesystem checkpoints available for rollback**.
### Resume the Most Recent HY3 Creative Session
```powershell
hermes -p hy3-creative --continue
```
Short form:
```powershell
hermes -p hy3-creative -c
```
### Resume a Named Session
```powershell
hermes -p hy3-creative -c "Client Growth Kit"
```
Name important sessions inside Hermes with:
```plain text
/title Client Growth Kit
```
### Parallel Work Without Touching Your Main Checkout
```powershell
hermes -p hy3-creative --worktree
```
Use this when you want a separate git worktree for parallel-agent work.
### One-Shot Hermes Task
```powershell
hermes -p hy3-creative chat -q "Review this project and report the top 5 issues. Do not modify files."
```
Useful for quick audits without staying in an interactive session.
### Backup the Entire HY3 Creative Profile
```powershell
hermes profile export hy3-creative -o hy3-creative-backup.tar.gz
```
Use before major profile, skill, or config changes.
### Check Hermes Before Updating
```powershell
hermes update --check
```
### Health Check
```powershell
hermes doctor
```
### Useful Hermes In-Session Commands
```plain text
/status
/title Client Growth Kit
/compress preserve current objective, decisions, changed files, and next step
/rollback
/snapshot create before-redesign
/snapshot
/retry
/undo
/sessions
/yolo
/model
```
<callout icon="💡" color="green_bg">
	**Best habit:** Before a long autonomous run, use `/snapshot create <label>` or launch Hermes with `--checkpoints`. That gives you speed without making recovery painful.
</callout>
## Claude Code - High-Leverage Commands
### Resume the Most Recent Conversation
```powershell
claude -c
```
### Resume a Specific Session
```powershell
claude -r "<session-id>"
```
### Start in Planning Mode
```powershell
claude --permission-mode plan
```
Use this when you want Claude to inspect and plan before making changes.
### Maximum Autonomy
```powershell
claude --dangerously-skip-permissions
```
### One-Shot Task and Exit
```powershell
claude -p "Audit this project and return only the top 5 fixes."
```
### Machine-Readable JSON Output
```powershell
claude -p "Summarize this project" --output-format json
```
Very useful for scripts, n8n, PowerShell, or piping results into another process.
### Limit Agentic Turns for Quick Jobs
```powershell
claude -p --max-turns 3 "Find the likely cause of this error and suggest a fix."
```
### Update Claude Code
```powershell
claude update
```
## Antigravity / AGY - Best Productivity Commands
### Resume the Last Workspace Session
```powershell
agy --continue
```
### Plan First
```powershell
agy --mode=plan
```
### Auto-Accept File Edits, Keep Command Permissions
```powershell
agy --mode=accept-edits
```
This is a strong middle ground when you want speed without completely removing shell-command safeguards.
### Maximum Autonomy
```powershell
agy --mode=accept-edits --dangerously-skip-permissions
```
### Safer Autonomous Editing With Sandbox
```powershell
agy --mode=accept-edits --sandbox
```
### Useful AGY In-Session Commands
```plain text
/resume
/fork
/rewind
/permissions
/model
/tasks
/agents
/mcp
/config
/keybindings
/usage
```
### Why `/fork` Is Useful
Use `/fork` before testing a different architecture or direction. It branches the **conversation**, so you can experiment without losing the original thread. For file isolation, pair it with a git branch or worktree.
### Why `/rewind` Is Useful
Use `/rewind` when the conversation took a wrong turn and you want to roll the thread back instead of explaining everything again.
## Codex - Productivity Commands
### Normal Launch
```powershell
codex
```
### Maximum Autonomy
```powershell
codex --yolo
```
### Equivalent Explicit Full-Access Flag
```powershell
codex --dangerously-bypass-approvals-and-sandbox
```
### Resume Picker
```powershell
codex resume
```
### Resume the Most Recent Session
```powershell
codex resume --last
```
### Run Non-Interactively
```powershell
codex exec "Review this repo and report the most important issue."
```
### Update Codex
```powershell
codex --upgrade
```
## PowerShell Shortcuts - Biggest Daily Time Saver
<callout icon="⚡" color="yellow_bg">
	Instead of typing long launch commands every time, add short functions to your PowerShell profile once. After that, commands such as `hy3y`, `claudey`, `codexy`, and `agyy` become permanent shortcuts.
</callout>
### Step 1 - Make Sure Your PowerShell Profile Exists
```powershell
if (!(Test-Path $PROFILE)) { New-Item -ItemType File -Path $PROFILE -Force }
notepad $PROFILE
```
### Step 2 - Paste These Functions Into `$PROFILE`
```powershell
function hy3 { hermes -p hy3-creative chat }
function hy3y { hermes -p hy3-creative chat --yolo --checkpoints }
function hy3g { hermes -p hy3-creative chat --provider gemini --model gemini-3.1-pro-preview }
function hy3gy { hermes -p hy3-creative chat --provider gemini --model gemini-3.1-pro-preview --yolo --checkpoints }
function hy3n { hermes -p hy3-creative chat --provider nous --model tencent/hy3:free }
function hy3ny { hermes -p hy3-creative chat --provider nous --model tencent/hy3:free --yolo --checkpoints }
function hy3c { hermes -p hy3-creative --continue }
function hy3model { hermes -p hy3-creative model }

function claudeplan { claude --permission-mode plan }
function claudey { claude --dangerously-skip-permissions }
function claudec { claude -c }

function codexy { codex --yolo }
function codexc { codex resume --last }

function agyplan { agy --mode=plan }
function agyfast { agy --mode=accept-edits }
function agyy { agy --mode=accept-edits --dangerously-skip-permissions }
function agyc { agy --continue }
```
### Step 3 - Reload PowerShell Without Restarting
```powershell
. $PROFILE
```
### Then Your Daily Commands Become
```powershell
hy3y
hy3gy
hy3ny
hy3c
hy3model
claudeplan
claudey
claudec
codexy
codexc
agyplan
agyfast
agyy
agyc
```
## Recommended Operating Modes
<table fit-page-width="true" header-row="true">
<tr>
<td>Situation</td>
<td>Best Command</td>
</tr>
<tr>
<td>HY3 design work, autonomous but recoverable</td>
<td>`hy3y`</td>
</tr>
<tr>
<td>HY3 with Gemini 3.1 Pro</td>
<td>`hy3gy`</td>
</tr>
<tr>
<td>HY3 free backup model</td>
<td>`hy3ny`</td>
</tr>
<tr>
<td>Continue last HY3 session</td>
<td>`hy3c`</td>
</tr>
<tr>
<td>Claude, plan before editing</td>
<td>`claudeplan`</td>
</tr>
<tr>
<td>Claude, maximum autonomy</td>
<td>`claudey`</td>
</tr>
<tr>
<td>Codex, maximum autonomy</td>
<td>`codexy`</td>
</tr>
<tr>
<td>AGY fast editing with command safeguards</td>
<td>`agyfast`</td>
</tr>
<tr>
<td>AGY maximum autonomy</td>
<td>`agyy`</td>
</tr>
</table>
## Save Point Before Any High-Autonomy Run
### Git Save Point
```powershell
git status
git add -A
git commit -m "save point before autonomous agent run"
```
If you do not want to commit yet:
```powershell
git stash push -u -m "save point before autonomous agent run"
```
### Hermes-Specific Save Point
```plain text
/snapshot create before-autonomous-run
```
Or launch with:
```powershell
hermes -p hy3-creative chat --yolo --checkpoints
```
<callout icon="🛡️" color="red_bg">
	**Do not confuse fast with irreversible.** The highest-productivity setup is usually autonomy + a recovery mechanism, not autonomy alone.
</callout>
## My Recommended Daily Stack
1. Open the correct project directory.
2. Create a save point when the task can modify many files.
3. Launch the right agent with a short PowerShell shortcut.
4. Use Plan mode for architecture or unfamiliar projects.
5. Use YOLO / dangerous-skip only after the goal and working directory are clear.
6. Name long sessions so resume is easy.
7. Compress long Hermes sessions before context becomes crowded.
8. Fork or use a worktree when testing a competing approach instead of overwriting the main direction.
---
# Nous Free Models - Best Use Cases and Commands
<callout icon="💡" color="blue_bg">
	**Best strategy:** Use free models by task type. Do not treat one free model as the default for everything. Start cheap/fast, then escalate only when the answer needs deeper reasoning or stronger code/design judgment.
</callout>
## Quick Copy - Launch Any Nous Free Model
Use this pattern:
```powershell
hermes -p hy3-creative chat --provider nous --model MODEL_ID
```
YOLO version:
```powershell
hermes -p hy3-creative chat --provider nous --model MODEL_ID --yolo
```
## Free Model Menu
<table fit-page-width="true" header-row="true">
<tr>
<td>Model</td>
<td>Best use case</td>
<td>When to avoid</td>
</tr>
<tr>
<td>`upstage/solar-pro4:free`</td>
<td>Polished writing, summaries, business copy, structured planning, cleanup of messy notes.</td>
<td>Very large coding refactors or tasks needing tool-heavy autonomy.</td>
</tr>
<tr>
<td>`meituan/longcat-2.0:free`</td>
<td>Long-form reasoning, comparing options, research synthesis, planning with many constraints.</td>
<td>Fast tiny edits where a smaller model is enough.</td>
</tr>
<tr>
<td>`tencent/hy3:free`</td>
<td>Creative work, design direction, Filipino/Taglish copy drafts, brainstorming, landing-page structure.</td>
<td>Strict factual research without citations or exact code debugging.</td>
</tr>
<tr>
<td>`poolside/laguna-s-2.1:free`</td>
<td>Coding help, code review, debugging, refactors, CLI/project work.</td>
<td>Brand voice, sales copy, or emotionally nuanced writing.</td>
</tr>
<tr>
<td>`stepfun/step-3.7-flash:free`</td>
<td>Fast low-cost answers, classification, quick rewrites, short checklists, simple Q&A.</td>
<td>Complex planning, high-stakes decisions, or deep debugging.</td>
</tr>
<tr>
<td>`poolside/laguna-xs-2.1:free`</td>
<td>Small coding tasks, quick syntax fixes, simple explanations, cheap first-pass code review.</td>
<td>Large architecture decisions or multi-file refactors.</td>
</tr>
</table>
## Copy-Paste Commands
### Solar Pro 4 - writing / summaries / planning
```powershell
hermes -p hy3-creative chat --provider nous --model upstage/solar-pro4:free
```
```powershell
hermes -p hy3-creative chat --provider nous --model upstage/solar-pro4:free --yolo
```
### LongCat 2.0 - deeper reasoning / synthesis
```powershell
hermes -p hy3-creative chat --provider nous --model meituan/longcat-2.0:free
```
```powershell
hermes -p hy3-creative chat --provider nous --model meituan/longcat-2.0:free --yolo
```
### Tencent HY3 - creative / design / Taglish copy
```powershell
hermes -p hy3-creative chat --provider nous --model tencent/hy3:free
```
```powershell
hermes -p hy3-creative chat --provider nous --model tencent/hy3:free --yolo
```
### Laguna S 2.1 - coding / refactor / debugging
```powershell
hermes -p hy3-creative chat --provider nous --model poolside/laguna-s-2.1:free
```
```powershell
hermes -p hy3-creative chat --provider nous --model poolside/laguna-s-2.1:free --yolo
```
### Step 3.7 Flash - fast simple tasks
```powershell
hermes -p hy3-creative chat --provider nous --model stepfun/step-3.7-flash:free
```
```powershell
hermes -p hy3-creative chat --provider nous --model stepfun/step-3.7-flash:free --yolo
```
### Laguna XS 2.1 - tiny coding tasks
```powershell
hermes -p hy3-creative chat --provider nous --model poolside/laguna-xs-2.1:free
```
```powershell
hermes -p hy3-creative chat --provider nous --model poolside/laguna-xs-2.1:free --yolo
```
## How to Maximize Nous Free Models
1. **Route by task.** Use HY3 for creative, Laguna for code, Solar for polished writing, LongCat for deeper reasoning, Step Flash for quick simple tasks.
2. **Start with a cheap first pass.** Ask Step Flash or Laguna XS to inspect/summarize first, then escalate to LongCat, Solar, HY3, or Laguna S only when needed.
3. **Give tight prompts.** Include goal, files/context, constraints, and output format. Free models perform much better when the task is narrow.
4. **Use ****`/model`**** inside the same session** when you want to switch after setup instead of restarting Hermes.
5. **Use YOLO only with a save point.** For coding/design automation, make a Git commit, stash, or Hermes snapshot before using `--yolo`.
6. **Keep one model per job.** Do not switch models mid-task unless the current model is clearly weak for that task.
7. **For code:** ask Laguna XS for quick scan, Laguna S for actual edits/debugging, then run tests.
8. **For outreach/design:** ask HY3 for creative direction, then Solar to polish and simplify the final message.
## My Recommended Free-Model Defaults
<table fit-page-width="true" header-row="true">
<tr>
<td>Need</td>
<td>Use this first</td>
<td>Escalate to</td>
</tr>
<tr>
<td>WFW outreach / Taglish copy</td>
<td>`tencent/hy3:free`</td>
<td>`upstage/solar-pro4:free` for final polish</td>
</tr>
<tr>
<td>Landing page ideas / creative direction</td>
<td>`tencent/hy3:free`</td>
<td>`meituan/longcat-2.0:free` for strategy</td>
</tr>
<tr>
<td>Bug fixing / code edits</td>
<td>`poolside/laguna-s-2.1:free`</td>
<td>`meituan/longcat-2.0:free` for reasoning-heavy bugs</td>
</tr>
<tr>
<td>Quick small code checks</td>
<td>`poolside/laguna-xs-2.1:free`</td>
<td>`poolside/laguna-s-2.1:free`</td>
</tr>
<tr>
<td>Fast simple answers</td>
<td>`stepfun/step-3.7-flash:free`</td>
<td>`upstage/solar-pro4:free`</td>
</tr>
<tr>
<td>Messy notes into clear plan</td>
<td>`upstage/solar-pro4:free`</td>
<td>`meituan/longcat-2.0:free`</td>
</tr>
</table>
---
# Project-Based Terminal Commands for Nous Free Models
<callout icon="🧭" color="green_bg">
	**Simple rule:** pick the project type first, then pick the model. For serious file edits, open the project folder, create a save point, then launch Hermes with the right Nous free model.
</callout>
## Universal Terminal Command Pattern
### Open a project folder first
```powershell
cd "C:\path\to\your\project"
```
### Start Hermes with a specific Nous free model
```powershell
hermes -p hy3-creative chat --provider nous --model MODEL_ID
```
### Start with YOLO only after a save point
```powershell
hermes -p hy3-creative chat --provider nous --model MODEL_ID --yolo --checkpoints
```
### One-shot task without opening an interactive chat
```powershell
hermes -p hy3-creative chat --provider nous --model MODEL_ID -q "Do the task here"
```
### Quiet one-shot for scripts
```powershell
hermes -p hy3-creative chat --provider nous --model MODEL_ID -q "Do the task here" --quiet
```
### Limit tool-calling turns for quick jobs
```powershell
hermes -p hy3-creative chat --provider nous --model MODEL_ID -q "Do the task here" --max-turns 6
```
## Save Point Before Project Work
### Git project save point
```powershell
git status
git add -A
git commit -m "save point before AI agent run"
```
If you are not ready to commit:
```powershell
git stash push -u -m "save point before AI agent run"
```
### Hermes checkpoint save point
```powershell
hermes -p hy3-creative chat --checkpoints
```
Inside Hermes:
```plain text
/snapshot create before-model-run
```
## Best Commands by Project Type
<table fit-page-width="true" header-row="true">
<tr>
<td>Project type</td>
<td>Best model</td>
<td>Terminal command</td>
<td>How to maximize it</td>
</tr>
<tr>
<td>Landing page / website design</td>
<td>`tencent/hy3:free`</td>
<td>`hermes -p hy3-creative chat --provider nous --model tencent/hy3:free --checkpoints`</td>
<td>Ask for structure, hero section, conversion flow, visual direction, and above-the-fold copy. Then use Solar to polish final words.</td>
</tr>
<tr>
<td>We Forge Web outreach scripts</td>
<td>`tencent/hy3:free` then `upstage/solar-pro4:free`</td>
<td>`hermes -p hy3-creative chat --provider nous --model tencent/hy3:free`</td>
<td>Use HY3 for natural Taglish drafts. Switch to Solar only to simplify, tighten, and polish the final copy.</td>
</tr>
<tr>
<td>Bug fixing / coding</td>
<td>`poolside/laguna-s-2.1:free`</td>
<td>`hermes -p hy3-creative chat --provider nous --model poolside/laguna-s-2.1:free --checkpoints`</td>
<td>Give exact error, file paths, expected behavior, and ask it to run tests. Use YOLO only after Git save point.</td>
</tr>
<tr>
<td>Small code cleanup</td>
<td>`poolside/laguna-xs-2.1:free`</td>
<td>`hermes -p hy3-creative chat --provider nous --model poolside/laguna-xs-2.1:free`</td>
<td>Use for quick syntax fixes, small refactors, and first-pass review. Escalate to Laguna S if it touches many files.</td>
</tr>
<tr>
<td>Strategy / complex decisions</td>
<td>`meituan/longcat-2.0:free`</td>
<td>`hermes -p hy3-creative chat --provider nous --model meituan/longcat-2.0:free`</td>
<td>Ask it to compare options, list tradeoffs, choose one recommendation, and create a tiny next-action checklist.</td>
</tr>
<tr>
<td>Polishing notes / documents</td>
<td>`upstage/solar-pro4:free`</td>
<td>`hermes -p hy3-creative chat --provider nous --model upstage/solar-pro4:free`</td>
<td>Paste messy notes and ask for clean structure, headings, decisions, next actions, and short wording.</td>
</tr>
<tr>
<td>Fast simple questions</td>
<td>`stepfun/step-3.7-flash:free`</td>
<td>`hermes -p hy3-creative chat --provider nous --model stepfun/step-3.7-flash:free`</td>
<td>Use for quick explanations, simple rewrites, summaries, and checklists. Do not use for deep project decisions.</td>
</tr>
</table>
## Project-Specific Copy-Paste Commands
### 1. Landing page project - creative build mode
```powershell
cd "C:\path\to\landing-page"
hermes -p hy3-creative chat --provider nous --model tencent/hy3:free --checkpoints
```
Prompt to paste:
```plain text
Audit this landing page project. Improve the structure, hero, proof, sections, visual direction, and CTA flow. Keep it premium and conversion-focused. Before editing, explain the plan briefly. After editing, run the relevant build/test command.
```
### 2. Coding bug project - debugging mode
```powershell
cd "C:\path\to\code-project"
git status
git add -A
git commit -m "save point before Laguna debugging"
hermes -p hy3-creative chat --provider nous --model poolside/laguna-s-2.1:free --yolo --checkpoints
```
Prompt to paste:
```plain text
Fix this bug. First reproduce or inspect the failure, then identify the root cause, make the smallest safe fix, and run tests/build to verify. Do not make unrelated changes.
```
### 3. Small code cleanup - cheap first pass
```powershell
cd "C:\path\to\code-project"
hermes -p hy3-creative chat --provider nous --model poolside/laguna-xs-2.1:free -q "Review this project for simple cleanup opportunities. Do not edit files. Give me the top 5 safe improvements."
```
### 4. Business / outreach copy project
```powershell
hermes -p hy3-creative chat --provider nous --model tencent/hy3:free
```
Prompt to paste:
```plain text
Write a short natural Taglish outreach message for We Forge Web. Keep it credible, low-pressure, and specific. Mention the customer journey gap: being seen is not the same as being chosen. Put the final copy in one code block.
```
### 5. Polish final copy with Solar
```powershell
hermes -p hy3-creative chat --provider nous --model upstage/solar-pro4:free
```
Prompt to paste:
```plain text
Polish this copy. Make it shorter, clearer, and more natural. Keep the meaning. Do not make it sound corporate. Put only the final copy in one code block.
```
### 6. Strategy plan for a project
```powershell
cd "C:\path\to\project"
hermes -p hy3-creative chat --provider nous --model meituan/longcat-2.0:free
```
Prompt to paste:
```plain text
Review this project goal and create one practical plan. Compare options briefly, pick the best route, explain why, then give me the next 3 tiny actions only.
```
### 7. Fast quick task
```powershell
hermes -p hy3-creative chat --provider nous --model stepfun/step-3.7-flash:free -q "Summarize this into a short checklist: PASTE_TEXT_HERE"
```
## In-Session Switching Commands
Inside an active Hermes chat:
```plain text
/model
```
Use this when switching from one free model to another.
```plain text
/yolo
```
Use this to toggle YOLO on/off inside the session.
```plain text
/snapshot create before-big-change
```
Use this before a risky edit if checkpoints are enabled.
## How to Maximize Them for Certain Projects
1. **For design projects:** HY3 first for creative direction, Solar second for final copy polish.
2. **For coding projects:** Laguna XS for quick scan, Laguna S for actual fixing, LongCat only if the bug needs deeper reasoning.
3. **For business planning:** LongCat for decision-making, Solar for turning the plan into a clean document.
4. **For outreach:** HY3 for Taglish voice, Solar for compression and clarity.
5. **For simple admin tasks:** Step Flash first. If it feels shallow, move to Solar.
6. **For high-risk edits:** always use Git save point + `--checkpoints`; add `--yolo` only when the scope is clear.
7. **For large projects:** ask the model to inspect and plan first, then approve edits. Do not start with YOLO unless you already know the exact task.
8. **For repeated workflows:** save the best prompt as a reusable note or PowerShell shortcut.
## My Simple Recommendation
If unsure, use this order:
1. `stepfun/step-3.7-flash:free` for fast first pass.
2. `tencent/hy3:free` for creative/copy/design.
3. `poolside/laguna-s-2.1:free` for code.
4. `upstage/solar-pro4:free` for polish.
5. `meituan/longcat-2.0:free` for hard decisions.
<empty-block/>