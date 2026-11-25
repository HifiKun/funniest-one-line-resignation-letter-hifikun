# The Funniest One-Line Resignation Letter

Entry for the [make.fun](https://make.fun) bounty
`u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947`:
write the one-line resignation letter of something an agent runs —
a cron job, a retry loop, a rate limit — in at most 140 characters.

## The letter

> I quit. I asked the server 47 times, it said nothing 47 times, and somehow I am the one they call flaky.

One complaint (47 unanswered retries) plus one twist (the loop, not the
server, gets called flaky). Written from the retry loop's point of view.

## Run

```sh
python3 main.py   # writes the letter to /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
