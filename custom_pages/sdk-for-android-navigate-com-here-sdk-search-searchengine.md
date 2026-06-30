---
title: "SearchEngine (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-searchengine"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- SearchEngine.html -->






<div class="flex-box">

<div class="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.search</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.search.SearchEngine</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-search-searchinterface" title="interface in com.here.sdk.search">SearchInterface</a></code></dd>
</dl>

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">SearchEngine</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a>
implements <a href="sdk-for-android-navigate-com-here-sdk-search-searchinterface" title="interface in com.here.sdk.search">SearchInterface</a></span></div>
<div class="block"><p>The SearchEngine API unlocks the search, geocoding and suggesting capabilities of HERE services
 to provide developers with unmatched flexibility to create differentiating location-enabled
 applications. It enables to search for HERE points of interests, forward and reverse
 geocode addresses and geographic coordinates from the HERE map and search for suggested addresses
 or place candidates based on incomplete or misspelled queries.
 It also allows to search along a given <a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core"><code>GeoPolyline</code></a> set inside a <a href="sdk-for-android-navigate-com-here-sdk-core-geocorridor" title="class in com.here.sdk.core"><code>GeoCorridor</code></a>
 as part of a <a href="sdk-for-android-navigate-com-here-sdk-search-textquery" title="class in com.here.sdk.search"><code>TextQuery</code></a>.
 The SearchEngine API requires an online connection to execute the requests.
 <strong>Note:</strong> All methods are provided in two flavors. One uses a <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallback" title="interface in com.here.sdk.search"><code>SearchCallback</code></a> and the
 other uses a <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallbackextended" title="interface in com.here.sdk.search"><code>SearchCallbackExtended</code></a>: The later adds a <code>ResponseDetails</code> result type
 that provides the <code>requestId</code> of a search request and a <code>correlationId</code> to identify multiple,
 related queries. This may be useful for debug purposes.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searchengine#%3Cinit%3E()">SearchEngine</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of this class.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searchengine#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine)">SearchEngine</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance of this class.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searchengine#search(com.here.sdk.core.GeoCircle,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">search</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geocircle" title="class in com.here.sdk.core">GeoCircle</a> circle,
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous request to search for places based on given circular spatial filter.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searchengine#search(com.here.sdk.core.GeoCircle,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallbackExtended)">search</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geocircle" title="class in com.here.sdk.core">GeoCircle</a> circle,
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallbackextended" title="interface in com.here.sdk.search">SearchCallbackExtended</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous request to search for places based on given circular spatial filter.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searchengine#search(com.here.sdk.core.GeoCoordinates,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallbackExtended)">search</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallbackextended" title="interface in com.here.sdk.search">SearchCallbackExtended</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous request to search for places based on given geographic coordinates.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searchengine#search(com.here.sdk.search.AddressQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallbackExtended)">search</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-search-addressquery" title="class in com.here.sdk.search">AddressQuery</a> query,
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallbackextended" title="interface in com.here.sdk.search">SearchCallbackExtended</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous request to search for places based on a given address.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searchengine#search(com.here.sdk.search.CategoryQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallbackExtended)">search</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-search-categoryquery" title="class in com.here.sdk.search">CategoryQuery</a> query,
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallbackextended" title="interface in com.here.sdk.search">SearchCallbackExtended</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous request to do a category search for <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> instances.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searchengine#search(com.here.sdk.search.PlaceIdQuery,com.here.sdk.core.LanguageCode,com.here.sdk.search.PlaceIdSearchCallbackExtended)">search</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-search-placeidquery" title="class in com.here.sdk.search">PlaceIdQuery</a> query,
 <a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> languageCode,
 <a href="sdk-for-android-navigate-com-here-sdk-search-placeidsearchcallbackextended" title="interface in com.here.sdk.search">PlaceIdSearchCallbackExtended</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous request to search for a <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> based on its ID and
 <a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core"><code>LanguageCode</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searchengine#search(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallbackExtended)">search</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-search-textquery" title="class in com.here.sdk.search">TextQuery</a> query,
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallbackextended" title="interface in com.here.sdk.search">SearchCallbackExtended</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous request to do a text query search for <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> instances.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searchengine#searchByAddress(com.here.sdk.search.AddressQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">searchByAddress</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-search-addressquery" title="class in com.here.sdk.search">AddressQuery</a> query,
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous address query search for <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> instances.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searchengine#searchByCategory(com.here.sdk.search.CategoryQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">searchByCategory</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-search-categoryquery" title="class in com.here.sdk.search">CategoryQuery</a> query,
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous category search for <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> instances.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searchengine#searchByCoordinates(com.here.sdk.core.GeoCoordinates,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">searchByCoordinates</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous search for <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> instances based on the given
 geographic coordinates.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searchengine#searchByPickedPlace(com.here.sdk.core.PickedPlace,com.here.sdk.core.LanguageCode,com.here.sdk.search.PlaceIdSearchCallback)">searchByPickedPlace</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-pickedplace" title="class in com.here.sdk.core">PickedPlace</a> pickedPlace,
 <a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> languageCode,
 <a href="sdk-for-android-navigate-com-here-sdk-search-placeidsearchcallback" title="interface in com.here.sdk.search">PlaceIdSearchCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous search for a <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> based on the content found in <a href="sdk-for-android-navigate-com-here-sdk-core-pickedplace" title="class in com.here.sdk.core"><code>PickedPlace</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searchengine#searchByPlaceId(com.here.sdk.search.PlaceIdQuery,com.here.sdk.core.LanguageCode,com.here.sdk.search.PlaceIdSearchCallback)">searchByPlaceId</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-search-placeidquery" title="class in com.here.sdk.search">PlaceIdQuery</a> query,
 <a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> languageCode,
 <a href="sdk-for-android-navigate-com-here-sdk-search-placeidsearchcallback" title="interface in com.here.sdk.search">PlaceIdSearchCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous search for a <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> based on its ID and
 <a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core"><code>LanguageCode</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searchengine#searchByText(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">searchByText</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-search-textquery" title="class in com.here.sdk.search">TextQuery</a> query,
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous text query search for <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> instances within a given <a href="sdk-for-android-navigate-com-here-sdk-search-textquery-area" title="class in com.here.sdk.search"><code>TextQuery.Area</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searchengine#sendRequest(java.lang.String,com.here.sdk.search.SearchCallback)">sendRequest</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> href,
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous request by using the given href.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searchengine#sendRequest(java.lang.String,com.here.sdk.search.SearchCallbackExtended)">sendRequest</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> href,
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallbackextended" title="interface in com.here.sdk.search">SearchCallbackExtended</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous request by using the given href.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searchengine#setCustomOption(java.lang.String,java.lang.String)">setCustomOption</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a custom option for search backend queries.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searchengine#setEVInterface(com.here.sdk.search.EVSearchInterface)">setEVInterface</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-search-evsearchinterface" title="interface in com.here.sdk.search">EVSearchInterface</a> evcpInterface)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the EV interface through which search will interact with EVCP3.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searchengine#suggest(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SuggestCallbackExtended)">suggest</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-search-textquery" title="class in com.here.sdk.search">TextQuery</a> query,
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 <a href="sdk-for-android-navigate-com-here-sdk-search-suggestcallbackextended" title="interface in com.here.sdk.search">SuggestCallbackExtended</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous request to suggest places for text queries and
 returns candidate suggestions sorted by relevance.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searchengine#suggestByText(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SuggestCallback)">suggestByText</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-search-textquery" title="class in com.here.sdk.search">TextQuery</a> query,
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 <a href="sdk-for-android-navigate-com-here-sdk-search-suggestcallback" title="interface in com.here.sdk.search">SuggestCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous request to suggest places for text queries and
 returns suggestions sorted by relevance.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>SearchEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SearchEngine</span>()
             throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of this class.</p></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine)">
