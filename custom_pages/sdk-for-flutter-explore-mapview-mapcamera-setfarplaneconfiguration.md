---
title: "setFarPlaneConfiguration abstract method"
slug: "sdk-for-flutter-explore-mapview-mapcamera-setfarplaneconfiguration"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setFarPlaneConfiguration.html -->


<div>
<h1>setFarPlaneConfiguration abstract method</h1></div>

void
setFarPlaneConfiguration(<ol class="parameter-list single-line"> <li>Map&lt;double, <a href="sdk-for-flutter-explore-mapview-mapcamerafarplaneconfiguration-class">MapCameraFarPlaneConfiguration</a>&gt; configs</li>
</ol>)

      

    

<p>Sets far plane distance configs per zoom level.</p>
<p>Values are linearly interpolated between provided zoom levels.
For z between z0 and z1:
t = (z - z0) / (z1 - z0)
distanceFactor(z) = lerp(distanceFactor0, distanceFactor1, t)
minDistance(z) = lerp(minDistance0, minDistance1, t)</p>
<p>Effective far plane for the current frame is:
farPlaneInMeters = max(
minDistance(z),
distanceToTargetInMeters * distanceFactor(z)
)</p>
<p>Sample Configuration (balanced quality/performance, tune per zoom level):
14.4  -&gt; FarPlaneConfiguration(1.3)
18.34 -&gt; FarPlaneConfiguration(2.0)
19.60 -&gt; FarPlaneConfiguration(1.3)
minDistanceInMeters remains default in this case.
Passing an empty map clears the per-zoom override and restores the default behavior.
Non-finite zoom levels or values are ignored. Distance factors are clamped to 0.1 to 10.0.
The minimum distance is clamped to a range of [100, 3000] meters.</p>
<ul>
<li><code>configs</code> Per-zoom override mapping from zoom level to distance configuration.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setFarPlaneConfiguration(Map&lt;double, MapCameraFarPlaneConfiguration&gt; configs);</code></pre>

 



</div>
`
}</HTMLBlock>
