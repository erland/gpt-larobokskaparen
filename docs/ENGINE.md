# Lärobokskaparen Engine ZIP

Release asset: `larobokskaparen-engine-X.Y.Z.zip`.

This archive is a byte-identical packaging of `templates/bokprojekt/`, the
original project scripts and the pinned official PlantUML 1.2026.9 JAR.
It does not contain a second implementation.

## Work-first, Engine fallback

1. First materialize installed canonical skill resources to a writable workspace.
2. When that is impossible, use the Engine ZIP for the **installed version**
   from https://github.com/erland/gpt-larobokskaparen/releases .
3. Verify `engine-package.json` file hashes and run
   `python3 scripts/engine_selftest.py --render`.
4. Copy `templates/bokprojekt/` into a new isolated project directory.
5. For PlantUML use the Engine JAR through `PLANTUML_JAR` or
   `--plantuml-jar` with an absolute path to `.engine-deps/plantuml.jar`.
6. If no writable runtime or Engine bytes are available, report the block and
   request the exact matching ZIP. Do not silently create substitute scripts.

PlantUML 1.2026.9 is retrieved at build time from the official GitHub
release and SHA-256 verified. The JAR is redistributable under its included
license information; retain bundled notices and refer to the upstream source
at https://github.com/plantuml/plantuml . Java, Pandoc, XeLaTeX, and Graphviz
are **not** bundled and must be detected separately. A missing renderer blocks
publication only for books that need that renderer.
