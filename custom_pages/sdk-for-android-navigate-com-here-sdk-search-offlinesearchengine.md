---
title: "OfflineSearchEngine (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-offlinesearchengine"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- OfflineSearchEngine.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-package-summary">com.here.sdk.search</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.search.OfflineSearchEngine</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchinterface" title="interface in com.here.sdk.search">SearchInterface</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">OfflineSearchEngine</span>
<span class="extends-implements">extends <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a>
implements <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchinterface" title="interface in com.here.sdk.search">SearchInterface</a></span></div>
<div class="block"><p>The OfflineSearchEngine works without internet and unlocks the search and geocoding
 capabilities of HERE services to provide developers with unmatched flexibility
 to create differentiating location-enabled applications.
 </p><p>It provides the same interfaces as the SearchEngine, but the results may slightly
 differ as the results are taken from already downloaded map data instead of initiating
 a new request to a HERE backend service. This way the data may be, for example, older
 compared to the data you may receive when using the SearchEngine. On the other hand,
 this class provides results faster as no online connection is necessary.
 </p><p>In comparison to the SearchEngine, there are a few limitations:
 <ul>
<li>The IDs of POIs are different and may differ among different map versions.</li>
<li>The implementation is different and the resources are limited, so the results can differ.</li>
<li>OfflineSearchEngine sometimes doesn't return the requested number of results.</li>
</ul>
</p><p>Note: You can search only within persistent map data (downloaded via MapDownloader) or existing cached data.
 However, cached data may be incomplete, which can result in searches returning partial or incomplete information.
 Therefore, it is recommended to use persistent map data.
 Make sure that at least <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-layerconfiguration.feature#OFFLINE_SEARCH"><code>LayerConfiguration.Feature.OFFLINE_SEARCH</code></a> is enabled.
 For EV rich attributes also enable <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-layerconfiguration.feature#EV"><code>LayerConfiguration.Feature.EV</code></a>,
 for truck rich attributes also enable <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-layerconfiguration.feature#TRUCK_SERVICE_ATTRIBUTES"><code>LayerConfiguration.Feature.TRUCK_SERVICE_ATTRIBUTES</code></a>,
 for fuel station rich attributes also enable <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-layerconfiguration.feature#FUEL_STATION_ATTRIBUTES"><code>LayerConfiguration.Feature.FUEL_STATION_ATTRIBUTES</code></a>
 in <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.</p></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E()">OfflineSearchEngine</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of this class.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine)">OfflineSearchEngine</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</code></div>
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
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#attach(com.here.sdk.search.MyPlaces,com.here.sdk.core.threading.OnTaskCompleted)">attach</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-myplaces" title="class in com.here.sdk.search">MyPlaces</a> dataSource,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-ontaskcompleted" title="interface in com.here.sdk.core.threading">OnTaskCompleted</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Attach data source into SearchEngine instance.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#search(com.here.sdk.search.StructuredQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">search</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-structuredquery" title="class in com.here.sdk.search">StructuredQuery</a> query,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous request to search for places.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#searchByAddress(com.here.sdk.search.AddressQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">searchByAddress</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-addressquery" title="class in com.here.sdk.search">AddressQuery</a> query,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous address query search for <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> instances.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#searchByCategory(com.here.sdk.search.CategoryQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">searchByCategory</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-categoryquery" title="class in com.here.sdk.search">CategoryQuery</a> query,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous category search for <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> instances.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#searchByCoordinates(com.here.sdk.core.GeoCoordinates,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">searchByCoordinates</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous search for <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> instances based on the given
 geographic coordinates.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#searchByPickedPlace(com.here.sdk.core.PickedPlace,com.here.sdk.core.LanguageCode,com.here.sdk.search.PlaceIdSearchCallback)">searchByPickedPlace</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-pickedplace" title="class in com.here.sdk.core">PickedPlace</a> pickedPlace,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> languageCode,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-placeidsearchcallback" title="interface in com.here.sdk.search">PlaceIdSearchCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous search for a <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> based on the content found in <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-pickedplace" title="class in com.here.sdk.core"><code>PickedPlace</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#searchByPlaceId(com.here.sdk.search.PlaceIdQuery,com.here.sdk.core.LanguageCode,com.here.sdk.search.PlaceIdSearchCallback)">searchByPlaceId</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-placeidquery" title="class in com.here.sdk.search">PlaceIdQuery</a> query,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> languageCode,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-placeidsearchcallback" title="interface in com.here.sdk.search">PlaceIdSearchCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous search for a <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> based on its ID and
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-languagecode" title="enum class in com.here.sdk.core"><code>LanguageCode</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#searchByText(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">searchByText</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-textquery" title="class in com.here.sdk.search">TextQuery</a> query,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous text query search for <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> instances within a given <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-textquery.area" title="class in com.here.sdk.search"><code>TextQuery.Area</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-offlinesearchindex.error" title="enum class in com.here.sdk.search">OfflineSearchIndex.Error</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#setIndexOptions(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.search.OfflineSearchIndex.Options,com.here.sdk.search.OfflineSearchIndexListener)">setIndexOptions</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-offlinesearchindex.options" title="class in com.here.sdk.search">OfflineSearchIndex.Options</a> options,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-offlinesearchindexlistener" title="interface in com.here.sdk.search">OfflineSearchIndexListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Enables or disables indexing.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#suggest(com.here.sdk.search.StructuredQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SuggestCallback)">suggest</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-structuredquery" title="class in com.here.sdk.search">StructuredQuery</a> query,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-suggestcallback" title="interface in com.here.sdk.search">SuggestCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous request to suggest places for a <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-structuredquery" title="class in com.here.sdk.search"><code>StructuredQuery</code></a> built with address elements and
 returns candidate suggestions sorted by relevance.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#suggestByText(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SuggestCallback)">suggestByText</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-textquery" title="class in com.here.sdk.search">TextQuery</a> query,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-suggestcallback" title="interface in com.here.sdk.search">SuggestCallback</a> callback)</code></div>
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
<h3>OfflineSearchEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">OfflineSearchEngine</span>()
                    throws <span class="exceptions"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of this class.</p></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine)">
