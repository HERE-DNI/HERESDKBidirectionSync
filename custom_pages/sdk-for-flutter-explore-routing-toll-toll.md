---
title: "Toll constructor"
slug: "sdk-for-flutter-explore-routing-toll-toll"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Toll.html -->


<div>
<h1>Toll constructor</h1></div>

Toll(<ol class="parameter-list single-line"> <li>String countryCode, </li>
<li>List&lt;String&gt; tollSystems, </li>
<li>List&lt;<a href="/sdk-for-flutter-explore-routing-tollfare-class">TollFare</a>&gt; fares</li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>countryCode</code> The country in which the toll is to be paid in ISO-3166-1 alpha-3 format, e.g. "USA".</li>
<li><code>tollSystems</code> Names of the multiple toll systems which are associated with the toll, e.g. ["ATLANDES“, "ASF", "COFIROUTE"].
When the toll information covers several toll roads and the toll system of the each road is different,
all toll system names are listed here and the last element will be one of the exit toll booth.</li>
<li><code>fares</code> The list of toll fares possible for the toll which may depend on time of day, payment method, vehicle
characteristics, etc. If there are multiple toll fares that the router cannot disambiguate, then the
list will contain more than one toll fare. Note that this list contains at least one element, i.e. it
is never empty.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Toll(this.countryCode, this.tollSystems, this.fares);</code></pre>

 



</div>
`
}</HTMLBlock>