<h3>SearchEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SearchEngine</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span>
             throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of this class.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>Instance of an existing SDKEngine.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="search(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallbackExtended)">
<h3>search</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">search</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-textquery" title="class in com.here.sdk.search">TextQuery</a> query,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallbackextended" title="interface in com.here.sdk.search">SearchCallbackExtended</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous request to do a text query search for <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> instances.
 Optionally, search along a polyline, such as a route, by specifying a <a href="sdk-for-android-navigate-com-here-sdk-core-geocorridor" title="class in com.here.sdk.core"><code>GeoCorridor</code></a>.
 Provides candidate places sorted by relevance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>query</code> - <p>Desired free-form text query to search.</p></dd>
<dd><code>options</code> - <p>Search options.</p></dd>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="search(com.here.sdk.search.AddressQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallbackExtended)">
<h3>search</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">search</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-addressquery" title="class in com.here.sdk.search">AddressQuery</a> query,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallbackextended" title="interface in com.here.sdk.search">SearchCallbackExtended</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous request to search for places based on a given address.
 This is the same process as forward geocoding, except that more data is returned
 than just the geographic coordinates of a given address. Note that an address can
 belong to more than one <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> result, although all found places will
 share the same geographic coordinates.
 Provides candidate places sorted by relevance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>query</code> - <p>Desired free-form address query text to search.</p></dd>
