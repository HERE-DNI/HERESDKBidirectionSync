---
title: "TollFare constructor"
slug: "sdk-for-flutter-navigate-routing-tollfare-tollfare"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TollFare.html -->


<div>
<h1>TollFare constructor</h1></div>

TollFare(<ol class="parameter-list"> <li>String currency, </li>
<li>double price, </li>
<li>List&lt;<a href="sdk-for-flutter-navigate-routing-paymentmethod">PaymentMethod</a>&gt; paymentMethods, [</li>
<li><a href="sdk-for-flutter-navigate-core-timerule-class">TimeRule</a>? timeRule = null, </li>
<li>List&lt;String&gt; transponders = const [], </li>
<li><a href="sdk-for-flutter-navigate-routing-tollfarepass-class">TollFarePass</a>? pass = null, </li>
</ol>])
    

<p>Creates a new instance.</p>
<ul>
<li><code>currency</code> The currency in which the toll is to be paid in ISO 4217 format, e.g. "USD".</li>
<li><code>price</code> The amount of the toll be paid.</li>
<li><code>paymentMethods</code> The list of accepted payment methods like cash and credit card.</li>
<li><code>timeRule</code> The time domain when this fare is valid.
If this field is missing, it means the fare is always valid.
For a detailed description of the Time Domain specification and usage in routing services, please refer to
the documentation available in the <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html">Time Domain</a></li>
<li><code>transponders</code> The list of available transponders.</li>
<li><code>pass</code> Specifies whether this <a href="sdk-for-flutter-navigate-routing-tollfare-class">TollFare</a> is a multi-travel pass, and its characteristics.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TollFare(String currency, double price, List&lt;PaymentMethod&gt; paymentMethods, [TimeRule? timeRule = null, List&lt;String&gt; transponders = const [], TollFarePass? pass = null])
  : currency = currency, price = price, paymentMethods = paymentMethods, timeRule = timeRule, transponders = transponders, pass = pass ?? null;</code></pre>

 



</div>
`
}</HTMLBlock>
