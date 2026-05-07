#!/usr/bin/env python3
"""Build Sentinel Ops 9-slide sales deck."""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Cm
import copy

# ── Colours ──────────────────────────────────────────────────────────────────
NAVY    = RGBColor(0x0D, 0x2B, 0x45)   # deep navy
TEAL    = RGBColor(0x00, 0x9B, 0x8A)   # accent teal
WHITE   = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT   = RGBColor(0xF5, 0xF7, 0xFA)   # slide background tint
DARK_TEXT = RGBColor(0x1A, 0x1A, 0x2E)
GREY_TEXT = RGBColor(0x5A, 0x5A, 0x7A)
ORANGE  = RGBColor(0xF4, 0x7B, 0x00)   # callout orange

# ── Helpers ───────────────────────────────────────────────────────────────────
prs = Presentation()
prs.slide_width  = Inches(13.33)
prs.slide_height = Inches(7.5)

BLANK = prs.slide_layouts[6]  # truly blank layout

def add_bg(slide, color=LIGHT):
    """Solid coloured background."""
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color

def textbox(slide, text, left, top, width, height,
            size=18, bold=False, color=DARK_TEXT, align=PP_ALIGN.LEFT,
            italic=False, wrap=True):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    txBox.word_wrap = wrap
    tf = txBox.text_frame
    tf.word_wrap = wrap
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    return txBox

def bullet_box(slide, items, left, top, width, height,
               size=16, color=DARK_TEXT, spacing_before=6):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    txBox.word_wrap = True
    tf = txBox.text_frame
    tf.word_wrap = True
    first = True
    for item in items:
        if first:
            p = tf.paragraphs[0]
            first = False
        else:
            p = tf.add_paragraph()
        p.space_before = Pt(spacing_before)
        run = p.add_run()
        run.text = f"• {item}"
        run.font.size = Pt(size)
        run.font.color.rgb = color
    return txBox

def section_header(slide, title, subtitle=None):
    """Full-width navy top bar."""
    bar = slide.shapes.add_shape(1, 0, 0, prs.slide_width, Inches(1.1))
    bar.fill.solid()
    bar.fill.fore_color.rgb = NAVY
    bar.line.fill.background()

    textbox(slide, title, Inches(0.5), Inches(0.2), Inches(12), Inches(0.7),
            size=28, bold=True, color=WHITE, align=PP_ALIGN.LEFT)
    if subtitle:
        textbox(slide, subtitle, Inches(0.5), Inches(0.72), Inches(12), Inches(0.35),
                size=14, bold=False, color=RGBColor(0xA0,0xC0,0xD0), align=PP_ALIGN.LEFT)

def accent_bar(slide, top_offset=Inches(1.3)):
    """Thin teal accent bar under header."""
    bar = slide.shapes.add_shape(1, 0, top_offset, prs.slide_width, Pt(4))
    bar.fill.solid()
    bar.fill.fore_color.rgb = TEAL
    bar.line.fill.background()

def callout_box(slide, text, left, top, width, height, size=14):
    box = slide.shapes.add_shape(1, left, top, width, height)
    box.fill.solid()
    box.fill.fore_color.rgb = RGBColor(0xE8, 0xF4, 0xF2)
    box.line.color.rgb = TEAL
    box.line.width = Pt(1.5)
    tf = box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.color.rgb = NAVY
    run.font.bold = True

def four_box_row(slide, items, row_top, box_w, box_h, gap=Inches(0.3)):
    """4 boxes across the slide."""
    total_w = 4 * box_w + 3 * gap
    start_x = (prs.slide_width - total_w) / 2
    colours = [NAVY, TEAL, RGBColor(0x1A,0x6B,0x5E), RGBColor(0x0A,0x4A,0x5A)]
    for i, (title, desc) in enumerate(items):
        x = start_x + i * (box_w + gap)
        box = slide.shapes.add_shape(1, x, row_top, box_w, box_h)
        box.fill.solid()
        box.fill.fore_color.rgb = colours[i]
        box.line.fill.background()
        tf = box.text_frame
        tf.word_wrap = True
        # Title
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        run = p.add_run()
        run.text = title
        run.font.size = Pt(14)
        run.font.bold = True
        run.font.color.rgb = WHITE
        # Desc
        p2 = tf.add_paragraph()
        p2.alignment = PP_ALIGN.CENTER
        run2 = p2.add_run()
        run2.text = desc
        run2.font.size = Pt(11)
        run2.font.color.rgb = RGBColor(0xD0,0xE8,0xF0)