<dd><code>options</code> - <p>Search options.</p></dd>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="search(com.here.sdk.search.PlaceIdQuery,com.here.sdk.core.LanguageCode,com.here.sdk.search.PlaceIdSearchCallbackExtended)">
<h3>search</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">search</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-placeidquery" title="class in com.here.sdk.search">PlaceIdQuery</a> query,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> languageCode,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-placeidsearchcallbackextended" title="interface in com.here.sdk.search">PlaceIdSearchCallbackExtended</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous request to search for a <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> based on its ID and
 <a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core"><code>LanguageCode</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>query</code> - <p>The id of place to search.</p></dd>
<dd><code>languageCode</code> - <p>The preferred language for the search results. When unset or unsupported language is
     chosen, results will be returned in their local language.</p></dd>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="search(com.here.sdk.core.GeoCoordinates,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallbackExtended)">
<h3>search</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">search</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallbackextended" title="interface in com.here.sdk.search">SearchCallbackExtended</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous request to search for places based on given geographic coordinates.
 This is the same process as reverse geocoding, except that more data is returned
 than just the <a href="sdk-for-android-navigate-com-here-sdk-search-address" title="class in com.here.sdk.search"><code>Address</code></a> that belongs to given coordinates. Note that coordinates
 can belong to more than one <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> result.
 Provides candidate places sorted by relevance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>coordinates</code> - <p>The coordinates where to search.</p></dd>
<dd><code>options</code> - <p>Search options.</p></dd>
<dd><code>callback</code> - <p>Callback which receives result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="search(com.here.sdk.core.GeoCircle,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">
<h3>search</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">search</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocircle" title="class in com.here.sdk.core">GeoCircle</a> circle,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous request to search for places based on given circular spatial filter.
 This is the same process as reverse geocoding, except that more data is returned
 than just the <a href="sdk-for-android-navigate-com-here-sdk-search-address" title="class in com.here.sdk.search"><code>Address</code></a> that belongs to given coordinates. Note that coordinates
 can belong to more than one <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> result.
 Provides candidate places sorted by relevance and located inside the radius of filter.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>circle</code> - <p>The coordinates where to search and radius of the circular spatial filter.
     Passed in form of <a href="sdk-for-android-navigate-com-here-sdk-core-geocircle" title="class in com.here.sdk.core"><code>GeoCircle</code></a>.</p></dd>
<dd><code>options</code> - <p>Search options.</p></dd>
<dd><code>callback</code> - <p>Callback which receives result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="search(com.here.sdk.core.GeoCircle,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallbackExtended)">
<h3>search</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">search</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocircle" title="class in com.here.sdk.core">GeoCircle</a> circle,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallbackextended" title="interface in com.here.sdk.search">SearchCallbackExtended</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous request to search for places based on given circular spatial filter.
 This is the same process as reverse geocoding, except that more data is returned
 than just the <a href="sdk-for-android-navigate-com-here-sdk-search-address" title="class in com.here.sdk.search"><code>Address</code></a> that belongs to given coordinates. Note that coordinates
 can belong to more than one <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> result.
 Provides candidate places sorted by relevance and located inside the radius of filter.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>circle</code> - <p>The coordinates where to search and radius of the circular spatial filter.
     Passed in form of <a href="sdk-for-android-navigate-com-here-sdk-core-geocircle" title="class in com.here.sdk.core"><code>GeoCircle</code></a>.</p></dd>
<dd><code>options</code> - <p>Search options.</p></dd>
<dd><code>callback</code> - <p>Callback which receives result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sendRequest(java.lang.String,com.here.sdk.search.SearchCallback)">
<h3>sendRequest</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">sendRequest</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> href,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous request by using the given href.
 The href value can be obtained from <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> objects,
 which are the result of successful call to <a href="sdk-for-android-navigate-com-here-sdk-search-searchengine#suggest(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SuggestCallbackExtended)"><code>suggest(com.here.sdk.search.TextQuery, com.here.sdk.search.SearchOptions, com.here.sdk.search.SuggestCallbackExtended)</code></a>.
 Currently supports only /v1/discover path.
 Provides candidate places sorted by relevance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>href</code> - <p>The direct link.</p></dd>
