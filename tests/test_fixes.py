import subprocess, sys
import numpy as np
from khoros_cantata.workspace_runtime import NativeOperatorRegistry, HistoricalWorkspaceParser, WorkspaceExecutor
from khoros_cantata.phase21_numeric import conv1d_khoros

R = NativeOperatorRegistry()

def op(name, params=None, **inputs):
    return R.resolve('DATAMANIP', name)(params or {}, inputs)

def test_unary_accepts_arrays_and_scalars():
    assert np.array_equal(op('kneg', i=[1, -2])['o'], [-1, 2])
    assert op('kneg', i=3)['o'] == -3
    assert np.allclose(op('ksqrt', i=np.array([4., 9.]))['o'], [2, 3])
    assert np.array_equal(op('kfloor', i=[1.5, -1.5])['o'], [1, -2])
    assert np.array_equal(op('kbitnot', i=[0])['o'], [-1])

def test_binary_broadcast():
    assert np.array_equal(op('kadd', i1=[1, 2], i2=10)['o'], [11, 12])
    assert op('kmul', i1=2, i2=3)['o'] == 6

def test_kclip_zero_lower_bound():
    assert op('kclip', {'lc': 0, 'uc': 5}, i=[-3, 2, 9])['o'] == [0, 2, 5]
    assert op('kclip', {'lc': 0}, i=-1)['o'] == 0
    assert np.array_equal(op('kclip', {'lc': 0, 'uc': 1}, i=np.array([-1., .5, 2]))['o'], [0, .5, 1])

def test_conv_vectorized_matches_loop():
    rng = np.random.default_rng(0); x = rng.normal(size=50); k = rng.normal(size=7)
    for w0 in (0, 3, 6):
        for ext in (False, True):
            got = conv1d_khoros(x, k, w0, ext)
            n = len(x) + len(k) - 1 if ext else len(x)
            ref = [sum(k[q] * (x[j - q] if 0 <= j - q < len(x) else 0) for q in range(len(k))) for j in range(w0, w0 + n)]
            assert np.allclose(got, ref)

def test_signal_workspace_runs(tmp_path):
    w = tmp_path / 'w.wksp'
    w.write_text("Glyph:SAMPLEDATA:signals:1:0:0::signals\nGlyph:DATAMANIP:kneg:2:0:0::kneg\n"
                 "NodeConnection:1:o:2:i:\n")
    r = NativeOperatorRegistry(); r.register('SAMPLEDATA', 'signals', lambda p, i: {'o': [0., 1., -1.]})
    ws = WorkspaceExecutor(r).execute(HistoricalWorkspaceParser().parse(w))
    assert np.array_equal(ws.nodes['2'].outputs['o'].data.value, [0., -1., 1.])

def test_cli_degrades_without_corpus(monkeypatch):
    for cmd in ('check', 'inventory'):
        p = subprocess.run([sys.executable, '-m', 'khoros_cantata.cli', cmd], capture_output=True, text=True,
                           env={'KHOROS_SOURCE_ROOT': '/nonexistent', 'PATH': ''})
        assert p.returncode == 0, p.stderr
