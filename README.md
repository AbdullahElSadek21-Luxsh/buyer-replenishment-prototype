# Buyer Replenishment — Prototype

An early **front-end prototype** (information dashboard) for the Buyer Replenishment
improvement project at B&S Distribution. It is the visual/design prototype only —
there is no live data connection, database, or forecast engine behind it yet.

## View it

- **Live link:** see the **GitHub Pages** URL in this repo's *Settings → Pages*
  (or the link shared with you).
- **Or locally:** download the repo and **double-click `index.html`** — it is a
  single self-contained file and opens in any browser, no install or internet needed.

## What it shows

A **product-based** view of the lines that need a buyer's attention, across four sections:

- **Under 14 days** of stock
- **Zero stock**
- **Selling fast** (above expected)
- **Selling slow** (below expected)

Pick a supplier to filter, or view all your assigned suppliers at once. Expand any
line to see a recommendation ("why this action"), the stock position, and a
**supplier price comparison** ranked by **net price after rebate**.

## Important

- **All figures are illustrative.** Stock, prices, suppliers and monthly sales are
  sample data modelled on the Buying History screens — nothing here is live.
- This is a **read-only dashboard**: it does not place orders or send anything.
- Internal to B&S — please keep this repository private.

## Run locally with a shareable link on your network

```bash
python serve.py
```

Serves the dashboard on `http://<your-lan-ip>:8090` (printed on start) so others on
the same network can open it. Keep the terminal open; close it to stop.
