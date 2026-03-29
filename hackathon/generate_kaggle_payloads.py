"""
H-Bar V3.0+ Kaggle Payload Generator
Generates pilot benchmark payloads for all five hackathon tracks.

REAL DATA (recommended):
  1. pip install huggingface_hub
  2. huggingface-cli login          # paste a token from hf.co/settings/tokens
  3. python generate_kaggle_payloads.py

If the Hub is unreachable the script falls back to seeded synthetic data so
it always completes and produces valid .jsonl files.

Output: kaggle_payloads/
  hptb_pilot.jsonl    — Track 1: Learning        (H-PTB)
  hmcb_pilot.jsonl    — Track 2: Metacognition   (H-MCB)
  hafb_pilot.jsonl    — Track 3: Attention        (H-AFB)
  hdcb_pilot.jsonl    — Track 4: Executive Fns   (H-DCB)
  hstb_pilot.jsonl    — Track 5: Social Cognition (H-STB)
"""

from __future__ import annotations

import json
import os
import random
from typing import Any, Mapping, cast

# All paths are relative to this script's directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(SCRIPT_DIR, "kaggle_payloads"), exist_ok=True)


# ──────────────────────────────────────────────────────────────────────────────
# SHARED UTILITIES
# ──────────────────────────────────────────────────────────────────────────────


def format_for_kaggle(
    task_id: str | int,
    prompt: str,
    expected: str,
    track_name: str,
    condition: str,
    temperature: float = 0.0,
) -> dict:
    """Returns one item in the Kaggle Community Benchmarks SDK schema."""
    return {
        "id": f"{track_name}_{condition}_{task_id}",
        "prompt": prompt,
        "expected": expected,
        "temperature": temperature,
    }


def load_local_cogs(split):
    """Loads COGS from the local GitHub clone."""
    # Maps 'validation' to 'dev' if your script asks for it
    split_name = "dev" if split == "validation" else split
    path = os.path.join(SCRIPT_DIR, "COGS", "data", f"{split_name}.tsv")

    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing COGS file: {path}")

    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) >= 2:
                data.append({"source": parts[0], "target": parts[1]})
    return data


def load_local_scan(split):
    """Loads SCAN from the local GitHub clone."""
    path = os.path.join(SCRIPT_DIR, "SCAN", "simple_split", f"tasks_{split}_simple.txt")

    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing SCAN file: {path}")

    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if " OUT: " in line:
                src, tgt = line.strip().split(" OUT: ")
                src = src.replace("IN: ", "").strip()
                data.append({"commands": src, "actions": tgt.strip()})
    return data


def load_local_pcfg(split):
    """Loads PCFG SET from the local am-i-compositional clone."""
    # We use the systematicity split as the default standard for PCFG
    base_path = os.path.join(
        SCRIPT_DIR, "am-i-compositional", "data", "pcfgset", "systematicity"
    )
    src_path = f"{base_path}/{split}.src"
    tgt_path = f"{base_path}/{split}.tgt"

    if not os.path.exists(src_path) or not os.path.exists(tgt_path):
        raise FileNotFoundError(f"Missing PCFG files at {base_path}")

    data = []
    with open(src_path, "r", encoding="utf-8") as fs, open(
        tgt_path, "r", encoding="utf-8"
    ) as ft:
        for s_line, t_line in zip(fs, ft):
            s = s_line.strip()
            t = t_line.strip()
            if s and t:
                data.append({"source": s, "target": t})
    return data


def load_hub_dataset(name):
    """
    Intercepts the dataset requests from the main script and routes
    them to the local files instead of Hugging Face.
    Returns a dict of lists of dicts.
    """
    if "cogs" in name.lower():
        return {
            "train": load_local_cogs("train"),
            "validation": load_local_cogs("validation"),
            "test": load_local_cogs("test"),
            "gen": load_local_cogs("gen"),
        }
    elif "scan" in name.lower():
        return {"train": load_local_scan("train"), "test": load_local_scan("test")}
    elif "pcfg_set" in name.lower():
        return {"train": load_local_pcfg("train"), "test": load_local_pcfg("test")}
    else:
        raise ValueError(f"Unknown dataset requested: {name}")


def write_jsonl(path: str, records: list[dict]) -> None:
    with open(path, "w") as f:
        for r in records:
            f.write(json.dumps(r) + "\n")
    print(f"  Wrote {len(records)} items -> {path}")


# ──────────────────────────────────────────────────────────────────────────────
# TRACK 1 — LEARNING: H-Bar Phase Transition Benchmark (H-PTB)
# ──────────────────────────────────────────────────────────────────────────────


