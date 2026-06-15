---
title: "azimuth property"
slug: "sdk-for-flutter-navigate-mapview-mapscenelightsdirection-azimuth"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- azimuth.html -->


<div>
<h1>azimuth property</h1></div>

        
        double
        azimuth
<div class="features">getter/setter pair</div>


<p>Direction azimuth value in degrees in the range [0, 360).
The default value is 0.0.
The azimuth range is half-open, meaning the maximum value is not included in the range.
If the azimuth value falls outside the range, it is wrapped to stay within [0, 360).
Specifically, values less than 0 will be increased by 360 until they fall within the range,
and values greater than or equal to 360 will be reduced by 360 until they fall within the range.
By convention, an azimuth of 0 degrees corresponds to North, and azimuth values increase clockwise.
Thus, 90 degrees corresponds to East, 180 degrees to South, and 270 degrees to West.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double azimuth;</code></pre>

 



</div>
`
}</HTMLBlock>
