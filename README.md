# NetProbe

NetProbe is a Python-based network monitoring and diagnostic toolkit designed to perform multiple network health checks from a single command-line interface.

It combines common network troubleshooting utilities into one workflow and provides a complete diagnosis and exportable report for a target host.

---

## Features

NetProbe currently supports:

- DNS resolution
- ICMP ping diagnostics
- HTTP/HTTPS health checks
- TCP port scanning
- Traceroute analysis
- Complete network diagnosis
- Text-based report generation
- Per-target report storage
- Automatic replacement of older reports for the same target

---

## Architecture

```text
                    ┌─────────────────┐
                    │     NetProbe    │
                    │   CLI Interface │
                    └────────┬────────┘
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
          ▼                  ▼                  ▼
     DNS Lookup         Ping Test        HTTP Check
          │                  │                  │
          └──────────────────┼──────────────────┘
                             │
                    ┌────────▼────────┐
                    │   Port Scanner  │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │   Traceroute    │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │ Complete        │
                    │ Diagnosis       │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │ Report Generator│
                    └────────┬────────┘
                             │
                             ▼
                    reports/<target>/
                         report.txt