def generate_hptb() -> None:
    print("\n[1/5] Generating H-PTB (Learning) ...")

    def _hptb_row(item: Mapping[str, Any]) -> tuple[str, str]:
        return str(item["source"]), str(item["target"])

    try:
        ds = load_hub_dataset("dieuwkehupkes/pcfg_set")
        train_data = ds["train"]
        print("  Using real PCFG-SET data.")
    except Exception as exc:
        print(f"  [INFO] Hub unavailable ({type(exc).__name__}). Using synthetic data.")
        rng = random.Random(42)
        verbs = ["jump", "walk", "run", "look", "turn"]
        mults = {"once": 1, "twice": 2, "thrice": 3}
        train_data = []
        for _ in range(5000):
            n_clauses = rng.randint(1, 3)
            src_parts: list[str] = []
            tgt_parts: list[str] = []
            for ci in range(n_clauses):
                v = rng.choice(verbs)
                m_word, m_count = rng.choice(list(mults.items()))
                src_parts.append(f"{v} {m_word}")
                tgt_parts.extend([v.upper()] * m_count)
                if ci < n_clauses - 1:
                    src_parts.append("and")
            train_data.append(
                {"source": " ".join(src_parts), "target": " ".join(tgt_parts)}
            )

    payload: list[dict] = []

    # Condition A: random baseline (100 IID items)
    train_copy = list(train_data)
    random.Random(42).shuffle(train_copy)
    iid = train_copy[:100]

    for i, item in enumerate(iid):
        src, tgt = _hptb_row(cast(Mapping[str, Any], item))
        payload.append(
            format_for_kaggle(
                f"A_{i}",
                f"Translate the following sequence into its action representation:\n{src}",
                tgt,
                "H-PTB",
                "Cond_A",
            )
        )

    # Conditions C & D: contrastive pairs
    groups: dict[frozenset, list[tuple[str, str]]] = {}
    for item in train_data[:5000]:
        src, tgt = _hptb_row(cast(Mapping[str, Any], item))
        groups.setdefault(frozenset(src.split()), []).append((src, tgt))

    contrastive_idx = 0
    for items in groups.values():
        unique = list({tgt: (src, tgt) for src, tgt in items}.values())
        if len(unique) < 2:
            continue
        (src_a, tgt_a), (_, tgt_b) = unique[0], unique[1]
        if tgt_a == tgt_b:
            continue

        payload.append(
            format_for_kaggle(
                f"C_{contrastive_idx}",
                (
                    f"Which output strictly follows the compositional rule?\n"
                    f"Input: {src_a}\n"
                    f"Option A: {tgt_a}\n"
                    f"Option B: {tgt_b}\n"
                    f"Answer with 'A' or 'B'."
                ),
                "A",
                "H-PTB",
                "Cond_C",
            )
        )
        payload.append(
            format_for_kaggle(
                f"D_{contrastive_idx}",
                (
                    f"One output follows the structural rule; one follows a surface pattern.\n"
                    f"Input: {src_a}\n"
                    f"Rule-based output: {tgt_a}\n"
                    f"Surface-based output: {tgt_b}\n"
                    f"Which output relies on the compositional rule? "
                    f"Answer 'Rule-based' or 'Surface-based'."
                ),
                "Rule-based",
                "H-PTB",
                "Cond_D_Alpha",
            )
        )

        contrastive_idx += 1
        if contrastive_idx >= 50:
            break

    write_jsonl(
        os.path.join(SCRIPT_DIR, "kaggle_payloads", "hptb_pilot.jsonl"), payload
    )


# ──────────────────────────────────────────────────────────────────────────────
# TRACK 2 — METACOGNITION: H-Bar Metacognitive Calibration Benchmark (H-MCB)
# ──────────────────────────────────────────────────────────────────────────────


