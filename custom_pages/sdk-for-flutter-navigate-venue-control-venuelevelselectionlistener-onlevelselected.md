---
title: "onLevelSelected abstract method"
slug: "sdk-for-flutter-navigate-venue-control-venuelevelselectionlistener-onlevelselected"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onLevelSelected.html -->


<div>
<h1>onLevelSelected abstract method</h1></div>

void
onLevelSelected(<ol class="parameter-list"> <li><a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> venue, </li>
<li><a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a> drawing, </li>
<li><a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a>? deselectedLevel, </li>
<li><a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a> selectedLevel, </li>
</ol>)

      

    

<p>Indicates that the selected <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a> of a venue changed.</p>
<ul>
<li>
<p><code>venue</code> The <a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> where the selected <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a> changed.</p>
</li>
<li>
<p><code>drawing</code> The <a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a> where the selected <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a> changed.</p>
</li>
<li>
<p><code>deselectedLevel</code> The previously selected <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a> or <code>null</code>
if there was no selected level before.</p>
</li>
<li>
<p><code>selectedLevel</code> The new selected <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a>.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onLevelSelected(Venue venue, VenueDrawing drawing, VenueLevel? deselectedLevel, VenueLevel selectedLevel);</code></pre>

 



</div>
`
}</HTMLBlock>
