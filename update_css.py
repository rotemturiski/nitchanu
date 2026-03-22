import re
import sys

def main():
    file_path = "c:/Users/rotem/OneDrive/Desktop/miluim-deploy/index.html"
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_css = """<style>
@import url('https://fonts.googleapis.com/css2?family=Heebo:wght@400;500;600;700;800;900&display=swap');

* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: 'Heebo', -apple-system, BlinkMacSystemFont, sans-serif;
  background: #f4f7f4;
  color: #1a3c28;
  direction: rtl;
  font-size: 15px;
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
}

.root { max-width: 480px; margin: 0 auto; padding: 20px 16px 80px; }

/* BRANDING */
.brand-header { padding: 30px 16px 24px; text-align: center; }
.brand-name { font-size: 32px; font-weight: 900; color: #112a1c; letter-spacing: -0.5px; line-height: 1.2; text-shadow: 0 2px 10px rgba(0,0,0,0.05); }
.brand-sub { font-size: 18px; font-weight: 700; color: #38bdf8; margin-top: 6px; letter-spacing: 0.02em; background: linear-gradient(135deg, #10b981, #3b82f6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.brand-tag { display: inline-block; font-size: 11px; font-weight: 700; padding: 4px 12px; border-radius: 999px; background: rgba(16, 185, 129, 0.1); color: #10b981; margin-top: 12px; box-shadow: 0 2px 10px rgba(16, 185, 129, 0.1); }

/* SECTION */
.sec { background: #ffffff; border-radius: 24px; margin-bottom: 16px; overflow: hidden; box-shadow: 0 8px 30px rgba(17, 42, 28, 0.04); border: 1px solid rgba(17, 42, 28, 0.05); transition: transform 0.2s, box-shadow 0.2s; }
.sec:hover { box-shadow: 0 12px 40px rgba(17, 42, 28, 0.06); }
.sec-title { font-size: 15px; font-weight: 800; color: #112a1c; padding: 20px 20px 8px; display: flex; align-items: center; gap: 8px; }
.sec-title .sec-icon { font-size: 18px; line-height: 1; padding: 6px; background: #edfae1; border-radius: 10px; }
.sec-row { display: flex; align-items: center; gap: 12px; padding: 14px 20px; border-bottom: 1px solid #f0f3f0; transition: background 0.2s; }
.sec-row:hover { background: #fafcfa; }
.sec-row:last-child { border-bottom: none; }
.rl { font-size: 14px; font-weight: 500; color: #2c4a3b; flex: 1; line-height: 1.3; }
.rl small { font-size: 11.5px; font-weight: 400; color: #789982; display: block; margin-top: 2px; }

/* INPUTS & CONTROLS */
.sal-input { background: #fdfdfd; border: 2px solid #e2e8e4; border-radius: 12px; padding: 8px 12px; font-size: 16px; font-weight: 700; width: 120px; text-align: left; color: #112a1c; font-family: inherit; -webkit-appearance: none; direction: ltr; transition: all 0.2s; box-shadow: inset 0 2px 4px rgba(0,0,0,0.02); }
.sal-input:focus { outline: none; border-color: #10b981; background: #fff; box-shadow: 0 0 0 4px rgba(16, 185, 129, 0.1); }
.sal-suffix { font-size: 14px; color: #789982; font-weight: 600; margin-right: 4px; }

/* SEGMENTS */
.seg { display: flex; border-radius: 12px; background: #f0f3f0; padding: 4px; flex-shrink: 0; box-shadow: inset 0 1px 3px rgba(0,0,0,0.05); }
.sb { padding: 6px 12px; font-size: 13px; font-weight: 600; border: none; background: transparent; color: #64816e; cursor: pointer; white-space: nowrap; border-radius: 8px; transition: all 0.2s ease; }
.sb:hover { color: #112a1c; }
.sb.on { background: #ffffff; color: #112a1c; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }

/* TOGGLE */
.toggle-wrap { display: flex; align-items: center; gap: 10px; }
.toggle { width: 48px; height: 28px; background: #dce4de; border-radius: 15px; border: none; cursor: pointer; position: relative; flex-shrink: 0; transition: background 0.2s, box-shadow 0.2s; }
.toggle.on { background: #10b981; box-shadow: 0 2px 10px rgba(16,185,129,0.3); }
.toggle::after { content: ''; position: absolute; width: 22px; height: 22px; background: #fff; border-radius: 50%; top: 3px; right: 3px; transition: transform 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275); box-shadow: 0 2px 5px rgba(0,0,0,0.15); }
.toggle.on::after { transform: translateX(-20px); }
.toggle-val { font-size: 13px; font-weight: 600; color: #64816e; min-width: 32px; }

/* STEPPER */
.stp { display: flex; align-items: center; gap: 8px; background: #f0f3f0; border-radius: 12px; padding: 4px; }
.stp button { width: 30px; height: 30px; border-radius: 8px; border: none; background: #fff; color: #112a1c; font-size: 16px; font-weight: 600; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: all 0.15s; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
.stp button:active { transform: scale(0.92); background: #e2e8e4; }
.stp-v { font-size: 16px; font-weight: 700; min-width: 24px; text-align: center; color: #112a1c; }

/* YEARS HEADING */
.years-head { display: flex; align-items: center; justify-content: space-between; padding: 20px 20px 12px; }
.years-title { font-size: 16px; font-weight: 800; color: #112a1c; display: flex; align-items: center; gap: 8px; }
.years-title .sec-icon { font-size: 18px; padding: 6px; background: #edfae1; border-radius: 10px; }
.add-btn { font-size: 13px; font-weight: 700; padding: 8px 16px; border-radius: 12px; border: none; background: #112a1c; color: #fff; cursor: pointer; transition: all 0.2s; box-shadow: 0 4px 12px rgba(17,42,28,0.15); display: flex; align-items: center; gap: 6px; }
.add-btn:hover { transform: translateY(-1px); box-shadow: 0 6px 15px rgba(17,42,28,0.2); }
.add-btn:active { transform: translateY(1px); }

/* YEAR CARDS */
.yr-card { border-top: 1px solid #f0f3f0; padding: 16px 20px; transition: background 0.2s; }
.yr-card.cur-yr { background: linear-gradient(90deg, #f7fdf9 0%, #fff 100%); border-right: 4px solid #10b981; }
.yr-top { display: flex; align-items: center; gap: 10px; margin-bottom: 12px; }
.yr-badge { font-size: 15px; font-weight: 800; color: #112a1c; background: #edfae1; padding: 4px 10px; border-radius: 8px; }
.yr-days-total { font-size: 13px; font-weight: 500; color: #64816e; flex: 1; }
.yr-sum { font-size: 14px; font-weight: 800; color: #10b981; background: rgba(16,185,129,0.1); padding: 4px 10px; border-radius: 8px; }
.yr-rm { font-size: 18px; color: #cbd5e1; background: none; border: none; cursor: pointer; padding: 4px; border-radius: 6px; transition: all 0.2s; display: flex; align-items: center; justify-content: center; }
.yr-rm:hover { background: #fee2e2; color: #ef4444; }

/* YEAR DATES */
.yr-dates { display: flex; gap: 12px; align-items: center; }
.yr-date { flex: 1; display: flex; flex-direction: column; gap: 4px; }
.yr-date label { font-size: 11px; font-weight: 600; color: #789982; }
.yr-date input[type=date] { width: 100%; border: 2px solid #e2e8e4; border-radius: 10px; padding: 8px 10px; font-size: 13px; font-weight: 600; color: #112a1c; background: #fdfdfd; font-family: inherit; transition: all 0.2s; }
.yr-date input[type=date]:focus { outline: none; border-color: #10b981; box-shadow: 0 0 0 4px rgba(16, 185, 129, 0.1); }

/* MANUAL PERIODS */
.yr-manual { display: flex; align-items: center; gap: 10px; margin-top: 12px; border-top: 1px dashed #e2e8e4; padding-top: 12px; }
.yr-manual-lbl { font-size: 12px; font-weight: 600; color: #64816e; flex: 1; }
.yr-period { display: flex; padding: 8px 12px; align-items: center; gap: 8px; margin-top: 8px; flex-wrap: wrap; background: #f9fbf9; border-radius: 10px; border: 1px solid #e2e8e4; }
.yr-period input[type=date] { width: 125px; border: 2px solid #e2e8e4; border-radius: 8px; padding: 6px 8px; font-size: 12px; font-weight: 600; color: #112a1c; background: #fff; font-family: inherit; }
.yr-period input[type=number] { width: 55px; border: 2px solid #e2e8e4; border-radius: 8px; padding: 6px 8px; font-size: 13px; font-weight: 700; text-align: center; color: #112a1c; background: #fff; font-family: inherit; }
.yr-period input:focus { border-color: #10b981; outline: none; }
.yr-period .p-rm { background: #fee2e2; border: none; color: #ef4444; border-radius: 6px; padding: 4px; cursor: pointer; display: flex; align-items: center; justify-content: center; width: 24px; height: 24px; transition: all 0.2s; }
.yr-period .p-rm:hover { background: #fecaca; }
.yr-period .p-type { font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 6px; border: none; cursor: pointer; background: #e2e8e4; color: #64816e; transition: all 0.2s; }
.yr-period .p-type.on { background: #112a1c; color: #fff; }
.yr-add-period { background: #fff; border: 2px dashed #cbd5e1; border-radius: 10px; color: #64816e; font-size: 12px; font-weight: 600; cursor: pointer; padding: 8px 16px; margin-top: 8px; width: 100%; transition: all 0.2s; display: block; }
.yr-add-period:hover { border-color: #10b981; color: #10b981; background: #f0fdf4; }

.yr-type-seg { display: flex; border-radius: 8px; background: #e2e8e4; padding: 3px; flex-shrink: 0; }
.ytb { padding: 4px 10px; font-size: 11px; font-weight: 600; border: none; background: none; color: #64816e; cursor: pointer; border-radius: 6px; transition: all 0.2s; }
.ytb.on { background: #fff; color: #112a1c; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }

/* HERO (PREMIUM GREEN GRADIENT) */
.hero { background: linear-gradient(135deg, #112a1c 0%, #174028 100%); border-radius: 24px; padding: 24px 20px; margin-bottom: 16px; color: #fff; box-shadow: 0 10px 30px rgba(17,42,28,0.2); position: relative; overflow: hidden; }
.hero::before { content: ''; position: absolute; top: -50%; left: -50%; width: 200%; height: 200%; background: radial-gradient(circle, rgba(255,255,255,0.05) 0%, transparent 60%); opacity: 0.5; pointer-events: none; }
.hero-lbl { font-size: 13px; font-weight: 600; color: rgba(255,255,255,0.7); margin-bottom: 6px; letter-spacing: 0.02em; }
.hero-amt { font-size: 48px; font-weight: 900; line-height: 1; letter-spacing: -1px; text-shadow: 0 4px 10px rgba(0,0,0,0.2); }
.hero-sub { font-size: 12px; font-weight: 500; color: rgba(255,255,255,0.6); margin-top: 8px; line-height: 1.4; }
.chips { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin-top: 20px; }
.chip { background: rgba(255,255,255,0.08); border-radius: 16px; padding: 12px; border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(10px); transition: transform 0.2s; }
.chip:hover { transform: translateY(-2px); background: rgba(255,255,255,0.12); }
.cl { font-size: 10.5px; font-weight: 600; color: rgba(255,255,255,0.7); margin-bottom: 4px; }
.cv { font-size: 16px; font-weight: 800; }
.cv.g { color: #34d399; }
.cv.a { color: #facc15; }
.cv.w { color: #fff; }

/* NEXT BAR */
.nxt { display: flex; align-items: center; gap: 12px; padding: 12px 16px; border-radius: 16px; background: linear-gradient(to right, #f0f9ff, #e0f2fe); border: 1px solid #bae6fd; margin-bottom: 16px; box-shadow: 0 4px 15px rgba(2,132,199,0.05); }
.nxt-txt { flex: 1; font-size: 13px; font-weight: 500; color: #0369a1; }
.nxt-txt strong { font-weight: 800; color: #0c4a6e; }
.npb { width: 56px; height: 6px; background: rgba(3,105,161,0.15); border-radius: 3px; flex-shrink: 0; overflow: hidden; }
.npbf { height: 100%; border-radius: 3px; background: linear-gradient(90deg, #38bdf8, #0ea5e9); transition: width 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
.npp { font-size: 12px; font-weight: 800; color: #0284c7; min-width: 32px; text-align: left; }

/* TIMELINE */
.tl-sec { margin-bottom: 16px; }
.tl-yh { display: flex; align-items: center; gap: 10px; padding: 12px 0 8px; }
.tl-yb { font-size: 14px; font-weight: 800; padding: 6px 14px; border-radius: 999px; background: #112a1c; color: #fff; letter-spacing: 0.02em; box-shadow: 0 4px 10px rgba(17,42,28,0.2); }
.tl-yn { font-size: 13px; color: #64816e; font-weight: 600; }
.tl-w { position: relative; }
.tl-spine { position: absolute; right: 14px; top: 16px; bottom: 16px; width: 2px; background: #e2e8e4; border-radius: 1px; }
.tl-i { display: flex; gap: 12px; margin-bottom: 8px; position: relative; }
.tl-dot { width: 28px; height: 28px; border-radius: 50%; flex-shrink: 0; z-index: 1; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 800; margin-top: 10px; border: 3px solid #f4f7f4; box-shadow: 0 2px 6px rgba(0,0,0,0.06); }
.d-done { background: #10b981; color: #fff; }
.d-pend { background: #fef08a; color: #854d0e; }
.d-lock { background: #f1f5f9; color: #94a3b8; }
.d-paid { background: #e2e8e4; color: #64816e; }
.tl-card { flex: 1; background: #fff; border: 1px solid rgba(17, 42, 28, 0.05); border-radius: 16px; padding: 12px 16px; position: relative; overflow: hidden; box-shadow: 0 4px 15px rgba(17, 42, 28, 0.02); transition: transform 0.2s, box-shadow 0.2s; }
.tl-card:hover { transform: translateY(-1px); box-shadow: 0 6px 20px rgba(17, 42, 28, 0.04); }
.tl-card.ac { border-right: 4px solid #10b981; }
.tl-card.mc { border-right: 4px solid #f59e0b; }
.tl-card.lc { opacity: 0.4; pointer-events: none; }
.tl-card.ec { border-right: 4px solid #ef4444; background: #fef2f2; }
.tl-am.exp { color: #ef4444; }
.expired-badge { display: inline-block; font-size: 10px; font-weight: 800; padding: 2px 8px; border-radius: 999px; background: #fecaca; color: #b91c1c; margin-top: 4px; }
.missed-badge { display: inline-block; font-size: 10px; font-weight: 800; padding: 2px 8px; border-radius: 999px; background: #fef08a; color: #854d0e; margin-top: 4px; }
.tl-card.pc { opacity: 0.8; background: #f8faf9; border: 1px dashed #cbd5e1; }
.tl-top { display: flex; justify-content: space-between; align-items: flex-start; gap: 8px; }
.tl-nm { font-size: 13.5px; font-weight: 700; color: #112a1c; flex: 1; line-height: 1.3; }
.tl-nm.st { text-decoration: line-through; color: #94a3b8; }
.tl-am { font-size: 14px; font-weight: 800; flex-shrink: 0; }
.tl-am.g { color: #10b981; } .tl-am.a { color: #f59e0b; } .tl-am.d { color: #94a3b8; font-weight: 600; }
.tl-wh { font-size: 11.5px; font-weight: 500; color: #64816e; margin-top: 4px; }
.tl-dead { font-size: 11.5px; color: #ef4444; margin-top: 2px; font-weight: 700; }
.paid-row { display: flex; align-items: center; gap: 6px; margin-top: 8px; cursor: pointer; padding: 4px 0; }
.paid-chk { width: 16px; height: 16px; border-radius: 5px; background: #e2e8e4; display: flex; align-items: center; justify-content: center; flex-shrink: 0; transition: all 0.2s; }
.paid-chk.on { background: #10b981; box-shadow: 0 2px 5px rgba(16,185,129,0.3); }
.t-sm { width: 8px; height: 5px; border-left: 2px solid #fff; border-bottom: 2px solid #fff; transform: rotate(-45deg) translate(0.5px, -1px); display: none; }
.paid-chk.on .t-sm { display: block; }
.paid-lbl { font-size: 11.5px; font-weight: 600; color: #64816e; }

/* CHECKLIST */
.chk-w { background: #fff; border-radius: 24px; border: 1px solid rgba(17, 42, 28, 0.05); overflow: hidden; margin-bottom: 16px; box-shadow: 0 8px 30px rgba(17, 42, 28, 0.04); }
.chk-h { padding: 20px 20px 14px; border-bottom: 1px solid #f0f3f0; display: flex; justify-content: space-between; align-items: center; }
.chk-ht { font-size: 16px; font-weight: 800; color: #112a1c; display: flex; align-items: center; gap: 8px; }
.chk-ht .sec-icon { font-size: 18px; line-height: 1; padding: 6px; background: #edfae1; border-radius: 10px; }
.chk-badge { font-size: 12px; padding: 4px 12px; border-radius: 999px; font-weight: 800; background: #dcfce7; color: #166534; box-shadow: 0 2px 6px rgba(22,101,52,0.1); }
.chk-badge.all { background: #f1f5f9; color: #64748b; box-shadow: none; }
.chk-badge.missed { background: #fecaca; color: #b91c1c; }
.ci { display: flex; align-items: flex-start; gap: 12px; padding: 16px 20px; border-bottom: 1px solid #f8faf9; cursor: pointer; -webkit-tap-highlight-color: transparent; user-select: none; transition: background 0.2s; }
.ci:hover { background: #fdfdfd; }
.ci:last-child { border-bottom: none; }
.ci.done .ci-t { text-decoration: line-through; color: #94a3b8; }
.ci-box { width: 22px; height: 22px; border-radius: 6px; border: 2px solid #cbd5e1; flex-shrink: 0; margin-top: 2px; display: flex; align-items: center; justify-content: center; background: #fff; transition: all 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
.ci-box.on { background: #10b981; border-color: #10b981; box-shadow: 0 2px 8px rgba(16,185,129,0.3); }
.ci-tick { width: 10px; height: 7px; border-left: 2.5px solid #fff; border-bottom: 2.5px solid #fff; transform: rotate(-45deg) translate(1px,-1px); display: none; }
.ci-box.on .ci-tick { display: block; }
.ci-b { flex: 1; }
.ci-t { font-size: 14.5px; font-weight: 700; color: #112a1c; }
.ci-m { font-size: 12px; font-weight: 500; color: #64816e; margin-top: 4px; line-height: 1.4; }
.ci-dead { font-size: 12px; color: #ef4444; margin-top: 2px; font-weight: 700; }
.ci-yr { font-size: 11px; font-weight: 800; padding: 2px 8px; border-radius: 999px; background: #f1f5f9; color: #475569; margin-top: 6px; display: inline-block; }
.ci-side { display: flex; flex-direction: column; align-items: flex-end; gap: 6px; flex-shrink: 0; }
.ci-amt { font-size: 13.5px; font-weight: 800; color: #f59e0b; }
.ci-btn { font-size: 12px; font-weight: 600; padding: 4px 12px; border-radius: 8px; border: 1px solid #e2e8e4; background: #fff; color: #112a1c; text-decoration: none; white-space: nowrap; transition: all 0.2s; }
.ci-btn:hover { background: #f8faf9; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }

/* HEADER ELEMENTS */
.tl-header { font-size: 16px; font-weight: 800; color: #112a1c; display: flex; align-items: center; gap: 8px; flex-wrap: wrap; padding: 8px 0 4px; }
.tl-header .sec-icon { font-size: 18px; padding: 6px; background: #edfae1; border-radius: 10px; margin-left: 4px; }
.tl-header .legend { margin-right: auto; margin-bottom: 0; }
.legend { display: flex; gap: 14px; margin-bottom: 12px; }
.leg { display: flex; align-items: center; gap: 6px; font-size: 12px; font-weight: 600; color: #64816e; }
.ld { width: 10px; height: 10px; border-radius: 3px; flex-shrink: 0; }
.foot { font-size: 12.5px; font-weight: 500; color: #94a3b8; text-align: center; line-height: 1.6; padding: 12px 16px; }

/* PDF UPLOAD SECTION */
.pdf-drop { border: 2px dashed #cbd5e1; border-radius: 16px; padding: 24px 20px; text-align: center; margin: 12px 20px; cursor: pointer; transition: all 0.2s; background: #f8faf9; }
.pdf-drop:hover, .pdf-drop.drag { border-color: #10b981; background: #f0fdf4; box-shadow: inset 0 0 0 1px #10b981; }
.pdf-drop-icon { font-size: 28px; margin-bottom: 8px; transition: transform 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
.pdf-drop:hover .pdf-drop-icon { transform: scale(1.1); }
.pdf-drop-txt { font-size: 13px; font-weight: 500; color: #64816e; line-height: 1.5; }
.pdf-drop-txt strong { color: #112a1c; font-weight: 800; font-size: 14px; }
.pdf-preview { background: #f0fdf4; border: 1px solid #86efac; border-radius: 16px; margin: 12px 20px; padding: 16px; box-shadow: 0 4px 12px rgba(22,163,74,0.06); }
.pdf-preview-row { display: flex; justify-content: space-between; align-items: center; padding: 6px 0; font-size: 13px; }
.pdf-preview-label { color: #166534; font-weight: 600; }
.pdf-preview-value { font-weight: 800; color: #14532d; }
.pdf-btn-row { display: flex; gap: 10px; margin-top: 12px; }
.pdf-apply { flex: 1; padding: 12px; border-radius: 12px; border: none; background: #10b981; color: #fff; font-size: 14px; font-weight: 800; cursor: pointer; transition: all 0.2s; box-shadow: 0 4px 12px rgba(16,185,129,0.2); }
.pdf-apply:hover { background: #059669; transform: translateY(-1px); }
.pdf-apply:active { background: #047857; transform: translateY(1px); }
.pdf-cancel { padding: 12px 16px; border-radius: 12px; border: 1px solid #cbd5e1; background: #fff; color: #64748b; font-size: 14px; font-weight: 700; cursor: pointer; transition: all 0.2s; }
.pdf-cancel:hover { background: #f8faf9; color: #475569; }
.pdf-error { color: #dc2626; font-size: 12.5px; font-weight: 600; margin-top: 8px; text-align: center; }
.pdf-loading { display: flex; align-items: center; justify-content: center; gap: 8px; padding: 16px; font-size: 13px; font-weight: 600; color: #112a1c; }
.pdf-year-row { display: flex; justify-content: space-between; align-items: center; padding: 8px 0; border-bottom: 1px solid #dcfce7; }
.pdf-year-row:last-child { border-bottom: none; }
.pdf-yr-badge { font-size: 13px; font-weight: 800; min-width: 40px; color: #14532d; }
.pdf-yr-days { font-size: 13px; color: #15803d; font-weight: 800; }
.pdf-yr-type { font-size: 11px; font-weight: 700; color: #166534; padding: 2px 8px; border-radius: 999px; background: #dcfce7; }
.pdf-warn { color: #b45309; font-size: 12.5px; font-weight: 600; margin-top: 8px; text-align: center; background: #fef3c7; padding: 6px; border-radius: 8px; }

/* DISCLAIMER */
.disclaimer { background: linear-gradient(to right, #fffbeb, #fef3c7); border: 1px solid #fde68a; border-radius: 16px; padding: 16px 20px; margin-bottom: 16px; font-size: 13px; font-weight: 500; color: #92400e; line-height: 1.6; text-align: center; box-shadow: 0 4px 15px rgba(217,119,6,0.05); }
.disclaimer a { color: #b45309; font-weight: 800; text-decoration: underline; text-underline-offset: 4px; transition: color 0.15s; }
.disclaimer a:hover { color: #78350f; }

/* SHARE BUTTONS */
.share-row { display: flex; justify-content: center; gap: 12px; margin-bottom: 16px; }
.share-btn-link, .share-btn-img { flex: 1; font-size: 14px; font-weight: 700; padding: 14px 20px; border-radius: 16px; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px; transition: all 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
.share-btn-link { background: #fff; color: #112a1c; border: 2px solid #e2e8e4; box-shadow: 0 4px 12px rgba(0,0,0,0.03); }
.share-btn-link:hover { border-color: #112a1c; transform: translateY(-2px); }
.share-btn-img { background: #112a1c; color: #fff; border: 2px solid #112a1c; box-shadow: 0 4px 15px rgba(17,42,28,0.2); }
.share-btn-img:hover { background: #1a432b; transform: translateY(-2px); box-shadow: 0 6px 20px rgba(17,42,28,0.3); }
.share-btn-link:active, .share-btn-img:active { transform: scale(0.96); }

/* ── RESPONSIVE ────────────────────────────────────── */
@media (max-width: 380px){
  .root { padding: 16px 12px 60px; }
  .brand-name { font-size: 26px; }
  .hero-amt { font-size: 40px; }
  .chips { grid-template-columns: 1fr; gap: 6px; }
  .chip { padding: 10px; display: flex; justify-content: space-between; align-items: center; }
  .cl { margin-bottom: 0; font-size: 12px; }
  .cv { font-size: 15px; }
  .seg { flex-wrap: wrap; }
  .sb { flex: 1; text-align: center; }
}

@media (min-width: 600px){
  body { background: #e8ede9; }
  .root { max-width: 600px; padding: 40px 24px 80px; background: #f4f7f4; border-radius: 32px; margin-top: 40px; margin-bottom: 40px; box-shadow: 0 20px 60px rgba(17,42,28,0.08); }
  .brand-header { padding: 20px 20px 32px; }
  .brand-name { font-size: 40px; }
  .hero { padding: 32px 28px; }
  .hero-amt { font-size: 56px; }
  .chip { padding: 16px; }
  .cl { font-size: 12px; }
  .cv { font-size: 18px; }
  .sec-title { font-size: 16px; }
  .rl { font-size: 15px; }
  .ci { padding: 20px 24px; gap: 16px; }
  .ci-t { font-size: 16px; }
}
</style>"""

    content = re.sub(r'(?s)<style>.*?</style>', new_css, content)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    main()
