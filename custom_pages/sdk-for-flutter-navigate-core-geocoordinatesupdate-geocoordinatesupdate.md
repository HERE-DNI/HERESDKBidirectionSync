---
title: "GeoCoordinatesUpdate constructor"
slug: "sdk-for-flutter-navigate-core-geocoordinatesupdate-geocoordinatesupdate"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- GeoCoordinatesUpdate.html -->


<div>
<h1>GeoCoordinatesUpdate constructor</h1></div>

GeoCoordinatesUpdate(<ol class="parameter-list single-line"> <li>double? latitude, </li>
<li>double? longitude</li>
</ol>)
    

<p>Constructs a GeoCoordinatesUpdate from the provided latitude and
longitude values.</p>
<p>Corrects values of latitude and longitude if they exceed the ranges.</p>
<ul>
<li>
<p><code>latitude</code> Latitude in degrees. Positive value means Northern hemisphere.
If the value is out of range of [-90.0, 90.0] it's clamped to that range.
NaN value is converted to <code>null</code>.</p>
</li>
<li>
<p><code>longitude</code> Longitude in degrees. Positive value means Eastern hemisphere.
If the value is out of range of [-180.0, 180.0] it's replaced with a value
within the range, representing effectively the same meridian.
NaN value is converted to <code>null</code>.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory GeoCoordinatesUpdate(double? latitude, double? longitude) =&gt; $prototype.$init(latitude, longitude);</code></pre>

 



</div>
`
}</HTMLBlock>
