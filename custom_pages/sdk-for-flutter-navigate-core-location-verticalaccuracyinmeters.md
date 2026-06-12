---
title: "verticalAccuracyInMeters property"
slug: "sdk-for-flutter-navigate-core-location-verticalaccuracyinmeters"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- verticalAccuracyInMeters.html -->


<div>
<h1>verticalAccuracyInMeters property</h1></div>

        
        double?
        verticalAccuracyInMeters
<div class="features">getter/setter pair</div>


<p>Estimated vertical accuracy.
Given that the received Location contains the altitude, the real value of the altitude
is estimated to lie within the following range:
[altitude - vertical accuracy, altitude + vertical accuracy].
For example, when the altitude is equal to 50 and the vertical accuracy
is 8, then the actual value is most likely in the range [42, 58].</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double? verticalAccuracyInMeters;</code></pre>

 



</div>
`
}</HTMLBlock>
