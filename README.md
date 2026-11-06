<h1 align="center">Hi, I'm Satya Thakur</h1>

<p align="center">
  <b>Computer Science senior at UMBC (graduating December 2026)</b><br>
  I build backend services and systems-level software, from FastAPI and PostgreSQL to Linux kernel modules.<br><br>
  <b>Open to full-time new-grad Software Engineer roles</b> · US Citizen · Maryland 
</p>

<p align="center">
  <a href="https://linkedin.com/in/satya-thakur-415706343"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="mailto:uw61778@umbc.edu"><img src="https://img.shields.io/badge/Email-D14836?style=flat&logo=gmail&logoColor=white" alt="Email" /></a>
  <!-- Optional: add a Portfolio badge and a Resume badge here once you have the URLs
  <a href="YOUR_PORTFOLIO_URL"><img src="https://img.shields.io/badge/Portfolio-111111?style=flat&logo=safari&logoColor=white" alt="Portfolio" /></a>
  <a href="./Satya_Thakur_Resume.pdf"><img src="https://img.shields.io/badge/Resume-PDF-success?style=flat" alt="Resume" /></a>
  -->
</p>

---

## About

I like understanding how software works under the hood. That shows up in my projects: a task scheduler that spans user space and the Linux kernel, a filesystem built on FUSE, and backend services where I care about concurrency, correctness, and measured performance.

**Right now:** building [PunchList Pro](https://github.com/SdThakur/PunchList), a real-time, role-based defect-tracking platform for construction teams.

**Looking for:** new-grad backend, systems, or full-stack roles where I can own features end to end and keep learning from experienced engineers.

---

## Tech Stack

<p align="left">
  <!-- Languages -->
  <img src="https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=c&logoColor=black" alt="C" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white" alt="Java" />
  <img src="https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white" alt="SQL" />
  <!-- Backend and data -->
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=node.js&logoColor=white" alt="Node.js" />
  <img src="https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=springboot&logoColor=white" alt="Spring Boot" />
  <img src="https://img.shields.io/badge/Socket.IO-010101?style=flat-square&logo=socketdotio&logoColor=white" alt="Socket.IO" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white" alt="SQLite" />
  <!-- Systems, infra, testing -->
  <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions" />
  <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" alt="Git" />
  <img src="https://img.shields.io/badge/Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white" alt="Pytest" />
  <!-- Frontend -->
  <img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black" alt="React" />
  <img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=next.js&logoColor=white" alt="Next.js" />
  <img src="https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white" alt="Tailwind CSS" />
</p>

---

## Featured Projects

### [PunchList Pro](https://github.com/SdThakur/PunchList)
*Tablet-first construction defect-tracking platform with six user roles.*

- Server-validated five-stage lifecycle (Open → In Progress → GC Review → Admin Review → Closed) with a JWT-authenticated, six-role RBAC permission matrix.
- Real-time collaboration through a WebSocket hub with room-based broadcasting, so status changes reach every connected client without a refresh.
- Dual-engine persistence (SQLAlchemy Core over PostgreSQL and SQLite) with automatic cloud-to-local failover for field use during connectivity loss.
- Pytest and Vitest suites, PDF/CSV reporting, Dockerized deployment, and GitHub Actions CI/CD.

`React 18` `Vite` `FastAPI` `PostgreSQL` `SQLite` `Socket.IO` `Docker`

### [CivicFix](https://github.com/SdThakur/CivicFix)
*311 civic dispatch platform that triages reports with AI.*

- AI photo triage with Gemini 2.5 Flash, reverse-geocoding, and a transparent five-factor priority score.
- Duplicate-report merging using CLIP embeddings and PostGIS spatial matching (0.75 similarity threshold).
- Background processing with Celery so uploads stay responsive.

`TypeScript` `Next.js` `FastAPI` `PostgreSQL/PostGIS` `Celery` `Gemini`

### Hybrid RAG Document Intelligence Platform
<!-- TODO: link this heading to the repo, e.g. ### [Hybrid RAG Document Intelligence Platform](https://github.com/SdThakur/YOUR-REPO) -->
*Search over PDF, DOCX, and Markdown files that combines keyword and semantic retrieval.*

- Non-blocking ingestion pipeline: uploads return immediately while files are parsed, chunked, and embedded in the background, with status polling.
- BM25 keyword search fused with 384-dimensional semantic embeddings through Reciprocal Rank Fusion, served from an embedded SQLite + NumPy vector store with no external database.
- 44 unit, integration, and mocked-LLM tests covering parsing, chunking, and ranking.

`Python` `FastAPI` `SQLite` `NumPy` `Streamlit`

### [Dual-Layer Task Scheduler & Kernel Module](https://github.com/SdThakur/Task-Scheduler-with-Priority-and-Resource-Constraints)
*Priority scheduler spanning Linux user space and a loadable kernel module.*

- User space (pthreads, mutexes, semaphores) and kernel space (kthreads, spinlocks, `cdev`/`ioctl`), scheduling tasks across three priority tiers.
- All-or-nothing atomic resource acquisition to avoid race conditions, with execution dispatched to kernel workqueues.
- Wait-For Graph deadlock detection (DFS cycle detection) and priority aging to prevent starvation.
- Stress-tested with 1,000+ concurrent task executions under AddressSanitizer, ThreadSanitizer, and Valgrind.

`C` `Linux Kernel` `POSIX Threads`

### [UMBC Parking Management System](https://github.com/SdThakur/UMBC-Parking-System)
*Containerized reservation database focused on correctness under concurrency.*

- Prevents double-booking with `SELECT ... FOR UPDATE` row locking.
- Cut query latency by 40% using composite B-Tree indexes.

`PostgreSQL 16` `Docker` `Python` `Streamlit`

---

## More Systems Work

- **[MEMEFS](https://github.com/SdThakur/Multimedia-Embedded-Memory-Encapsulation-File-System):** a FAT-style filesystem in C on FUSE 3, with a formatting utility.
- **Linux Kernel Connect Four Module:** a character device driver (`/dev/fourinarow`) that keeps game state in kernel memory.
- **Custom UNIX Shell (C):** `fork`/`execvp`/`wait`, pipes, I/O redirection, background jobs, signal handling, and command history.
- **Hash Table (Python):** linear probing, quadratic probing, double hashing, lazy deletion, and dynamic resizing at a 0.75 load factor.

---

## Connect

- **LinkedIn:** [/in/satya-thakur-415706343](https://linkedin.com/in/satya-thakur-415706343)
- **Email:** [uw61778@umbc.edu](mailto:uw61778@umbc.edu)
