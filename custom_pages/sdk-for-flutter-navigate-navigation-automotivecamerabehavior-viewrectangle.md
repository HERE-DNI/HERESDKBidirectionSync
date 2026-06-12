---
title: "viewRectangle property"
slug: "sdk-for-flutter-navigate-navigation-automotivecamerabehavior-viewrectangle"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- viewRectangle.html -->


<div>
<h1>viewRectangle property</h1></div>
<section id="getter">

<a href="/sdk-for-flutter-navigate-core-rectangle2d-class">Rectangle2D</a>?
viewRectangle


<p>The view rectangle for camera updates.
Defines a sub-space of the screen that the behavior should consider
for camera updates. This property is forwarded to both the tracking and area cameras,
ensuring consistent viewport constraints across all camera modes.
If not set, it uses the viewport bounds of the underlying map view.
Gets the current view rectangle, if it's set.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Rectangle2D? get viewRectangle;</code></pre>

</section>
<section id="setter">

void
viewRectangle=(<a href="/sdk-for-flutter-navigate-core-rectangle2d-class">Rectangle2D</a>? value)


<p>The view rectangle for camera updates.
Defines a sub-space of the screen that the behavior should consider
for camera updates. This property is forwarded to both the tracking and area cameras,
ensuring consistent viewport constraints across all camera modes.
If not set, it uses the viewport bounds of the underlying map view.
Sets a view rectangle for both child cameras.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set viewRectangle(Rectangle2D? value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
