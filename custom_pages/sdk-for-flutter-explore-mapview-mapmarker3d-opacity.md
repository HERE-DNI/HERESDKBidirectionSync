---
title: "opacity property"
slug: "sdk-for-flutter-explore-mapview-mapmarker3d-opacity"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- opacity.html -->


<div>
<h1>opacity property</h1></div>
<section id="getter">

double
opacity


<p>The opacity factor adjusting the opacity of a 3D marker.
The factor is applied to the alpha channel of the resulting texture of the marker.
Default value is 1.0 meaning marker is displayed with the default opacity of the texture image or the
specified fill color specified
in <a href="/sdk-for-flutter-explore-mapview-mapmarker3dmodel-class">MapMarker3DModel</a>.
Returns an opacity factor which specifies the translucency of a 3D map marker.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double get opacity;</code></pre>

</section>
<section id="setter">

void
opacity=(double value)


<p>The opacity factor adjusting the opacity of a 3D marker.
The factor is applied to the alpha channel of the resulting texture of the marker.
Default value is 1.0 meaning marker is displayed with the default opacity of the texture image or the
specified fill color specified
in <a href="/sdk-for-flutter-explore-mapview-mapmarker3dmodel-class">MapMarker3DModel</a>.
Sets an opacity factor which specifies the translucency of a 3D map marker.</p>
<p>Provided value is clamped to the [0.0, 1.0] range.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set opacity(double value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
