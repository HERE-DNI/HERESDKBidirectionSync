---
title: "isOverlapAllowed property"
slug: "sdk-for-flutter-explore-mapview-mapmarker-isoverlapallowed"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- isOverlapAllowed.html -->


<div>
<h1>isOverlapAllowed property</h1></div>
<section id="getter">

bool
isOverlapAllowed


<p>Determines whether or not the marker can overlap other markers.
Returns <code>true</code> if the marker allows overlap with other markers, <code>false</code> otherwise.
Defaults to <code>true</code>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool get isOverlapAllowed;</code></pre>

</section>
<section id="setter">

void
isOverlapAllowed=(bool value)


<p>Determines whether or not the marker can overlap other markers.
Sets whether the marker is allowed to overlap with other markers.</p>
<p>If <code>false</code>, it will disappear the moment it overlaps another marker that has
a higher visibility priority. A marker that allows overlap will always be drawn.
Among markers that don't allow overlap, the one with the highest draw order has
priority. Marker that is hidden due to overlapping with other markers is not pickable.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set isOverlapAllowed(bool value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
