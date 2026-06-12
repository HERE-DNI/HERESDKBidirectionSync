---
title: "drawOrder property"
slug: "sdk-for-flutter-explore-mapview-mapmarker-draworder"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- drawOrder.html -->


<div>
<h1>drawOrder property</h1></div>
<section id="getter">

int
drawOrder


<p>The draw order of this marker relative to other markers.
Gets draw order of this marker relative to other markers. The default value is 0.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int get drawOrder;</code></pre>

</section>
<section id="setter">

void
drawOrder=(int value)


<p>The draw order of this marker relative to other markers.
Sets draw order of this marker relative to other markers.</p>
<p>Markers with higher draw order value are drawn on top of markers with lower draw order.
In case multiple markers have the same draw order value
then the order in which they were added to the scene matters. Last added marker is drawn on top.</p>
<p>Allowed range is [0, 1023]. Values outside this range will be clamped. The default value is 0.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set drawOrder(int value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
