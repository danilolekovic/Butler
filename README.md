<div align="center">
<p>
    <img src="https://i.imgur.com/kLdlHsN.jpg">
</p>
<h1>Butler: an AI stock trading bot using WealthSimple's API.</h1>
</div>

## How It Works

The bot will only either be buying one security at a time or selling one security at a time. It does not doo anything synchronously. It buys and sells in an alternating fashion. The bot also uses static thresholds for deciding when it will buy or sell.

Basically, the bot will loop through the following logic:

**Buying:**
- 1) If the price has dropped enough, place a BUY order and change next state to SELL.
- 2) If the price hasn't dropped enough, check for a trend indication. If there is a trend, return to step 1. If there isn't a trend, do nothing.

**Selling:**
- 1) If the current price indicates a profit, place a SELL order and change next state to BUY.
- 2) If the price isn't giving us a desired profit, look for a trend. If there is a trend, go to step 1. If there isn't, do nothing.

## License & Disclaimer

The code in this repository is licensed under the permissive MIT license:

```
MIT License

Copyright (c) 2020 Danilo Lekovic

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

Nothing contained in this repository should be considered to be advice. I am not qualified to provide any sort of investment advice or legal advice. Any decisions, risks, or investments made with using anything in this repository is your responsibility.

You should be very cautious and careful. Bots can lose you a lot of money very quickly. Everything in this repository is for **EDUCATIONAL PURPOSES ONLY** and is not meant to be used in the real world.