# ── SLIDE 1 — Title ───────────────────────────────────────────────────────────
s1 = prs.slides.add_slide(BLANK)
add_bg(s1, NAVY)

# Big title
textbox(s1, "Sentinel Ops",
        Inches(0.8), Inches(1.5), Inches(11.5), Inches(1.2),
        size=60, bold=True, color=WHITE, align=PP_ALIGN.LEFT)

# Tagline
textbox(s1, "Lean Managed Cybersecurity for Malaysian SMEs & Growing Teams",
        Inches(0.8), Inches(2.7), Inches(10), Inches(0.6),
        size=22, bold=False, color=TEAL, align=PP_ALIGN.LEFT)

# Sub-tagline
textbox(s1, "Monitoring, Hardening, and Audit-Ready Reporting",
        Inches(0.8), Inches(3.4), Inches(10), Inches(0.5),
        size=18, bold=False, color=RGBColor(0xA0,0xC0,0xD0), align=PP_ALIGN.LEFT)
textbox(s1, "without building a full SOC.",
        Inches(0.8), Inches(3.85), Inches(10), Inches(0.5),
        size=18, bold=False, color=RGBColor(0xA0,0xC0,0xD0), align=PP_ALIGN.LEFT)

# Teal divider
bar = s1.shapes.add_shape(1, Inches(0.8), Inches(4.55), Inches(3), Pt(4))
bar.fill.solid()
bar.fill.fore_color.rgb = TEAL
bar.line.fill.background()

# Footer contact
textbox(s1, "[Your Name]  |  Founder / Operator",
        Inches(0.8), Inches(4.8), Inches(8), Inches(0.4),
        size=13, bold=False, color=RGBColor(0x80,0xA0,0xB0), align=PP_ALIGN.LEFT)
textbox(s1, "[email@domain.com]  |  [WhatsApp]  |  [LinkedIn]",
        Inches(0.8), Inches(5.15), Inches(8), Inches(0.4),
        size=12, bold=False, color=RGBColor(0x60,0x80,0x90), align=PP_ALIGN.LEFT)

# ── SLIDE 2 — The Problem ────────────────────────────────────────────────────
s2 = prs.slides.add_slide(BLANK)
add_bg(s2, LIGHT)
section_header(s2, "The Problem", "Why growing companies struggle with cybersecurity operations")
accent_bar(s2)

items = [
    "Security tools generate noise, not clarity",
    "Small IT teams don't have time to triage alerts",
    "Hardening and patching hygiene is inconsistent",
    "Compliance pressure is rising: PDPA, customer questionnaires, audit expectations",
    "Hiring a full SOC team is expensive and unrealistic for many SMEs",
]
bullet_box(s2, items,
           Inches(0.7), Inches(1.5), Inches(8.5), Inches(4),
           size=17, color=DARK_TEXT, spacing_before=10)

callout_box(s2,
            "Most companies know they need better security operations — "
            "but not a heavyweight security program.",
            Inches(9.6), Inches(1.5), Inches(3.3), Inches(2.5), size=13)

# ── SLIDE 3 — Our Answer ──────────────────────────────────────────────────────
s3 = prs.slides.add_slide(BLANK)
add_bg(s3, LIGHT)
section_header(s3, "What Sentinel Ops Does", "The lean managed security layer for critical systems")
accent_bar(s3)

items = [
    "Managed monitoring for Linux / cloud environments",
    "Alert triage — reduce noise, surface real issues",
    "Baseline hardening using practical CIS-aligned controls",
    "Monthly management-ready reporting",
    "Limited-scope pilots designed to prove value fast",
]
bullet_box(s3, items,
           Inches(0.7), Inches(1.5), Inches(8.5), Inches(3.8),
           size=17, color=DARK_TEXT, spacing_before=10)

