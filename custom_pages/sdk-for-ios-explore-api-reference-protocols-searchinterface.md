---
title: "SearchInterface Protocol Reference"
slug: "sdk-for-ios-explore-api-reference-protocols-searchinterface"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- SearchInterface.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Protocol/SearchInterface"></a>
<a title="SearchInterface Protocol Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="sdk-for-ios-explore-api-reference-..-index">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-search">Search</a>
<img alt="" id="carat" src="../img/carat.png"/>
        SearchInterface Protocol Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public protocol SearchInterface : AnyObject</code></pre>
</div>
</div>
<p>Provides the protocol for the online and offline
search engines.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SearchInterfaceP12searchByText_7options10completionAA10TaskHandle_pAA0F5QueryV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/searchByText(_:options:completion:)"></a>
<a class="token" href="#/s:7heresdk15SearchInterfaceP12searchByText_7options10completionAA10TaskHandle_pAA0F5QueryV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgtctF">searchByText(_:<wbr/>options:<wbr/>completion:<wbr/>)</a>
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
<pre><code>@discardableResult
func searchByText(_ query: TextQuery, options: SearchOptions, completion: @escaping SearchCompletionHandler) -&gt; TaskHandle</code></pre>
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
<a name="/s:7heresdk15SearchInterfaceP15searchByAddress_7options10completionAA10TaskHandle_pAA0F5QueryV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/searchByAddress(_:options:completion:)"></a>
<a class="token" href="#/s:7heresdk15SearchInterfaceP15searchByAddress_7options10completionAA10TaskHandle_pAA0F5QueryV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgtctF">searchByAddress(_:<wbr/>options:<wbr/>completion:<wbr/>)</a>
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
<pre><code>@discardableResult
func searchByAddress(_ query: AddressQuery, options: SearchOptions, completion: @escaping SearchCompletionHandler) -&gt; TaskHandle</code></pre>
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
<a name="/s:7heresdk15SearchInterfaceP16searchByCategory_7options10completionAA10TaskHandle_pAA0F5QueryV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/searchByCategory(_:options:completion:)"></a>
<a class="token" href="#/s:7heresdk15SearchInterfaceP16searchByCategory_7options10completionAA10TaskHandle_pAA0F5QueryV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgtctF">searchByCategory(_:<wbr/>options:<wbr/>completion:<wbr/>)</a>
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
<pre><code>@discardableResult
func searchByCategory(_ query: CategoryQuery, options: SearchOptions, completion: @escaping SearchCompletionHandler) -&gt; TaskHandle</code></pre>
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
<a name="/s:7heresdk15SearchInterfaceP19searchByCoordinates_7options10completionAA10TaskHandle_pAA03GeoF0V_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/searchByCoordinates(_:options:completion:)"></a>
<a class="token" href="#/s:7heresdk15SearchInterfaceP19searchByCoordinates_7options10completionAA10TaskHandle_pAA03GeoF0V_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgtctF">searchByCoordinates(_:<wbr/>options:<wbr/>completion:<wbr/>)</a>
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
<pre><code>@discardableResult
func searchByCoordinates(_ coordinates: GeoCoordinates, options: SearchOptions, completion: @escaping SearchCompletionHandler) -&gt; TaskHandle</code></pre>
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
<a name="/s:7heresdk15SearchInterfaceP15searchByPlaceId_12languageCode10completionAA10TaskHandle_pAA0fG5QueryV_AA08LanguageI0OSgyAA0B5ErrorOSg_AA0F0CSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/searchByPlaceId(_:languageCode:completion:)"></a>
<a class="token" href="#/s:7heresdk15SearchInterfaceP15searchByPlaceId_12languageCode10completionAA10TaskHandle_pAA0fG5QueryV_AA08LanguageI0OSgyAA0B5ErrorOSg_AA0F0CSgtctF">searchByPlaceId(_:<wbr/>languageCode:<wbr/>completion:<wbr/>)</a>
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
<pre><code>@discardableResult
func searchByPlaceId(_ query: PlaceIdQuery, languageCode: LanguageCode?, completion: @escaping PlaceIdSearchCompletionHandler) -&gt; TaskHandle</code></pre>
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
<a name="/s:7heresdk15SearchInterfaceP19searchByPickedPlace_12languageCode10completionAA10TaskHandle_pAA0fG0V_AA08LanguageI0OSgyAA0B5ErrorOSg_AA0G0CSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/searchByPickedPlace(_:languageCode:completion:)"></a>
<a class="token" href="#/s:7heresdk15SearchInterfaceP19searchByPickedPlace_12languageCode10completionAA10TaskHandle_pAA0fG0V_AA08LanguageI0OSgyAA0B5ErrorOSg_AA0G0CSgtctF">searchByPickedPlace(_:<wbr/>languageCode:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous search for a <code><a href="sdk-for-ios-explore-api-reference-..-classes-place">Place</a></code> based on the content found in <code><a href="sdk-for-ios-explore-api-reference-..-structs-pickedplace">PickedPlace</a></code>.
If <code><a href="sdk-for-ios-explore-api-reference-..-structs-pickedplace">PickedPlace</a></code> data is obtained from the offline map, it may happen that the newer version
that is used by the online service represented by <code><a href="sdk-for-ios-explore-api-reference-..-classes-searchengine">SearchEngine</a></code> no longer contains the
related POI. In that case, <code><a href="../Enums/SearchError.html#/s:7heresdk11SearchErrorO14noResultsFoundyA2CmF">SearchError.noResultsFound</a></code> error is reported.
When that happens, you may try to obtain the POI from the offline map by calling
<code>OfflineSearchEngine.searchByPickedPlace</code>, only available for the Navigate license.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>@discardableResult
func searchByPickedPlace(_ pickedPlace: PickedPlace, languageCode: LanguageCode?, completion: @escaping PlaceIdSearchCompletionHandler) -&gt; TaskHandle</code></pre>
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
<a name="/s:7heresdk15SearchInterfaceP13suggestByText_7options10completionAA10TaskHandle_pAA0F5QueryV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA10SuggestionCGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/suggestByText(_:options:completion:)"></a>
<a class="token" href="#/s:7heresdk15SearchInterfaceP13suggestByText_7options10completionAA10TaskHandle_pAA0F5QueryV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA10SuggestionCGSgtctF">suggestByText(_:<wbr/>options:<wbr/>completion:<wbr/>)</a>
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
<code><a href="sdk-for-ios-explore-api-reference-..-classes-searchengine">SearchEngine</a></code> includes only the information that is relevant for autosuggest use cases.
Complete details can be obtained by searching with <code><a href="sdk-for-ios-explore-api-reference-..-structs-placeidquery">PlaceIdQuery</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>@discardableResult
func suggestByText(_ query: TextQuery, options: SearchOptions, completion: @escaping SuggestCompletionHandler) -&gt; TaskHandle</code></pre>
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



</div>
`
}</HTMLBlock>
