---
title: "selectedLevel property"
slug: "sdk-for-flutter-navigate-venue-control-venue-selectedlevel"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- selectedLevel.html -->


<div>
<h1>selectedLevel property</h1></div>
<section id="getter">

<a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a>
selectedLevel


<p>The selected level.
Only the selected level will be visible as active on the map. All others will be
hidden or displayed without details, depending on a renderer implementation.
If the level doesn't belong to the currently selected drawing, it can not be selected.
Gets the currently selected <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a> from the selected <a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">VenueLevel get selectedLevel;</code></pre>

</section>
<section id="setter">

void
selectedLevel=(<a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a> value)


<p>The selected level.
Only the selected level will be visible as active on the map. All others will be
hidden or displayed without details, depending on a renderer implementation.
If the level doesn't belong to the currently selected drawing, it can not be selected.
Sets the selected <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a> from the currently selected <a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set selectedLevel(VenueLevel value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
