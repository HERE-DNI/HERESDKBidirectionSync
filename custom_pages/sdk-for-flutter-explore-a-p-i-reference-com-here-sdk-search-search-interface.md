---
title: "Untitled"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-interface"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.search/SearchInterface///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search/SearchInterface</div>
<div class="cover">
<h1 class="cover">Search<wbr/>Interface</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">interface /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-interface</div><p class="paragraph">Provides the interface for the online and offline search engines.</p><h4 class="">Inheritors</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine</div></div></div></div></div></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="searchByAddress" data-filterable-set=":modules:dokkaHtml/release" data-name="-859402960%2FFunctions%2F1617540583" id="-859402960%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-interface-search-by-address</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">abstract fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-interface-search-by-address(query: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-address-query, options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Performs an asynchronous address query search for /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place instances. This is the same type of search as forward geocoding, except that more data is returned than just the geographic coordinates of a given address. Note that an address can belong to more than one /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place result, although all found places will share the same geographic coordinates. The returned places are sorted by relevance.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="searchByCategory" data-filterable-set=":modules:dokkaHtml/release" data-name="1565320426%2FFunctions%2F1617540583" id="1565320426%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-interface-search-by-category</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">abstract fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-interface-search-by-category(query: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-category-query, options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Performs an asynchronous category search for /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place instances. A list containing at least one /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place-category must be provided as part of the com.here.sdk.search.SearchInterface.searchByCategory.query.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="searchByCoordinates" data-filterable-set=":modules:dokkaHtml/release" data-name="159331414%2FFunctions%2F1617540583" id="159331414%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-interface-search-by-coordinates</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">abstract fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-interface-search-by-coordinates(coordinates: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates, options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Performs an asynchronous search for /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place instances based on the given geographic coordinates. This is the same search type as reverse geocoding, except that more data is returned than just the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-address related to the given coordinates. Note that more than one /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place can be related to the given coordinates. The returned places are sorted by relevance.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="searchByPickedPlace" data-filterable-set=":modules:dokkaHtml/release" data-name="-415195880%2FFunctions%2F1617540583" id="-415195880%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-interface-search-by-picked-place</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">abstract fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-interface-search-by-picked-place(pickedPlace: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-picked-place, languageCode: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-language-code?, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place-id-search-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Performs an asynchronous search for a /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place based on the content found in /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-picked-place. If /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-picked-place data is obtained from the offline map, it may happen that the newer version that is used by the online service represented by <code class="lang-kotlin">SearchEngine</code> no longer contains the related POI. In that case, /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-error-n-o-r-e-s-u-l-t-s-f-o-u-n-d error is reported. When that happens, you may try to obtain the POI from the offline map by calling <code class="lang-kotlin">OfflineSearchEngine.searchByPickedPlace</code>, only available for the Navigate license.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="searchByPlaceId" data-filterable-set=":modules:dokkaHtml/release" data-name="-729501317%2FFunctions%2F1617540583" id="-729501317%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-interface-search-by-place-id</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">abstract fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-interface-search-by-place-id(query: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place-id-query, languageCode: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-language-code?, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place-id-search-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Performs an asynchronous search for a /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place based on its ID and /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-language-code.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="searchByText" data-filterable-set=":modules:dokkaHtml/release" data-name="972397708%2FFunctions%2F1617540583" id="972397708%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-interface-search-by-text</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">abstract fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-interface-search-by-text(query: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-text-query, options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Performs an asynchronous text query search for /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place instances within a given /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-text-query-area. The returned places are sorted by relevance.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="suggestByText" data-filterable-set=":modules:dokkaHtml/release" data-name="-1109038724%2FFunctions%2F1617540583" id="-1109038724%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-interface-suggest-by-text</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">abstract fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-interface-suggest-by-text(query: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-text-query, options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggest-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Performs an asynchronous request to suggest places for text queries and returns suggestions sorted by relevance.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="footer">
<a class="footer--button footer--button_go-to-top" href="#content" id="go-to-top-link"></a>
© 2026 Copyright

Generated by 
<a class="footer--link footer--link_external" href="https://github.com/Kotlin/dokka">
dokka
</a>

</div>
</div>

</div>

</div>
`
}</HTMLBlock>