<h3>OfflineSearchEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">OfflineSearchEngine</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span>
                    throws <span class="exceptions"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of this class.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>Instance of an existing SDKEngine.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
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
<section class="detail" id="attach(com.here.sdk.search.MyPlaces,com.here.sdk.core.threading.OnTaskCompleted)">
<h3>attach</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">attach</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-myplaces" title="class in com.here.sdk.search">MyPlaces</a> dataSource,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-ontaskcompleted" title="interface in com.here.sdk.core.threading">OnTaskCompleted</a> callback)</span></div>
<div class="block"><p>Attach data source into SearchEngine instance.
 Places from MyPlaces ranked the same
 way as places from default source.
 New data source replaces old one.
 Note: Only OfflineSearchEngine supports search over MyPlaces.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dataSource</code> - <p>The data source.</p></dd>
<dd><code>callback</code> - <p>The callback to be called when task is completed.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="search(com.here.sdk.search.StructuredQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">
<h3>search</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">search</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-structuredquery" title="class in com.here.sdk.search">StructuredQuery</a> query,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous request to search for places. The user submits a <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-structuredquery" title="class in com.here.sdk.search"><code>StructuredQuery</code></a>
 that returns places adhering to the constraints provided in <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-structuredquery" title="class in com.here.sdk.search"><code>StructuredQuery</code></a>.
 For example, when user wants results of type street for a text query <code>Invalidenstraße</code> in <code>Berlin</code>, it can be searched
 by preparing <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-structuredquery" title="class in com.here.sdk.search"><code>StructuredQuery</code></a> providing <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-structuredquery#query"><code>StructuredQuery.query</code></a> as <code>Invalidenstraße</code>,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-structuredquery#areaCenter"><code>StructuredQuery.areaCenter</code></a>, <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-structuredquery.addresselements#country"><code>StructuredQuery.AddressElements.country</code></a> as <code>Germany</code>,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-structuredquery.addresselements#city"><code>StructuredQuery.AddressElements.city</code></a> as <code>Berlin</code> and <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-structuredquery.resulttype" title="enum class in com.here.sdk.search"><code>StructuredQuery.ResultType</code></a> as <code>STREET</code>.
 The results will be presented only from the given geographical area.
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>query</code> - <p>Desired structured query to search.</p></dd>
<dd><code>options</code> - <p>Search options.</p></dd>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="suggest(com.here.sdk.search.StructuredQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SuggestCallback)">
<h3>suggest</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">suggest</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-structuredquery" title="class in com.here.sdk.search">StructuredQuery</a> query,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-suggestcallback" title="interface in com.here.sdk.search">SuggestCallback</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous request to suggest places for a <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-structuredquery" title="class in com.here.sdk.search"><code>StructuredQuery</code></a> built with address elements and
 returns candidate suggestions sorted by relevance.
 For example, when user wants suggestions of type street for a text query <code>Invalidenstraße</code> in <code>Berlin</code>, it can be searched
 by preparing <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-structuredquery" title="class in com.here.sdk.search"><code>StructuredQuery</code></a> providing <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-structuredquery#query"><code>StructuredQuery.query</code></a> as <code>Invalidenstraße</code>,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-structuredquery#areaCenter"><code>StructuredQuery.areaCenter</code></a>, <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-structuredquery.addresselements#country"><code>StructuredQuery.AddressElements.country</code></a> as <code>Germany</code>,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-structuredquery.addresselements#city"><code>StructuredQuery.AddressElements.city</code></a> as <code>Berlin</code> and <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-structuredquery.resulttype" title="enum class in com.here.sdk.search"><code>StructuredQuery.ResultType</code></a> as <code>STREET</code>.
 The suggestions will be presented only from the given geographical area.
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>query</code> - <p>Desired structured query to search.</p></dd>
<dd><code>options</code> - <p>Search options.</p></dd>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIndexOptions(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.search.OfflineSearchIndex.Options,com.here.sdk.search.OfflineSearchIndexListener)">
<h3>setIndexOptions</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public static</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-offlinesearchindex.error" title="enum class in com.here.sdk.search">OfflineSearchIndex.Error</a></span> <span class="element-name">setIndexOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-offlinesearchindex.options" title="class in com.here.sdk.search">OfflineSearchIndex.Options</a> options,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-offlinesearchindexlistener" title="interface in com.here.sdk.search">OfflineSearchIndexListener</a> listener)</span></div>
<div class="block"><p>Enables or disables indexing.
 When indexing is enabled, HERE SDK will create a detailed index over persistent
 map data and update it as needed.
 A detailed index enables finding data faster and over entire persistent map.
 Creating an index takes time, but usually no more than a few seconds up to a couple of
 minutes, depending on persistent map size.
 As the feature is improved, the indexing time will improve.
 Also please note that this is a heavy processing task.
 The stored index increases the space taken by offline maps by around 2-5%.
 This may also improve in future versions.
 </p><p>Indexing is disabled by default.
 If you want it enabled, make sure to call setIndexOptions with <code>OfflineSearchIndex.Options.enabled</code> as <code>true</code> before
 any operations in <code>MapDownloader</code> or <code>MapUpdater</code> that modify the persistent map.
 Calling setIndexOptions may also create or remove map index to match the previously
 installed map regions. If the matching index for installed map regions is found, then
 indexing is skipped.
 While a new index is being created, <code>OfflineSearchEngine</code> functionality can still be used.
 However, without a valid index in place yet, it operates as though indexing is disabled.
 If <code>SDKNativeEngine</code> is disposed during indexing (for example, by closing the app),
 the indexing is cancelled. Recreating <code>SDKNativeEngine</code> and enabling indexing will
 ensure that index is created.
 </p><p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>Indexing is enabled and disabled per SDKNativeEngine instance.
     The index is created inside the related <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdkoptions#persistentMapStoragePath"><code>SDKOptions.persistentMapStoragePath</code></a>.</p></dd>