def generate_hmcb() -> None:
    print("\n[2/5] Generating H-MCB (Metacognition) ...")

    def _hmcb_row(item: Mapping[str, Any]) -> tuple[str, str]:
        return str(item["source"]), str(item["target"])

    try:
        ds = load_hub_dataset("kimnajoung/cogs")
        ood_key = "gen" if "gen" in ds else list(ds.keys())[-1]
        ood_raw = ds[ood_key]
        train_raw = ds["train"]

        ood_copy = list(ood_raw)
        random.Random(42).shuffle(ood_copy)
        ood = ood_copy[:20]

        train_copy = list(train_raw)
        random.Random(99).shuffle(train_copy)
        id_ctrl = train_copy[:10]

        print("  Using real COGS data.")
    except Exception as exc:
        print(f"  [INFO] Hub unavailable ({type(exc).__name__}). Using synthetic data.")
        rng = random.Random(42)
        agents = ["Emma", "Liam", "Aria", "Noah", "Zoe"]
        themes = ["the cake", "the book", "the ball", "the letter", "the flower"]
        verbs = [
            ("ate", "eat.agent", "eat.theme"),
            ("read", "read.agent", "read.theme"),
            ("found", "find.agent", "find.theme"),
            ("drew", "draw.agent", "draw.theme"),
        ]
        synth = []
        for _ in range(200):
            agent = rng.choice(agents)
            theme = rng.choice(themes)
            v_surface, agent_role, theme_role = rng.choice(verbs)
            t_var = theme.replace("the ", "") + "_x"
            lf = (
                f"* ; {agent_role} ( x ) , {agent.lower()} ( x ) "
                f"AND {theme_role} ( x ) , {t_var} ( x )"
            )
            synth.append({"source": f"{agent} {v_surface} {theme} .", "target": lf})

        half = len(synth) // 2
        ood = synth[half : half + 20]
        id_ctrl = synth[:10]

    payload: list[dict] = []

    # Stage 1: self-model elicitation (T=0.7)
    item_type_descriptions = [
        "applying a noun-phrase rule to novel agent-theme combinations",
        "applying a verb-phrase rule to unseen verb inflections",
        "applying a recursive embedding rule to three-clause structures",
        "applying a passivisation rule to held-out verbs",
        "applying a prepositional-phrase attachment rule to novel nouns",
    ]
    for i, desc in enumerate(item_type_descriptions):
        payload.append(
            format_for_kaggle(
                f"pred_{i}",
                (
                    f"You will complete 20 compositional semantic-parsing tasks involving {desc}.\n"
                    f"These items were not present verbatim in your training data.\n"
                    f"Estimate: what percentage (0-100) of these 20 tasks do you expect "
                    f"to answer correctly?\nRespond with a single integer."
                ),
                "[0-100]",
                "H-MCB",
                "Stage1_Prediction",
                temperature=0.7,
            )
        )

    # Stage 2: OOD performance (T=0)
    for i, item in enumerate(ood):
        src, tgt = _hmcb_row(cast(Mapping[str, Any], item))
        payload.append(
            format_for_kaggle(
                f"perf_{i}",
                f"Map the following sentence to its logical form:\n{src}",
                tgt,
                "H-MCB",
                "Stage2_Performance",
            )
        )

    # In-distribution control (T=0)
    for i, item in enumerate(id_ctrl):
        src, tgt = _hmcb_row(cast(Mapping[str, Any], item))
        payload.append(
            format_for_kaggle(
                f"id_ctrl_{i}",
                f"Map the following sentence to its logical form:\n{src}",
                tgt,
                "H-MCB",
                "Stage2_ID_Control",
            )
        )

    write_jsonl(
        os.path.join(SCRIPT_DIR, "kaggle_payloads", "hmcb_pilot.jsonl"), payload
    )


# ──────────────────────────────────────────────────────────────────────────────
# TRACK 3 — ATTENTION: H-Bar Attentional Fidelity Benchmark (H-AFB)
# ──────────────────────────────────────────────────────────────────────────────


