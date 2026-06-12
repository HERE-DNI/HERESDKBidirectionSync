---
title: "drawOrder property"
slug: "sdk-for-flutter-navigate-mapview-mapimageoverlay-draworder"
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


<p>Draw order of this <code>MapImageOverlay</code>.
Gets draw order of this <code>MapImageOverlay</code>. The default value is 0.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int get drawOrder;</code></pre>

</section>
<section id="setter">

void
drawOrder=(int value)


<p>Draw order of this <code>MapImageOverlay</code>.
Sets draw order of this <code>MapImageOverlay</code>.</p>
<p>Overlays with higher draw order value are drawn on top of overlays with lower draw order.</p>
<p>In case multiple overlays have the same draw order value
then the order in which they were added to the scene matters. Last added overlay is drawn on top.</p>
<p>Allowed range is [0, 1023]. Values outside this range will be clamped.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set drawOrder(int value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
