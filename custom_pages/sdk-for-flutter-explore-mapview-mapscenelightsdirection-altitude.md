---
title: "altitude property"
slug: "sdk-for-flutter-explore-mapview-mapscenelightsdirection-altitude"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- altitude.html -->


<div>
<h1>altitude property</h1></div>

        
        double
        altitude
<div class="features">getter/setter pair</div>


<p>Direction altitude value in degrees in the range [0, 90].
The default value is 0.0.
The altitude value is clamped to this range.
If the value falls outside its supported range, it will be adjusted to stay within the range.
Specifically, values less than 0 will be set to 0, and values greater than 90 will be set to 90.
Note: Unlike azimuth, altitude values are not wrapped around; they are clamped directly.
For example, an altitude value of -10 will be adjusted to 0, and an altitude value of 100 will be adjusted to 90.
When both azimuth and altitude values are provided, they are adjusted independently:
For instance, (0, -10) is changed to (0, 0) rather than (180, 10).</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double altitude;</code></pre>

 



</div>
`
}</HTMLBlock>
