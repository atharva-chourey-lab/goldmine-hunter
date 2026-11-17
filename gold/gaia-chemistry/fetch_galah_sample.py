"""Range-download first chunk of GALAH DR3 main allstar FITS and extract a sample.
GALAH DR3: https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/GALAH_DR3_main_allstar_v2.fits
Total 873,518,400 B, 588,571 rows x 1484 B/row (header-verified).
We fetch bytes 0..24MB-1 (206 Partial Content) -> ~16k complete rows after headers.
This is a FIRST-ROWS sample (file order = observation/sobject order), NOT random. Declared.
"""
import requests, os, sys
URL="https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/GALAH_DR3_main_allstar_v2.fits"
OUT=os.path.expanduser("~/workspace/goldmine-hunter/gold/gaia-chemistry/galah_dr3_first24MB.fits")
N=24_000_000
r=requests.get(URL, headers={"Range":f"bytes=0-{N-1}"}, timeout=120)
print("status", r.status_code, "content-range", r.headers.get("Content-Range"), "len", len(r.content))
assert r.status_code==206 and len(r.content)==N
open(OUT,"wb").write(r.content)
print("wrote", OUT)
