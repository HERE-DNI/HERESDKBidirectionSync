---
title: "onSelectedVenueChanged abstract method"
slug: "sdk-for-flutter-navigate-venue-control-venueselectionlistener-onselectedvenuechanged"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onSelectedVenueChanged.html -->


<div>
<h1>onSelectedVenueChanged abstract method</h1></div>

void
onSelectedVenueChanged(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-venue-control-venue-class">Venue</a>? deselectedVenue, </li>
<li><a href="/sdk-for-flutter-navigate-venue-control-venue-class">Venue</a>? selectedVenue</li>
</ol>)

      

    

<p>Indicates that the current selected <a href="/sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> changed.</p>
<ul>
<li>
<p><code>deselectedVenue</code> The <a href="/sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> that was deselected or <code>null</code>
if there was no selected venue before.</p>
</li>
<li>
<p><code>selectedVenue</code> The <a href="/sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> that was selected or <code>null</code>
if there was no new selected venue.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onSelectedVenueChanged(Venue? deselectedVenue, Venue? selectedVenue);</code></pre>

 



</div>
`
}</HTMLBlock>
