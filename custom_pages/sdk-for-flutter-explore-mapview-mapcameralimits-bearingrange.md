---
title: "bearingRange property"
slug: "sdk-for-flutter-explore-mapview-mapcameralimits-bearingrange"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- bearingRange.html -->


<div>
<h1>bearingRange property</h1></div>
<section id="getter">

<a href="sdk-for-flutter-explore-core-anglerange-class">AngleRange</a>
bearingRange


<p>The bearing range within which the camera can be rotated.
Gets the currently set bearing range.</p>
<p>This may not be active now if no rendering loop has been executed since
the last call to set the range.</p>
<p>By default, range for a full circle is set during initialization.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">AngleRange get bearingRange;</code></pre>

</section>
<section id="setter">

void
bearingRange=(<a href="sdk-for-flutter-explore-core-anglerange-class">AngleRange</a> value)


<p>The bearing range within which the camera can be rotated.
Sets a new bearing range.</p>
<p>It will be updated during the next rendering loop.
All previously set bearing ranges are cleared and the new bearing range is applied for all zoom values.</p>
<p>If the current camera bearing exceeds the limit range, it will immediately be set to minimum or
maximum, depending on which is closest.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set bearingRange(AngleRange value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
