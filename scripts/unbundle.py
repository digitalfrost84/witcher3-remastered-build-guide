"""Extract files from a Witcher 3 .bundle archive (POTATO70 format).

Usage:

    python3 scripts/unbundle.py <bundle> <outdir> [filter]

Writes every file whose internal path contains `filter` (for example ".xml"
or ".w2phase") under <outdir>, keeping the internal paths, and prints how many
files passed and failed their size and CRC32 check. Handles uncompressed,
zlib and LZ4 entries; entries in other formats are counted as skipped.

The chapter 19 audits used it on content/content0/bundles/xml.bundle (game
definitions), ep1.bundle and bob.bundle (the expansions' definitions), and on
startup, blob, bob, ep1 and dlc0 for the quest graphs. Run Python with -I
when you point it at game files, and extract into an empty directory.
"""
import struct, sys, zlib, os, binascii

def lz4_block(src, usize):
    dst = bytearray(); i = 0; n = len(src)
    while i < n:
        tok = src[i]; i += 1
        lit = tok >> 4
        if lit == 15:
            while True:
                b = src[i]; i += 1; lit += b
                if b != 255: break
        dst += src[i:i+lit]; i += lit
        if i >= n: break
        off = src[i] | (src[i+1] << 8); i += 2
        ml = tok & 15
        if ml == 15:
            while True:
                b = src[i]; i += 1; ml += b
                if b != 255: break
        ml += 4
        start = len(dst) - off
        for k in range(ml):
            dst.append(dst[start + k])
    return bytes(dst)

def main(bundle, out, flt=None):
    with open(bundle, 'rb') as f:
        data = f.read()
    assert data[:8] == b'POTATO70', data[:8]
    toc_size = struct.unpack_from('<I', data, 16)[0]
    pos, end = 0x20, 0x20 + toc_size
    stats = {}
    while pos + 0x130 <= end:
        name = data[pos:pos+0x100].split(b'\0')[0].decode('latin1')
        off, _, size, zsize, crc, comp = struct.unpack_from('<IIIIII', data, pos + 0x110)
        pos += 0x130
        if not name: continue
        if flt and flt not in name.replace('\\', '/'): continue
        raw = data[off:off+zsize]
        if comp == 0: buf = raw
        elif comp == 1: buf = zlib.decompress(raw)
        elif comp in (4, 5): buf = lz4_block(raw, size)
        else:
            stats['skipped_comp_%d' % comp] = stats.get('skipped_comp_%d' % comp, 0) + 1
            continue
        ok = len(buf) == size and (crc == 0 or (binascii.crc32(buf) & 0xffffffff) == crc)
        stats['ok' if ok else 'bad'] = stats.get('ok' if ok else 'bad', 0) + 1
        p = os.path.join(out, name.replace('\\', os.sep))
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, 'wb') as g:
            g.write(buf)
    print(stats)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