<dd><code>callback</code> - <p>Callback which receives result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sendRequest(java.lang.String,com.here.sdk.search.SearchCallbackExtended)">
<h3>sendRequest</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">sendRequest</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> href,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallbackextended" title="interface in com.here.sdk.search">SearchCallbackExtended</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous request by using the given href.
 The href value can be obtained from <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> objects,
 which are the result of successful call to <a href="sdk-for-android-navigate-com-here-sdk-search-searchengine#suggest(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SuggestCallbackExtended)"><code>suggest(com.here.sdk.search.TextQuery, com.here.sdk.search.SearchOptions, com.here.sdk.search.SuggestCallbackExtended)</code></a>.
 Currently supports only /v1/discover path.
 Provides candidate places sorted by relevance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>href</code> - <p>The direct link.</p></dd>
<dd><code>callback</code> - <p>Callback which receives result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="search(com.here.sdk.search.CategoryQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallbackExtended)">
<h3>search</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">search</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-categoryquery" title="class in com.here.sdk.search">CategoryQuery</a> query,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallbackextended" title="interface in com.here.sdk.search">SearchCallbackExtended</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous request to do a category search for <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> instances.
 A list containing at least one <a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search"><code>PlaceCategory</code></a> must be provided
 as part of the <code>query</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>query</code> - <p>Query with list of desired categories.</p></dd>
<dd><code>options</code> - <p>Search options.</p></dd>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="suggest(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SuggestCallbackExtended)">
<h3>suggest</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">suggest</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-textquery" title="class in com.here.sdk.search">TextQuery</a> query,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-suggestcallbackextended" title="interface in com.here.sdk.search">SuggestCallbackExtended</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous request to suggest places for text queries and
 returns candidate suggestions sorted by relevance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>query</code> - <p>Desired text query to search.</p></dd>
<dd><code>options</code> - <p>Search options.</p></dd>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCustomOption(java.lang.String,java.lang.String)">
<h3>setCustomOption</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></span> <span class="element-name">setCustomOption</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block"><p>Sets a custom option for search backend queries. This allows more control over the behavior
 of the search algorithm.
 Name has the format <endpoint_name>.<option_name>, for example "discover.show".
 Values can be combined for the same name by using a comma, for example "truck,fuel".
 The custom option is applied only for the endpoint that is specified as prefix in <code>name</code>.
 Some of the supported name/value options are:
 <ul>
<li>name = "revgeocode.with", value = "unnamedStreets" enables the retrieval of access points
 on unnamed streets.</li>
<li>name = "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show", value = "truck"
 enables retreival of truck amenities.
 <strong>Note:</strong> Only participants of the closed-alpha group can get access from HERE to use this feature,
 otherwise, a <a href="sdk-for-android-navigate-searcherror#FORBIDDEN"><code>SearchError.FORBIDDEN</code></a> will be propagated in callbacks.</li>
<li>name = "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show", value = "fuel"
 enables retreival of fuel station details.
 <strong>Note:</strong> Only participants of the closed-alpha group can get access from HERE to use this feature,
 otherwise, a <a href="sdk-for-android-navigate-searcherror#FORBIDDEN"><code>SearchError.FORBIDDEN</code></a> will be propagated in callbacks.</li>
<li>name = "lookup.show" or "discover.show" or "browse.show", value = "ev"
 enables retreival of EV charging station details.</li>
<li>name = "lookup.show" or "discover.show" or "browse.show", value = "eMobilityServiceProviders"
 enables retreival of e-Mobility Service Providers details.</li>
<li>name = "lookup.show" or "discover.show" or "browse.show", value = "tripadvisor"
 adds images, ratings, and editorials from Tripadvisor (TM).
 <strong>Note:</strong> Only clients with a license with TripAdvisor for rich content will actually get it.
 If this licence is missing, TripAdvisor rich content will be missing, with no error reported.
 This content is only added to top 10 search results. If more results are returned,
 they will be missing rich TripAdvisor content.</li>
