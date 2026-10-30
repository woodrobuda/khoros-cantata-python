# Operator status (operators branch)

Source list: `reports/final_134_operator_closure_matrix.csv` (134 operators). Status:
- **implemented** — new native implementation on this branch, registered in `NativeOperatorRegistry`, with a pytest test (`tests/test_registry_ops.py` plus module tests).
- **previously existed** — present before this branch (now also registered/extended where noted).
- **skipped** — not implemented, with reason.

Module key: S = `khoros_cantata.ops_signal`, I = `ops_image`, D = `ops_datamanip`.

| # | toolbox | operator | status | implementation | notes |
|---|---|---|---|---|---|
| 1 | bootstrap | conductor | skipped | — | system/build tool (toolbox generation, file utilities, daemons); not a data operator |
| 2 | bootstrap | ghostwriter | skipped | — | system/build tool (toolbox generation, file utilities, daemons); not a data operator |
| 3 | bootstrap | kcp | skipped | — | system/build tool (toolbox generation, file utilities, daemons); not a data operator |
| 4 | bootstrap | kecho | skipped | — | system/build tool (toolbox generation, file utilities, daemons); not a data operator |
| 5 | bootstrap | kexec | skipped | — | system/build tool (toolbox generation, file utilities, daemons); not a data operator |
| 6 | bootstrap | kgendepend | skipped | — | system/build tool (toolbox generation, file utilities, daemons); not a data operator |
| 7 | bootstrap | kgenimake | skipped | — | system/build tool (toolbox generation, file utilities, daemons); not a data operator |
| 8 | bootstrap | kgenmanual | skipped | — | system/build tool (toolbox generation, file utilities, daemons); not a data operator |
| 9 | bootstrap | kgenobj | skipped | — | system/build tool (toolbox generation, file utilities, daemons); not a data operator |
| 10 | bootstrap | kgentb | skipped | — | system/build tool (toolbox generation, file utilities, daemons); not a data operator |
| 11 | bootstrap | kman | skipped | — | system/build tool (toolbox generation, file utilities, daemons); not a data operator |
| 12 | bootstrap | krename | skipped | — | system/build tool (toolbox generation, file utilities, daemons); not a data operator |
| 13 | bootstrap | krm | skipped | — | system/build tool (toolbox generation, file utilities, daemons); not a data operator |
| 14 | bootstrap | kset | skipped | — | system/build tool (toolbox generation, file utilities, daemons); not a data operator |
| 15 | bootstrap | phantomd | skipped | — | system/build tool (toolbox generation, file utilities, daemons); not a data operator |
| 16 | datamanip | kappend | implemented | `D.kappend` |  |
| 17 | datamanip | karith1 | implemented | `D.karith1` |  |
| 18 | datamanip | karith2 | implemented | `D.karith2` |  |
| 19 | datamanip | kasc2loc | implemented | `D.kasc2seg` | ASCII -> location segment |
| 20 | datamanip | kasc2map | implemented | `D.kasc2seg` | ASCII -> map segment |
| 21 | datamanip | kasc2mask | implemented | `D.kasc2seg` | ASCII -> mask segment |
| 22 | datamanip | kasc2time | implemented | `D.kasc2seg` | ASCII -> time segment |
| 23 | datamanip | kasc2val | implemented | `D.kasc2seg` | ASCII -> value segment |
| 24 | datamanip | kaxis | implemented | `D.kaxis` |  |
| 25 | datamanip | kbessel | implemented | `D.kbessel` |  |
| 26 | datamanip | kbitwise | implemented | `D.kbitwise` |  |
| 27 | datamanip | kblend | implemented | `D.kblend` |  |
| 28 | datamanip | kclip | previously existed | default registry op `kclip` | fixed: lower bound 0 was treated as unset; ndarray support |
| 29 | datamanip | kcmplx | implemented | `D.kcmplx` |  |
| 30 | datamanip | kcmplx2real | previously existed | default registry op `kcmplx2real` | re-registered: -real/-imag/-mag/-phase/-logmag, ndarray support |
| 31 | datamanip | kcomment | implemented | `D.kcomment` |  |
| 32 | datamanip | kcompare | implemented | `D.kcompare` |  |
| 33 | datamanip | kconvert | implemented | `D.kconvert` |  |
| 34 | datamanip | kcpfromval | implemented | `D.kcpfromval` |  |
| 35 | datamanip | kcpseg | implemented | `D.kcpseg` |  |
| 36 | datamanip | kcptoval | implemented | `D.kcptoval` |  |
| 37 | datamanip | kextract | implemented | `D.kextract` |  |
| 38 | datamanip | kfft | previously existed | `phase21_numeric.khoros_fft` | now registered as DATAMANIP:kfft (-dir -scale -center -w -h ...) |
| 39 | datamanip | kflip | implemented | `D.kflip` |  |
| 40 | datamanip | kformats | skipped | — | lists supported file formats (informational CLI) |
| 41 | datamanip | kgate | implemented | `D.kgate` |  |
| 42 | datamanip | kgconst | implemented | `S.kgconst` |  |
| 43 | datamanip | kgeneric | skipped | — | generic external-command wrapper; semantics depend on the GUI form |
| 44 | datamanip | kgenloc | implemented | `D.kgenloc` |  |
| 45 | datamanip | kgnoise | implemented | `S.kgnoise` | gaussian/uniform/rayleigh/exponential/poisson |
| 46 | datamanip | kgsin | previously existed | `phase21_numeric.khoros_sine` | now registered as DATAMANIP:kgsin |
| 47 | datamanip | khisto | implemented | `S.khisto` |  |
| 48 | datamanip | khistops | implemented | `S.khistops` | equalize / stretch / match |
| 49 | datamanip | kimportasc | implemented | `D.kimportasc` |  |
| 50 | datamanip | kimportraw | implemented | `D.kimportraw` |  |
| 51 | datamanip | kimpulse | implemented | `S.kimpulse` |  |
| 52 | datamanip | kinsertseg | implemented | `D.kinsertseg` |  |
| 53 | datamanip | kinset | implemented | `D.kinset` |  |
| 54 | datamanip | kinverse | implemented | `D.karith1(op="recip")` | semantics not confirmed from Khoros docs; implemented as multiplicative inverse 1/x |
| 55 | datamanip | kkmeans | implemented | `I.kmeans` |  |
| 56 | datamanip | klinearop | previously existed | `phase21_numeric.conv1d_khoros` | vectorized (np.convolve); registered as DATAMANIP:klinearop |
| 57 | datamanip | klocxform | implemented | `D.klocxform` |  |
| 58 | datamanip | klogexp | implemented | `D.klogexp` |  |
| 59 | datamanip | kmapdata | implemented | `D.kmapdata` |  |
| 60 | datamanip | kmsquish | skipped | — | semantics not established from available sources |
| 61 | datamanip | knoise | implemented | `S.knoise` | additive/multiplicative/signal-dependent Poisson |
| 62 | datamanip | knormal | implemented | `D.knormal` |  |
| 63 | datamanip | korient | implemented | `D.korient` |  |
| 64 | datamanip | kpad | implemented | `D.kpad` |  |
| 65 | datamanip | kprdata | implemented | `D.kprdata` | returns text |
| 66 | datamanip | kprval | implemented | `D.kprval` | returns text |
| 67 | datamanip | kreal2cmplx | implemented | `D.kreal2cmplx` |  |
| 68 | datamanip | kreplace | implemented | `D.kreplace` |  |
| 69 | datamanip | kresample | implemented | `S.kresample` | per-axis -wsize..-esize; interp zero/linear/fft |
| 70 | datamanip | krmseg | implemented | `D.krmseg` |  |
| 71 | datamanip | ksampline | implemented | `D.ksampline` |  |
| 72 | datamanip | ksegcmp | implemented | `D.ksegcmp` |  |
| 73 | datamanip | ksetdattr | implemented | `D.ksetdattr` |  |
| 74 | datamanip | kshot | implemented | `S.kshot` | salt-and-pepper impulse noise |
| 75 | datamanip | kstats | previously existed | `phase21_numeric.stats` | now registered as DATAMANIP:kstats |
| 76 | datamanip | kunmask | implemented | `D.kunmask` |  |
| 77 | datamanip | kwiener | implemented | `S.kwiener` | frequency-domain Wiener restoration (PSF on i2, -nsr) or adaptive local Wiener (no PSF) |
| 78 | dataserv | kgdbm_dump | skipped | — | database dump utility (system tool); KDBM read support already lives in kdbm_compat |
| 79 | design | kcat | skipped | — | DESIGN toolbox entry; historical semantics not documented in available sources |
| 80 | envision | kautocolor | skipped | — | interactive display colour allocation (GUI/X11 visual) |
| 81 | envision | kcolorspace | implemented | `D.kcolorspace` | rgb<->hsv, rgb<->yiq, rgb2grey |
| 82 | geometry | gapplytex | skipped | — | 3-D renderer texture mapping (render pipeline not reconstructed) |
| 83 | geometry | gcmaplegend | skipped | — | GEOMETRY render/mesh object operator; the geometry object model and renderer are not reconstructed |
| 84 | geometry | gcolorize | implemented | `D.gcolorize` |  |
| 85 | geometry | gcuberille | skipped | — | GEOMETRY render/mesh object operator; the geometry object model and renderer are not reconstructed |
| 86 | geometry | gextents | implemented | `D.gextents` |  |
| 87 | geometry | gflipnorms | skipped | — | GEOMETRY render/mesh object operator; the geometry object model and renderer are not reconstructed |
| 88 | geometry | ggencmap | implemented | `D.ggencmap` |  |
| 89 | geometry | ggridder2d | implemented | `D.ggridder2d` |  |
| 90 | geometry | gimpfacet | skipped | — | GEOMETRY render/mesh object operator; the geometry object model and renderer are not reconstructed |
| 91 | geometry | gisosurface | skipped | — | GEOMETRY render/mesh object operator; the geometry object model and renderer are not reconstructed |
| 92 | geometry | glinecolor | skipped | — | GEOMETRY render/mesh object operator; the geometry object model and renderer are not reconstructed |
| 93 | geometry | glinexyz | skipped | — | GEOMETRY render/mesh object operator; the geometry object model and renderer are not reconstructed |
| 94 | geometry | goctmesh | skipped | — | GEOMETRY render/mesh object operator; the geometry object model and renderer are not reconstructed |
| 95 | geometry | gprgeom | skipped | — | GEOMETRY render/mesh object operator; the geometry object model and renderer are not reconstructed |
| 96 | geometry | gquadmesh | skipped | — | GEOMETRY render/mesh object operator; the geometry object model and renderer are not reconstructed |
| 97 | geometry | gspheres | skipped | — | GEOMETRY render/mesh object operator; the geometry object model and renderer are not reconstructed |
| 98 | geometry | gtubeness | skipped | — | GEOMETRY render/mesh object operator; the geometry object model and renderer are not reconstructed |
| 99 | geometry | kslicer | implemented | `D.kslicer` |  |
| 100 | image | ifilt_design | implemented | `I.ifilt_design` |  |
| 101 | image | igamut | implemented | `I.igamut` | k-means colour quantization -> index image + colormap |
| 102 | image | igauss_func | implemented | `I.igauss_func` |  |
| 103 | image | igeowarp | implemented | `I.igeowarp` |  |
| 104 | image | igradient | implemented | `I.igradient` |  |
| 105 | image | imedian | implemented | `I.imedian` |  |
| 106 | image | ipostscr | skipped | — | PostScript printer output (obsolete device driver) |
| 107 | image | irotate | implemented | `I.irotate` |  |
| 108 | image | itexture | implemented | `I.itexture` |  |
| 109 | matrix | mcovar | implemented | `D.mcovar` |  |
| 110 | matrix | meigen | implemented | `D.meigen` |  |
| 111 | matrix | mexchg | implemented | `D.mexchg` |  |
| 112 | matrix | mextract_diag | implemented | `D.mextract_diag` |  |
| 113 | matrix | mgdiag | implemented | `D.mgdiag` |  |
| 114 | matrix | minvert | implemented | `D.minvert` |  |
| 115 | matrix | mlse | implemented | `D.mlse` |  |
| 116 | matrix | mlud | implemented | `D.mlud` |  |
| 117 | matrix | mmul | implemented | `D.mmul` |  |
| 118 | matrix | mpow | implemented | `D.mpow` |  |
| 119 | matrix | mrcsum | implemented | `D.mrcsum` |  |
| 120 | matrix | mreplicate | implemented | `D.mreplicate` |  |
| 121 | matrix | msvd | implemented | `D.msvd` |  |
| 122 | migration | dbcnvrt | skipped | — | Khoros 1->2 migration utility for obsolete file/toolbox formats |
| 123 | migration | kdarwin | skipped | — | Khoros 1->2 migration utility for obsolete file/toolbox formats |
| 124 | migration | ktbupdb | skipped | — | Khoros 1->2 migration utility for obsolete file/toolbox formats |
| 125 | migration | mkproto | skipped | — | Khoros 1->2 migration utility for obsolete file/toolbox formats |
| 126 | migration | uisupdate | skipped | — | Khoros 1->2 migration utility for obsolete file/toolbox formats |
| 127 | support | kdbmcat | skipped | — | developer/support utility (man pages, toolbox index, object search) |
| 128 | support | kdiffobj | skipped | — | developer/support utility (man pages, toolbox index, object search) |
| 129 | support | kfindobj | skipped | — | developer/support utility (man pages, toolbox index, object search) |
| 130 | support | kgenman | skipped | — | developer/support utility (man pages, toolbox index, object search) |
| 131 | support | kgentbindex | skipped | — | developer/support utility (man pages, toolbox index, object search) |
| 132 | support | kgenwhatis | skipped | — | developer/support utility (man pages, toolbox index, object search) |
| 133 | support | kgrepobj | skipped | — | developer/support utility (man pages, toolbox index, object search) |
| 134 | support | ksync | skipped | — | developer/support utility (man pages, toolbox index, object search) |

