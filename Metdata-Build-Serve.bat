python generate_docs_toc.py
rmdir /s /q _site
rmdir /s /q api
docfx metadata
docfx build --serve