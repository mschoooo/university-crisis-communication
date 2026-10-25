"""Build the published source index from the archived research manifests."""
import csv
import html
import re
from pathlib import Path

repo = Path(__file__).resolve().parents[1]
deck = repo / 'versions' / 'deck_v19'
research = repo.parents[1] / '대학통합_위기커뮤니케이션_연구' / '부산대_부산교대_조사'

def rows(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

bn = {r['id']:r for r in rows(research/'bnue_board_sources.csv')}
ext = {r['id']:r for r in rows(research/'external_sources.csv')}
dd = {r['문서ID']:r for r in rows(repo/'versions'/'deck_v18'/'동덕여대_sources.csv')}
used = set(re.findall(r'sources\.html#([A-Za-z0-9]+)',(deck/'index.html').read_text(encoding='utf-8')))

def link(url):
    u=html.escape(url,quote=True)
    return f'<a href="{u}" target="_blank" rel="noopener">원문 열기 ↗</a>' if url else ''

groups=[]
items=[]
for ident in sorted(used & set(bn), key=lambda x:int(re.search(r'\d+',x).group())):
    r=bn[ident]
    items.append(f'<tr id="{ident}"><th>{ident}</th><td>{html.escape(r["date"][:10])}</td><td>{html.escape(r["title"])}</td><td>부산교육대학교 공식 게시판</td><td>{link(r["post_url"])}</td></tr>')
groups.append(('부산교육대학교 공식 자료',items))
items=[]
for ident in sorted(used & set(ext)):
    r=ext[ident]
    items.append(f'<tr id="{ident}"><th>{ident}</th><td>{html.escape(r["date"])}</td><td>{html.escape(r["title"])}</td><td>{"공식 자료" if r["type"]=="official" else "대학 언론·보도"}</td><td>{link(r["url"])}</td></tr>')
groups.append(('부산대학교 공식 자료·대학 언론',items))
items=[]
for ident in sorted(used & set(dd), key=lambda x:int(x[1:])):
    r=dd[ident]
    items.append(f'<tr id="{ident}"><th>{ident}</th><td>{html.escape(r["발행일"])}</td><td>{html.escape(r["제목"])}</td><td>{html.escape(r["발행기관"])}</td><td>{link(r["URL"])}</td></tr>')
groups.append(('동덕여자대학교 공식 자료·후속 보도',items))
theory=[
    ('T01','1997','Cancel et al., “It depends: A contingency theory of accommodation in public relations”','Journal of Public Relations Research 9(1), 31–63'),
    ('T02','교재','『PR커뮤니케이션』 제2장, 표 2-5, 80–82쪽','81개 변수 전사: 카메론 위기 상황변수 목록.md'),
    ('T03','1997','Benoit, “Image repair discourse and crisis communication”','Public Relations Review 23(2), 177–186'),
]
items=[]
for ident,date,title,where in theory:
    if ident in used:
        target='<a href="카메론 위기 상황변수 목록.md">변수 목록</a>' if ident=='T02' else ''
        items.append(f'<tr id="{ident}"><th>{ident}</th><td>{date}</td><td>{html.escape(title)}</td><td>{html.escape(where)}</td><td>{target}</td></tr>')
groups.append(('이론 문헌',items))

body='\n'.join(f'<section><h2>{html.escape(title)}</h2><table><thead><tr><th>ID</th><th>발행일</th><th>문서</th><th>기관·성격</th><th>링크</th></tr></thead><tbody>{"".join(items)}</tbody></table></section>' for title,items in groups)
moe='https://www.moe.go.kr/boardCnts/viewRenew.do?boardID=294&boardSeq=97030&lev=0&m=020402&opType=N&page=1&s=moe&searchType=null&statusYN=W'
page=f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>deck_v19 출처 색인</title><style>body{{font-family:Arial,'Malgun Gothic',sans-serif;max-width:1200px;margin:50px auto;padding:0 20px;color:#202426;line-height:1.55}}h1{{font-size:32px}}h2{{margin-top:46px;font-size:25px}}table{{border-collapse:collapse;width:100%}}th,td{{border-bottom:1px solid #d7dddd;text-align:left;padding:11px;vertical-align:top}}th{{white-space:nowrap}}a{{color:#27656a}}p{{font-size:17px}}</style></head><body><p><a href="index.html">← 발표로 돌아가기</a></p><h1>deck_v19 원문·참고문헌 색인</h1><p>슬라이드 하단의 문서 ID와 일치한다. 대학 공식 문서, 학내 보도, 사건 취재를 구분했다. 발언 보도는 발언의 존재를 확인하는 자료이며 해당 주장의 객관적 사실 여부는 별도 검증한다.</p><p>2장 전국 통계: <a href="{html.escape(moe,quote=True)}">교육부, 2023년 글로컬대학 본지정 평가 결과(2023.11.13)</a>. 선정 과제 10개 중 대학 간 통합 제안 4개를 목록에서 집계했다.</p>{body}<p>사진 및 문서 이미지: <a href="asset_sources.md">시각자료 출처</a>. 부산대–부산교대 원문 보관·해시는 별도 조사 자료의 CSV 색인에 있다.</p></body></html>'''
(deck/'sources.html').write_text(page,encoding='utf-8')
print('sources',len(used),'indexed',sum(len(x[1]) for x in groups))
