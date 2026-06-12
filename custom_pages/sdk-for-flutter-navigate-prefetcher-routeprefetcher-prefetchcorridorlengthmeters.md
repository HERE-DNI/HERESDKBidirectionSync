---
title: "prefetchCorridorLengthMeters property"
slug: "sdk-for-flutter-navigate-prefetcher-routeprefetcher-prefetchcorridorlengthmeters"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- prefetchCorridorLengthMeters.html -->


<div>
<h1>prefetchCorridorLengthMeters property</h1></div>
<section id="getter">

int
prefetchCorridorLengthMeters


<p>The length of the corridor along the route in front of the car which will be used to prefetch data.
Upper limit for length is 50000 meters, when the requested length is greater than upper limit, then 50000 meters set.
Lower limit for length is 1000 meters, when the requested length is less than lower limit, then 1000 meters set.
The route corridor has a default length of 10 km and a width of 5 km.
Gets the length of the corridor along the route in front of the car which will be used to prefetch data.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int get prefetchCorridorLengthMeters;</code></pre>

</section>
<section id="setter">

void
prefetchCorridorLengthMeters=(int value)


<p>The length of the corridor along the route in front of the car which will be used to prefetch data.
Upper limit for length is 50000 meters, when the requested length is greater than upper limit, then 50000 meters set.
Lower limit for length is 1000 meters, when the requested length is less than lower limit, then 1000 meters set.
The route corridor has a default length of 10 km and a width of 5 km.
Sets the length of the corridor along the route in front of the car which will be used to prefetch data.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set prefetchCorridorLengthMeters(int value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
