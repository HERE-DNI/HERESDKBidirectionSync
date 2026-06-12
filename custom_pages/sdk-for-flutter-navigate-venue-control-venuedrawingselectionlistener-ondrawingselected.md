---
title: "onDrawingSelected abstract method"
slug: "sdk-for-flutter-navigate-venue-control-venuedrawingselectionlistener-ondrawingselected"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onDrawingSelected.html -->


<div>
<h1>onDrawingSelected abstract method</h1></div>

void
onDrawingSelected(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> venue, </li>
<li><a href="/sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a>? deselectedDrawing, </li>
<li><a href="/sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a> selectedDrawing</li>
</ol>)

      

    

<p>Indicates that new <a href="/sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a> has been selected.</p>
<ul>
<li>
<p><code>venue</code> The <a href="/sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> where a selected drawing was changed.</p>
</li>
<li>
<p><code>deselectedDrawing</code> The previously selected <a href="/sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a> object or <code>null</code>
if there was no selected drawing before.</p>
</li>
<li>
<p><code>selectedDrawing</code> The new selected <a href="/sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a> object.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onDrawingSelected(Venue venue, VenueDrawing? deselectedDrawing, VenueDrawing selectedDrawing);</code></pre>

 



</div>
`
}</HTMLBlock>
