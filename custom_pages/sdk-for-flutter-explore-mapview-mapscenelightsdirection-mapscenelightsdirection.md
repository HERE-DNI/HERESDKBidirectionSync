---
title: "MapSceneLightsDirection constructor"
slug: "sdk-for-flutter-explore-mapview-mapscenelightsdirection-mapscenelightsdirection"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapSceneLightsDirection.html -->


<div>
<h1>MapSceneLightsDirection constructor</h1></div>

MapSceneLightsDirection(<ol class="parameter-list single-line"> <li>double azimuth, </li>
<li>double altitude</li>
</ol>)
    

<p>Constructs a Direction from the values.</p>
<ul>
<li><code>azimuth</code> Direction azimuth value in degrees in the range [0, 360).
The default value is 0.0.
The azimuth range is half-open, meaning the maximum value is not included in the range.
If the azimuth value falls outside the range, it is wrapped to stay within [0, 360).
Specifically, values less than 0 will be increased by 360 until they fall within the range,
and values greater than or equal to 360 will be reduced by 360 until they fall within the range.
By convention, an azimuth of 0 degrees corresponds to North, and azimuth values increase clockwise.
Thus, 90 degrees corresponds to East, 180 degrees to South, and 270 degrees to West.</li>
<li><code>altitude</code> Direction altitude value in degrees in the range [0, 90].
The default value is 0.0.
The altitude value is clamped to this range.
If the value falls outside its supported range, it will be adjusted to stay within the range.
Specifically, values less than 0 will be set to 0, and values greater than 90 will be set to 90.
Note: Unlike azimuth, altitude values are not wrapped around; they are clamped directly.
For example, an altitude value of -10 will be adjusted to 0, and an altitude value of 100 will be adjusted to 90.
When both azimuth and altitude values are provided, they are adjusted independently:
For instance, (0, -10) is changed to (0, 0) rather than (180, 10).</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapSceneLightsDirection(this.azimuth, this.altitude);</code></pre>

 



</div>
`
}</HTMLBlock>
