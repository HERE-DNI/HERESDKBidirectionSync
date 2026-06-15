---
title: "timestampSinceBoot property"
slug: "sdk-for-flutter-explore-core-location-timestampsinceboot"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- timestampSinceBoot.html -->


<div>
<h1>timestampSinceBoot property</h1></div>

        
        Duration?
        timestampSinceBoot
<div class="features">getter/setter pair</div>


<p>The time at which the location was determined, relative to device
boot time. This time is monotonic and not affected by leap time or other system
time adjustments, so this is the recommended basis for general purpose interval timing
between location updates.
If it cannot be determined, the value is <code>null</code>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Duration? timestampSinceBoot;</code></pre>

 



</div>
`
}</HTMLBlock>
