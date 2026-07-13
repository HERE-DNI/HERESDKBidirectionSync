---
title: "SearchEngine class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-searchengine-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/SearchEngine-class-sidebar.html">

<div>

# <span class="kind-class">SearchEngine</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

The SearchEngine API unlocks the search, geocoding and suggesting capabilities of HERE services to provide developers with unmatched flexibility to create differentiating location-enabled applications.

It enables to search for HERE points of interests, forward and reverse geocode addresses and geographic coordinates from the HERE map and search for suggested addresses or place candidates based on incomplete or misspelled queries.

It also allows to search along a given <a href="sdk-for-flutter-explore-core-geopolyline-class">GeoPolyline</a> set inside a <a href="sdk-for-flutter-explore-core-geocorridor-class">GeoCorridor</a> as part of a <a href="sdk-for-flutter-explore-search-textquery-class">TextQuery</a>.

The SearchEngine API requires an online connection to execute the requests.

**Note:** All methods are provided in two flavors. One uses a <a href="sdk-for-flutter-explore-search-searchcallback">SearchCallback</a> and the other uses a <a href="sdk-for-flutter-explore-search-searchcallbackextended">SearchCallbackExtended</a>: The later adds a `ResponseDetails` result type that provides the `requestId` of a search request and a `correlationId` to identify multiple, related queries. This may be useful for debug purposes.

</div>

<div class="section">

Implemented types  
- <a href="sdk-for-flutter-explore-search-searchinterface-class">SearchInterface</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-search-searchengine-searchengine">SearchEngine</a></span><span class="signature">()</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-searchengine-searchengine-withsdkengine">SearchEngine.withSdkEngine</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withSdkEngine-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span></span>)</span>  
Creates a new instance of this class.

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

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-searchengine-searchbyaddressextended">searchByAddressExtended</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-searchByAddressExtended-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-addressquery-class">AddressQuery</a></span> <span class="parameter-name">query</span>, </span><span id="sdk-for-flutter-explore-searchByAddressExtended-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span><span id="sdk-for-flutter-explore-searchByAddressExtended-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchcallbackextended">SearchCallbackExtended</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous request to search for places based on a given address.

<span class="name"><a href="sdk-for-flutter-explore-search-searchinterface-searchbycategory">searchByCategory</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-searchByCategory-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-categoryquery-class">CategoryQuery</a></span> <span class="parameter-name">query</span>, </span><span id="sdk-for-flutter-explore-searchByCategory-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span><span id="sdk-for-flutter-explore-searchByCategory-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchcallback">SearchCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous category search for <a href="sdk-for-flutter-explore-search-place-class">Place</a> instances.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-searchengine-searchbycategoryextended">searchByCategoryExtended</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-searchByCategoryExtended-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-categoryquery-class">CategoryQuery</a></span> <span class="parameter-name">query</span>, </span><span id="sdk-for-flutter-explore-searchByCategoryExtended-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span><span id="sdk-for-flutter-explore-searchByCategoryExtended-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchcallbackextended">SearchCallbackExtended</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous request to do a category search for <a href="sdk-for-flutter-explore-search-place-class">Place</a> instances.

<span class="name"><a href="sdk-for-flutter-explore-search-searchinterface-searchbycoordinates">searchByCoordinates</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-searchByCoordinates-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span>, </span><span id="sdk-for-flutter-explore-searchByCoordinates-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span><span id="sdk-for-flutter-explore-searchByCoordinates-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchcallback">SearchCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous search for <a href="sdk-for-flutter-explore-search-place-class">Place</a> instances based on the given geographic coordinates.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-searchengine-searchbycoordinatesextended">searchByCoordinatesExtended</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-searchByCoordinatesExtended-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span>, </span><span id="sdk-for-flutter-explore-searchByCoordinatesExtended-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span><span id="sdk-for-flutter-explore-searchByCoordinatesExtended-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchcallbackextended">SearchCallbackExtended</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous request to search for places based on given geographic coordinates.

<span class="name"><a href="sdk-for-flutter-explore-search-searchengine-searchbycoordinateswithradius">searchByCoordinatesWithRadius</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-searchByCoordinatesWithRadius-param-circle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocircle-class">GeoCircle</a></span> <span class="parameter-name">circle</span>, </span><span id="sdk-for-flutter-explore-searchByCoordinatesWithRadius-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span><span id="sdk-for-flutter-explore-searchByCoordinatesWithRadius-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchcallback">SearchCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous request to search for places based on given circular spatial filter.

<span class="name"><a href="sdk-for-flutter-explore-search-searchengine-searchbycoordinateswithradiusextended">searchByCoordinatesWithRadiusExtended</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-searchByCoordinatesWithRadiusExtended-param-circle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocircle-class">GeoCircle</a></span> <span class="parameter-name">circle</span>, </span><span id="sdk-for-flutter-explore-searchByCoordinatesWithRadiusExtended-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span><span id="sdk-for-flutter-explore-searchByCoordinatesWithRadiusExtended-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchcallbackextended">SearchCallbackExtended</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous request to search for places based on given circular spatial filter.