callout_box(s3,
            "Enterprise-style security visibility and hardening — "
            "without hiring a SOC.",
            Inches(0.7), Inches(5.5), Inches(11.9), Inches(1.1), size=16)

# ── SLIDE 4 — Who It's For ───────────────────────────────────────────────────
s4 = prs.slides.add_slide(BLANK)
add_bg(s4, LIGHT)
section_header(s4, "Who It's For", "Ideal customer profile")
accent_bar(s4)

# Best fit — left
textbox(s4, "✓  Best fit",
           Inches(0.7), Inches(1.45), Inches(5.5), Inches(0.4),
           size=15, bold=True, color=TEAL, align=PP_ALIGN.LEFT)
fit_items = [
    "Malaysian SMEs and mid-sized companies",
    "SaaS, logistics-tech, healthtech, fintech-adjacent businesses",
    "Teams with Linux/cloud workloads",
    "Companies facing enterprise security questionnaires or PDPA compliance",
    "Businesses with lean IT teams and no internal SOC",
]
bullet_box(s4, fit_items,
           Inches(0.7), Inches(1.9), Inches(5.8), Inches(3.8),
           size=14, color=DARK_TEXT, spacing_before=8)

# Not ideal — right
textbox(s4, "✗  Not ideal initially",
           Inches(7.0), Inches(1.45), Inches(5.5), Inches(0.4),
           size=15, bold=True, color=RGBColor(0xB0,0x30,0x30), align=PP_ALIGN.LEFT)
not_items = [
    "Very large enterprises",
    "Banks needing full formal SOC coverage",
    "Clients expecting broad custom consulting from day one",
]
bullet_box(s4, not_items,
           Inches(7.0), Inches(1.9), Inches(5.8), Inches(3.0),
           size=14, color=GREY_TEXT, spacing_before=8)

# Footer note
textbox(s4, "We are intentionally focused. Early on, we win where security pressure is real but internal security operations are still lean.",
        Inches(0.7), Inches(5.8), Inches(11.9), Inches(0.8),
        size=12, italic=True, color=GREY_TEXT, align=PP_ALIGN.LEFT)

# ── SLIDE 5 — How It Works ───────────────────────────────────────────────────
s5 = prs.slides.add_slide(BLANK)
add_bg(s5, LIGHT)
section_header(s5, "How It Works in Practice", "Four steps to operational security clarity")
accent_bar(s5)

four_box_row(s5,
    [
        ("1. Onboard", "Deploy monitoring on a small, agreed scope of critical systems"),
        ("2. Detect", "Filter noisy alerts and identify meaningful issues first"),
        ("3. Harden", "Apply practical security improvements on approved systems"),
        ("4. Report", "Deliver clear findings, risks, and recommended next actions"),
    ],
    row_top=Inches(2.0),
    box_w=Inches(2.7),
    box_h=Inches(3.2),
    gap=Inches(0.3))

# Bottom note
textbox(s5, "Small scope. Clear signal. Practical improvements. Useful reporting.",
        Inches(0.7), Inches(5.8), Inches(11.9), Inches(0.8),
        size=13, italic=True, color=TEAL, align=PP_ALIGN.CENTER)

# ── SLIDE 6 — Demo Proof ─────────────────────────────────────────────────────
s6 = prs.slides.add_slide(BLANK)
add_bg(s6, LIGHT)
section_header(s6, "What We've Already Proven", "MVP Demo Results")
accent_bar(s6)

