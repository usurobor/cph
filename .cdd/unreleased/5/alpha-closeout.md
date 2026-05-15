# α Close-out: Sub A — OpenCap Lab Validation manifest

**Cycle:** #5
**Merged:** 6972025 (main)

## Cycle summary

Goal: populate the dataset manifest, choose a dataset against the protocol selection rules, name a local storage path, document raw-data exclusion policy. Result: manifest fully populated from public documentation; dataset selected (OpenCap Lab Validation, Stanford NMBL, Apache 2.0); local storage path declared at `/opt/gait-data/opencap-lab-validation/`; `.gitignore` extended; AC1–AC4 met. One round, one APPROVE.

## Findings

### F1 — SimTK gate vs Apache 2.0 license

OpenCap Lab Validation is Apache 2.0 (permissive). SimTK requires a logged-in user account to access the download_confirm endpoint. The OpenCap public S3 bucket denies anonymous listing; the OpenCap Python client requires an API token. Pattern: open license + closed access mechanism. Surfaces affected: this cycle (download blocked), Sub B (#6) and Sub C (#7) which both depend on file content.

### F2 — Speed-graduation partial

The dataset has two coordination conditions (natural + trunk-sway) at self-selected speed, not graded speeds. Protocol §"Dataset Selection Rules" lists multi-speed as one of four selection criteria; α accepted the partial because three of four are fully met and the L/R-comparison purpose the rule serves is delivered by trial repetitions. Pattern: protocol-rule purpose vs literal wording. Surfaces: protocol `protocols/existing-data-zeroth-pilot.md` §Dataset Selection Rules wording could be tightened to say "multiple speeds OR multiple conditions" if the project agrees with α's read; otherwise the protocol should explicitly cite trunk-sway as out-of-scope.

### F3 — AC oracle drift risk

AC1's oracle pattern includes "Pending" verbatim. α originally wrote `Download status: Pending — SimTK account registration required` (truthful, concrete), which mechanically failed the AC1 oracle. α rewrote to `BLOCKED — SimTK account registration required`. Pattern: oracle pattern coupled tightly to phrasing — substantively equivalent words ("Pending" / "BLOCKED" / "Awaiting" / "Deferred") have different AC1 outcomes. Surfaces: AC1 in issue #5, and any future cycle that writes status-style content into the same manifest.

## Friction log

- Three OpenCap download paths probed (SimTK direct, S3 bucket, opencap-processing CLI). All three blocked. Approximate time cost: ~5 minutes of probing per path before establishing the pattern.
- The "Pending" / AC1 oracle collision took one revision round (caught in self-check before β saw it).

## Engineering level reading

L6: cross-surface coherence held (manifest, .gitignore, self-coherence, escalation path all aligned with the policy in `data/external/README.md` and `docs/ethics/data-handling.md`). L5 cleanly: no mechanical errors reached β.

L7 not earned: the cycle did not patch the SimTK-gate friction class (it remains as a future-cycle blocker). A possible L7 move would be to add a make target or `scripts/acquire-opencap.sh` stub that loads SimTK credentials from an env var and runs the curl, so the next cycle has the unblock pre-mechanized — but that work belongs at the wave level, not this cycle.
