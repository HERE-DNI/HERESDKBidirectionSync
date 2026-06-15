---
title: "step property"
slug: "sdk-for-flutter-navigate-search-evchargingtariffpricecomponent-step"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- step.html -->


<div>
<h1>step property</h1></div>

        
        double?
        step
<div class="features">getter/setter pair</div>


<p>Dimension quantity used as a unit of billing. Present for all other dimensions except
<a href="sdk-for-flutter-navigate-search-evchargingtariffdimension">EVChargingTariffDimension.flat</a>. The customer is charged price for each full or partial
step of the dimension consumed. For <a href="sdk-for-flutter-navigate-search-evchargingtariffdimension">EVChargingTariffDimension.energy</a>, the step size unit
is 1 Wh, for <a href="sdk-for-flutter-navigate-search-evchargingtariffdimension">EVChargingTariffDimension.time</a> and <a href="sdk-for-flutter-navigate-search-evchargingtariffdimension">EVChargingTariffDimension.parkingTime</a>
it is 1 second. For example, if step is 300 for time, then time is billed in 5 minute steps, rounded upwards.
Similarly, if step is 100 for energy, then energy is billed in 100 Wh = 0.1 kWh steps.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double? step;</code></pre>

 



</div>
`
}</HTMLBlock>
