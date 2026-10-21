# -*- coding: utf-8 -*-
"""Build GitHub-profile images. Output is PNG/GIF, no text encoding issues."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(r"D:\TASRIK\Portfolio-CV-Resume-CoverLetters\github-readme")
PHOTO = Path(
    r"C:\Users\USER\.cursor\projects\d-TASRIK-Portfolio-CV-Resume-CoverLetters-github-readme"
    r"\assets\file_0000000066a48211b3092d3a792aa386-613ea48d-f9b2-49bf-ada8-b06017ee7a0b.jpg"
)
FONT = Path(r"C:\Windows\Fonts")

BG = (13, 17, 23)
CARD = (22, 27, 34)
WHITE = (240, 246, 252)
MUTED = (139, 148, 158)
DIM = (110, 118, 129)
TEAL = (45, 212, 191)
TEAL_DIM = (15, 70, 64)
LINE = (48, 54, 61)


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


def hero():
    w, h = 1280, 520
    canvas = Image.new("RGB", (w, h), BG)
    glow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse((860, -80, 1460, 560), fill=(45, 212, 191, 28))
    glow = glow.filter(ImageFilter.GaussianBlur(40))
    canvas = Image.alpha_composite(canvas.convert("RGBA"), glow).convert("RGB")
    draw = ImageDraw.Draw(canvas)
    draw.rectangle((0, 0, 8, h), fill=TEAL)

    photo = Image.open(PHOTO).convert("RGB").crop((96, 0, 624, 760))
    portrait = rounded_photo(photo, (300, 412), 28)
    frame = Image.new("RGBA", (312, 424), (0, 0, 0, 0))
    ImageDraw.Draw(frame).rounded_rectangle((0, 0, 311, 423), radius=34, outline=TEAL + (255,), width=2)
    px, py = 908, 48
    canvas.paste(portrait, (px + 6, py + 6), portrait)
    canvas.paste(frame, (px, py), frame)
    draw = ImageDraw.Draw(canvas)

    f_eye = font("segoeui.ttf", 16)
    f_name = font("segoeuib.ttf", 52)
    f_tag = font("segoeui.ttf", 24)
    f_pill = font("segoeui.ttf", 16)

    x = 56
    draw.text((x, 108), "SOFTWARE ENGINEER", font=f_eye, fill=TEAL)
    draw.text((x, 142), "Nimur Rahman Sharif", font=f_name, fill=WHITE)
    draw.rectangle((x, 214, x + 92, 218), fill=TEAL)
    tag = "I build backends that stay correct after the demo."
    draw.text((x, 240), tag, font=f_tag, fill=(201, 209, 217))

    pills = ["Dhaka", "Outlio", "The Logits", "AUST CSE"]
    cx, cy = x, 312
    for label in pills:
        tw, th, top = text_size(draw, label, f_pill)
        pw, ph = tw + 28, 36
        draw.rounded_rectangle((cx, cy, cx + pw, cy + ph), radius=18, outline=LINE, width=1)
        draw.text((cx + 14, cy + (ph - th) / 2 - top), label, font=f_pill, fill=MUTED)
        cx += pw + 12

    draw.text((x, 392), "Spring Boot   |   Node.js   |   PostgreSQL   |   TypeScript", font=font("segoeui.ttf", 16), fill=DIM)
    canvas.save(ROOT / "hero.png", "PNG", optimize=True)


def experience():
    w, h = 1280, 620
    canvas = Image.new("RGB", (w, h), BG)
    draw = ImageDraw.Draw(canvas)
    draw.rectangle((0, 0, 8, h), fill=TEAL)

    items = [
        ("Aug 2026 - Present", "Contract Backend Engineer", "Outlio  |  SteadyTurtles  |  Remote", "Collection workers, row-level security, usage limits, and cost controls on a live SaaS."),
        ("Jan 2026 - Present", "Founder", "The Logits  |  Dhaka", "A small software studio. Outlio is the product we are building with SteadyTurtles."),
        ("Nov 2025 - Dec 2025", "Software Engineer Intern", "Dohatec New Media  |  Dhaka", "Procurement system in Spring Boot: tenders, JWT, and role-based access."),
        ("Nov 2022 - Nov 2026", "B.Sc. Computer Science", "Ahsanullah University of Science and Technology", "Finishing this November. Research on whether a model can solve a Bangla murder mystery."),
    ]

    f_date = font("segoeui.ttf", 16)
    f_role = font("segoeuib.ttf", 26)
    f_org = font("segoeui.ttf", 18)
    f_body = font("segoeui.ttf", 16)

    line_x = 300
    top = 46
    row_h = 140
    draw.line((line_x, top + 8, line_x, top + row_h * (len(items) - 1) + 16), fill=TEAL_DIM, width=3)

    for i, (date, role, org, body) in enumerate(items):
        y = top + i * row_h
        tw, th, ttop = text_size(draw, date, f_date)
        draw.text((line_x - 28 - tw, y + 4), date, font=f_date, fill=TEAL)
        draw.ellipse((line_x - 7, y + 6, line_x + 7, y + 20), fill=TEAL)
        draw.text((line_x + 28, y - 2), role, font=f_role, fill=WHITE)
        draw.text((line_x + 28, y + 36), org, font=f_org, fill=MUTED)
        for n, line in enumerate(wrap(draw, body, f_body, 860)):
            draw.text((line_x + 28, y + 68 + n * 22), line, font=f_body, fill=DIM)

    canvas.save(ROOT / "experience.png", "PNG", optimize=True)


def carousel():
    slides = [
        ("01", "Outlio", "LIVE", "Content intelligence for short-form video. I own the backend: retries, a circuit breaker, a daily cost cap, and Postgres with row-level security.", "Next.js   |   Node.js   |   TypeScript   |   Supabase   |   PostgreSQL", "outlio.ai"),
        ("02", "Procurement System", "DOHATEC", "Tenders move from draft to award. Spring Security, JWT, one bid per contractor, and Angular screens for the people running it.", "Java   |   Spring Boot   |   Spring Security   |   Angular   |   PostgreSQL", "github.com/shariftasrik/My_Internship_Dohatec"),
        ("03", "AUST CSE Society", "CAMPUS", "A student feed, course resources, alumni referrals, and hiring posts, with Admin and User roles.", "C#   |   ASP.NET Core   |   Entity Framework   |   SQL Server", "github.com/shariftasrik/aust-cse-society"),
        ("04", "Text-to-SQL", "RESEARCH", "A plain-language question goes in. Executable SQL comes out. T5 fine-tuned on SPIDER, with the schema in the model input.", "Python   |   PyTorch   |   Hugging Face   |   T5   |   SQL", "github.com/shariftasrik/text-to-sql"),
        ("05", "EPZExport", "DATA", "Export-performance prediction on 5,000+ EPZ records. J48 reached 97.2% accuracy on that set. K-Means and Apriori found patterns a person can read.", "Java   |   WEKA   |   Random Forest   |   J48   |   K-Means", "github.com/shariftasrik/EPZExport"),
        ("06", "Cravings", "LIVE DEMO", "Multi-restaurant ordering for customers, owners, and admins. Passport.js for sign-in and real-time messaging over XMPP.", "PHP   |   Laravel   |   MySQL   |   Passport.js", "cravings-tasrik.42web.io"),
    ]

    w, h = 1280, 380
    f_kicker = font("segoeui.ttf", 15)
    f_num = font("segoeuib.ttf", 92)
    f_title = font("segoeuib.ttf", 40)
    f_body = font("segoeui.ttf", 20)
    f_stack = font("consola.ttf", 16)
    f_link = font("segoeui.ttf", 15)

    frames = []
    for i, (num, title, badge, body, stack, link) in enumerate(slides):
        canvas = Image.new("RGB", (w, h), BG)
        draw = ImageDraw.Draw(canvas)
        draw.rectangle((0, 0, 8, h), fill=TEAL)
        # ghost index
        draw.text((48, 70), num, font=f_num, fill=(28, 36, 44))
        draw.text((250, 58), "SELECTED WORK", font=f_kicker, fill=TEAL)
        # badge
        bw = text_size(draw, badge, f_kicker)[0] + 22
        draw.rounded_rectangle((250, 86, 250 + bw, 114), radius=14, fill=TEAL_DIM)
        draw.text((261, 90), badge, font=f_kicker, fill=TEAL)
        draw.text((250, 128), title, font=f_title, fill=WHITE)
        y = 188
        for line in wrap(draw, body, f_body, 960):
            draw.text((250, y), line, font=f_body, fill=(201, 209, 217))
            y += 28
        draw.text((250, 292), stack, font=f_stack, fill=DIM)
        draw.text((250, 328), link, font=f_link, fill=TEAL)

        # carousel progress
        bar_x, bar_y, bar_w = 980, 344, 240
        draw.rounded_rectangle((bar_x, bar_y, bar_x + bar_w, bar_y + 6), radius=3, fill=LINE)
        filled = int(bar_w * (i + 1) / len(slides))
        draw.rounded_rectangle((bar_x, bar_y, bar_x + filled, bar_y + 6), radius=3, fill=TEAL)
        frames.append(canvas)

    first, rest = frames[0], frames[1:]
    first.save(
        ROOT / "carousel.gif",
        save_all=True,
        append_images=rest,
        duration=2800,
        loop=0,
        optimize=True,
        disposal=2,
    )
    # stills so the slides can be checked
    for i, frame in enumerate(frames, start=1):
        frame.save(ROOT / f"slide-{i}.png", "PNG", optimize=True)


if __name__ == "__main__":
    hero()
    experience()
    carousel()
    print("ok", (ROOT / "hero.png").stat().st_size, (ROOT / "experience.png").stat().st_size, (ROOT / "carousel.gif").stat().st_size)
