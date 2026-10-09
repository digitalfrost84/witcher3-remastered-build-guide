"""Show the script calls in a Witcher 3 quest graph (.w2phase, CR2W format).

Usage:

    python3 scripts/cr2w_calls.py <file.w2phase> [functionName]

Prints every CQuestScriptBlock, or only those calling `functionName`, with
their properties: comment, caption, function name and the raw parameter and
connection data. Chapter 19 used it on Blood and Wine's
mq7023_mutations.w2phase, the only quest graph that calls AddSkillPoints, to
find the two Moreau lab grants. The condition block in front of them was
traced by following the cachedConnections chunk indices.
"""
import struct, sys

def main(path, fn=None):
    d = open(path, 'rb').read()
    assert d[:4] == b'CR2W'
    tables = [struct.unpack_from('<III', d, 0x28 + 12 * i) for i in range(10)]
    s_off, s_size, _ = tables[0]
    strings = d[s_off:s_off + s_size]
    def cstr(o):
        return strings[o:strings.index(b'\0', o)].decode('latin1')
    n_off, n_cnt, _ = tables[1]
    names = [cstr(struct.unpack_from('<I', d, n_off + 8 * i)[0]) for i in range(n_cnt)]
    e_off, e_cnt, _ = tables[4]
    chunks = []
    for i in range(e_cnt):
        cls, flags, parent, size, off, tmpl, crc = struct.unpack_from('<HHIIIII', d, e_off + 24 * i)
        chunks.append((names[cls], parent, d[off:off + size]))

    def props(buf):
        out, p = [], 1
        while p + 8 <= len(buf):
            ni, ti, sz = struct.unpack_from('<HHI', buf, p)
            if ni == 0: break
            out.append((names[ni], names[ti], buf[p + 8:p + 4 + sz]))
            p += 4 + sz
        return out

    def fmt(t, v):
        if t == 'CName' and len(v) == 2: return names[struct.unpack('<H', v)[0]]
        if t in ('Int32', 'Uint32') and len(v) == 4: return struct.unpack('<i', v)[0]
        if t == 'Bool' and len(v) == 1: return bool(v[0])
        if t == 'String' and v:
            n = v[0] & 0x7f
            return v[1:1 + n].decode('latin1') if v[0] & 0x80 else v[1:1 + 2 * n].decode('utf-16-le', 'replace')
        return v.hex()

    for idx, (cls, parent, buf) in enumerate(chunks):
        if cls != 'CQuestScriptBlock': continue
        ps = props(buf)
        f = next((fmt(t, v) for n, t, v in ps if n == 'functionName'), None)
        if fn and f != fn: continue
        print('chunk #%d parent=%d' % (idx + 1, parent))
        for n, t, v in ps:
            print('   %s : %s = %s' % (n, t, fmt(t, v)))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
