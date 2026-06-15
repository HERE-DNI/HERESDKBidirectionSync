---
title: "progress property"
slug: "sdk-for-flutter-navigate-mapview-mappolyline-progress"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- progress.html -->


<div>
<h1>progress property</h1></div>
<section id="getter">

double
progress


<p>The progress from the polyline's starting point, as a ratio of its total length clamped to
the range [0, 1].
Gets the progress of the polyline, 0 by default.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double get progress;</code></pre>

</section>
<section id="setter">

void
progress=(double value)


<p>The progress from the polyline's starting point, as a ratio of its total length clamped to
the range [0, 1].
Sets the progress of the polyline from its starting point as a ratio of its total length
clamped to the range [0; 1].</p>
<p>As the progress varies, the equivalent part of the
polyline gets covered by the progress color and progress outline color. The rest of the
polyline until its end point retains the line color and outline color along with an
optional dash pattern.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set progress(double value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
