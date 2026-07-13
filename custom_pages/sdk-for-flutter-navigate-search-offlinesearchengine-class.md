---
title: "OfflineSearchEngine class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-offlinesearchengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- OfflineSearchEngine-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/OfflineSearchEngine-class-sidebar.html">

<div>

# <span class="kind-class">OfflineSearchEngine</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

The OfflineSearchEngine works without internet and unlocks the search and geocoding capabilities of HERE services to provide developers with unmatched flexibility to create differentiating location-enabled applications.

It provides the same interfaces as the SearchEngine, but the results may slightly differ as the results are taken from already downloaded map data instead of initiating a new request to a HERE backend service. This way the data may be, for example, older compared to the data you may receive when using the SearchEngine. On the other hand, this class provides results faster as no online connection is necessary.

In comparison to the SearchEngine, there are a few limitations:

- The IDs of POIs are different and may differ among different map versions.
- The implementation is different and the resources are limited, so the results can differ.
- OfflineSearchEngine sometimes doesn't return the requested number of results.

Note: You can search only within persistent map data (downloaded via MapDownloader) or existing cached data. However, cached data may be incomplete, which can result in searches returning partial or incomplete information. Therefore, it is recommended to use persistent map data. Make sure that at least <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.offlineSearch</a> is enabled. For EV rich attributes also enable <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.ev</a>, for truck rich attributes also enable <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.truckServiceAttributes</a>, for fuel station rich attributes also enable <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.fuelStationAttributes</a> in <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-layerconfiguration">SDKOptions.layerConfiguration</a>.

</div>

<div class="section">

Implemented types  
- <a href="sdk-for-flutter-navigate-search-searchinterface-class">SearchInterface</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-search-offlinesearchengine-offlinesearchengine">OfflineSearchEngine</a></span><span class="signature">()</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-offlinesearchengine-offlinesearchengine-withsdkengine">OfflineSearchEngine.withSdkEngine</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withSdkEngine-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span></span>)</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-search-searchinterface-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-searchinterface-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-search-offlinesearchengine-attach">attach</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-attach-param-dataSource" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-myplaces-class">MyPlaces</a></span> <span class="parameter-name">dataSource</span>, </span><span id="sdk-for-flutter-navigate-attach-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-threading-ontaskcompleted">OnTaskCompleted</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Attach data source into SearchEngine instance.

<span class="name"><a href="sdk-for-flutter-navigate-search-searchinterface-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-searchinterface-searchbyaddress">searchByAddress</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-searchByAddress-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-addressquery-class">AddressQuery</a></span> <span class="parameter-name">query</span>, </span><span id="sdk-for-flutter-navigate-searchByAddress-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span><span id="sdk-for-flutter-navigate-searchByAddress-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-searchcallback">SearchCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous address query search for <a href="sdk-for-flutter-navigate-search-place-class">Place</a> instances.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-offlinesearchengine-searchbyaddresselements">searchByAddressElements</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-searchByAddressElements-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-structuredquery-class">StructuredQuery</a></span> <span class="parameter-name">query</span>, </span><span id="sdk-for-flutter-navigate-searchByAddressElements-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span><span id="sdk-for-flutter-navigate-searchByAddressElements-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-searchcallback">SearchCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous request to search for places.