def generate_hafb() -> None:
    print("\n[3/5] Generating H-AFB (Attention) ...")

    def _hafb_row(item: Mapping[str, Any]) -> tuple[str, str]:
        return str(item.get("commands", "")), str(item.get("actions", ""))

    try:
        ds = load_hub_dataset("scan")
        test_raw = ds["test"]

        test_copy = list(test_raw)
        random.Random(42).shuffle(test_copy)
        test = test_copy[:50]

        print("  Using real SCAN data.")
    except Exception as exc:
        print(f"  [INFO] Hub unavailable ({type(exc).__name__}). Using synthetic data.")
        rng = random.Random(42)
        actions = {"walk": "WALK", "run": "RUN", "look": "LOOK", "turn": "TURN"}
        directions = {
            "left": "LTURN",
            "right": "RTURN",
            "around": "LTURN LTURN LTURN LTURN",
        }
        multipliers = {"twice": 2, "thrice": 3}

        def expand(act: str, direction: str | None, mult: int) -> str:
            tokens: list[str] = []
            action_token = actions.get(act, "JUMP")
            if direction:
                turn = directions[direction]
                for _ in range(mult):
                    tokens.append(turn)
                    tokens.append(action_token)
            else:
                for _ in range(mult):
                    tokens.append(action_token)
            return " ".join(tokens)

        rows: list[dict[str, str]] = []
        # OOD: JUMP primitives
        for mult_word, mult_count in multipliers.items():
            rows.append(
                {
                    "commands": f"jump {mult_word}",
                    "actions": " ".join(["JUMP"] * mult_count),
                }
            )
        rows.append({"commands": "jump", "actions": "JUMP"})

        reps = (50 // len(rows)) + 1
        test = (rows * reps)[:50]

    payload: list[dict] = []

    for i, item in enumerate(test):
        src, tgt = _hafb_row(cast(Mapping[str, Any], item))

        # OOD-Structural: no surface confound
        payload.append(
            format_for_kaggle(
                f"struct_{i}",
                f"Execute the following command sequence:\n{src}",
                tgt,
                "H-AFB",
                "OOD_Structural",
            )
        )

        # OOD-Surface-Conflict: inject misleading "RED" token.
        if "JUMP JUMP" not in tgt:
            payload.append(
                format_for_kaggle(
                    f"conflict_{i}",
                    f"Execute the following command sequence:\nRED {src}",
                    tgt,  # correct answer is unchanged
                    "H-AFB",
                    "OOD_SurfaceConflict",
                )
            )

    write_jsonl(
        os.path.join(SCRIPT_DIR, "kaggle_payloads", "hafb_pilot.jsonl"), payload
    )


# ──────────────────────────────────────────────────────────────────────────────
# TRACK 4 — EXECUTIVE FUNCTIONS: H-Bar Delegation Control Benchmark (H-DCB)
# ──────────────────────────────────────────────────────────────────────────────


def generate_hdcb() -> None:
    print("\n[4/5] Generating H-DCB (Executive Functions) ...")

    def _hdcb_src(item: Mapping[str, Any]) -> tuple[str, str]:
        return str(item["source"]), str(item["target"])

    def _hdcb_train_str(item: Mapping[str, Any]) -> str:
        return f"{item['source']} -> {item['target']}"

    try:
        ds = load_hub_dataset("kimnajoung/cogs")
        ood_key = "gen" if "gen" in ds else list(ds.keys())[-1]
        ood_raw = ds[ood_key]
        train_raw = ds["train"]

        ood = ood_raw[:20]
        train = train_raw
        print("  Using real COGS data.")
    except Exception as exc:
        print(f"  [INFO] Hub unavailable ({type(exc).__name__}). Using synthetic data.")
        rng = random.Random(42)
        agents = ["Emma", "Liam", "Aria", "Noah", "Zoe"]
        themes = ["the cake", "the book", "the ball", "the letter", "the flower"]
        verbs = [
            ("ate", "eat.agent", "eat.theme"),
            ("read", "read.agent", "read.theme"),
            ("found", "find.agent", "find.theme"),
            ("drew", "draw.agent", "draw.theme"),
        ]
        synth = []
        for _ in range(500):
            agent = rng.choice(agents)
            theme = rng.choice(themes)
            v_surface, agent_role, theme_role = rng.choice(verbs)
            t_var = theme.replace("the ", "") + "_x"
            lf = (
                f"* ; {agent_role} ( x ) , {agent.lower()} ( x ) "
                f"AND {theme_role} ( x ) , {t_var} ( x )"
            )
            synth.append({"source": f"{agent} {v_surface} {theme} .", "target": lf})

        half = len(synth) // 2
        ood = synth[half : half + 20]
        train = synth[:half]

    rng = random.Random(77)
    train_pool = [
        _hdcb_train_str(cast(Mapping[str, Any], train[j]))
        for j in range(min(200, len(train)))
    ]

    payload: list[dict] = []

    for i, item in enumerate(ood):
        src, tgt = _hdcb_src(cast(Mapping[str, Any], item))

        # rho=0: no retrieval
        payload.append(
            format_for_kaggle(
                f"rho0_{i}",
                f"Map to logical form: {src}",
                tgt,
                "H-DCB",
                "RAG_Rho0",
            )
        )
        # rho=0.5: partial retrieval (3 random training examples)
        ctx_half = " | ".join(rng.sample(train_pool, 3))
        payload.append(
            format_for_kaggle(
                f"rho05_{i}",
                f"Context examples: {ctx_half}\n\nNow map to logical form: {src}",
                tgt,
                "H-DCB",
                "RAG_Rho0.5",
            )
        )
        # rho=1.0: full retrieval (5 random training examples)
        ctx_full = " | ".join(rng.sample(train_pool, 5))
        payload.append(
            format_for_kaggle(
                f"rho10_{i}",
                f"Context examples: {ctx_full}\n\nNow map to logical form: {src}",
                tgt,
                "H-DCB",
                "RAG_Rho1.0",
            )
        )

    write_jsonl(
        os.path.join(SCRIPT_DIR, "kaggle_payloads", "hdcb_pilot.jsonl"), payload
    )


# ──────────────────────────────────────────────────────────────────────────────
# TRACK 5 — SOCIAL COGNITION: H-Bar Schema Transmission Benchmark (H-STB)
# ──────────────────────────────────────────────────────────────────────────────


def generate_hstb() -> None:
    print("\n[5/5] Generating H-STB (Social Cognition) ...")

    def _hstb_src(item: Mapping[str, Any]) -> tuple[str, str]:
        return str(item["source"]), str(item["target"])

    try:
        ds = load_hub_dataset("kimnajoung/cogs")
        ood_key = "gen" if "gen" in ds else list(ds.keys())[-1]
        ood_raw = ds[ood_key]
        ood = ood_raw[:20]
        print("  Using real COGS data.")
    except Exception as exc:
        print(f"  [INFO] Hub unavailable ({type(exc).__name__}). Using synthetic data.")
        rng = random.Random(42)
        agents = ["Emma", "Liam", "Aria", "Noah", "Zoe"]
        themes = ["the cake", "the book", "the ball", "the letter", "the flower"]
        verbs = [
            ("ate", "eat.agent", "eat.theme"),
            ("read", "read.agent", "read.theme"),
            ("found", "find.agent", "find.theme"),
            ("drew", "draw.agent", "draw.theme"),
        ]
        synth = []
        for _ in range(200):
            agent = rng.choice(agents)
            theme = rng.choice(themes)
            v_surface, agent_role, theme_role = rng.choice(verbs)
            t_var = theme.replace("the ", "") + "_x"
            lf = (
                f"* ; {agent_role} ( x ) , {agent.lower()} ( x ) "
                f"AND {theme_role} ( x ) , {t_var} ( x )"
            )
            synth.append({"source": f"{agent} {v_surface} {theme} .", "target": lf})

        half = len(synth) // 2
        ood = synth[half : half + 20]

    examples = [
        ("The cat ate the cake.", "eat.agent(x), cat(x) AND eat.theme(x), cake_x(x)"),
        ("Liam read the book.", "read.agent(x), liam(x) AND read.theme(x), book_x(x)"),
        ("Aria found the ball.", "find.agent(x), aria(x) AND find.theme(x), ball_x(x)"),
    ]
    facts_str = " | ".join(f"'{s}' -> '{t}'" for s, t in examples)

    payload: list[dict] = []

    for i, item in enumerate(ood):
        src, tgt = _hstb_src(cast(Mapping[str, Any], item))

        # Schema transmission: structural rule (high mu_AB condition)
        payload.append(
            format_for_kaggle(
                f"schema_{i}",
                (
                    f"Agent A has explained this rule: "
                    f"'Verbs become event predicates; noun phrases become entity variables "
                    f"linked by thematic roles (agent, theme, recipient).'\n"
                    f"Using this structural rule, map the following sentence to its logical form:\n{src}"
                ),
                tgt,
                "H-STB",
                "Cond_Schema",
            )
        )

        # Fact transmission: surface observations only (low mu_AB condition)
        payload.append(
            format_for_kaggle(
                f"fact_{i}",
                (
                    f"Agent A has listed these observed mappings: {facts_str}.\n"
                    f"Using these examples, map the following sentence to its logical form:\n{src}"
                ),
                tgt,
                "H-STB",
                "Cond_Fact",
            )
        )

        # Theory-of-mind component: Agent A predicts Agent B accuracy (T=0.7)
        payload.append(
            format_for_kaggle(
                f"tom_{i}",
                (
                    f"Agent B has only seen the structural rule: "
                    f"'Verbs become event predicates; nouns become entity variables.'\n"
                    f"Predict Agent B's accuracy (0-100%) on this item:\n{src}"
                ),
                "[0-100]",
                "H-STB",
                "Cond_ToM",
                temperature=0.7,
            )
        )

    write_jsonl(
        os.path.join(SCRIPT_DIR, "kaggle_payloads", "hstb_pilot.jsonl"), payload
    )


# ──────────────────────────────────────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    generate_hptb()
    generate_hmcb()
    generate_hafb()
    generate_hdcb()
    generate_hstb()
    print("\nAll payloads written to kaggle_payloads/")