<dd><code>options</code> - <p>Sets indexing options.</p></dd>
<dd><code>listener</code> - <p>The listener that will receive updates about indexing process.
     When <code>OfflineSearchIndex.Options.enabled</code> is true, SDK would store listener and the listener will receive updates
     about indexing progress every time it is performed.
     When <code>OfflineSearchIndex.Options.enabled</code> is false, SDK would report indexing removal progress to the listener
     one last time and remove storage of listener.</p></dd>
<dt>Returns:</dt>
<dd><p>An error in case there was one. It's <code>null</code> if the indexing listener could be
     configured successfully.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="searchByText(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">
<h3>searchByText</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">searchByText</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-textquery" title="class in com.here.sdk.search">TextQuery</a> query,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous text query search for <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> instances within a given <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-textquery.area" title="class in com.here.sdk.search"><code>TextQuery.Area</code></a>.
 The returned places are sorted by relevance.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchinterface#searchByText(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">searchByText</a></code> in interface <code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchinterface" title="interface in com.here.sdk.search">SearchInterface</a></code></dd>
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
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">searchByAddress</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-addressquery" title="class in com.here.sdk.search">AddressQuery</a> query,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous address query search for <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> instances.
 This is the same type of search as forward geocoding, except that more data is returned
 than just the geographic coordinates of a given address. Note that an address can
 belong to more than one <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> result, although all found places will
 share the same geographic coordinates.
 The returned places are sorted by relevance.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchinterface#searchByAddress(com.here.sdk.search.AddressQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">searchByAddress</a></code> in interface <code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchinterface" title="interface in com.here.sdk.search">SearchInterface</a></code></dd>
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
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">searchByCategory</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-categoryquery" title="class in com.here.sdk.search">CategoryQuery</a> query,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous category search for <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> instances.
 A list containing at least one <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-placecategory" title="class in com.here.sdk.search"><code>PlaceCategory</code></a> must be provided
 as part of the <code>query</code>.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchinterface#searchByCategory(com.here.sdk.search.CategoryQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">searchByCategory</a></code> in interface <code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchinterface" title="interface in com.here.sdk.search">SearchInterface</a></code></dd>
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
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">searchByCoordinates</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous search for <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> instances based on the given
 geographic coordinates.
 This is the same search type as reverse geocoding, except that more data is returned
 than just the <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-address" title="class in com.here.sdk.search"><code>Address</code></a> related to the given coordinates.
 Note that more than one <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> can be related to the given coordinates.
 The returned places are sorted by relevance.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchinterface#searchByCoordinates(com.here.sdk.core.GeoCoordinates,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">searchByCoordinates</a></code> in interface <code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchinterface" title="interface in com.here.sdk.search">SearchInterface</a></code></dd>
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
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">searchByPlaceId</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-placeidquery" title="class in com.here.sdk.search">PlaceIdQuery</a> query,
 @Nullable
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> languageCode,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-placeidsearchcallback" title="interface in com.here.sdk.search">PlaceIdSearchCallback</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous search for a <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> based on its ID and
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-languagecode" title="enum class in com.here.sdk.core"><code>LanguageCode</code></a>.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchinterface#searchByPlaceId(com.here.sdk.search.PlaceIdQuery,com.here.sdk.core.LanguageCode,com.here.sdk.search.PlaceIdSearchCallback)">searchByPlaceId</a></code> in interface <code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchinterface" title="interface in com.here.sdk.search">SearchInterface</a></code></dd>
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
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">searchByPickedPlace</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-pickedplace" title="class in com.here.sdk.core">PickedPlace</a> pickedPlace,
 @Nullable
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> languageCode,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-placeidsearchcallback" title="interface in com.here.sdk.search">PlaceIdSearchCallback</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous search for a <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> based on the content found in <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-pickedplace" title="class in com.here.sdk.core"><code>PickedPlace</code></a>.
 If <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-pickedplace" title="class in com.here.sdk.core"><code>PickedPlace</code></a> data is obtained from the offline map, it may happen that the newer version
 that is used by the online service represented by <code>SearchEngine</code> no longer contains the
 related POI. In that case, <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searcherror#NO_RESULTS_FOUND"><code>SearchError.NO_RESULTS_FOUND</code></a> error is reported.
 When that happens, you may try to obtain the POI from the offline map by calling
 <code>OfflineSearchEngine.searchByPickedPlace</code>, only available for the Navigate license.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchinterface#searchByPickedPlace(com.here.sdk.core.PickedPlace,com.here.sdk.core.LanguageCode,com.here.sdk.search.PlaceIdSearchCallback)">searchByPickedPlace</a></code> in interface <code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchinterface" title="interface in com.here.sdk.search">SearchInterface</a></code></dd>
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
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">suggestByText</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-textquery" title="class in com.here.sdk.search">TextQuery</a> query,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-suggestcallback" title="interface in com.here.sdk.search">SuggestCallback</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous request to suggest places for text queries and
 returns suggestions sorted by relevance.
 </p><p>Note that while <code>OfflineSearchEngine</code> includes as many details as are available,
 <code>SearchEngine</code> includes only the information that is relevant for autosuggest use cases.
 Complete details can be obtained by searching with <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-placeidquery" title="class in com.here.sdk.search"><code>PlaceIdQuery</code></a>.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchinterface#suggestByText(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SuggestCallback)">suggestByText</a></code> in interface <code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-searchinterface" title="interface in com.here.sdk.search">SearchInterface</a></code></dd>
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
</main>





</div>
`
}</HTMLBlock>