# Stats row
stats = [
    ("2", "Active agents enrolled\nand monitoring"),
    ("1,243", "Security events captured\nin 24-hr window"),
    ("373", "CIS benchmark checks\nrun across demo"),
    ("42", "Medium risk score\npost-hardening"),
]
total_w = 4 * Inches(2.6) + 3 * Inches(0.5)
start_x = (prs.slide_width - total_w) / 2
for i, (num, desc) in enumerate(stats):
    x = start_x + i * (Inches(2.6) + Inches(0.5))
    # number
    textbox(s6, num, x, Inches(1.6), Inches(2.6), Inches(1.0),
            size=48, bold=True, color=TEAL, align=PP_ALIGN.CENTER)
    # description
    textbox(s6, desc, x, Inches(2.65), Inches(2.6), Inches(0.8),
            size=13, bold=False, color=GREY_TEXT, align=PP_ALIGN.CENTER)

# Findings detail
textbox(s6, "Key findings from demo environment:",
        Inches(0.7), Inches(3.6), Inches(11.9), Inches(0.4),
        size=15, bold=True, color=NAVY, align=PP_ALIGN.LEFT)

findings = [
    "SSH brute-force attempts detected and alerted within minutes",
    "PAM authentication failures flagged by rule 5503",
    "Rancher agent service failures captured automatically",
    "373 CIS benchmark failures identified; 14 remediated post-hardening",
    "Before/after SCA comparison shows measurable improvement in security posture",
]
bullet_box(s6, findings,
           Inches(0.7), Inches(4.0), Inches(11.9), Inches(2.8),
           size=14, color=DARK_TEXT, spacing_before=6)

# ── SLIDE 7 — Pilot Details ──────────────────────────────────────────────────
s7 = prs.slides.add_slide(BLANK)
add_bg(s7, LIGHT)
section_header(s7, "The 30-Day Pilot", "Proven process, limited scope, fast results")
accent_bar(s7)

# Left column — what you get
textbox(s7, "What you get",
           Inches(0.7), Inches(1.45), Inches(5.5), Inches(0.4),
           size=15, bold=True, color=NAVY, align=PP_ALIGN.LEFT)
pilot_get = [
    "Baseline security scan on agreed scope",
    "Wazuh agent deployment + enrollment",
    "CIS-aligned hardening on approved systems",
    "24/7 managed monitoring + alert triage",
    "Weekly findings summary",
    "End-of-pilot management report",
]
bullet_box(s7, pilot_get,
           Inches(0.7), Inches(1.9), Inches(5.8), Inches(3.5),
           size=14, color=DARK_TEXT, spacing_before=8)

# Right column — pilot structure
textbox(s7, "Pilot structure",
           Inches(7.0), Inches(1.45), Inches(5.5), Inches(0.4),
           size=15, bold=True, color=NAVY, align=PP_ALIGN.LEFT)
pilot_struct = [
    "Week 1: Deploy monitoring, establish baseline",
    "Week 2: Apply hardening on agreed systems",
    "Weeks 3–4: Monitor, triage, report",
    "Day 30: Review call + conversion options",
    "RM 2,000 one-time pilot fee",
    "No long-term commitment required",
]
bullet_box(s7, pilot_struct,
           Inches(7.0), Inches(1.9), Inches(5.8), Inches(3.5),
           size=14, color=DARK_TEXT, spacing_before=8)

# Bottom callout
callout_box(s7,
            "RM 2,000 | 30 days | No ongoing commitment | Management report included",
            Inches(0.7), Inches(5.7), Inches(11.9), Inches(0.9), size=14)

# ── SLIDE 8 — Pricing / Next Steps ──────────────────────────────────────────
s8 = prs.slides.add_slide(BLANK)
add_bg(s8, LIGHT)
section_header(s8, "After the Pilot — Conversion Paths", "Three options based on where you are")
accent_bar(s8)

tiers = [
    ("Watcher\nRM 1,500 / month",
     ["Managed monitoring only",
      "Alert triage + weekly digest",
      "Monthly report",
      "Up to 5 agents"]),
    ("Guardian\nRM 3,000 / month",
     ["Everything in Watcher",
      "Proactive hardening (monthly)",
      "Quarterly SCA scan",
      "Up to 15 agents",
      "Monthly sync call"]),
    ("Fortress\nCustom pricing",
     ["Everything in Guardian",
      "Continuous hardening",
      "Weekly SCA scans",
      "Unlimited agents",
      "Dedicated analyst (PT)",
      "Incident response SLA"]),
]