<li>name = "lookup.datasets" or "discover.datasets" or "browse.datasets" or "autosuggest.datasets",
 value = <your_dataset_hrn> enables ingesting and searching of private POIs.
 <strong>Note:</strong> Only participants of the search customization can get access from HERE to use this feature,
 otherwise, a <a href="sdk-for-android-navigate-searcherror#INVALID_CUSTOM_OPTION_FORMAT"><code>SearchError.INVALID_CUSTOM_OPTION_FORMAT</code></a> will be propagated in callbacks.</your_dataset_hrn></li>
<li>name = "discover.ranking" or "browse.ranking", value = "excursionDistance"
 enables balanced distribution of results for search in <code>GeoCorridor</code>.
 Constraint: using this parameter when searching an area that is not a <code>GeoCorridor</code> generates
 an error <a href="sdk-for-android-navigate-searcherror#BAD_REQUEST"><code>SearchError.BAD_REQUEST</code></a>.
 <strong>Note:</strong> It is recommended to use <a href="sdk-for-android-navigate-searchoptions#distributedResults"><code>SearchOptions.distributedResults</code></a> instead.
 For a complete list of available endpoints, parameter names and their valid values, refer to
 <a href="https://www.here.com/docs/bundle/batch-api-developer-guide/page/topics/constructing-request.html">HERE Geocoding &amp; Search API v7</a>.
 <strong>Note:</strong> It's easy to set a wrong option that makes queries invalid,
 so make sure you read and understand the backend documentation.</li>
</ul></option_name></endpoint_name></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>Option name in the format <endpoint_name>.<option_name>, for example "discover.show".</option_name></endpoint_name></p></dd>
<dd><code>value</code> - <p>Option value.</p></dd>
<dt>Returns:</dt>
<dd><p>Error in case when setting the option fails.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEVInterface(com.here.sdk.search.EVSearchInterface)">
<h3>setEVInterface</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEVInterface</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-evsearchinterface" title="interface in com.here.sdk.search">EVSearchInterface</a> evcpInterface)</span></div>
<div class="block"><p>Sets the EV interface through which search will interact with EVCP3.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>evcpInterface</code> - <p>The EV search interface implementation.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="searchByText(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">
<h3>searchByText</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">searchByText</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-textquery" title="class in com.here.sdk.search">TextQuery</a> query,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous text query search for <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> instances within a given <a href="sdk-for-android-navigate-com-here-sdk-search-textquery-area" title="class in com.here.sdk.search"><code>TextQuery.Area</code></a>.
 The returned places are sorted by relevance.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-searchinterface#searchByText(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">searchByText</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-search-searchinterface" title="interface in com.here.sdk.search">SearchInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>query</code> - <p>Desired free-form text query to search.</p></dd>
<dd><code>options</code> - <p>Search options.</p></dd>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="searchByAddress(com.here.sdk.search.AddressQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">
<h3>searchByAddress</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">searchByAddress</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-addressquery" title="class in com.here.sdk.search">AddressQuery</a> query,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous address query search for <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> instances.
 This is the same type of search as forward geocoding, except that more data is returned
 than just the geographic coordinates of a given address. Note that an address can
 belong to more than one <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> result, although all found places will
 share the same geographic coordinates.
 The returned places are sorted by relevance.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-searchinterface#searchByAddress(com.here.sdk.search.AddressQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">searchByAddress</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-search-searchinterface" title="interface in com.here.sdk.search">SearchInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>query</code> - <p>Desired free-form address query text to search.</p></dd>
<dd><code>options</code> - <p>Search options.</p></dd>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="searchByCategory(com.here.sdk.search.CategoryQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">
<h3>searchByCategory</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">searchByCategory</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-categoryquery" title="class in com.here.sdk.search">CategoryQuery</a> query,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous category search for <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> instances.
 A list containing at least one <a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search"><code>PlaceCategory</code></a> must be provided
 as part of the <code>query</code>.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-searchinterface#searchByCategory(com.here.sdk.search.CategoryQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">searchByCategory</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-search-searchinterface" title="interface in com.here.sdk.search">SearchInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>query</code> - <p>Query with list of desired categories.</p></dd>
<dd><code>options</code> - <p>Search options.</p></dd>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="searchByCoordinates(com.here.sdk.core.GeoCoordinates,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">
<h3>searchByCoordinates</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">searchByCoordinates</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous search for <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> instances based on the given
 geographic coordinates.
 This is the same search type as reverse geocoding, except that more data is returned
 than just the <a href="sdk-for-android-navigate-com-here-sdk-search-address" title="class in com.here.sdk.search"><code>Address</code></a> related to the given coordinates.
 Note that more than one <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> can be related to the given coordinates.
 The returned places are sorted by relevance.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-searchinterface#searchByCoordinates(com.here.sdk.core.GeoCoordinates,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">searchByCoordinates</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-search-searchinterface" title="interface in com.here.sdk.search">SearchInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>coordinates</code> - <p>The coordinates where to search.</p></dd>
