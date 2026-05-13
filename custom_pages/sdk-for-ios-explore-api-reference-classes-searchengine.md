---
title: "Untitled"
slug: "sdk-for-ios-explore-api-reference-classes-searchengine"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- SearchEngine.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/SearchEngine"></a>
<a title="SearchEngine Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-search">Search</a>
<img alt="" id="carat" src="../img/carat.png"/>
        SearchEngine Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SearchEngine</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">SearchEngine</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-searchinterface">SearchInterface</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SearchEngine</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SearchEngine</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>The SearchEngine API unlocks the search, geocoding and suggesting capabilities of HERE services
to provide developers with unmatched flexibility to create differentiating location-enabled
applications. It enables to search for HERE points of interests, forward and reverse
geocode addresses and geographic coordinates from the HERE map and search for suggested addresses
or place candidates based on incomplete or misspelled queries.</p>
<p>It also allows to search along a given <code><a href="sdk-for-ios-explore-api-reference-..-structs-geopolyline">GeoPolyline</a></code> set inside a <code><a href="sdk-for-ios-explore-api-reference-..-structs-geocorridor">GeoCorridor</a></code>
as part of a <code><a href="sdk-for-ios-explore-api-reference-..-structs-textquery">TextQuery</a></code>.</p>
<p>The SearchEngine API requires an online connection to execute the requests.</p>
<p><strong>Note:</strong> All methods are provided in two flavors. One uses a <code><a href="../Search.html#/s:7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a></code> and the
other uses a <code><a href="../Search.html#/s:7heresdk31SearchExtendedCompletionHandlera">SearchExtendedCompletionHandler</a></code>: The later adds a <code><a href="sdk-for-ios-explore-api-reference-..-structs-responsedetails">ResponseDetails</a></code> result type
that provides the <code>requestId</code> of a search request and a <code>correlationId</code> to identify multiple,
related queries. This may be useful for debug purposes.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12SearchEngineCACyKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk12SearchEngineCACyKcfc">init()</a>
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
<a name="/s:7heresdk12SearchEngineCyAcA09SDKNativeC0CKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk12SearchEngineCyAcA09SDKNativeC0CKcfc">init(_:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
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
<a name="/s:7heresdk12SearchEngineC12searchByText_7options10completionAA10TaskHandle_pAA0F5QueryV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/searchByText(_:options:completion:)"></a>
<a class="token" href="#/s:7heresdk12SearchEngineC12searchByText_7options10completionAA10TaskHandle_pAA0F5QueryV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgtctF">searchByText(_:<wbr/>options:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous text query search for <code><a href="sdk-for-ios-explore-api-reference-..-classes-place">Place</a></code> instances within a given <code><a href="sdk-for-ios-explore-api-reference-..-structs-textquery-area">TextQuery.Area</a></code>.
The returned places are sorted by relevance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">searchByText</span><span class="p">(</span><span class="n">_</span> <span class="nv">query</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-textquery">TextQuery</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-searchoptions">SearchOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Search.html#/s:7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk12SearchEngineC15searchByAddress_7options10completionAA10TaskHandle_pAA0F5QueryV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/searchByAddress(_:options:completion:)"></a>
<a class="token" href="#/s:7heresdk12SearchEngineC15searchByAddress_7options10completionAA10TaskHandle_pAA0F5QueryV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgtctF">searchByAddress(_:<wbr/>options:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous address query search for <code><a href="sdk-for-ios-explore-api-reference-..-classes-place">Place</a></code> instances.
This is the same type of search as forward geocoding, except that more data is returned
than just the geographic coordinates of a given address. Note that an address can
belong to more than one <code><a href="sdk-for-ios-explore-api-reference-..-classes-place">Place</a></code> result, although all found places will
share the same geographic coordinates.
The returned places are sorted by relevance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">searchByAddress</span><span class="p">(</span><span class="n">_</span> <span class="nv">query</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-addressquery">AddressQuery</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-searchoptions">SearchOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Search.html#/s:7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk12SearchEngineC16searchByCategory_7options10completionAA10TaskHandle_pAA0F5QueryV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/searchByCategory(_:options:completion:)"></a>
<a class="token" href="#/s:7heresdk12SearchEngineC16searchByCategory_7options10completionAA10TaskHandle_pAA0F5QueryV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgtctF">searchByCategory(_:<wbr/>options:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous category search for <code><a href="sdk-for-ios-explore-api-reference-..-classes-place">Place</a></code> instances.
A list containing at least one <code><a href="sdk-for-ios-explore-api-reference-..-classes-placecategory">PlaceCategory</a></code> must be provided
as part of the <code>searchByCategory(...).query</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">searchByCategory</span><span class="p">(</span><span class="n">_</span> <span class="nv">query</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-categoryquery">CategoryQuery</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-searchoptions">SearchOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Search.html#/s:7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk12SearchEngineC19searchByCoordinates_7options10completionAA10TaskHandle_pAA03GeoF0V_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/searchByCoordinates(_:options:completion:)"></a>
<a class="token" href="#/s:7heresdk12SearchEngineC19searchByCoordinates_7options10completionAA10TaskHandle_pAA03GeoF0V_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgtctF">searchByCoordinates(_:<wbr/>options:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous search for <code><a href="sdk-for-ios-explore-api-reference-..-classes-place">Place</a></code> instances based on the given
geographic coordinates.
This is the same search type as reverse geocoding, except that more data is returned
than just the <code><a href="sdk-for-ios-explore-api-reference-..-structs-address">Address</a></code> related to the given coordinates.
Note that more than one <code><a href="sdk-for-ios-explore-api-reference-..-classes-place">Place</a></code> can be related to the given coordinates.
The returned places are sorted by relevance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">searchByCoordinates</span><span class="p">(</span><span class="n">_</span> <span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geocoordinates">GeoCoordinates</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-searchoptions">SearchOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Search.html#/s:7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk12SearchEngineC15searchByPlaceId_12languageCode10completionAA10TaskHandle_pAA0fG5QueryV_AA08LanguageI0OSgyAA0B5ErrorOSg_AA0F0CSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/searchByPlaceId(_:languageCode:completion:)"></a>
<a class="token" href="#/s:7heresdk12SearchEngineC15searchByPlaceId_12languageCode10completionAA10TaskHandle_pAA0fG5QueryV_AA08LanguageI0OSgyAA0B5ErrorOSg_AA0F0CSgtctF">searchByPlaceId(_:<wbr/>languageCode:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous search for a <code><a href="sdk-for-ios-explore-api-reference-..-classes-place">Place</a></code> based on its ID and
<code><a href="sdk-for-ios-explore-api-reference-..-enums-languagecode">LanguageCode</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">searchByPlaceId</span><span class="p">(</span><span class="n">_</span> <span class="nv">query</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-placeidquery">PlaceIdQuery</a></span><span class="p">,</span> <span class="nv">languageCode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-languagecode">LanguageCode</a></span><span class="p">?,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Search.html#/s:7heresdk30PlaceIdSearchCompletionHandlera">PlaceIdSearchCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk12SearchEngineC19searchByPickedPlace_12languageCode10completionAA10TaskHandle_pAA0fG0V_AA08LanguageI0OSgyAA0B5ErrorOSg_AA0G0CSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/searchByPickedPlace(_:languageCode:completion:)"></a>
<a class="token" href="#/s:7heresdk12SearchEngineC19searchByPickedPlace_12languageCode10completionAA10TaskHandle_pAA0fG0V_AA08LanguageI0OSgyAA0B5ErrorOSg_AA0G0CSgtctF">searchByPickedPlace(_:<wbr/>languageCode:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous search for a <code><a href="sdk-for-ios-explore-api-reference-..-classes-place">Place</a></code> based on the content found in <code><a href="sdk-for-ios-explore-api-reference-..-structs-pickedplace">PickedPlace</a></code>.
If <code><a href="sdk-for-ios-explore-api-reference-..-structs-pickedplace">PickedPlace</a></code> data is obtained from the offline map, it may happen that the newer version
that is used by the online service represented by <code>SearchEngine</code> no longer contains the
related POI. In that case, <code><a href="../Enums/SearchError.html#/s:7heresdk11SearchErrorO14noResultsFoundyA2CmF">SearchError.noResultsFound</a></code> error is reported.
When that happens, you may try to obtain the POI from the offline map by calling
<code>OfflineSearchEngine.searchByPickedPlace</code>, only available for the Navigate license.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">searchByPickedPlace</span><span class="p">(</span><span class="n">_</span> <span class="nv">pickedPlace</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-pickedplace">PickedPlace</a></span><span class="p">,</span> <span class="nv">languageCode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-languagecode">LanguageCode</a></span><span class="p">?,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Search.html#/s:7heresdk30PlaceIdSearchCompletionHandlera">PlaceIdSearchCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk12SearchEngineC13suggestByText_7options10completionAA10TaskHandle_pAA0F5QueryV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA10SuggestionCGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/suggestByText(_:options:completion:)"></a>
<a class="token" href="#/s:7heresdk12SearchEngineC13suggestByText_7options10completionAA10TaskHandle_pAA0F5QueryV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA10SuggestionCGSgtctF">suggestByText(_:<wbr/>options:<wbr/>completion:<wbr/>)</a>
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
<code>SearchEngine</code> includes only the information that is relevant for autosuggest use cases.
Complete details can be obtained by searching with <code><a href="sdk-for-ios-explore-api-reference-..-structs-placeidquery">PlaceIdQuery</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">suggestByText</span><span class="p">(</span><span class="n">_</span> <span class="nv">query</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-textquery">TextQuery</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-searchoptions">SearchOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Search.html#/s:7heresdk24SuggestCompletionHandlera">SuggestCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk12SearchEngineC6search9textQuery7options10completionAA10TaskHandle_pAA04TextF0V_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgAA15ResponseDetailsVSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/search(textQuery:options:completion:)"></a>
<a class="token" href="#/s:7heresdk12SearchEngineC6search9textQuery7options10completionAA10TaskHandle_pAA04TextF0V_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgAA15ResponseDetailsVSgtctF">search(textQuery:<wbr/>options:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous request to do a text query search for <code><a href="sdk-for-ios-explore-api-reference-..-classes-place">Place</a></code> instances.
Optionally, search along a polyline, such as a route, by specifying a <code><a href="sdk-for-ios-explore-api-reference-..-structs-geocorridor">GeoCorridor</a></code>.
Provides candidate places sorted by relevance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">search</span><span class="p">(</span><span class="n">textQuery</span> <span class="nv">query</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-textquery">TextQuery</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-searchoptions">SearchOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Search.html#/s:7heresdk31SearchExtendedCompletionHandlera">SearchExtendedCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk12SearchEngineC6search12addressQuery7options10completionAA10TaskHandle_pAA07AddressF0V_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgAA15ResponseDetailsVSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/search(addressQuery:options:completion:)"></a>
<a class="token" href="#/s:7heresdk12SearchEngineC6search12addressQuery7options10completionAA10TaskHandle_pAA07AddressF0V_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgAA15ResponseDetailsVSgtctF">search(addressQuery:<wbr/>options:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous request to search for places based on a given address.
This is the same process as forward geocoding, except that more data is returned
than just the geographic coordinates of a given address. Note that an address can
belong to more than one <code><a href="sdk-for-ios-explore-api-reference-..-classes-place">Place</a></code> result, although all found places will
share the same geographic coordinates.
Provides candidate places sorted by relevance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">search</span><span class="p">(</span><span class="n">addressQuery</span> <span class="nv">query</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-addressquery">AddressQuery</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-searchoptions">SearchOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Search.html#/s:7heresdk31SearchExtendedCompletionHandlera">SearchExtendedCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk12SearchEngineC6search12placeIdQuery12languageCode10completionAA10TaskHandle_pAA05PlacefG0V_AA08LanguageI0OSgyAA0B5ErrorOSg_AA0M0CSgAA15ResponseDetailsVSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/search(placeIdQuery:languageCode:completion:)"></a>
<a class="token" href="#/s:7heresdk12SearchEngineC6search12placeIdQuery12languageCode10completionAA10TaskHandle_pAA05PlacefG0V_AA08LanguageI0OSgyAA0B5ErrorOSg_AA0M0CSgAA15ResponseDetailsVSgtctF">search(placeIdQuery:<wbr/>languageCode:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous request to search for a <code><a href="sdk-for-ios-explore-api-reference-..-classes-place">Place</a></code> based on its ID and
<code><a href="sdk-for-ios-explore-api-reference-..-enums-languagecode">LanguageCode</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">search</span><span class="p">(</span><span class="n">placeIdQuery</span> <span class="nv">query</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-placeidquery">PlaceIdQuery</a></span><span class="p">,</span> <span class="nv">languageCode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-languagecode">LanguageCode</a></span><span class="p">?,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Search.html#/s:7heresdk38PlaceIdSearchExtendedCompletionHandlera">PlaceIdSearchExtendedCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<p>The preferred language for the search results. When unset or unsupported language is
chosen, results will be returned in their local language.</p>
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
<a name="/s:7heresdk12SearchEngineC6search11coordinates7options10completionAA10TaskHandle_pAA14GeoCoordinatesV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgAA15ResponseDetailsVSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/search(coordinates:options:completion:)"></a>
<a class="token" href="#/s:7heresdk12SearchEngineC6search11coordinates7options10completionAA10TaskHandle_pAA14GeoCoordinatesV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgAA15ResponseDetailsVSgtctF">search(coordinates:<wbr/>options:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous request to search for places based on given geographic coordinates.
This is the same process as reverse geocoding, except that more data is returned
than just the <code><a href="sdk-for-ios-explore-api-reference-..-structs-address">Address</a></code> that belongs to given coordinates. Note that coordinates
can belong to more than one <code><a href="sdk-for-ios-explore-api-reference-..-classes-place">Place</a></code> result.
Provides candidate places sorted by relevance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">search</span><span class="p">(</span><span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geocoordinates">GeoCoordinates</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-searchoptions">SearchOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Search.html#/s:7heresdk31SearchExtendedCompletionHandlera">SearchExtendedCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk12SearchEngineC6search6circle7options10completionAA10TaskHandle_pAA9GeoCircleV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/search(circle:options:completion:)"></a>
<a class="token" href="#/s:7heresdk12SearchEngineC6search6circle7options10completionAA10TaskHandle_pAA9GeoCircleV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgtctF">search(circle:<wbr/>options:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous request to search for places based on given circular spatial filter.
This is the same process as reverse geocoding, except that more data is returned
than just the <code><a href="sdk-for-ios-explore-api-reference-..-structs-address">Address</a></code> that belongs to given coordinates. Note that coordinates
can belong to more than one <code><a href="sdk-for-ios-explore-api-reference-..-classes-place">Place</a></code> result.
Provides candidate places sorted by relevance and located inside the radius of filter.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">search</span><span class="p">(</span><span class="nv">circle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geocircle">GeoCircle</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-searchoptions">SearchOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Search.html#/s:7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>circle</em>
</code>
</td>
<td>
<div>
<p>The coordinates where to search and radius of the circular spatial filter.
Passed in form of <code><a href="sdk-for-ios-explore-api-reference-..-structs-geocircle">GeoCircle</a></code>.</p>
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
<a name="/s:7heresdk12SearchEngineC6search6circle7options10completionAA10TaskHandle_pAA9GeoCircleV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgAA15ResponseDetailsVSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/search(circle:options:completion:)"></a>
<a class="token" href="#/s:7heresdk12SearchEngineC6search6circle7options10completionAA10TaskHandle_pAA9GeoCircleV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgAA15ResponseDetailsVSgtctF">search(circle:<wbr/>options:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous request to search for places based on given circular spatial filter.
This is the same process as reverse geocoding, except that more data is returned
than just the <code><a href="sdk-for-ios-explore-api-reference-..-structs-address">Address</a></code> that belongs to given coordinates. Note that coordinates
can belong to more than one <code><a href="sdk-for-ios-explore-api-reference-..-classes-place">Place</a></code> result.
Provides candidate places sorted by relevance and located inside the radius of filter.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">search</span><span class="p">(</span><span class="nv">circle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geocircle">GeoCircle</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-searchoptions">SearchOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Search.html#/s:7heresdk31SearchExtendedCompletionHandlera">SearchExtendedCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>circle</em>
</code>
</td>
<td>
<div>
<p>The coordinates where to search and radius of the circular spatial filter.
Passed in form of <code><a href="sdk-for-ios-explore-api-reference-..-structs-geocircle">GeoCircle</a></code>.</p>
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
<a name="/s:7heresdk12SearchEngineC11sendRequest4href10completionAA10TaskHandle_pSS_yAA0B5ErrorOSg_SayAA5PlaceCGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/sendRequest(href:completion:)"></a>
<a class="token" href="#/s:7heresdk12SearchEngineC11sendRequest4href10completionAA10TaskHandle_pSS_yAA0B5ErrorOSg_SayAA5PlaceCGSgtctF">sendRequest(href:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous request by using the given href.
The href value can be obtained from <code><a href="sdk-for-ios-explore-api-reference-..-classes-suggestion">Suggestion</a></code> objects,
which are the result of successful call to <code><a href="../Classes/SearchEngine.html#/s:7heresdk12SearchEngineC7suggest9textQuery7options10completionAA10TaskHandle_pAA04TextF0V_AA0B7OptionsVyAA0B5ErrorOSg_SayAA10SuggestionCGSgAA15ResponseDetailsVSgtctF">SearchEngine.suggest(...)</a></code>.
Currently supports only /v1/discover path.
Provides candidate places sorted by relevance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">sendRequest</span><span class="p">(</span><span class="nv">href</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Search.html#/s:7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>href</em>
</code>
</td>
<td>
<div>
<p>The direct link.</p>
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
<a name="/s:7heresdk12SearchEngineC11sendRequest4href10completionAA10TaskHandle_pSS_yAA0B5ErrorOSg_SayAA5PlaceCGSgAA15ResponseDetailsVSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/sendRequest(href:completion:)"></a>
<a class="token" href="#/s:7heresdk12SearchEngineC11sendRequest4href10completionAA10TaskHandle_pSS_yAA0B5ErrorOSg_SayAA5PlaceCGSgAA15ResponseDetailsVSgtctF">sendRequest(href:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous request by using the given href.
The href value can be obtained from <code><a href="sdk-for-ios-explore-api-reference-..-classes-suggestion">Suggestion</a></code> objects,
which are the result of successful call to <code><a href="../Classes/SearchEngine.html#/s:7heresdk12SearchEngineC7suggest9textQuery7options10completionAA10TaskHandle_pAA04TextF0V_AA0B7OptionsVyAA0B5ErrorOSg_SayAA10SuggestionCGSgAA15ResponseDetailsVSgtctF">SearchEngine.suggest(...)</a></code>.
Currently supports only /v1/discover path.
Provides candidate places sorted by relevance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">sendRequest</span><span class="p">(</span><span class="nv">href</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Search.html#/s:7heresdk31SearchExtendedCompletionHandlera">SearchExtendedCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>href</em>
</code>
</td>
<td>
<div>
<p>The direct link.</p>
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
<a name="/s:7heresdk12SearchEngineC6search13categoryQuery7options10completionAA10TaskHandle_pAA08CategoryF0V_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgAA15ResponseDetailsVSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/search(categoryQuery:options:completion:)"></a>
<a class="token" href="#/s:7heresdk12SearchEngineC6search13categoryQuery7options10completionAA10TaskHandle_pAA08CategoryF0V_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgAA15ResponseDetailsVSgtctF">search(categoryQuery:<wbr/>options:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous request to do a category search for <code><a href="sdk-for-ios-explore-api-reference-..-classes-place">Place</a></code> instances.
A list containing at least one <code><a href="sdk-for-ios-explore-api-reference-..-classes-placecategory">PlaceCategory</a></code> must be provided
as part of the <code>SearchEngine.search(CategoryQuery, SearchOptions, SearchExtendedCompletionHandler).query</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">search</span><span class="p">(</span><span class="n">categoryQuery</span> <span class="nv">query</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-categoryquery">CategoryQuery</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-searchoptions">SearchOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Search.html#/s:7heresdk31SearchExtendedCompletionHandlera">SearchExtendedCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk12SearchEngineC7suggest9textQuery7options10completionAA10TaskHandle_pAA04TextF0V_AA0B7OptionsVyAA0B5ErrorOSg_SayAA10SuggestionCGSgAA15ResponseDetailsVSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/suggest(textQuery:options:completion:)"></a>
<a class="token" href="#/s:7heresdk12SearchEngineC7suggest9textQuery7options10completionAA10TaskHandle_pAA04TextF0V_AA0B7OptionsVyAA0B5ErrorOSg_SayAA10SuggestionCGSgAA15ResponseDetailsVSgtctF">suggest(textQuery:<wbr/>options:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous request to suggest places for text queries and
returns candidate suggestions sorted by relevance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">suggest</span><span class="p">(</span><span class="n">textQuery</span> <span class="nv">query</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-textquery">TextQuery</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-searchoptions">SearchOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Search.html#/s:7heresdk32SuggestExtendedCompletionHandlera">SuggestExtendedCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk12SearchEngineC15setCustomOption4name5valueAA0B5ErrorOSgSS_SStF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setCustomOption(name:value:)"></a>
<a class="token" href="#/s:7heresdk12SearchEngineC15setCustomOption4name5valueAA0B5ErrorOSgSS_SStF">setCustomOption(name:<wbr/>value:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets a custom option for search backend queries. This allows more control over the behavior
of the search algorithm.
Name has the format <endpoint_name>.<option_name>, for example “discover.show”.
Values can be combined for the same name by using a comma, for example “truck,fuel”.
The custom option is applied only for the endpoint that is specified as prefix in <code>name</code>.
Some of the supported name/value options are:</option_name></endpoint_name></p>
<ul>
<li>name = “revgeocode.with”, value = “unnamedStreets” enables the retrieval of access points
on unnamed streets.</li>
<li>name = “lookup.show” or “discover.show” or “autosuggest.show” or “browse.show”, value = “truck”
enables retreival of truck amenities.
<strong>Note:</strong> Only participants of the closed-alpha group can get access from HERE to use this feature,
otherwise, a <code><a href="../Enums/SearchError.html#/s:7heresdk11SearchErrorO9forbiddenyA2CmF">SearchError.forbidden</a></code> will be propagated in callbacks.</li>
<li>name = “lookup.show” or “discover.show” or “autosuggest.show” or “browse.show”, value = “fuel”
enables retreival of fuel station details.
<strong>Note:</strong> Only participants of the closed-alpha group can get access from HERE to use this feature,
otherwise, a <code><a href="../Enums/SearchError.html#/s:7heresdk11SearchErrorO9forbiddenyA2CmF">SearchError.forbidden</a></code> will be propagated in callbacks.</li>
<li>name = “lookup.show” or “discover.show” or “browse.show”, value = “ev”
enables retreival of EV charging station details.</li>
<li>name = “lookup.show” or “discover.show” or “browse.show”, value = “eMobilityServiceProviders”
enables retreival of e-Mobility Service Providers details.</li>
<li>name = “lookup.show” or “discover.show” or “browse.show”, value = “tripadvisor”
adds images, ratings, and editorials from Tripadvisor ™.
<strong>Note:</strong> Only clients with a license with TripAdvisor for rich content will actually get it.
If this licence is missing, TripAdvisor rich content will be missing, with no error reported.
This content is only added to top 10 search results. If more results are returned,
they will be missing rich TripAdvisor content.</li>
<li>name = “lookup.datasets” or “discover.datasets” or “browse.datasets” or “autosuggest.datasets”,
value = <your_dataset_hrn> enables ingesting and searching of private POIs.
<strong>Note:</strong> Only participants of the search customization can get access from HERE to use this feature,
otherwise, a <code><a href="../Enums/SearchError.html#/s:7heresdk11SearchErrorO25invalidCustomOptionFormatyA2CmF">SearchError.invalidCustomOptionFormat</a></code> will be propagated in callbacks.</your_dataset_hrn></li>
<li>name = “discover.ranking” or “browse.ranking”, value = “excursionDistance”
enables balanced distribution of results for search in <code><a href="sdk-for-ios-explore-api-reference-..-structs-geocorridor">GeoCorridor</a></code>.
Constraint: using this parameter when searching an area that is not a <code><a href="sdk-for-ios-explore-api-reference-..-structs-geocorridor">GeoCorridor</a></code> generates
an error <code><a href="../Enums/SearchError.html#/s:7heresdk11SearchErrorO10badRequestyA2CmF">SearchError.badRequest</a></code>.
<strong>Note:</strong> It is recommended to use <code><a href="../Structs/SearchOptions.html#/s:7heresdk13SearchOptionsV18distributedResultsSbvp">SearchOptions.distributedResults</a></code> instead.
For a complete list of available endpoints, parameter names and their valid values, refer to
<a href="https://www.here.com/docs/bundle/batch-api-developer-guide/page/topics/constructing-request.html">HERE Geocoding &amp; Search API v7</a>.
<strong>Note:</strong> It’s easy to set a wrong option that makes queries invalid,
so make sure you read and understand the backend documentation.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setCustomOption</span><span class="p">(</span><span class="nv">name</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">value</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-searcherror">SearchError</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>name</em>
</code>
</td>
<td>
<div>
<p>Option name in the format <endpoint_name>.<option_name>, for example “discover.show”.</option_name></endpoint_name></p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>value</em>
</code>
</td>
<td>
<div>
<p>Option value.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Error in case when setting the option fails.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12SearchEngineC14setEVInterface13evcpInterfaceyAA08EVSearchG0_p_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setEVInterface(evcpInterface:)"></a>
<a class="token" href="#/s:7heresdk12SearchEngineC14setEVInterface13evcpInterfaceyAA08EVSearchG0_p_tF">setEVInterface(evcpInterface:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the EV interface through which search will interact with EVCP3.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setEVInterface</span><span class="p">(</span><span class="nv">evcpInterface</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-evsearchinterface">EVSearchInterface</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>evcpInterface</em>
</code>
</td>
<td>
<div>
<p>The EV search interface implementation.</p>
</div>
</td>
</tr>
</tbody>
</table>
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

</div>
`
}</HTMLBlock>
