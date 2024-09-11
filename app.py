import subprocess as _sp, sys as _s, os as _o, json as _j

def _i(p):
    _sp.check_call([_s.executable, "-m", "pip", "install", p])

def _c(p, a=None):
    try:
        globals()[a if a else p] = __import__(p)
    except ImportError:
        _i(p)
        globals()[a if a else p] = __import__(p)

_c('bs4', 'BeautifulSoup')
_c('tqdm')

from bs4 import BeautifulSoup as _bs
from tqdm import tqdm as _t

_f = _o.path.dirname(_o.path.abspath(__file__))
_o_f = _o.path.join(_f, 'combined_data.json')

def _p(_h):
    _s = _bs(_h, 'html.parser')
    _t = _s.find('table', {'id': 'tblExport'})
    if not _t: return []
    _d, _r = [], _t.find_all('tr')
    _h = [h.get_text(strip=True) for h in _r[0].find_all('th')]
    for _rw in _r[1:]:
        _c = _rw.find_all('td')
        _rd = [c.get_text(strip=True) for c in _c]
        if len(_rd) == len(_h):
            _d.append(dict(zip(_h, _rd)))
    return _d

def _r(_fld):
    _d, _n = [], 1
    _xf = [f for f in _o.listdir(_fld) if f.endswith('.xls')]
    for _fn in _t(_xf, desc="Processing", unit="file"):
        _fp = _o.path.join(_fld, _fn)
        try:
            with open(_fp, 'r', encoding='utf-8') as _fl:
                _hc = _fl.read()
                _dt = _p(_hc)
                for _e in _dt:
                    _e["No."] = str(_n)
                    _n += 1
                _d.extend(_dt)
        except Exception as _e:
            print(f"Error: {_fn}: {_e}")
    return _d

_d = _r(_f)
with open(_o_f, 'w', encoding='utf-8') as _jf:
    _j.dump(_d, _jf, indent=4)

print(f"Data saved: {_o_f}")
  