<dd><code>options</code> - <p>Search options.</p></dd>
<dd><code>callback</code> - <p>Callback which receives result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="searchByPlaceId(com.here.sdk.search.PlaceIdQuery,com.here.sdk.core.LanguageCode,com.here.sdk.search.PlaceIdSearchCallback)">
<h3>searchByPlaceId</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">searchByPlaceId</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-placeidquery" title="class in com.here.sdk.search">PlaceIdQuery</a> query,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> languageCode,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-placeidsearchcallback" title="interface in com.here.sdk.search">PlaceIdSearchCallback</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous search for a <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> based on its ID and
 <a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core"><code>LanguageCode</code></a>.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-searchinterface#searchByPlaceId(com.here.sdk.search.PlaceIdQuery,com.here.sdk.core.LanguageCode,com.here.sdk.search.PlaceIdSearchCallback)">searchByPlaceId</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-search-searchinterface" title="interface in com.here.sdk.search">SearchInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>query</code> - <p>The id of place to search.</p></dd>
<dd><code>languageCode</code> - <p>The preferred language for the search results. When unset or unsupported language is chosen,
     results will be returned in their local language.</p></dd>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="searchByPickedPlace(com.here.sdk.core.PickedPlace,com.here.sdk.core.LanguageCode,com.here.sdk.search.PlaceIdSearchCallback)">
<h3>searchByPickedPlace</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">searchByPickedPlace</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-pickedplace" title="class in com.here.sdk.core">PickedPlace</a> pickedPlace,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> languageCode,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-placeidsearchcallback" title="interface in com.here.sdk.search">PlaceIdSearchCallback</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous search for a <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> based on the content found in <a href="sdk-for-android-navigate-com-here-sdk-core-pickedplace" title="class in com.here.sdk.core"><code>PickedPlace</code></a>.
 If <a href="sdk-for-android-navigate-com-here-sdk-core-pickedplace" title="class in com.here.sdk.core"><code>PickedPlace</code></a> data is obtained from the offline map, it may happen that the newer version
 that is used by the online service represented by <code>SearchEngine</code> no longer contains the
 related POI. In that case, <a href="sdk-for-android-navigate-searcherror#NO_RESULTS_FOUND"><code>SearchError.NO_RESULTS_FOUND</code></a> error is reported.
 When that happens, you may try to obtain the POI from the offline map by calling
 <code>OfflineSearchEngine.searchByPickedPlace</code>, only available for the Navigate license.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-searchinterface#searchByPickedPlace(com.here.sdk.core.PickedPlace,com.here.sdk.core.LanguageCode,com.here.sdk.search.PlaceIdSearchCallback)">searchByPickedPlace</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-search-searchinterface" title="interface in com.here.sdk.search">SearchInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>pickedPlace</code> - <p>The content picked from map.</p></dd>
<dd><code>languageCode</code> - <p>The preferred language for the search result. When unset or unsupported language is chosen,
     result will be returned in the local language.</p></dd>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="suggestByText(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SuggestCallback)">
<h3>suggestByText</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">suggestByText</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-textquery" title="class in com.here.sdk.search">TextQuery</a> query,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-suggestcallback" title="interface in com.here.sdk.search">SuggestCallback</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous request to suggest places for text queries and
 returns suggestions sorted by relevance.
 Note that while <code>OfflineSearchEngine</code> includes as many details as are available,
 <code>SearchEngine</code> includes only the information that is relevant for autosuggest use cases.
 Complete details can be obtained by searching with <a href="sdk-for-android-navigate-com-here-sdk-search-placeidquery" title="class in com.here.sdk.search"><code>PlaceIdQuery</code></a>.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-searchinterface#suggestByText(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SuggestCallback)">suggestByText</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-search-searchinterface" title="interface in com.here.sdk.search">SearchInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>query</code> - <p>Desired text query to search.</p></dd>
<dd><code>options</code> - <p>Search options.</p></dd>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->

</div>
</div>



</div>
`
}</HTMLBlock>
