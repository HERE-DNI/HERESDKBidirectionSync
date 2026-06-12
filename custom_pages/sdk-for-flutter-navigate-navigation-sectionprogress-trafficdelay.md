---
title: "trafficDelay property"
slug: "sdk-for-flutter-navigate-navigation-sectionprogress-trafficdelay"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- trafficDelay.html -->


<div>
<h1>trafficDelay property</h1></div>

        
        Duration
        trafficDelay
<div class="features">getter/setter pair</div>


<p>The estimated traffic delay in seconds from current location until the end of the
<a href="/sdk-for-flutter-navigate-routing-section-class">Section</a> is reached.
Note that the value is accumulated per section, and that the last section contains the overall
traffic delay until the destination is reached. The delay might be a negative value:
Negative values indicate that the part of this section can be traversed faster than usual.
Note that this is based on a delay value received at the moment of route calculation.
Defaults to 0 seconds.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Duration trafficDelay;</code></pre>

 



</div>
`
}</HTMLBlock>
