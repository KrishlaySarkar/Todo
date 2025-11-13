# 🎯 Simple CLI Marksheet Generator

# CLI -> HTML Marksheet
import os, webbrowser
from datetime import datetime

print("MARKSHEET Generator")
name = input("Student Name: ").strip() or "Student"
roll = input("Roll No: ").strip() or "0"

subjects = ["English","Math","Science","Social","Computer","Hindi"]
marks = []
sub_num = 1
for s in subjects:
    while True:
        val = input(f"{sub_num}]    Marks for {s} (0-100): ").strip()
        sub_num += 1
        try:
            m = int(val)
            if 0 <= m <= 100:
                marks.append(m)
                break
        except:
            pass
        print("Enter a number 0-100.")
        

total = sum(marks)
percent = total / len(subjects)
grade = "A+" if percent >= 90 else "A" if percent >= 80 else "B" if percent >= 70 else "C"

# filename
filename = f"_marksheet.html"
path = os.path.abspath(filename)

# simple styled HTML
html = f"""
<!doctype html>
<html>
<head><title>Marksheet - {name}</title>

<style>
body{{font-family:Arial,Helvetica,sans-serif;background:#f6f8ff;color:#16213e;padding:30px}}

.card{{max-width:700px;margin:auto;background:#fff;border-radius:10px;box-shadow:0 6px 18px rgba(10,20,50,.08);padding:20px}}

h1{{color:#0f172a;margin-bottom:6px}} .meta{{color:#516076;font-size:14px;margin-bottom:12px}}

table{{width:100%;border-collapse:collapse;margin-top:12px}}

td,th{{padding:8px;border-bottom:1px solid #eef2ff;text-align:left}}

.total{{font-weight:bold}}

.footer{{margin-top:14px;color:#3b3b98}}

.badge{{display:inline-block;padding:6px 10px;border-radius:6px;background:#e6f7ea;color:#0b6b3a}}
</style>

</head>
<body>
<div class="card">
  <h1>Marksheet</h1>
  <h3>
  <div class="meta">Name: {name} &nbsp;|&nbsp; Roll: {roll} &nbsp;|&nbsp; Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}</div>
  <table>
  </h3>
    <tr><th>Subject</th><th>Marks</th></tr>
    {''.join(f"<tr><td>{sub}</td><td>{m}</td></tr>" for sub,m in zip(subjects,marks))}
    <tr class="total"><td>Total</td><td>{total}/600</td></tr>
    <tr class="total"><td>Percentage</td><td>{percent:.2f}%</td></tr>
    <tr class="total"><td>Grade</td><td><span class="badge">{grade}</span></td></tr>
  </table>
</div>
</body></html>"""

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\nSaved -> {filename}\n...\n...\nOpening...")
webbrowser.open("file://" + path)
