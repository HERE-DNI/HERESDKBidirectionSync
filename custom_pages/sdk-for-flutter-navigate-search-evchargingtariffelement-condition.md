---
title: "condition property"
slug: "sdk-for-flutter-navigate-search-evchargingtariffelement-condition"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- condition.html -->


<div>
<h1>condition property</h1></div>

<a href="sdk-for-flutter-navigate-search-evchargingtariffelementcondition-class">EVChargingTariffElementCondition</a>?
        condition
<div class="features">getter/setter pair</div>


<p>Condition that the charging session needs to meet to apply the tariff element. An element without any
condition is typically present for charging sessions that do not meet any of the conditions.</p>
<p>For example, a tariff element with a lower price can be valid only during nighttime, while a generic
tariff element without conditions applies for daytime charging sessions. The conditions are listed in
priority order. I.e., when <a href="sdk-for-flutter-navigate-search-evchargingtariffelementcondition-date">EVChargingTariffElementCondition.date</a> is present, it should be matched first,
followed by <a href="sdk-for-flutter-navigate-search-evchargingtariffelementcondition-days">EVChargingTariffElementCondition.days</a> and so on.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">EVChargingTariffElementCondition? condition;</code></pre>

 



</div>
`
}</HTMLBlock>
