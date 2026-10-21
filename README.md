<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./banner-dark.svg">
  <img alt="Nimur Rahman Sharif, software engineer in Dhaka. I build backends that stay correct after the demo." src="./banner-light.svg" width="100%">
</picture>

<br>

[![Portfolio](https://img.shields.io/badge/portfolio-111111?style=flat&logo=vercel&logoColor=white)](https://portfolio-tasrik.vercel.app/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nimur-rahman-sharif-946108349/)
[![Email](https://img.shields.io/badge/email-EA4335?style=flat&logo=gmail&logoColor=white)](mailto:shariftasrik12@gmail.com)
[![Outlio](https://img.shields.io/badge/Outlio-111111?style=flat&logo=googlechrome&logoColor=white)](https://outlio.ai)

</div>

## About

I am Nimur Rahman Sharif. On GitHub, Tasrik.

I build the part of a product that has to stay correct after launch: authenticated APIs, usage limits, and queries that belong in the database. When the team is small, I ship the interface too.

I founded [The Logits](https://www.linkedin.com/company/the-logits-ai). Through that work I am the contract backend engineer on [Outlio](https://outlio.ai) for SteadyTurtles. Outlio watches TikTok, Instagram, and YouTube, finds posts that beat an account's own average, and turns them into scripts and a content plan. My piece is the collection worker, the PostgreSQL layer, and the cost controls around scraping and model calls.

Before that I interned at Dohatec New Media and built a procurement system in Java and Spring Boot. A tender moves from draft to published to awarded, with JWT, role-based access, and one bid per contractor.

I am finishing a B.Sc. in Computer Science and Engineering at Ahsanullah University of Science and Technology this November. My research asks whether a language model can read a full Bangla murder-mystery novel, from a scanned page to a named murderer.

I am open to a junior software engineer role on a team that treats the backend as the product.

## Now

- **Contract backend, [Outlio](https://outlio.ai)** at SteadyTurtles. August 2026 to present. Remote.
- **Founder, [The Logits](https://www.linkedin.com/company/the-logits-ai).** January 2026 to present. Dhaka.
- **Software engineer intern, Dohatec New Media.** November 2025 to December 2025. Dhaka.
- **B.Sc. CSE, Ahsanullah University of Science and Technology.** November 2022 to November 2026.

Certifications: The Complete Full-Stack Web Development Bootcamp (Udemy), Introduction to SQL (DataCamp), Introduction to Shell (DataCamp).

## Selected work

<table>
<tr>
<td width="50%" valign="top">

### [Outlio](https://outlio.ai)

Content intelligence for short-form video, live for SteadyTurtles. I moved collection onto a Node.js worker with retries, a circuit breaker, handle quarantine, and a daily cost cap. Supabase PostgreSQL holds row-level security, plan limits, and atomic usage metering. Watch-stats run in SQL, which cut Radar latency, and cheaper model routing cut LLM cost.

Next.js · Node.js · TypeScript · Supabase · PostgreSQL · Sentry

</td>
<td width="50%" valign="top">

### [Procurement Management System](https://github.com/shariftasrik/My_Internship_Dohatec)

Dohatec New Media internship. REST APIs for tenders, bids, and evaluations, secured with Spring Security, JWT access and refresh tokens, and role-based access. One bid per contractor. Remaining bids are rejected when a tender is awarded. Angular screens for the people running the workflow.

Java · Spring Boot · Spring Security · Angular · PostgreSQL

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [AUST CSE Society](https://github.com/shariftasrik/aust-cse-society)

Campus app for the AUST CSE Society: a student feed, course resources, alumni referrals, and hiring posts. ASP.NET Identity with Admin and User roles, plus posts, likes, comments, favorites, and hashtags.

C# · ASP.NET Core MVC · Entity Framework Core · SQL Server

</td>
<td width="50%" valign="top">

### [Text-to-SQL](https://github.com/shariftasrik/text-to-sql)

A natural-language question goes in, executable SQL comes out. I fine-tuned T5 on SPIDER and placed the database schema in the model input so it can pick the right columns.

Python · PyTorch · Hugging Face · T5 · SQL

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [EPZExport](https://github.com/shariftasrik/EPZExport)

Export-performance prediction over 5,000+ Export Processing Zone records. Compared Random Forest, J48, and SMO. J48 reached 97.2% accuracy on that set. K-Means found operational profiles. Apriori pulled association rules a person can read.

Java · WEKA · classification · clustering

</td>
<td width="50%" valign="top">

### [Cravings](https://github.com/shariftasrik/Cravings)

Multi-restaurant food ordering for customers, owners, and admins. Passport.js for auth, real-time messaging over XMPP. [Live demo](https://cravings-tasrik.42web.io/).

PHP · Laravel · MySQL · Passport.js

</td>
</tr>
</table>

Also on GitHub: [CPU Scheduling Simulator](https://github.com/shariftasrik/cpu-scheduling-simulator) ([live](https://cpu-scheduling-simulator-tasrik.vercel.app/)), [portfolio](https://github.com/shariftasrik/portfolio), [dev_documentation](https://github.com/shariftasrik/dev_documentation), [NeetCode submissions](https://github.com/shariftasrik/neetcode-submissions).

## Research

**Evaluating LLM proficiency in Bangla murder-mystery novel reasoning.** November 2025 to present.

I am testing whether a model can read an entire Bangla murder mystery and name the murderer and the victim. The path runs from a scanned page through Bengali OCR, speaker-safe chunking, and retrieval (dense, BM25, fusion, then a reranker) to an event timeline and an eight-dimension suspect score. OCR word error rate was 4.3% and character error rate was 3.0%. On 62 characters, role F1 and identity F1 were both 1.00.

## Stack

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=java,spring,nodejs,ts,js,react,nextjs,angular,python,pytorch,postgres,supabase,mysql,mongodb,cs,dotnet,php,tailwind,cpp,c,laravel,huggingface,git,postman&perline=8&theme=dark">
  <img alt="Java, Spring, Node.js, TypeScript, JavaScript, React, Next.js, Angular, Python, PyTorch, PostgreSQL, Supabase, MySQL, MongoDB, C#, .NET, PHP, Tailwind, C++, C, Laravel, Hugging Face, Git, Postman" src="https://skillicons.dev/icons?i=java,spring,nodejs,ts,js,react,nextjs,angular,python,pytorch,postgres,supabase,mysql,mongodb,cs,dotnet,php,tailwind,cpp,c,laravel,huggingface,git,postman&perline=8&theme=light" />
</picture>

</div>

**Languages.** Java, C#, TypeScript, JavaScript, Python, C, C++, SQL.

**Backend.** Spring Boot, Spring Security, Spring Data JPA, Node.js, Express, ASP.NET Core, Laravel, REST, Supabase.

**Frontend.** Next.js, React, Angular, Tailwind CSS, Framer Motion, Three.js.

**Data.** PostgreSQL, MySQL, MongoDB, SQL Server.

**AI.** PyTorch, Hugging Face Transformers, T5, scikit-learn.

**Tools.** Git, IntelliJ IDEA, VS Code, Postman, Swagger, Vercel, Sentry.

## GitHub

<div align="center">

<img height="165" alt="GitHub stats for shariftasrik" src="https://github-readme-stats.vercel.app/api?username=shariftasrik&show_icons=true&hide_border=true&include_all_commits=true&title_color=0f766e&icon_color=0f766e&text_color=c9d1d9&bg_color=0d1117" />
<img height="165" alt="Top languages for shariftasrik" src="https://github-readme-stats.vercel.app/api/top-langs/?username=shariftasrik&layout=compact&hide_border=true&langs_count=8&title_color=0f766e&text_color=c9d1d9&bg_color=0d1117" />

</div>

## Contact

Dhaka, Bangladesh.

- Email: [shariftasrik12@gmail.com](mailto:shariftasrik12@gmail.com)
- Portfolio: [portfolio-tasrik.vercel.app](https://portfolio-tasrik.vercel.app/)
- LinkedIn: [Nimur Rahman Sharif](https://www.linkedin.com/in/nimur-rahman-sharif-946108349/)
- Product: [outlio.ai](https://outlio.ai)

If you are hiring for backend or full-stack work, in Dhaka or remote, write to me.
