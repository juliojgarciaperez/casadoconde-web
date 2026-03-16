# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Static single-page website for **Casa do Conde Dental** (casadocondedental.es), a dental clinic in Huelva, Spain. Built with Astro v5.10.0 and Tailwind CSS v4, deployed as pre-rendered static HTML.

## Development

There is no build system or package manager. The site is a pre-rendered `index.html` with compiled `index.css`. Edit files directly and commit.

**Deployment**: GitHub Pages via the `CNAME` file pointing to `casadocondedental.es`.

## Architecture

- **index.html** — Entire site in a single file. Sections use anchor navigation (`#equipo`, `#instalaciones`, `#contact`).
- **index.css** — Compiled Tailwind CSS bundle (do not hand-edit; regenerate if Tailwind source is available).
- **favicon.svg** — Site icon.
- **aviso.pdf / privacidad.pdf** — Legal documents (Spanish).

## External Services

- **Cloudinary** (`res.cloudinary.com/dvjb4do4c`) — All images and video assets are hosted here, not in the repo.
- **Google Analytics** — GA4 with ID `G-NQLL9RFCVP`, loaded via Google Tag Manager.
- **WhatsApp** — CTA buttons link to `wa.me/34629635875`.
- **Instagram** — `@casadocondedental`.

## Language

All user-facing content is in **Spanish**. Maintain Spanish for any new copy.