total_w = 3 * Inches(3.5) + 2 * Inches(0.5)
start_x = (prs.slide_width - total_w) / 2
colours = [GREY_TEXT, TEAL, NAVY]
for i, (title, bullets) in enumerate(tiers):
    x = start_x + i * (Inches(3.5) + Inches(0.5))
    # Box
    box = s8.shapes.add_shape(1, x, Inches(1.5), Inches(3.5), Inches(4.5))
    box.fill.solid()
    box.fill.fore_color.rgb = colours[i]
    box.line.fill.background()
    tf = box.text_frame
    tf.word_wrap = True

    # Title
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = title
    run.font.size = Pt(15)
    run.font.bold = True
    run.font.color.rgb = WHITE

    for b in bullets:
        p2 = tf.add_paragraph()
        p2.alignment = PP_ALIGN.LEFT
        p2.space_before = Pt(4)
        run2 = p2.add_run()
        run2.text = f"✓ {b}"
        run2.font.size = Pt(12)
        run2.font.color.rgb = WHITE if i != 1 else RGBColor(0xD0,0xF0,0xEC)

textbox(s8, "* All tiers include PDPA-aligned reporting. Custom scopes available on request.",
        Inches(0.7), Inches(6.2), Inches(11.9), Inches(0.5),
        size=11, italic=True, color=GREY_TEXT, align=PP_ALIGN.CENTER)

# ── SLIDE 9 — Contact / CTA ───────────────────────────────────────────────────
s9 = prs.slides.add_slide(BLANK)
add_bg(s9, NAVY)

textbox(s9, "Let's find out if we're a fit.",
        Inches(0.8), Inches(1.8), Inches(11.5), Inches(0.9),
        size=36, bold=True, color=WHITE, align=PP_ALIGN.LEFT)

textbox(s9, "The first step is a 20-minute discovery call — no pitch, no pressure.",
        Inches(0.8), Inches(2.7), Inches(10), Inches(0.6),
        size=20, bold=False, color=RGBColor(0xA0,0xC0,0xD0), align=PP_ALIGN.LEFT)

bar = s9.shapes.add_shape(1, Inches(0.8), Inches(3.4), Inches(3), Pt(4))
bar.fill.solid()
bar.fill.fore_color.rgb = TEAL
bar.line.fill.background()

textbox(s9, "[Your Name]",
        Inches(0.8), Inches(3.7), Inches(10), Inches(0.5),
        size=18, bold=True, color=WHITE, align=PP_ALIGN.LEFT)
textbox(s9, "Founder / Operator, Sentinel Ops",
        Inches(0.8), Inches(4.15), Inches(10), Inches(0.4),
        size=14, bold=False, color=RGBColor(0xA0,0xC0,0xD0), align=PP_ALIGN.LEFT)

textbox(s9, "📧  [email@domain.com]",
        Inches(0.8), Inches(4.8), Inches(10), Inches(0.4),
        size=15, bold=False, color=WHITE, align=PP_ALIGN.LEFT)
textbox(s9, "💬  [WhatsApp number]",
        Inches(0.8), Inches(5.2), Inches(10), Inches(0.4),
        size=15, bold=False, color=WHITE, align=PP_ALIGN.LEFT)
textbox(s9, "💼  [LinkedIn profile URL]",
        Inches(0.8), Inches(5.6), Inches(10), Inches(0.4),
        size=15, bold=False, color=WHITE, align=PP_ALIGN.LEFT)

textbox(s9, "sentinelops.my  |  demo: seeln.site",
        Inches(0.8), Inches(6.3), Inches(10), Inches(0.4),
        size=12, bold=False, color=RGBColor(0x60,0x80,0x90), align=PP_ALIGN.LEFT)

# ── Save ─────────────────────────────────────────────────────────────────────
out = "/root/.openclaw/workspace/projects/sentinel_ops/sales/Sentinel_Ops_Sales_Deck.pptx"
prs.save(out)
print(f"Saved: {out}")