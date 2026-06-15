---
title: "Details.withDefaults constructor"
slug: "sdk-for-flutter-explore-search-details-details-withdefaults"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Details.withDefaults.html -->


<div>
<h1>Details.withDefaults constructor</h1></div>

Details.withDefaults(<ol class="parameter-list"> <li>List&lt;<a href="sdk-for-flutter-explore-search-contact-class">Contact</a>&gt; contacts, </li>
<li>List&lt;<a href="sdk-for-flutter-explore-search-openinghours-class">OpeningHours</a>&gt; openingHours, </li>
<li>List&lt;<a href="sdk-for-flutter-explore-search-placecategory-class">PlaceCategory</a>&gt; categories, </li>
<li>List&lt;<a href="sdk-for-flutter-explore-search-webimage-class">WebImage</a>&gt; images, </li>
<li>List&lt;<a href="sdk-for-flutter-explore-search-webeditorial-class">WebEditorial</a>&gt; editorials, </li>
<li>List&lt;<a href="sdk-for-flutter-explore-search-webrating-class">WebRating</a>&gt; ratings, </li>
<li>List&lt;<a href="sdk-for-flutter-explore-search-supplierreference-class">SupplierReference</a>&gt; references, </li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>contacts</code> The list of contact information of the place.</li>
</ul>
<p><strong>Note:</strong> Not available as part of <a href="sdk-for-flutter-explore-search-suggestion-class">Suggestion</a> results.</p>
<ul>
<li><code>openingHours</code> The list of opening hours information of the place.</li>
</ul>
<p><strong>Note:</strong> Not available as part of <a href="sdk-for-flutter-explore-search-suggestion-class">Suggestion</a> results.</p>
<ul>
<li><code>categories</code> The list of categories assigned to this place.</li>
<li><code>images</code> The list of images associated with the place.
The images are provided by external suppliers and are only available to users with
valid contracts with said suppliers. If the user has no such contracts, the list is empty.</li>
</ul>
<p><strong>Note:</strong> Not available as part of <a href="sdk-for-flutter-explore-search-suggestion-class">Suggestion</a> results.</p>
<ul>
<li><code>editorials</code> The list of editorials associated with the place.
The editorials are provided by external suppliers and are only available to users with
valid contracts with said suppliers. If the user has no such contracts, the list is empty.</li>
</ul>
<p><strong>Note:</strong> Not available as part of <a href="sdk-for-flutter-explore-search-suggestion-class">Suggestion</a> results.</p>
<ul>
<li><code>ratings</code> The list of ratings associated with the place.
The ratings are provided by external suppliers and are only available to users with
valid contracts with said suppliers. If the user has no such contracts, the list is empty.</li>
</ul>
<p><strong>Note:</strong> Not available as part of <a href="sdk-for-flutter-explore-search-suggestion-class">Suggestion</a> results.</p>
<ul>
<li><code>references</code> The list of supplier references to this place.
The references are provided by external suppliers and are only available to users with
valid contracts with said suppliers. If the user has no such contracts, the list is empty.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Details.withDefaults(this.contacts, this.openingHours, this.categories, this.images, this.editorials, this.ratings, this.references)
    : evChargingPool = null, truckAmenities = null, fuelStation = null, foodTypes = [], payment = null, evChargingLocation = null;</code></pre>

 



</div>
`
}</HTMLBlock>