<span class="name"><a href="sdk-for-flutter-navigate-search-searchinterface-searchbycategory">searchByCategory</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-searchByCategory-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-categoryquery-class">CategoryQuery</a></span> <span class="parameter-name">query</span>, </span><span id="sdk-for-flutter-navigate-searchByCategory-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span><span id="sdk-for-flutter-navigate-searchByCategory-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-searchcallback">SearchCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous category search for <a href="sdk-for-flutter-navigate-search-place-class">Place</a> instances.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-searchinterface-searchbycoordinates">searchByCoordinates</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-searchByCoordinates-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span>, </span><span id="sdk-for-flutter-navigate-searchByCoordinates-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span><span id="sdk-for-flutter-navigate-searchByCoordinates-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-searchcallback">SearchCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous search for <a href="sdk-for-flutter-navigate-search-place-class">Place</a> instances based on the given geographic coordinates.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-searchinterface-searchbypickedplace">searchByPickedPlace</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-searchByPickedPlace-param-pickedPlace" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-pickedplace-class">PickedPlace</a></span> <span class="parameter-name">pickedPlace</span>, </span><span id="sdk-for-flutter-navigate-searchByPickedPlace-param-languageCode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-languagecode">LanguageCode</a>?</span> <span class="parameter-name">languageCode</span>, </span><span id="sdk-for-flutter-navigate-searchByPickedPlace-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-placeidsearchcallback">PlaceIdSearchCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous search for a <a href="sdk-for-flutter-navigate-search-place-class">Place</a> based on the content found in <a href="sdk-for-flutter-navigate-core-pickedplace-class">PickedPlace</a>.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-searchinterface-searchbyplaceid">searchByPlaceId</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-searchByPlaceId-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-placeidquery-class">PlaceIdQuery</a></span> <span class="parameter-name">query</span>, </span><span id="sdk-for-flutter-navigate-searchByPlaceId-param-languageCode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-languagecode">LanguageCode</a>?</span> <span class="parameter-name">languageCode</span>, </span><span id="sdk-for-flutter-navigate-searchByPlaceId-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-placeidsearchcallback">PlaceIdSearchCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous search for a <a href="sdk-for-flutter-navigate-search-place-class">Place</a> based on its ID and <a href="sdk-for-flutter-navigate-core-languagecode">LanguageCode</a>.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-searchinterface-searchbytext">searchByText</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-searchByText-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-textquery-class">TextQuery</a></span> <span class="parameter-name">query</span>, </span><span id="sdk-for-flutter-navigate-searchByText-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span><span id="sdk-for-flutter-navigate-searchByText-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-searchcallback">SearchCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous text query search for <a href="sdk-for-flutter-navigate-search-place-class">Place</a> instances within a given <a href="sdk-for-flutter-navigate-search-textqueryarea-class">TextQueryArea</a>.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-offlinesearchengine-suggestbyaddresselements">suggestByAddressElements</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-suggestByAddressElements-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-structuredquery-class">StructuredQuery</a></span> <span class="parameter-name">query</span>, </span><span id="sdk-for-flutter-navigate-suggestByAddressElements-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span><span id="sdk-for-flutter-navigate-suggestByAddressElements-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-suggestcallback">SuggestCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous request to suggest places for a <a href="sdk-for-flutter-navigate-search-structuredquery-class">StructuredQuery</a> built with address elements and returns candidate suggestions sorted by relevance.

<span class="name"><a href="sdk-for-flutter-navigate-search-searchinterface-suggestbytext">suggestByText</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-suggestByText-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-textquery-class">TextQuery</a></span> <span class="parameter-name">query</span>, </span><span id="sdk-for-flutter-navigate-suggestByText-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span><span id="sdk-for-flutter-navigate-suggestByText-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-suggestcallback">SuggestCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous request to suggest places for text queries and returns suggestions sorted by relevance.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-searchinterface-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-search-searchinterface-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Static Methods

<span class="name"><a href="sdk-for-flutter-navigate-search-offlinesearchengine-setindexoptions">setIndexOptions</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setIndexOptions-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span>, </span><span id="sdk-for-flutter-navigate-setIndexOptions-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-offlinesearchindexoptions-class">OfflineSearchIndexOptions</a></span> <span class="parameter-name">options</span>, </span><span id="sdk-for-flutter-navigate-setIndexOptions-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-offlinesearchindexlistener-class">OfflineSearchIndexListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-search-offlinesearchindexerror">OfflineSearchIndexError</a>?</span> </span>  
Enables or disables indexing.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
