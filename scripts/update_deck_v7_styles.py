# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
p = ROOT / "versions" / "deck_v7" / "style.css"
content = p.read_text(encoding="utf-8")

old_slip = """.paper-slip{width:590px;height:358px;padding:22px 26px 16px;background:#f5f0e4;border:1px solid #d3c6af;outline:1px dashed #c8baa2;outline-offset:-10px;box-shadow:6px 14px 30px rgba(0,0,0,.38),0 1px 3px rgba(0,0,0,.18);z-index:2}
.paper-slip-a{top:20px;left:44px;transform:rotate(-1.5deg)}
.paper-slip-b{top:410px;left:56px;transform:rotate(1.3deg)}
.paper-kicker{display:flex;justify-content:space-between;align-items:center;font-size:12.5px;font-weight:800;letter-spacing:.03em;color:var(--brick);border-bottom:2px solid #2c2c29;padding-bottom:8px}
.paper-kicker span:last-child{color:#5e5a52;font-weight:700}
.paper-slip h3{font-family:var(--serif);font-size:25px;line-height:1.27;margin:12px 0 11px;letter-spacing:-.045em;color:#1f221d}
.paper-image{height:156px;padding:8px 12px;overflow:hidden;border:1px solid #c9c0b1;background:#fff;display:flex;align-items:center;justify-content:center}
.paper-image img{width:100%;height:auto;max-height:100%;object-fit:contain;object-position:center;margin:0;filter:grayscale(.9) sepia(.06)}
.paper-slip p{font-size:12.5px;font-weight:600;color:#5c584f;margin:10px 0 0}
.paper-slip p b{color:var(--brick);font-weight:800}"""

new_slip = """.paper-slip{width:600px;height:360px;padding:20px 24px 14px;background:#f5f0e4;border:1px solid #d3c6af;outline:1px dashed #c8baa2;outline-offset:-10px;box-shadow:6px 14px 30px rgba(0,0,0,.38),0 1px 3px rgba(0,0,0,.18);z-index:2;display:flex;flex-direction:column;box-sizing:border-box}
.paper-slip-a{top:20px;left:40px;transform:rotate(-1.5deg)}
.paper-slip-b{top:410px;left:56px;transform:rotate(1.3deg)}
.paper-kicker{display:flex;justify-content:space-between;align-items:center;font-size:12px;font-weight:800;letter-spacing:.03em;color:var(--brick);border-bottom:2px solid #2c2c29;padding-bottom:6px}
.paper-kicker span:last-child{color:#5e5a52;font-weight:700}
.paper-slip h3{font-family:var(--serif);font-size:22px;line-height:1.24;margin:8px 0 6px;letter-spacing:-.045em;color:#1f221d}
.paper-sub{font-family:var(--sans);font-size:12.5px;font-weight:700;line-height:1.35;color:#454139;margin:0 0 6px;padding-left:8px;border-left:3px solid var(--brick)}
.paper-body{font-family:var(--serif);font-size:12.5px;line-height:1.44;color:#2b2e29;margin:0 0 8px;background:rgba(255,255,255,.6);padding:7px 11px;border:1px solid #ddd4c3;border-radius:2px;text-align:justify;flex-grow:1}
.paper-cite{font-size:11.5px;font-weight:600;color:#5c584f;margin:auto 0 0;border-top:1px dashed #cfc5b3;padding-top:6px}
.paper-cite b{color:var(--brick);font-weight:800}
.paper-cite.slip-split{display:flex;flex-direction:column;gap:2px}
.paper-cite.slip-split span{display:block}"""

content_norm = content.replace("\r\n", "\n")
old_slip_norm = old_slip.replace("\r\n", "\n")
if old_slip_norm in content_norm:
    content = content_norm.replace(old_slip_norm, new_slip.replace("\r\n", "\n"))
    print("Replaced old_slip")
else:
    print("Warning: old_slip not found in content")

extra_rules = """

/* Additional v7 layout refinements */
.rq-cases .case-plate{grid-template-columns:220px 1fr}
.case-logo{margin:0;position:relative;overflow:hidden;background:#ffffff;display:flex;align-items:center;justify-content:center;padding:16px;border-right:1px solid #e5ded2}
.case-logo img{width:auto;height:auto;max-width:82%;max-height:82%;object-fit:contain}
.case-logo figcaption{position:absolute;left:8px;bottom:6px;background:rgba(20,24,22,.82);color:#fff;font-size:11px;padding:3px 6px;border-radius:2px}

.parallel-plate.plate-tall{grid-template-rows:150px 1fr}
.parallel-plate.plate-tall .parallel-photo.tall{height:150px}
.parallel-plate.plate-tall .parallel-content{padding:13px 22px}
.parallel-plate.plate-tall .parallel-content h3{font-size:23px;margin:3px 0 8px}
.parallel-plate.plate-tall .timeline-step{gap:6px;margin-top:6px}
.parallel-plate.plate-tall .timeline-step > div{padding:2px 0 2px 8px}
.parallel-plate.plate-tall .timeline-step time{font-size:13.5px}
.parallel-plate.plate-tall .timeline-step b{font-size:16.5px}
.parallel-plate.plate-tall .timeline-step span{font-size:13.5px;line-height:1.3}
"""

if "/* Additional v7 layout refinements */" not in content:
    content += extra_rules
    print("Appended extra_rules")

p.write_text(content, encoding="utf-8")
print("Updated style.css successfully!")
