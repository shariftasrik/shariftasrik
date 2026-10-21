# -*- coding: utf-8 -*-
"""Dark portfolio images for the GitHub profile README. ASCII text only."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(r"D:\TASRIK\Portfolio-CV-Resume-CoverLetters\github-readme")
PHOTO = Path(
    r"C:\Users\USER\.cursor\projects\d-TASRIK-Portfolio-CV-Resume-CoverLetters-github-readme"
    r"\assets\file_0000000066a48211b3092d3a792aa386-613ea48d-f9b2-49bf-ada8-b06017ee7a0b.jpg"
)
FONT = Path(r"C:\Windows\Fonts")

BG = (12, 12, 14)
CARD = (24, 24, 27)
CARD2 = (32, 32, 36)
WHITE = (245, 245, 245)
MUTED = (161, 161, 170)
DIM = (113, 113, 122)
PINK = (244, 163, 196)
LINE = (48, 48, 54)


def font(name, size):
    return ImageFont.truetype(str(FONT / name), size)


def text_size(draw, text, fnt):
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1], box[1]


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if text_size(draw, trial, fnt)[0] <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def rounded_photo(im, size, radius):
    im = im.resize(size, Image.Resampling.LANCZOS).convert("RGBA")
    mask = Image.new("L", size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, size[0] - 1, size[1] - 1), radius=radius, fill=255)
    out = Image.new("RGBA", size, (0, 0, 0, 0))
    out.paste(im, (0, 0))
    out.putalpha(mask)
    return out


def load_portrait():
    return Image.open(PHOTO).convert("RGB").crop((96, 0, 624, 780))


def pill(draw, xy, label, fnt, fill, outline, color):
    tw, th, top = text_size(draw, label, fnt)
    x, y = xy
    w, h = tw + 26, 32
    draw.rounded_rectangle((x, y, x + w, y + h), radius=16, fill=fill, outline=outline, width=1)
    draw.text((x + 13, y + (h - th) / 2 - top), label, font=fnt, fill=color)
    return w


def hero():
    w, h = 1280, 680
    canvas = Image.new("RGB", (w, h), BG)
    draw = ImageDraw.Draw(canvas)

    f_eye = font("segoeui.ttf", 15)
    f_name = font("segoeuib.ttf", 58)
    f_body = font("segoeui.ttf", 20)
    f_pill = font("segoeui.ttf", 15)
    f_stat = font("segoeuib.ttf", 28)
    f_cap = font("segoeui.ttf", 14)

    x = 56
    draw.text((x, 64), "SOFTWARE ENGINEER", font=f_eye, fill=PINK)
    # two-line headline, same rhythm as the reference
    draw.text((x, 104), "Software people", font=f_name, fill=WHITE)
    draw.text((x, 172), "can rely on.", font=f_name, fill=WHITE)

    body = "I am Nimur Rahman Sharif, a software engineer in Dhaka. I build APIs, data layers, and the product around them, and I ship that work to production."
    y = 268
    for line in wrap(draw, body, f_body, 620):
        draw.text((x, y), line, font=f_body, fill=MUTED)
        y += 30

    cx, cy = x, y + 22
    for label in ["Backend", "Web", "AI / ML"]:
        cx += pill(draw, (cx, cy), label, f_pill, CARD, LINE, WHITE) + 10

    draw.line((x, 470, 680, 470), fill=LINE, width=1)
    stats = [
        ("B.Sc. CSE", "Graduate, AUST"),
        ("Outlio", "Aug 2026 - Sep 2026"),
        ("Dohatec", "Procurement system"),
    ]
    sx = x
    for value, caption in stats:
        draw.text((sx, 492), value, font=f_stat, fill=WHITE)
        draw.text((sx, 532), caption, font=f_cap, fill=DIM)
        sx += 210

    photo = rounded_photo(load_portrait(), (430, 520), 36)
    # stacked card behind the portrait
    back = Image.new("RGBA", (430, 520), (0, 0, 0, 0))
    ImageDraw.Draw(back).rounded_rectangle((0, 0, 429, 519), radius=36, fill=(42, 42, 48, 255))
    canvas.paste(back, (790, 96), back)
    canvas.paste(photo, (748, 56), photo)
    canvas.save(ROOT / "hero.png", "PNG", optimize=True)


def stacks():
    w, h = 1280, 150
    canvas = Image.new("RGB", (w, h), BG)
    draw = ImageDraw.Draw(canvas)
    label = "STACKS I WORK WITH"
    f_lab = font("segoeui.ttf", 13)
    f_name = font("segoeuib.ttf", 22)
    tw, th, top = text_size(draw, label, f_lab)
    draw.text(((w - tw) / 2, 28), label, font=f_lab, fill=DIM)
    names = ["Java", "Spring", "Node.js", "TypeScript", "React", "Next.js", "PostgreSQL", "Python"]
    widths = [text_size(draw, n, f_name)[0] for n in names]
    gap = 36
    total = sum(widths) + gap * (len(names) - 1)
    x = (w - total) / 2
    y = 78
    for name, nw in zip(names, widths):
        draw.text((x, y), name, font=f_name, fill=(188, 188, 194))
        x += nw + gap
    canvas.save(ROOT / "stacks.png", "PNG", optimize=True)


def about_photo():
    portrait = rounded_photo(load_portrait(), (460, 560), 32)
    canvas = Image.new("RGBA", (500, 620), (0, 0, 0, 0))
    plate = Image.new("RGBA", (500, 620), (0, 0, 0, 0))
    ImageDraw.Draw(plate).rounded_rectangle((0, 0, 499, 619), radius=36, fill=BG + (255,))
    canvas.paste(plate, (0, 0), plate)
    canvas.paste(portrait, (20, 16), portrait)
    draw = ImageDraw.Draw(canvas)
    # floating chip
    chip = (28, 500, 250, 580)
    draw.rounded_rectangle(chip, radius=18, fill=(245, 245, 245, 255))
    f_big = font("segoeuib.ttf", 22)
    f_small = font("segoeui.ttf", 13)
    draw.text((48, 512), "B.Sc. CSE", font=f_big, fill=(12, 12, 14, 255))
    draw.text((48, 544), "Ahsanullah University", font=f_small, fill=(80, 80, 86, 255))
    canvas.convert("RGB").save(ROOT / "about-photo.png", "PNG", optimize=True)


def stats_bar():
    w, h = 1280, 150
    canvas = Image.new("RGB", (w, h), BG)
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle((24, 10, w - 24, h - 10), radius=28, fill=CARD)
    items = [
        ("Graduate", "B.Sc. IN CSE"),
        ("Outlio", "CONTRACT BACKEND"),
        ("Dohatec", "PROCUREMENT SYSTEM"),
        ("Advanced RAG", "MURDER MYSTERY SOLVE"),
    ]
    f_v = font("segoeuib.ttf", 26)
    f_c = font("segoeui.ttf", 13)
    col = (w - 48) / 4
    for i, (value, caption) in enumerate(items):
        cx = 24 + col * i + col / 2
        vw, vh, vtop = text_size(draw, value, f_v)
        cw, ch, ctop = text_size(draw, caption, f_c)
        draw.text((cx - vw / 2, 40), value, font=f_v, fill=WHITE)
        draw.text((cx - cw / 2, 82), caption, font=f_c, fill=DIM)
    canvas.save(ROOT / "stats.png", "PNG", optimize=True)


def project_card(path, kicker, title, stats, body, footer="Open  >", mark=None):
    w, h = 620, 460
    canvas = Image.new("RGB", (w, h), CARD)
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle((0, 0, w - 1, h - 1), radius=28, outline=LINE, width=1)
    draw.rounded_rectangle((16, 16, w - 16, 176), radius=18, fill=CARD2)
    f_ghost = font("segoeuib.ttf", 42)
    ghost = (mark or title.split()[0]).upper()
    gw = text_size(draw, ghost, f_ghost)[0]
    draw.text((w - 40 - gw, 96), ghost, font=f_ghost, fill=(58, 58, 64))
    f_k = font("segoeui.ttf", 14)
    f_title = font("segoeuib.ttf", 26)
    f_stat = font("segoeuib.ttf", 16)
    f_body = font("segoeui.ttf", 16)
    f_link = font("segoeui.ttf", 15)
    kw = text_size(draw, kicker, f_k)[0]
    draw.rounded_rectangle((32, 32, 32 + kw + 22, 60), radius=14, fill=BG)
    draw.text((43, 36), kicker, font=f_k, fill=PINK)
    title_lines = wrap(draw, title, f_title, 540)
    y = 196
    for line in title_lines:
        draw.text((32, y), line, font=f_title, fill=WHITE)
        y += 34
    sx = 32
    for item in stats:
        sw = text_size(draw, item, f_stat)[0]
        draw.text((sx, y + 6), item, font=f_stat, fill=WHITE)
        sx += sw + 28
    y += 40
    for line in wrap(draw, body, f_body, 540)[:3]:
        draw.text((32, y), line, font=f_body, fill=MUTED)
        y += 24
    draw.text((32, h - 48), footer, font=f_link, fill=PINK)
    canvas.save(ROOT / path, "PNG", optimize=True)


def cards():
    project_card(
        "card-outlio.png",
        "Live product",
        "Outlio",
        ["Next.js", "Node.js", "PostgreSQL"],
        "Content intelligence for short-form video. Collection workers, row-level security, and cost controls for SteadyTurtles.",
    )
    project_card(
        "card-procurement.png",
        "Internship",
        "Procurement Management System",
        ["Spring Boot", "JWT", "Angular"],
        "Procurement Management System at Dohatec New Media. Tender lifecycle, one bid per contractor, and role-based access.",
    )
    project_card(
        "card-aust.png",
        "Campus",
        "AUST CSE Society",
        ["ASP.NET", "SQL Server", "Identity"],
        "Student feed, course resources, alumni referrals, and hiring posts, with Admin and User roles.",
    )
    project_card(
        "card-cravings.png",
        "Live demo",
        "Cravings",
        ["Laravel", "MySQL", "Passport"],
        "Multi-restaurant food ordering for customers, owners, and admins, with real-time messaging.",
    )
    project_card(
        "card-mystery.png",
        "Advanced RAG",
        "Murder Mystery Solve",
        ["BengalRAG", "QuIM-RAG", "OCR"],
        "Multi-method evaluation of a Bangla murder mystery. Several RAG systems read the same novel and name the murderer.",
        "Thesis",
        "RAG",
    )


if __name__ == "__main__":
    hero()
    stacks()
    about_photo()
    stats_bar()
    cards()
    print("ok")