<span class="name"><a href="sdk-for-flutter-explore-search-searchinterface-searchbypickedplace">searchByPickedPlace</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-searchByPickedPlace-param-pickedPlace" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-pickedplace-class">PickedPlace</a></span> <span class="parameter-name">pickedPlace</span>, </span><span id="sdk-for-flutter-explore-searchByPickedPlace-param-languageCode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-languagecode">LanguageCode</a>?</span> <span class="parameter-name">languageCode</span>, </span><span id="sdk-for-flutter-explore-searchByPickedPlace-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-placeidsearchcallback">PlaceIdSearchCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous search for a <a href="sdk-for-flutter-explore-search-place-class">Place</a> based on the content found in <a href="sdk-for-flutter-explore-core-pickedplace-class">PickedPlace</a>.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-searchinterface-searchbyplaceid">searchByPlaceId</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-searchByPlaceId-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-placeidquery-class">PlaceIdQuery</a></span> <span class="parameter-name">query</span>, </span><span id="sdk-for-flutter-explore-searchByPlaceId-param-languageCode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-languagecode">LanguageCode</a>?</span> <span class="parameter-name">languageCode</span>, </span><span id="sdk-for-flutter-explore-searchByPlaceId-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-placeidsearchcallback">PlaceIdSearchCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous search for a <a href="sdk-for-flutter-explore-search-place-class">Place</a> based on its ID and <a href="sdk-for-flutter-explore-core-languagecode">LanguageCode</a>.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-searchengine-searchbyplaceidwithlanguagecodeextended">searchByPlaceIdWithLanguageCodeExtended</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-searchByPlaceIdWithLanguageCodeExtended-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-placeidquery-class">PlaceIdQuery</a></span> <span class="parameter-name">query</span>, </span><span id="sdk-for-flutter-explore-searchByPlaceIdWithLanguageCodeExtended-param-languageCode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-languagecode">LanguageCode</a>?</span> <span class="parameter-name">languageCode</span>, </span><span id="sdk-for-flutter-explore-searchByPlaceIdWithLanguageCodeExtended-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-placeidsearchcallbackextended">PlaceIdSearchCallbackExtended</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous request to search for a <a href="sdk-for-flutter-explore-search-place-class">Place</a> based on its ID and <a href="sdk-for-flutter-explore-core-languagecode">LanguageCode</a>.

<span class="name"><a href="sdk-for-flutter-explore-search-searchinterface-searchbytext">searchByText</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-searchByText-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-textquery-class">TextQuery</a></span> <span class="parameter-name">query</span>, </span><span id="sdk-for-flutter-explore-searchByText-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span><span id="sdk-for-flutter-explore-searchByText-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchcallback">SearchCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous text query search for <a href="sdk-for-flutter-explore-search-place-class">Place</a> instances within a given <a href="sdk-for-flutter-explore-search-textqueryarea-class">TextQueryArea</a>.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-searchengine-searchbytextextended">searchByTextExtended</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-searchByTextExtended-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-textquery-class">TextQuery</a></span> <span class="parameter-name">query</span>, </span><span id="sdk-for-flutter-explore-searchByTextExtended-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span><span id="sdk-for-flutter-explore-searchByTextExtended-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchcallbackextended">SearchCallbackExtended</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous request to do a text query search for <a href="sdk-for-flutter-explore-search-place-class">Place</a> instances.

<span class="name"><a href="sdk-for-flutter-explore-search-searchengine-sendrequest">sendRequest</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-sendRequest-param-href" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">href</span>, </span><span id="sdk-for-flutter-explore-sendRequest-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchcallback">SearchCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous request by using the given href.

<span class="name"><a href="sdk-for-flutter-explore-search-searchengine-sendrequestextended">sendRequestExtended</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-sendRequestExtended-param-href" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">href</span>, </span><span id="sdk-for-flutter-explore-sendRequestExtended-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchcallbackextended">SearchCallbackExtended</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous request by using the given href.

<span class="name"><a href="sdk-for-flutter-explore-search-searchengine-setcustomoption">setCustomOption</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-setCustomOption-param-name" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">name</span>, </span><span id="sdk-for-flutter-explore-setCustomOption-param-value" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">value</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-search-searcherror">SearchError</a>?</span> </span>  
Sets a custom option for search backend queries.

<span class="name"><a href="sdk-for-flutter-explore-search-searchengine-setevinterface">setEVInterface</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-setEVInterface-param-evcpInterface" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-evsearchinterface-class">EVSearchInterface</a></span> <span class="parameter-name">evcpInterface</span></span>) <span class="returntype parameter">→ void</span> </span>  
Sets the EV interface through which search will interact with EVCP3.

<span class="name"><a href="sdk-for-flutter-explore-search-searchinterface-suggestbytext">suggestByText</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-suggestByText-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-textquery-class">TextQuery</a></span> <span class="parameter-name">query</span>, </span><span id="sdk-for-flutter-explore-suggestByText-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span><span id="sdk-for-flutter-explore-suggestByText-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-suggestcallback">SuggestCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous request to suggest places for text queries and returns suggestions sorted by relevance.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-searchengine-suggestextended">suggestExtended</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-suggestExtended-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-textquery-class">TextQuery</a></span> <span class="parameter-name">query</span>, </span><span id="sdk-for-flutter-explore-suggestExtended-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span><span id="sdk-for-flutter-explore-suggestExtended-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-suggestcallbackextended">SuggestCallbackExtended</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous request to suggest places for text queries and returns candidate suggestions sorted by relevance.

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

