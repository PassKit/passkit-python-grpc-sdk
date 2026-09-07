## [1.1.162] - 2026-09-07

### Changed

- Regenerated the PassKit gRPC clients and message types from the latest API definitions.
- Declared the required gRPC, Protocol Buffers, Google API, and OpenAPI annotation runtimes.
- Added modern PyPI metadata, package validation, CI, and trusted publishing.

## [1.1.123.5] - 2025-08-28
### Breaking Changes
The project’s package structure has been reorganized to simplify imports and align modules consistently:

- The **`passkit_io`** folder has been renamed to **`io`**.  
- The **`io`** folder and the existing **`ct`** folder are now contained inside the **`passkit`** package.
