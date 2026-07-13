---
title: "SearchInterface class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-searchinterface-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/SearchInterface-class-sidebar.html">

<div>

# <span class="kind-class">SearchInterface</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Provides the abstract class for the online and offline search engines.

</div>

<div class="section">

Implementers  
- <a href="sdk-for-flutter-explore-search-searchengine-class">SearchEngine</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-search-searchinterface-searchinterface">SearchInterface</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-searchByTextLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> <span class="parameter-name">searchByTextLambda</span>(<span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-textquery-class">TextQuery</a></span>, </span><span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span>, </span><span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchcallback">SearchCallback</a></span> <span class="parameter-name"></span></span>), </span><span id="sdk-for-flutter-explore-param-searchByAddressLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> <span class="parameter-name">searchByAddressLambda</span>(<span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-addressquery-class">AddressQuery</a></span>, </span><span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span>, </span><span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchcallback">SearchCallback</a></span> <span class="parameter-name"></span></span>), </span><span id="sdk-for-flutter-explore-param-searchByCategoryLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> <span class="parameter-name">searchByCategoryLambda</span>(<span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-categoryquery-class">CategoryQuery</a></span>, </span><span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span>, </span><span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchcallback">SearchCallback</a></span> <span class="parameter-name"></span></span>), </span><span id="sdk-for-flutter-explore-param-searchByCoordinatesLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> <span class="parameter-name">searchByCoordinatesLambda</span>(<span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span>, </span><span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span>, </span><span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchcallback">SearchCallback</a></span> <span class="parameter-name"></span></span>), </span><span id="sdk-for-flutter-explore-param-searchByPlaceIdLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> <span class="parameter-name">searchByPlaceIdLambda</span>(<span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-placeidquery-class">PlaceIdQuery</a></span>, </span><span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-languagecode">LanguageCode</a>?</span>, </span><span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-placeidsearchcallback">PlaceIdSearchCallback</a></span> <span class="parameter-name"></span></span>), </span><span id="sdk-for-flutter-explore-param-searchByPickedPlaceLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> <span class="parameter-name">searchByPickedPlaceLambda</span>(<span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-pickedplace-class">PickedPlace</a></span>, </span><span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-languagecode">LanguageCode</a>?</span>, </span><span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-placeidsearchcallback">PlaceIdSearchCallback</a></span> <span class="parameter-name"></span></span>), </span><span id="sdk-for-flutter-explore-param-suggestByTextLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> <span class="parameter-name">suggestByTextLambda</span>(<span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-textquery-class">TextQuery</a></span>, </span><span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span>, </span><span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-suggestcallback">SuggestCallback</a></span> <span class="parameter-name"></span></span>)</span>)</span>  
Provides the abstract class for the online and offline search engines.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-search-searchinterface-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-searchinterface-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-search-searchinterface-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-searchinterface-searchbyaddress">searchByAddress</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-searchByAddress-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-addressquery-class">AddressQuery</a></span> <span class="parameter-name">query</span>, </span><span id="sdk-for-flutter-explore-searchByAddress-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span><span id="sdk-for-flutter-explore-searchByAddress-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchcallback">SearchCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous address query search for <a href="sdk-for-flutter-explore-search-place-class">Place</a> instances.

<span class="name"><a href="sdk-for-flutter-explore-search-searchinterface-searchbycategory">searchByCategory</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-searchByCategory-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-categoryquery-class">CategoryQuery</a></span> <span class="parameter-name">query</span>, </span><span id="sdk-for-flutter-explore-searchByCategory-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span><span id="sdk-for-flutter-explore-searchByCategory-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchcallback">SearchCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous category search for <a href="sdk-for-flutter-explore-search-place-class">Place</a> instances.

<span class="name"><a href="sdk-for-flutter-explore-search-searchinterface-searchbycoordinates">searchByCoordinates</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-searchByCoordinates-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span>, </span><span id="sdk-for-flutter-explore-searchByCoordinates-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span><span id="sdk-for-flutter-explore-searchByCoordinates-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchcallback">SearchCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous search for <a href="sdk-for-flutter-explore-search-place-class">Place</a> instances based on the given geographic coordinates.

<span class="name"><a href="sdk-for-flutter-explore-search-searchinterface-searchbypickedplace">searchByPickedPlace</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-searchByPickedPlace-param-pickedPlace" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-pickedplace-class">PickedPlace</a></span> <span class="parameter-name">pickedPlace</span>, </span><span id="sdk-for-flutter-explore-searchByPickedPlace-param-languageCode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-languagecode">LanguageCode</a>?</span> <span class="parameter-name">languageCode</span>, </span><span id="sdk-for-flutter-explore-searchByPickedPlace-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-placeidsearchcallback">PlaceIdSearchCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous search for a <a href="sdk-for-flutter-explore-search-place-class">Place</a> based on the content found in <a href="sdk-for-flutter-explore-core-pickedplace-class">PickedPlace</a>.

<span class="name"><a href="sdk-for-flutter-explore-search-searchinterface-searchbyplaceid">searchByPlaceId</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-searchByPlaceId-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-placeidquery-class">PlaceIdQuery</a></span> <span class="parameter-name">query</span>, </span><span id="sdk-for-flutter-explore-searchByPlaceId-param-languageCode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-languagecode">LanguageCode</a>?</span> <span class="parameter-name">languageCode</span>, </span><span id="sdk-for-flutter-explore-searchByPlaceId-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-placeidsearchcallback">PlaceIdSearchCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous search for a <a href="sdk-for-flutter-explore-search-place-class">Place</a> based on its ID and <a href="sdk-for-flutter-explore-core-languagecode">LanguageCode</a>.

<span class="name"><a href="sdk-for-flutter-explore-search-searchinterface-searchbytext">searchByText</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-searchByText-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-textquery-class">TextQuery</a></span> <span class="parameter-name">query</span>, </span><span id="sdk-for-flutter-explore-searchByText-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span><span id="sdk-for-flutter-explore-searchByText-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchcallback">SearchCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous text query search for <a href="sdk-for-flutter-explore-search-place-class">Place</a> instances within a given <a href="sdk-for-flutter-explore-search-textqueryarea-class">TextQueryArea</a>.

<span class="name"><a href="sdk-for-flutter-explore-search-searchinterface-suggestbytext">suggestByText</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-suggestByText-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-textquery-class">TextQuery</a></span> <span class="parameter-name">query</span>, </span><span id="sdk-for-flutter-explore-suggestByText-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span><span id="sdk-for-flutter-explore-suggestByText-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-suggestcallback">SuggestCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous request to suggest places for text queries and returns suggestions sorted by relevance.

<span class="name"><a href="sdk-for-flutter-explore-search-searchinterface-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-search-searchinterface-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

