---
title: "opacity property"
slug: "sdk-for-flutter-navigate-mapview-mapmarker-opacity"
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


<p>Opacity, the factor applied to the alpha channel of the marker image.
Gets the current opacity of the marker image. Value is in the range of [0.0, 1.0].
Default value is 1.0.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double get opacity;</code></pre>

</section>
<section id="setter">

void
opacity=(double value)


<p>Opacity, the factor applied to the alpha channel of the marker image.
Sets the opacity of the marker image.</p>
<p>Provided value is clamped to the range of [0.0, 1.0]. Default value is 1.0,
which means marker is displayed with the default opacity of the image.</p>
<p>Markers with opacity value set to 0.0 are still on the map and are considered for picking.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set opacity(double value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