**Totals:** implemented 80, previously existed 6, skipped 48 (of 134).

## Extended operators (not in the 134 list)

Registered operators requested for the library but absent from the historical matrix (windows, FIR/IIR, correlation, spectra, wavelets, morphology, thresholding, etc.) and single-op aliases:

`IMAGE:iclose`, `IMAGE:idilate`, `IMAGE:iedge`, `IMAGE:ierode`, `IMAGE:ilabel`, `IMAGE:ilaplacian`, `IMAGE:imorph`, `IMAGE:iopen`, `IMAGE:iscale`, `IMAGE:ithresh`, `IMAGE:itranslate`, `DATAMANIP:kabsdiff`, `DATAMANIP:kadd`, `DATAMANIP:katan`, `DATAMANIP:kceil`, `SIGNAL:kconvolve`, `SIGNAL:kcorr`, `DATAMANIP:kcos`, `DATAMANIP:kdiv`, `DATAMANIP:kdivinto`, `SIGNAL:kdwt`, `DATAMANIP:kexp`, `SIGNAL:kfir`, `SIGNAL:kgwindow`, `SIGNAL:kidwt`, `SIGNAL:kiir`, `DATAMANIP:klog`, `DATAMANIP:klog10`, `DATAMANIP:kmag`, `DATAMANIP:kmax`, `DATAMANIP:kmin`, `DATAMANIP:kmul`, `DATAMANIP:kpow`, `SIGNAL:kpsd`, `DATAMANIP:ksign`, `DATAMANIP:ksin`, `SIGNAL:kspectrum`, `DATAMANIP:ksub`, `DATAMANIP:ktan`, `SIGNAL:kwindow`

## Conventions

- Ports: `i` (single input), `i1`/`i2` (dual), `o` (+ `o2`, `o3`, ... for secondary outputs); `kcmplx2real`/`kmag` output `om`, as in historical workspaces.
- Options come from the glyph command (`-name value`); dual-input arithmetic falls back to the `-real` constant when `i2` is unconnected (Khoros behaviour).
- Generators take sizes from `-wsize -hsize -dsize -tsize -esize`.
- `ViffObject` inputs: operator runs on the `value` segment and returns a deep copy with new value data (attributes and other segments preserved).
- Image axes: axis 0 = width (x), axis 1 = height (y), matching VIFF value layout; N-D inputs are processed per (w,h) plane.
- Matrices: ndarray in NumPy (row, col) order; ViffObject converted with rows = height.
- Every operator is also resolvable under toolbox `*`.
