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

## 0.22.0 — Phase 22 release

- Completed the planned Phase 0–22 reconstruction program.
- Added Python-native workspace restoration and execution.
- Added historical UIS/pane parsing and operator specifications.
- Added focused VIFF and KDBM compatibility layers.
- Added recovered numerical behavior and regression support.
- Added release tests and legacy-dependency audit.
- Added user manual, programmer guide, API reference, and compatibility documentation.
- Preserved explicit limits where a historical executable oracle or original sample data is unavailable.
