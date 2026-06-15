---
title: "orbitBy static method"
slug: "sdk-for-flutter-explore-mapview-mapcameraupdatefactory-orbitby"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- orbitBy.html -->


<div>
<h1>orbitBy static method</h1></div>

<a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>
orbitBy(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-core-geoorientationupdate-class">GeoOrientationUpdate</a> delta, </li>
<li><a href="sdk-for-flutter-explore-core-point2d-class">Point2D</a> origin</li>
</ol>)

      

    

<p>Creates an update to orbit map camera around a pixel origin by specified geodetic orientation delta.</p>
<p>If the origin cannot be converted to geo coordinates, no update will be applied to the map camera.</p>
<p>Orientation elements that are not valid will be excluded from the update.
Resulting bearing values are wrapped around degrees range [0, 360].
Resulting tilt values are clamped inside degrees range [0, 180].
Resulting roll values are wrapped around degrees range [-180, 180].</p>
<ul>
<li>
<p><code>delta</code> Geodetic orientation delta update.</p>
</li>
<li>
<p><code>origin</code> Screen pixel origin of rotation.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraUpdate orbitBy(GeoOrientationUpdate delta, Point2D origin) =&gt; $prototype.orbitBy(delta, origin);</code></pre>

 



</div>
`
}</HTMLBlock>
