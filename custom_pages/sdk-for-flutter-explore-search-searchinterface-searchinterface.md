---
title: "SearchInterface constructor"
slug: "sdk-for-flutter-explore-search-searchinterface-searchinterface"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SearchInterface.html -->


<div>
<h1>SearchInterface constructor</h1></div>

SearchInterface(<ol class="parameter-list"> <li><a href="/sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a> searchByTextLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-search-textquery-class">TextQuery</a>, </li>
<li><a href="/sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a>, </li>
<li><a href="/sdk-for-flutter-explore-search-searchcallback">SearchCallback</a> </li>
</ol>), </li>
<li><a href="/sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a> searchByAddressLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-search-addressquery-class">AddressQuery</a>, </li>
<li><a href="/sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a>, </li>
<li><a href="/sdk-for-flutter-explore-search-searchcallback">SearchCallback</a> </li>
</ol>), </li>
<li><a href="/sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a> searchByCategoryLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-search-categoryquery-class">CategoryQuery</a>, </li>
<li><a href="/sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a>, </li>
<li><a href="/sdk-for-flutter-explore-search-searchcallback">SearchCallback</a> </li>
</ol>), </li>
<li><a href="/sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a> searchByCoordinatesLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a>, </li>
<li><a href="/sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a>, </li>
<li><a href="/sdk-for-flutter-explore-search-searchcallback">SearchCallback</a> </li>
</ol>), </li>
<li><a href="/sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a> searchByPlaceIdLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-search-placeidquery-class">PlaceIdQuery</a>, </li>
<li><a href="/sdk-for-flutter-explore-core-languagecode">LanguageCode</a>?, </li>
<li><a href="/sdk-for-flutter-explore-search-placeidsearchcallback">PlaceIdSearchCallback</a> </li>
</ol>), </li>
<li><a href="/sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a> searchByPickedPlaceLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-core-pickedplace-class">PickedPlace</a>, </li>
<li><a href="/sdk-for-flutter-explore-core-languagecode">LanguageCode</a>?, </li>
<li><a href="/sdk-for-flutter-explore-search-placeidsearchcallback">PlaceIdSearchCallback</a> </li>
</ol>), </li>
<li><a href="/sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a> suggestByTextLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-search-textquery-class">TextQuery</a>, </li>
<li><a href="/sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a>, </li>
<li><a href="/sdk-for-flutter-explore-search-suggestcallback">SuggestCallback</a> </li>
</ol>), </li>
</ol>)
    

<p>Provides the abstract class for the online and offline
search engines.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory SearchInterface(
  TaskHandle Function(TextQuery, SearchOptions, SearchCallback) searchByTextLambda,
  TaskHandle Function(AddressQuery, SearchOptions, SearchCallback) searchByAddressLambda,
  TaskHandle Function(CategoryQuery, SearchOptions, SearchCallback) searchByCategoryLambda,
  TaskHandle Function(GeoCoordinates, SearchOptions, SearchCallback) searchByCoordinatesLambda,
  TaskHandle Function(PlaceIdQuery, LanguageCode?, PlaceIdSearchCallback) searchByPlaceIdLambda,
  TaskHandle Function(PickedPlace, LanguageCode?, PlaceIdSearchCallback) searchByPickedPlaceLambda,
  TaskHandle Function(TextQuery, SearchOptions, SuggestCallback) suggestByTextLambda,

) =&gt; SearchInterface$Lambdas(
  searchByTextLambda,
  searchByAddressLambda,
  searchByCategoryLambda,
  searchByCoordinatesLambda,
  searchByPlaceIdLambda,
  searchByPickedPlaceLambda,
  suggestByTextLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
