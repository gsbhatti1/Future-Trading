---

Name: M-Language-Turtle-Trading-strategy-implementationsV-10

Author: InventorQuant - XiaoXiaoMeng

Strategy Description:

* Fully compatible with WenHua Ma Language syntax
* Based on Inventor's powerful low-level framework, fully supports spot and futures trading of digital currencies and domestic commodity futures
* Compatibility work continues, currently at 90% compatibility; most strategies can run without modification
* API documentation: https://www.fmz.com/bbs-topic/2569

Language Enhancement:

InventorQuant not only implements the Ma Language interpreter but also enhances it to allow hybrid programming with advanced languages like JavaScript. Here's an example:

```
%%
// You can call any InventorQuant API here
scope.TEST = function(obj) {
    return obj.val * 100;
}
%%
Close: C;
Close magnified by 100x: TEST(C);
Previous Close magnified by 100x: TEST(REF(C, 1)); // Hovering the mouse over the backtest K-line will show variable values
```

![IMG](https://www.fmz.com/upload/asset/81cecb83b47ecca04ddd63c3206eb0db.png)

---

Background:

In 1994, Covell picked up an issue of Financial World and skimmed through an article titled "Wall Street's Top Players." Among famous investors like George Soros and Julian Robertson, Covell noticed a name he did not recognize at 25th on the list: R. Jerry Parker, who stated that he was trained as a "Turtle" by Richard Dennis (another name Covell did not recognize). Parker was the only investor in the top hundred advertised as being "trained," and as an investor himself, Covell found this story intriguing.

Synopsis:

Richard Dennis made over $200 million as a trader. After having a debate with his partner, William Eckhardt, about whether trading is learnable or an inborn talent, they proposed an experiment where they would spend two weeks training novices in the science of trading and then give them each $1 million to invest. The inspiration came from a trip Dennis took to a turtle-breeding farm in Singapore, stating, "We are going to grow traders just like they grow turtles."

Although each of the 1,000 applicants went through a rigorous application process designed to test their intelligence, ability to manage risk and mathematical skills, the makeup of the chosen Turtles differed greatly; they included a Czechoslovakian-born blackjack master, a Dungeons and Dragons game designer, an evangelical accountant, a Harvard MBA, a U.S. Air Force pilot, and a former pianist. The Turtles would go on to gross over $150 million in four years.

Trading Rules:

In capturing trend signals, the Turtle Trading Law uses a very important technical indicator, the Donchian channel. This channel is quite similar to the well-known Bollinger Bands but differs slightly in specific calculations.

Richard Donchian invented this indicator. It consists of three differently colored curves. The indicator uses the highest price within the period (usually 20; some platform system settings can be changed, some cannot) and the lowest price to show market price volatility. When the channel is narrow, it means that the market volatility is small; otherwise, the channel width indicates relatively large market volatility.

When the price breaks through the upper track of the channel, it is a possible buy signal; conversely, breaking the lower track is a possible sell signal.

The calculation methods for the Donchian channel are as follows:

- Upper rail = Max (highest, n), where 'n' is the highest value of the highest price over n days.
- Lower rail = Min (lowest, n), where 'n' is the minimum value of the lowest price over n days.
- Middle rail = (upper rail + lower rail) / 2

Within the framework of multi-factor analysis in finance, this strategy predicts the price trend after a breakthrough based on the validity hypothesis of the momentum factor. Of course, the effectiveness of this factor has indeed been rigorously verified and complemented by the Fama-French three-factor model, making it widely used in financial markets.

Of course, we can optimize and use more reasonable trend-breaking indicators.

So, since the momentum factor is a public and widely used factor, then why can the Turtle Trading Law stand out from the crowd? The answer is simple. The Turtle Trading Rules define a set of very strict rules for position control and stop-loss. Let's take a look at each one:

1. Basic Unit N of Position

The principle of the Turtle Rule is to define a small unit (Unit) so that the expected value fluctuation of the position corresponds to 1% of the total net assets. In other words, if you buy this asset in the small unit, the market value of the position on that day will not change by more than 1% of the total net assets.

So how do you define this small unit? How do you estimate the value fluctuations that this small unit can bring? First, to predict the value volatility of this small unit (this value volatility is called N), the Turtle Strategy uses a method of statistically averaging historical price volatility. The specific calculation formula is as follows:

TrueRange = Max(High−Low, High−PreClose, PreClose−Low)

N = (the sum of the N values of the previous 19 days + the TrueRange at the time) / 20

Among them, High indicates the highest price of the day, Low indicates the lowest price of the day, and PreClose indicates the closing price of the previous day. We can see from the definition that the value of N indeed properly expresses recent fluctuations in the asset's price.

Thus, a Unit should be calculated like this:

Unit = (1% * Total_net) / N, where Total_net is the total net asset value

It can be seen that the price volatility of a Unit's assets = 1% of the total net assets.

2. When to open a position

The action of opening a position comes from the generation of a trend breakthrough signal. If the current price breaks through the upper track, it will generate a buy position signal. If the current price falls below the lower track, it will generate a short position signal (short selling is supported in the cryptocurrency market).

Initial build size = 1 Unit

3. When to add to a position?

If the holding position is long positions and the pr