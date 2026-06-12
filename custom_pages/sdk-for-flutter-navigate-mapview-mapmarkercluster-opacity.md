---
title: "opacity property"
slug: "sdk-for-flutter-navigate-mapview-mapmarkercluster-opacity"
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


<p>Opacity is the factor which is applied to the alpha channel of the image used for marker cluster.
Gets the current opacity of the marker cluster image.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double get opacity;</code></pre>

</section>
<section id="setter">

void
opacity=(double value)


<p>Opacity is the factor which is applied to the alpha channel of the image used for marker cluster.
Sets the opacity of the marker cluster image.</p>
<p>Provided value is clamped in range [0.0, 1.0]. Default value is 1.0 which means marker cluster
is displayed with the default opacity of the image.</p>
<p>Marker clusters with opacity value set to 0.0 are still on the map and are considered for picking.</p>
<p>Markers part of cluster will use their respective opacity when not displayed as a cluster icon.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set opacity(double value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
