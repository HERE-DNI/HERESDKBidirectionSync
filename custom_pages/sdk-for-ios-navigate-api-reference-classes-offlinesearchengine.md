---
title: "OfflineSearchEngine"
slug: "sdk-for-ios-navigate-api-reference-classes-offlinesearchengine"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/OfflineSearchEngine"></a>
<a title="OfflineSearchEngine Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-search">Search</a>

        OfflineSearchEngine Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>OfflineSearchEngine</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">OfflineSearchEngine</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-searchinterface">SearchInterface</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">OfflineSearchEngine</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">OfflineSearchEngine</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>The OfflineSearchEngine works without internet and unlocks the search and geocoding
capabilities of HERE services to provide developers with unmatched flexibility
to create differentiating location-enabled applications.</p>
<p>It provides the same interfaces as the SearchEngine, but the results may slightly
differ as the results are taken from already downloaded map data instead of initiating
a new request to a HERE backend service. This way the data may be, for example, older
compared to the data you may receive when using the SearchEngine. On the other hand,
this class provides results faster as no online connection is necessary.</p>
<p>In comparison to the SearchEngine, there are a few limitations:</p>
<ul>
<li>The IDs of POIs are different and may differ among different map versions.</li>
<li>The implementation is different and the resources are limited, so the results can differ.</li>
<li>OfflineSearchEngine sometimes doesn’t return the requested number of results.</li>
</ul>
<p>Note: You can search only within persistent map data (downloaded via MapDownloader) or existing cached data.
However, cached data may be incomplete, which can result in searches returning partial or incomplete information.
Therefore, it is recommended to use persistent map data.
Make sure that at least <code><a href="../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO13offlineSearchyA2EmF">LayerConfiguration.Feature.offlineSearch</a></code> is enabled.
For EV rich attributes also enable <code><a href="../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO2evyA2EmF">LayerConfiguration.Feature.ev</a></code>,
for truck rich attributes also enable <code><a href="../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO22truckServiceAttributesyA2EmF">LayerConfiguration.Feature.truckServiceAttributes</a></code>,
for fuel station rich attributes also enable <code><a href="../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO21fuelStationAttributesyA2EmF">LayerConfiguration.Feature.fuelStationAttributes</a></code>
in <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp">SDKOptions.layerConfiguration</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19OfflineSearchEngineCACyKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk19OfflineSearchEngineCACyKcfc">init()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">()</span> <span class="k">throws</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19OfflineSearchEngineCyAcA09SDKNativeD0CKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk19OfflineSearchEngineCyAcA09SDKNativeD0CKcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>sdkEngine</em>
</code>
</td>
<td>
<div>
<p>Instance of an existing SDKEngine.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19OfflineSearchEngineC12searchByText_7options10completionAA10TaskHandle_pAA0G5QueryV_AA0C7OptionsVyAA0C5ErrorOSg_SayAA5PlaceCGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/searchByText(_:options:completion:)"></a>
<a class="token" href="#/s:7heresdk19OfflineSearchEngineC12searchByText_7options10completionAA10TaskHandle_pAA0G5QueryV_AA0C7OptionsVyAA0C5ErrorOSg_SayAA5PlaceCGSgtctF">searchByText(_:<wbr/>options:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous text query search for <code><a href="sdk-for-ios-navigate-api-reference-classes-place">Place</a></code> instances within a given <code><a href="sdk-for-ios-navigate-api-reference-structs-textquery-area">TextQuery.Area</a></code>.
The returned places are sorted by relevance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">searchByText</span><span class="p">(</span><span class="n">_</span> <span class="nv">query</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-textquery">TextQuery</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-searchoptions">SearchOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Search.html#/s:7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>query</em>
</code>
</td>
<td>
<div>
<p>Desired free-form text query to search.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>options</em>
</code>
</td>
<td>
<div>
<p>Search options.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>Callback which receives the result on the main thread.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19OfflineSearchEngineC15searchByAddress_7options10completionAA10TaskHandle_pAA0G5QueryV_AA0C7OptionsVyAA0C5ErrorOSg_SayAA5PlaceCGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/searchByAddress(_:options:completion:)"></a>
<a class="token" href="#/s:7heresdk19OfflineSearchEngineC15searchByAddress_7options10completionAA10TaskHandle_pAA0G5QueryV_AA0C7OptionsVyAA0C5ErrorOSg_SayAA5PlaceCGSgtctF">searchByAddress(_:<wbr/>options:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous address query search for <code><a href="sdk-for-ios-navigate-api-reference-classes-place">Place</a></code> instances.
This is the same type of search as forward geocoding, except that more data is returned
than just the geographic coordinates of a given address. Note that an address can
belong to more than one <code><a href="sdk-for-ios-navigate-api-reference-classes-place">Place</a></code> result, although all found places will
share the same geographic coordinates.
The returned places are sorted by relevance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">searchByAddress</span><span class="p">(</span><span class="n">_</span> <span class="nv">query</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-addressquery">AddressQuery</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-searchoptions">SearchOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Search.html#/s:7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>query</em>
</code>
</td>
<td>
<div>
<p>Desired free-form address query text to search.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>options</em>
</code>
</td>
<td>
<div>
<p>Search options.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>Callback which receives the result on the main thread.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19OfflineSearchEngineC16searchByCategory_7options10completionAA10TaskHandle_pAA0G5QueryV_AA0C7OptionsVyAA0C5ErrorOSg_SayAA5PlaceCGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/searchByCategory(_:options:completion:)"></a>
<a class="token" href="#/s:7heresdk19OfflineSearchEngineC16searchByCategory_7options10completionAA10TaskHandle_pAA0G5QueryV_AA0C7OptionsVyAA0C5ErrorOSg_SayAA5PlaceCGSgtctF">searchByCategory(_:<wbr/>options:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous category search for <code><a href="sdk-for-ios-navigate-api-reference-classes-place">Place</a></code> instances.
A list containing at least one <code><a href="sdk-for-ios-navigate-api-reference-classes-placecategory">PlaceCategory</a></code> must be provided
as part of the <code>searchByCategory(...).query</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">searchByCategory</span><span class="p">(</span><span class="n">_</span> <span class="nv">query</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-categoryquery">CategoryQuery</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-searchoptions">SearchOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Search.html#/s:7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>query</em>
</code>
</td>
<td>
<div>
<p>Query with list of desired categories.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>options</em>
</code>
</td>
<td>
<div>
<p>Search options.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>Callback which receives the result on the main thread.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19OfflineSearchEngineC19searchByCoordinates_7options10completionAA10TaskHandle_pAA03GeoG0V_AA0C7OptionsVyAA0C5ErrorOSg_SayAA5PlaceCGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/searchByCoordinates(_:options:completion:)"></a>
<a class="token" href="#/s:7heresdk19OfflineSearchEngineC19searchByCoordinates_7options10completionAA10TaskHandle_pAA03GeoG0V_AA0C7OptionsVyAA0C5ErrorOSg_SayAA5PlaceCGSgtctF">searchByCoordinates(_:<wbr/>options:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous search for <code><a href="sdk-for-ios-navigate-api-reference-classes-place">Place</a></code> instances based on the given
geographic coordinates.
This is the same search type as reverse geocoding, except that more data is returned
than just the <code><a href="sdk-for-ios-navigate-api-reference-structs-address">Address</a></code> related to the given coordinates.
Note that more than one <code><a href="sdk-for-ios-navigate-api-reference-classes-place">Place</a></code> can be related to the given coordinates.
The returned places are sorted by relevance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">searchByCoordinates</span><span class="p">(</span><span class="n">_</span> <span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-searchoptions">SearchOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Search.html#/s:7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>coordinates</em>
</code>
</td>
<td>
<div>
<p>The coordinates where to search.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>options</em>
</code>
</td>
<td>
<div>
<p>Search options.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>Callback which receives result on the main thread.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19OfflineSearchEngineC15searchByPlaceId_12languageCode10completionAA10TaskHandle_pAA0gH5QueryV_AA08LanguageJ0OSgyAA0C5ErrorOSg_AA0G0CSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/searchByPlaceId(_:languageCode:completion:)"></a>
<a class="token" href="#/s:7heresdk19OfflineSearchEngineC15searchByPlaceId_12languageCode10completionAA10TaskHandle_pAA0gH5QueryV_AA08LanguageJ0OSgyAA0C5ErrorOSg_AA0G0CSgtctF">searchByPlaceId(_:<wbr/>languageCode:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous search for a <code><a href="sdk-for-ios-navigate-api-reference-classes-place">Place</a></code> based on its ID and
<code><a href="sdk-for-ios-navigate-api-reference-enums-languagecode">LanguageCode</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">searchByPlaceId</span><span class="p">(</span><span class="n">_</span> <span class="nv">query</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-placeidquery">PlaceIdQuery</a></span><span class="p">,</span> <span class="nv">languageCode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-languagecode">LanguageCode</a></span><span class="p">?,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Search.html#/s:7heresdk30PlaceIdSearchCompletionHandlera">PlaceIdSearchCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>query</em>
</code>
</td>
<td>
<div>
<p>The id of place to search.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>languageCode</em>
</code>
</td>
<td>
<div>
<p>The preferred language for the search results. When unset or unsupported language is chosen,
results will be returned in their local language.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>Callback which receives the result on the main thread.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19OfflineSearchEngineC19searchByPickedPlace_12languageCode10completionAA10TaskHandle_pAA0gH0V_AA08LanguageJ0OSgyAA0C5ErrorOSg_AA0H0CSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/searchByPickedPlace(_:languageCode:completion:)"></a>
<a class="token" href="#/s:7heresdk19OfflineSearchEngineC19searchByPickedPlace_12languageCode10completionAA10TaskHandle_pAA0gH0V_AA08LanguageJ0OSgyAA0C5ErrorOSg_AA0H0CSgtctF">searchByPickedPlace(_:<wbr/>languageCode:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous search for a <code><a href="sdk-for-ios-navigate-api-reference-classes-place">Place</a></code> based on the content found in <code><a href="sdk-for-ios-navigate-api-reference-structs-pickedplace">PickedPlace</a></code>.
If <code><a href="sdk-for-ios-navigate-api-reference-structs-pickedplace">PickedPlace</a></code> data is obtained from the offline map, it may happen that the newer version
that is used by the online service represented by <code><a href="sdk-for-ios-navigate-api-reference-classes-searchengine">SearchEngine</a></code> no longer contains the
related POI. In that case, <code><a href="../Enums/SearchError.html#/s:7heresdk11SearchErrorO14noResultsFoundyA2CmF">SearchError.noResultsFound</a></code> error is reported.
When that happens, you may try to obtain the POI from the offline map by calling
<code>OfflineSearchEngine.searchByPickedPlace</code>, only available for the Navigate license.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">searchByPickedPlace</span><span class="p">(</span><span class="n">_</span> <span class="nv">pickedPlace</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-pickedplace">PickedPlace</a></span><span class="p">,</span> <span class="nv">languageCode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-languagecode">LanguageCode</a></span><span class="p">?,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Search.html#/s:7heresdk30PlaceIdSearchCompletionHandlera">PlaceIdSearchCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>pickedPlace</em>
</code>
</td>
<td>
<div>
<p>The content picked from map.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>languageCode</em>
</code>
</td>
<td>
<div>
<p>The preferred language for the search result. When unset or unsupported language is chosen,
result will be returned in the local language.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>Callback which receives the result on the main thread.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19OfflineSearchEngineC13suggestByText_7options10completionAA10TaskHandle_pAA0G5QueryV_AA0C7OptionsVyAA0C5ErrorOSg_SayAA10SuggestionCGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/suggestByText(_:options:completion:)"></a>
<a class="token" href="#/s:7heresdk19OfflineSearchEngineC13suggestByText_7options10completionAA10TaskHandle_pAA0G5QueryV_AA0C7OptionsVyAA0C5ErrorOSg_SayAA10SuggestionCGSgtctF">suggestByText(_:<wbr/>options:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous request to suggest places for text queries and
returns suggestions sorted by relevance.</p>
<p>Note that while <code>OfflineSearchEngine</code> includes as many details as are available,
<code><a href="sdk-for-ios-navigate-api-reference-classes-searchengine">SearchEngine</a></code> includes only the information that is relevant for autosuggest use cases.
Complete details can be obtained by searching with <code><a href="sdk-for-ios-navigate-api-reference-structs-placeidquery">PlaceIdQuery</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">suggestByText</span><span class="p">(</span><span class="n">_</span> <span class="nv">query</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-textquery">TextQuery</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-searchoptions">SearchOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Search.html#/s:7heresdk24SuggestCompletionHandlera">SuggestCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>query</em>
</code>
</td>
<td>
<div>
<p>Desired text query to search.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>options</em>
</code>
</td>
<td>
<div>
<p>Search options.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>Callback which receives the result on the main thread.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19OfflineSearchEngineC6attach10dataSource8callbackAA10TaskHandle_pAA8MyPlacesC_yAA0I7OutcomeOctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/attach(dataSource:callback:)"></a>
<a class="token" href="#/s:7heresdk19OfflineSearchEngineC6attach10dataSource8callbackAA10TaskHandle_pAA8MyPlacesC_yAA0I7OutcomeOctF">attach(dataSource:<wbr/>callback:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Attach data source into SearchEngine instance.
Places from MyPlaces ranked the same
way as places from default source.
New data source replaces old one.
Note: Only OfflineSearchEngine supports search over MyPlaces.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">attach</span><span class="p">(</span><span class="nv">dataSource</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-myplaces">MyPlaces</a></span><span class="p">,</span> <span class="nv">callback</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Core.html#/s:7heresdk21TaskCompletionHandlera">TaskCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>dataSource</em>
</code>
</td>
<td>
<div>
<p>The data source.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>callback</em>
</code>
</td>
<td>
<div>
<p>The callback to be called when task is completed.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19OfflineSearchEngineC6search11structQuery7options10completionAA10TaskHandle_pAA010StructuredG0V_AA0C7OptionsVyAA0C5ErrorOSg_SayAA5PlaceCGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/search(structQuery:options:completion:)"></a>
<a class="token" href="#/s:7heresdk19OfflineSearchEngineC6search11structQuery7options10completionAA10TaskHandle_pAA010StructuredG0V_AA0C7OptionsVyAA0C5ErrorOSg_SayAA5PlaceCGSgtctF">search(structQuery:<wbr/>options:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous request to search for places. The user submits a <code><a href="sdk-for-ios-navigate-api-reference-structs-structuredquery">StructuredQuery</a></code>
that returns places adhering to the constraints provided in <code><a href="sdk-for-ios-navigate-api-reference-structs-structuredquery">StructuredQuery</a></code>.
For example, when user wants results of type street for a text query <code>Invalidenstraße</code> in <code>Berlin</code>, it can be searched
by preparing <code><a href="sdk-for-ios-navigate-api-reference-structs-structuredquery">StructuredQuery</a></code> providing <code><a href="../Structs/StructuredQuery.html#/s:7heresdk15StructuredQueryV5querySSvp">StructuredQuery.query</a></code> as <code>Invalidenstraße</code>,
<code><a href="../Structs/StructuredQuery.html#/s:7heresdk15StructuredQueryV10areaCenterAA14GeoCoordinatesVvp">StructuredQuery.areaCenter</a></code>, <code><a href="../Structs/StructuredQuery/AddressElements.html#/s:7heresdk15StructuredQueryV15AddressElementsV7countrySSSgvp">StructuredQuery.AddressElements.country</a></code> as <code>Germany</code>,
<code><a href="../Structs/StructuredQuery/AddressElements.html#/s:7heresdk15StructuredQueryV15AddressElementsV4citySSSgvp">StructuredQuery.AddressElements.city</a></code> as <code>Berlin</code> and <code><a href="sdk-for-ios-navigate-api-reference-structs-structuredquery-resulttype">StructuredQuery.ResultType</a></code> as <code>STREET</code>.
The results will be presented only from the given geographical area.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">search</span><span class="p">(</span><span class="n">structQuery</span> <span class="nv">query</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-structuredquery">StructuredQuery</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-searchoptions">SearchOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Search.html#/s:7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>query</em>
</code>
</td>
<td>
<div>
<p>Desired structured query to search.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>options</em>
</code>
</td>
<td>
<div>
<p>Search options.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>Callback which receives the result on the main thread.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19OfflineSearchEngineC7suggest11structQuery7options10completionAA10TaskHandle_pAA010StructuredG0V_AA0C7OptionsVyAA0C5ErrorOSg_SayAA10SuggestionCGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/suggest(structQuery:options:completion:)"></a>
<a class="token" href="#/s:7heresdk19OfflineSearchEngineC7suggest11structQuery7options10completionAA10TaskHandle_pAA010StructuredG0V_AA0C7OptionsVyAA0C5ErrorOSg_SayAA10SuggestionCGSgtctF">suggest(structQuery:<wbr/>options:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous request to suggest places for a <code><a href="sdk-for-ios-navigate-api-reference-structs-structuredquery">StructuredQuery</a></code> built with address elements and
returns candidate suggestions sorted by relevance.
For example, when user wants suggestions of type street for a text query <code>Invalidenstraße</code> in <code>Berlin</code>, it can be searched
by preparing <code><a href="sdk-for-ios-navigate-api-reference-structs-structuredquery">StructuredQuery</a></code> providing <code><a href="../Structs/StructuredQuery.html#/s:7heresdk15StructuredQueryV5querySSvp">StructuredQuery.query</a></code> as <code>Invalidenstraße</code>,
<code><a href="../Structs/StructuredQuery.html#/s:7heresdk15StructuredQueryV10areaCenterAA14GeoCoordinatesVvp">StructuredQuery.areaCenter</a></code>, <code><a href="../Structs/StructuredQuery/AddressElements.html#/s:7heresdk15StructuredQueryV15AddressElementsV7countrySSSgvp">StructuredQuery.AddressElements.country</a></code> as <code>Germany</code>,
<code><a href="../Structs/StructuredQuery/AddressElements.html#/s:7heresdk15StructuredQueryV15AddressElementsV4citySSSgvp">StructuredQuery.AddressElements.city</a></code> as <code>Berlin</code> and <code><a href="sdk-for-ios-navigate-api-reference-structs-structuredquery-resulttype">StructuredQuery.ResultType</a></code> as <code>STREET</code>.
The suggestions will be presented only from the given geographical area.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">suggest</span><span class="p">(</span><span class="n">structQuery</span> <span class="nv">query</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-structuredquery">StructuredQuery</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-searchoptions">SearchOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Search.html#/s:7heresdk24SuggestCompletionHandlera">SuggestCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>query</em>
</code>
</td>
<td>
<div>
<p>Desired structured query to search.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>options</em>
</code>
</td>
<td>
<div>
<p>Search options.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>Callback which receives the result on the main thread.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19OfflineSearchEngineC15setIndexOptions03sdkD07options8listenerAA0bcF0C5ErrorOSgAA09SDKNativeD0C_AI0G0VAA0bcF8Listener_ptFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setIndexOptions(sdkEngine:options:listener:)"></a>
<a class="token" href="#/s:7heresdk19OfflineSearchEngineC15setIndexOptions03sdkD07options8listenerAA0bcF0C5ErrorOSgAA09SDKNativeD0C_AI0G0VAA0bcF8Listener_ptFZ">setIndexOptions(sdkEngine:<wbr/>options:<wbr/>listener:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Enables or disables indexing.
When indexing is enabled, HERE SDK will create a detailed index over persistent
map data and update it as needed.
A detailed index enables finding data faster and over entire persistent map.
Creating an index takes time, but usually no more than a few seconds up to a couple of
minutes, depending on persistent map size.
As the feature is improved, the indexing time will improve.
Also please note that this is a heavy processing task.
The stored index increases the space taken by offline maps by around 2-5%.
This may also improve in future versions.</p>
<p>Indexing is disabled by default.
If you want it enabled, make sure to call setIndexOptions with <code><a href="../Classes/OfflineSearchIndex/Options.html#/s:7heresdk18OfflineSearchIndexC7OptionsV7enabledSbvp">OfflineSearchIndex.Options.enabled</a></code> as <code>true</code> before
any operations in <code><a href="sdk-for-ios-navigate-api-reference-classes-mapdownloader">MapDownloader</a></code> or <code><a href="sdk-for-ios-navigate-api-reference-classes-mapupdater">MapUpdater</a></code> that modify the persistent map.
Calling setIndexOptions may also create or remove map index to match the previously
installed map regions. If the matching index for installed map regions is found, then
indexing is skipped.
While a new index is being created, <code>OfflineSearchEngine</code> functionality can still be used.
However, without a valid index in place yet, it operates as though indexing is disabled.
If <code><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></code> is disposed during indexing (for example, by closing the app),
the indexing is cancelled. Recreating <code><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></code> and enabling indexing will
ensure that index is created.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">setIndexOptions</span><span class="p">(</span><span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-offlinesearchindex">OfflineSearchIndex</a></span><span class="o">.</span><span class="kt">Options</span><span class="p">,</span> <span class="nv">listener</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-offlinesearchindexlistener">OfflineSearchIndexListener</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-offlinesearchindex">OfflineSearchIndex</a></span><span class="o">.</span><span class="kt">Error</span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>sdkEngine</em>
</code>
</td>
<td>
<div>
<p>Indexing is enabled and disabled per SDKNativeEngine instance.
The index is created inside the related <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">SDKOptions.persistentMapStoragePath</a></code>.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>options</em>
</code>
</td>
<td>
<div>
<p>Sets indexing options.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>listener</em>
</code>
</td>
<td>
<div>
<p>The listener that will receive updates about indexing process.
When <code><a href="../Classes/OfflineSearchIndex/Options.html#/s:7heresdk18OfflineSearchIndexC7OptionsV7enabledSbvp">OfflineSearchIndex.Options.enabled</a></code> is true, SDK would store listener and the listener will receive updates
about indexing progress every time it is performed.
When <code><a href="../Classes/OfflineSearchIndex/Options.html#/s:7heresdk18OfflineSearchIndexC7OptionsV7enabledSbvp">OfflineSearchIndex.Options.enabled</a></code> is false, SDK would report indexing removal progress to the listener
one last time and remove storage of listener.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>An error in case there was one. It’s <code>nil</code> if the indexing listener could be
configured successfully.</p>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>
</body>
</html>

`
}</HTMLBlock>
