---
title: "PickedPlace constructor"
slug: "sdk-for-flutter-explore-core-pickedplace-pickedplace"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PickedPlace.html -->


<div>
<h1>PickedPlace constructor</h1></div>

PickedPlace(<ol class="parameter-list single-line"> <li>String name, </li>
<li><a href="/sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a> coordinates, </li>
<li>String placeCategoryId</li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>name</code> The name of the POI localized in the currently selected map language.</li>
<li><code>coordinates</code> The geographic coordinates of the POI.</li>
<li><code>placeCategoryId</code> The place category ID of the POI.
This is the same String value as <code>PlaceCategory.id</code> that can be obtained from the
<code>SearchEngine</code> and the <code>OfflineSearchEngine</code>. Note that not all editions include the
<code>OfflineSearchEngine</code>.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">PickedPlace(this.name, this.coordinates, this.placeCategoryId);</code></pre>

 



</div>
`
}</HTMLBlock>
