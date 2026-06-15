---
title: "fuelTypes property"
slug: "sdk-for-flutter-navigate-search-placefilter-fueltypes"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- fuelTypes.html -->


<div>
<h1>fuelTypes property</h1></div>

        
        List&lt;<a href="sdk-for-flutter-navigate-transport-fueltype">FuelType</a>&gt;
fuelTypes
<div class="features">getter/setter pair</div>


<p>The list of <a href="sdk-for-flutter-navigate-transport-fueltype">FuelType</a> elements that should be used to find only
the <a href="sdk-for-flutter-navigate-search-fuelstation-class">FuelStation</a> search results that support all of them.
This filter is available to use with the <code>SearchEngine</code> and
<code>OfflineSearchEngine</code> (only available for the Navigate license), however <code>OfflineSearchEngine</code>
supports it only for <code>searchByText</code> and <code>searchByCategory</code> with allowed fuel types <code>DIESEL</code>, <code>LPG</code>,
<code>BIO_DIESEL</code>, <code>CNG</code>, <code>DIESEL_WITH_ADDITIVES</code>, <code>E10</code>, <code>E85</code>, <code>ETHANOL</code>, <code>ETHANOL_WITH_ADDITIVES</code>,
<code>GASOLINE</code>, <code>HYDROGEN</code>, <code>LNG</code>, <code>MIDGRADE</code>, <code>PREMIUM</code> and <code>REGULAR</code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;FuelType&gt; fuelTypes;</code></pre>

 



</div>
`
}</HTMLBlock>
