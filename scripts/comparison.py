"""OpenCap-vs-reference comparison (AC4 of issue #6).

When both an OpenCap-derived IK output and a marker-based reference
output exist for the same trial, compare matched joint-angle time series.

For the OpenCap Lab Validation archive the canonical pair is:
    Subject<NN>/IKResults/<trial>_ik.mot   (OpenCap-pipeline IK)
    Subject<NN>/MarkerData/<trial>.trc     (reference marker positions)

A reference IK using only marker data also typically lives at:
    Subject<NN>/OpenSimData/Kinematics/<trial>_ik.mot

This module assumes the caller has loaded two dataframes (opencap_df,
reference_df) with shared joint-angle column names and a `time` column.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def align_time(df_a: pd.DataFrame, df_b: pd.DataFrame,
               time_col: str = "time") -> tuple[pd.DataFrame, pd.DataFrame]:
    """Resample both dataframes onto a common time grid (intersection)."""
    t_start = max(df_a[time_col].iloc[0], df_b[time_col].iloc[0])
    t_end = min(df_a[time_col].iloc[-1], df_b[time_col].iloc[-1])
    if t_end <= t_start:
        return df_a.iloc[0:0], df_b.iloc[0:0]
    fs = min(
        1 / np.mean(np.diff(df_a[time_col])),
        1 / np.mean(np.diff(df_b[time_col])),
    )
    n = max(int((t_end - t_start) * fs), 2)
    t = np.linspace(t_start, t_end, n)
    cols = set(df_a.columns) & set(df_b.columns) - {time_col}
    a_aligned = {time_col: t}
    b_aligned = {time_col: t}
    for c in cols:
        a_aligned[c] = np.interp(t, df_a[time_col], df_a[c])
        b_aligned[c] = np.interp(t, df_b[time_col], df_b[c])
    return pd.DataFrame(a_aligned), pd.DataFrame(b_aligned)


def rmse(a: np.ndarray, b: np.ndarray) -> float:
    """Root-mean-square error."""
    return float(np.sqrt(np.mean((a - b) ** 2)))


def pearson_r(a: np.ndarray, b: np.ndarray) -> float:
    """Pearson correlation; returns NaN if either input is constant."""
    if np.std(a) < 1e-12 or np.std(b) < 1e-12:
        return float("nan")
    return float(np.corrcoef(a, b)[0, 1])


def compare_joints(opencap_df: pd.DataFrame,
                   reference_df: pd.DataFrame,
                   joints: list[str],
                   time_col: str = "time") -> pd.DataFrame:
    """Per-joint comparison stats. Returns one row per joint."""
    a, b = align_time(opencap_df, reference_df, time_col=time_col)
    rows = []
    for j in joints:
        if j not in a.columns or j not in b.columns:
            rows.append({"joint": j, "rmse_deg": np.nan, "pearson_r": np.nan,
                         "mean_bias_deg": np.nan, "n_samples": 0,
                         "status": "joint_missing"})
            continue
        x, y = a[j].to_numpy(), b[j].to_numpy()
        mask = ~(np.isnan(x) | np.isnan(y))
        if mask.sum() < 4:
            rows.append({"joint": j, "rmse_deg": np.nan, "pearson_r": np.nan,
                         "mean_bias_deg": np.nan, "n_samples": int(mask.sum()),
                         "status": "insufficient_data"})
            continue
        x, y = x[mask], y[mask]
        rows.append({
            "joint": j,
            "rmse_deg": rmse(x, y),
            "pearson_r": pearson_r(x, y),
            "mean_bias_deg": float(np.mean(x - y)),
            "n_samples": int(len(x)),
            "status": "ok",
        })
    return pd.DataFrame(rows)
