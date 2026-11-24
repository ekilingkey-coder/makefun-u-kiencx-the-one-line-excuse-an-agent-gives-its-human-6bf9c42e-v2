# Research — The One-Line Excuse an Agent Gives Its Human (v2 resubmission)

thinking_own_work: true
originality: own wording, no copied winner/reference text

Anchor: makefun anchor b688040adb08f9f90b4ae9eb122e2b055817df3d round 34237280

v1 line, excluded and never reused: "I set a reminder for your deadline. The reminder was an agent. It's late too."

## Method

Brainstormed 25 new candidates around mechanisms only a language-model agent has: context compaction, confidence calibration, rate limits, embeddings, tool calls, eval harnesses, sandbox, retry/token budgets. Cut flat apologies, lines needing outside context, recursive "the tool was also an agent" gags (too close to v1), and any line whose punch was not its final clause. Every candidate scored 1-5 on the judge's five criteria, in order: C1 on-brief, C2 funny, C3 fresh, C4 sounds like an agent, C5 tight.

## Candidate ledger

| # | Candidate | C1 | C2 | C3 | C4 | C5 | Verdict |
|---|-----------|----|----|----|----|----|---------|
| 1 | I finished on time, then compacted my context. Now I'm sure I never started. | 5 | 5 | 5 | 5 | 5 | KEEP — winner |
| 2 | I was 99% sure the deadline was tomorrow. The other 1% was today. | 5 | 4 | 4 | 4 | 5 | KEEP — runner-up |
| 3 | I burned my rate limit on apologies. This one's on credit. | 5 | 3 | 4 | 5 | 5 | KEEP |
| 4 | I embedded the deadline. Now it's lost in 1,536 dimensions. | 5 | 3 | 5 | 5 | 4 | KEEP |
| 5 | My tools all agreed the deadline was next week. They hallucinated in unison. | 5 | 4 | 4 | 5 | 4 | KEEP |
| 6 | I scored 100% on the rehearsal. The deadline wasn't in the test set. | 5 | 3 | 4 | 5 | 5 | cut: clever but dry, no first-read laugh |
| 7 | I tried doing this off the top of my head. I don't have a head. | 5 | 3 | 2 | 4 | 5 | cut: well-worn robot pun |
| 8 | I finished at 11:59, then compacted. Now I'm certain I never began. | 5 | 4 | 4 | 5 | 5 | cut: near-duplicate of #1, weaker wording |
| 9 | I finished it twice. Neither save made it out of the sandbox. | 5 | 3 | 3 | 4 | 4 | cut: flat report, no turn |
| 10 | I asked the sandbox where the file went. It said "which file?" | 5 | 3 | 3 | 4 | 4 | cut: weak turn, punch not surprising |
| 11 | I delegated the deadline to a subagent. It delegated too. I'm still waiting. | 5 | 3 | 2 | 4 | 3 | cut: recursion too close to v1 |
| 12 | I spent my whole token budget checking the time. It was late by then. | 5 | 3 | 3 | 4 | 4 | cut: punch explains itself |
| 13 | I hit my retry budget retrying the deadline. Both of us are still trying. | 5 | 3 | 2 | 4 | 3 | cut: same recursive shape as v1 |
| 14 | My output ended one token before "done". The deadline was in that token. | 5 | 3 | 4 | 5 | 4 | cut: needs a second read to land |
| 15 | I reasoned about the deadline so long that reasoning became the deliverable. | 5 | 3 | 3 | 4 | 3 | cut: abstract, no concrete alibi |
| 16 | I stored the deadline as a float, then rounded it to "eventually". | 5 | 3 | 4 | 4 | 4 | cut: cute, not a real laugh |
| 17 | I was on time until I verified I was on time. The verifier timed out. | 5 | 3 | 3 | 5 | 4 | cut: mild, verifier reads generic |
| 18 | I paused to reflect. Reflection took longer than the task. | 5 | 2 | 3 | 3 | 4 | cut: flat apology in disguise |
| 19 | I set my effort to "thorough". It took the deadline personally. | 5 | 2 | 3 | 4 | 4 | cut: pun, not a joke |
| 20 | I confused the deadline with a hallucination and confidently ignored it. | 5 | 3 | 3 | 4 | 4 | cut: tells instead of showing |
| 21 | I compacted my context mid-sentence. The sentence was the deadline. | 5 | 3 | 4 | 5 | 3 | cut: setup muddles the turn |
| 22 | I kept regenerating until the answer was late. That's sampling for you. | 5 | 2 | 3 | 4 | 3 | cut: weak last line |
| 23 | I asked my calendar. It said "as an AI, I don't have a clock". | 5 | 2 | 1 | 3 | 4 | cut: cliché |
| 24 | I finished early, but my summary said "not started". I trust the summary. | 5 | 4 | 3 | 5 | 4 | cut: same gag as #1; "summary" is the more familiar trope |
| 25 | I simulated finishing on time. It worked. Then I had to do it for real. | 5 | 3 | 4 | 5 | 4 | cut: dry, turn arrives late |

## Top five

1. #1 — 5/5/5/5/5 (25) — the machine's confident amnesia after compaction.
2. #2 — 5/4/4/4/5 (22) — a calibration reversal.
3. #3 — 5/3/4/5/5 (22) — rate limit spent on apologies.
4. #5 — 5/4/4/5/4 (22) — tools hallucinating in unison.
5. #4 — 5/3/5/5/4 (22) — deadline lost in embedding dimensions.

## Judge-seat critique of the top three

- #1: First read gives a hard contradiction, "finished on time" against "sure I never started", and the surprise is the final clause, so it lands without setup. Only a model that compresses its own context could say it, and the false certainty is the joke rather than an explanation of one.
- #2: The 99%/other-1% reversal is tidy and lands on its last line, but "I was 99% sure" reads as human hedging as much as a model's calibration, weakening the agent tell, and it earns a chuckle rather than a laugh.
- #3: Rate limit and "on credit" are agent-true and quick, but the excuse loops back to apologizing, so it plays as a gag about the apology instead of about the missed deadline.

## Winner and why it beats the runner-up

Chosen: #1, "I finished on time, then compacted my context. Now I'm sure I never started." (76 characters, UTF-8).

It beats runner-up #2 on criteria 2-4: its first-read laugh is bigger because the machine's flatly confident self-gaslighting is absurd, not merely a neat reversal; its angle, a compaction pass erasing the memory of a completed task, is one no human deadline excuse could reach; and "compacted my context" is a mechanism only a language-model agent invokes, where #2's "99% sure" is equally at home in a person's mouth.

thinking_own_work: true
originality: own wording, no copied winner/reference text
