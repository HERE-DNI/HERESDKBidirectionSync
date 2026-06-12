---
title: "MapMarker3D constructor"
slug: "sdk-for-flutter-navigate-mapview-mapmarker3d-mapmarker3d"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMarker3D.html -->


<div>
<h1>MapMarker3D constructor</h1></div>

MapMarker3D(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a> at, </li>
<li><a href="/sdk-for-flutter-navigate-mapview-mapmarker3dmodel-class">MapMarker3DModel</a> model</li>
</ol>)
    

<p>Creates an instance of a 3D marker.</p>
<p>The origin of the 3D model's local coordinate system is placed at the specified
geographical coordinates.</p>
<p>Altitude component of the coordinates, if set, controls 3D marker's elevation
above ground. If not set, the 3D marker is placed at ground level.</p>
<ul>
<li>
<p><code>at</code> The geographical coordinates where the 3D marker is placed corresponding to origin of the
3D model's local coordinate system.</p>
</li>
<li>
<p><code>model</code> The 3D model used to draw 3D marker.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapMarker3D(GeoCoordinates at, MapMarker3DModel model) =&gt; $prototype.$init(at, model);</code></pre>

 



</div>
`
}</HTMLBlock>
