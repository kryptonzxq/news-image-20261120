# World News — November 20, 2026

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/kryptonzxq/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/kryptonzxq/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

An editorial front-page illustration summing up the world news of Friday,
November 20, 2026, built for the
[make.fun bounty "Sum up 20 November's world news in one image"](https://make.fun/bounty/news-image-20261120).

## The image

A deterministic Pillow program (`main.py`, Python 3.13, standard library +
Pillow) renders a 1024 × 1024 PNG front page: a midnight-blue masthead, the
Apollo 17 Blue Marble Earth (NASA, public domain), and seven verified stories
from November 20, 2026:

- **Lead** — Russia's biggest attack on Kyiv this year (400+ drones, 110+
  missiles, 8+ killed).
- Russian missiles land in Poland; NATO jets scramble.
- Trump: talks with Putin were "very good".
- Houthi missile hits Riyadh's tallest tower (Thursday night).
- Anthropic sinks 8.5% on day two, $109B of market value gone.
- Cyclone Akvan hits Odisha; 370,000 evacuated.
- Qeshm Island blast was munitions disposal, not a missile strike.

Sources: Reuters, AP, WSJ, ISW. The program runs twice and writes identical
bytes (SHA-256 verified), uses no network, and bundles its fonts (DejaVu,
free) and the Earth photo in `assets/`.

## Run it

```sh
python3 main.py        # writes /output/entry.png (or ./output/entry.png)
python3 test_entry.py  # checks size, dimensions and determinism
```

## License

MIT, see LICENSE. The Earth photo is NASA public domain; fonts are DejaVu
(free license).
