# Changelog

## Unreleased — operators branch

- Native operator library (`ops_signal`, `ops_image`, `ops_datamanip`, `operators`): 80 of the 134 listed
  operators newly implemented and registered, plus 40 extended/alias operators; see `OPERATORS_STATUS.md`.
- Registry ops accept NumPy arrays and lists (previously scalar-only); `kclip` honours a lower bound of 0.
- `klinearop` convolution vectorized; deprecated `np.fromstring` removed.
- Parser: Khoros 2.x `Glyph:TB:op::ID:...` lines, option-only commands, negative option values,
  and connections after `#GlyphEnd` (previously dropped).
- `check`/`inventory` CLI report SKIP / unavailable instead of erroring when `historical_source/` is absent.
- Packaging: explicit `packages`, new `scipy` dependency.
- Causal streaming mode (`khoros_cantata.streaming`, `docs/STREAMING.md`): `StreamingExecutor` pushes
  samples/chunks through a workspace with per-glyph state; operators declare a stateful `StreamOp`;
  non-causal glyphs are rejected unless wrapped in `STREAM:krolling -window N`; `find_lookahead` /
  `assert_no_lookahead` verification utility; `batch_execute` runs the same graph in batch.
- New causal operators `kema`, `krunstats`, `kdelay`, `kdiff`, `kcross`; new (non-causal) `khilbert`.
- Example: `examples/streaming_ema_crossover.{wk,py}` (EMA 10/40 crossover on a synthetic price series).
- `OPERATORS_STATUS.md` gains a streamable column.

## 0.22.0 — Phase 22 release

- Completed the planned Phase 0–22 reconstruction program.
- Added Python-native workspace restoration and execution.
- Added historical UIS/pane parsing and operator specifications.
- Added focused VIFF and KDBM compatibility layers.
- Added recovered numerical behavior and regression support.
- Added release tests and legacy-dependency audit.
- Added user manual, programmer guide, API reference, and compatibility documentation.
- Preserved explicit limits where a historical executable oracle or original sample data is unavailable.
