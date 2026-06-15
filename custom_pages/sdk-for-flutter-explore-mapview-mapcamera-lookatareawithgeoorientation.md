---
title: "lookAtAreaWithGeoOrientation abstract method"
slug: "sdk-for-flutter-explore-mapview-mapcamera-lookatareawithgeoorientation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtAreaWithGeoOrientation.html -->


<div>
<h1>lookAtAreaWithGeoOrientation abstract method</h1></div>

void
lookAtAreaWithGeoOrientation(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a> target, </li>
<li><a href="sdk-for-flutter-explore-core-geoorientationupdate-class">GeoOrientationUpdate</a> orientation</li>
</ol>)

      

    

<p>Makes the camera look at the specified geodetic area.</p>
<p>The supplied orientation is the orientation of the camera looking
at the target, so the resulting camera state will have the
same orientation as the one supplied to this method.</p>
<p>The altitude of the target points is ignored.</p>
<ul>
<li>
<p><code>target</code> Geodetic area at which the camera will point</p>
</li>
<li>
<p><code>orientation</code> Desired orientation of the camera</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void lookAtAreaWithGeoOrientation(GeoBox target, GeoOrientationUpdate orientation);</code></pre>

 



</div>
`
}</HTMLBlock>
