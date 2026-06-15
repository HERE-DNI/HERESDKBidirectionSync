---
title: "truckAccess property"
slug: "sdk-for-flutter-navigate-search-evchargingtruckrestriction-truckaccess"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- truckAccess.html -->


<div>
<h1>truckAccess property</h1></div>

        
        List&lt;<a href="sdk-for-flutter-navigate-transport-truckclass">TruckClass</a>&gt;
truckAccess
<div class="features">getter/setter pair</div>


<p>Access categories for trucks and light commercial vehicles that the
EV charging location is designed to serve.</p>
<p>While the classifications used as basis for the categories are solely based on vehicle mass,
in EV charging context they can be interpreted to give an idea of the dimensional class too,
as well as possible other restrictions set by the operator. If there are true dimensional or
weight limits at the EV charging location, they are specified separately in vehicleLimitations.</p>
<p>The classification is available only to a subset of EV charging locations, depending on the
information available from the operators. Hence, at least vehicles belonging to the
<a href="sdk-for-flutter-navigate-transport-truckclass">TruckClass.lightClass</a> category can be charged also in many EV charging locations not having
explicit signaling for the <a href="sdk-for-flutter-navigate-transport-truckclass">TruckClass.lightClass</a> category.</p>
<p>Furthermore, although the classification is based on mass/weight ranges in growing order,
an upper class does not automatically mean that also all lower class vehicles are welcome to charge.
For example, a location marked only with category <a href="sdk-for-flutter-navigate-transport-truckclass">TruckClass.heavyClass</a>
is reserved for long-haul trucks only.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;TruckClass&gt; truckAccess;</code></pre>

 



</div>
`
}</HTMLBlock>
