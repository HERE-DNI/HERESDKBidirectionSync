---
title: "rotateBy static method"
slug: "sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-rotateby"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- rotateBy.html -->


<div>
<h1>rotateBy static method</h1></div>

<a href="/sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a>
rotateBy(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-core-geoorientationupdate-class">GeoOrientationUpdate</a> delta</li>
</ol>)

      

    

<p>Creates an update to change map camera orientation by specified geodetic orientation delta.</p>
<p>Orientation elements that are not valid will be excluded from the update.
Resulting bearing values are wrapped around degrees range [0, 360].
Resulting tilt values are clamped inside degrees range [0, 180].
Resulting roll values are wrapped around degrees range [-180, 180].</p>
<ul>
<li><code>delta</code> Geodetic orientation delta update.</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraUpdate rotateBy(GeoOrientationUpdate delta) =&gt; $prototype.rotateBy(delta);</code></pre>

 



</div>
`
}</HTMLBlock>
