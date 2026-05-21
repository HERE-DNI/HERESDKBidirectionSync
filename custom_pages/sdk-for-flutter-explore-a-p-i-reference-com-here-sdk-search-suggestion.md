---
title: "Suggestion"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggestion"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.search/Suggestion///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search/Suggestion</div>
<div class="cover">
<h1 class="cover">Suggestion</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggestion : /sdk-for-flutter-explore-a-p-i-reference-com-here-native-base</div><p class="paragraph">Suggestion is meant to provide relevant suggestions to partial queries, like "restaur", "starbu", "eiffel". Represents a relevant response to user queries. Suggestions (please check /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggestion-type) are either: Place: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggestion-type-p-l-a-c-e Query: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggestion-type-c-h-a-i-n or /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggestion-type-c-a-t-e-g-o-r-y</p><p class="paragraph">With "Place" you get data for a concrete place in the world. With "Query" something to follow-up, a way to perform more focused search.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="Companion" data-filterable-set=":modules:dokkaHtml/release" data-name="622664301%2FClasslikes%2F1617540583" id="622664301%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggestion-companion</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggestion-companion</div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="PROPERTY">
<h2 class="">Properties</h2>
<div class="table"><a anchor-label="href" data-filterable-set=":modules:dokkaHtml/release" data-name="-336439319%2FProperties%2F1617540583" id="-336439319%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggestion-href</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggestion-href: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>?</div><div class="brief"><p class="paragraph">Direct URL for precise query. Available only for /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggestion-type-c-h-a-i-n and /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggestion-type-c-a-t-e-g-o-r-y. This is not supported in offline search.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="id" data-filterable-set=":modules:dokkaHtml/release" data-name="149596601%2FProperties%2F1617540583" id="149596601%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggestion-id</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggestion-id: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>?</div><div class="brief"><p class="paragraph">The unique id of suggested item. It can be used to query further information. For online search, suggestion of type /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggestion-type-p-l-a-c-e will have Suggestion.id same as Place.id. For offline search, only suggestion of type /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggestion-type-c-h-a-i-n, will have this property filled with identifier number of an associated chain. For example, the chain ID "8778" corresponds to the chain name "ABC Shop". For other types, /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggestion-type-p-l-a-c-e and /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggestion-type-c-a-t-e-g-o-r-y this property will be null.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="place" data-filterable-set=":modules:dokkaHtml/release" data-name="1948250751%2FProperties%2F1617540583" id="1948250751%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggestion-place</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggestion-place: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place?</div><div class="brief"><p class="paragraph">The suggested place. Available only for /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggestion-type-p-l-a-c-e.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="title" data-filterable-set=":modules:dokkaHtml/release" data-name="-566225330%2FProperties%2F1617540583" id="-566225330%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggestion-title</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggestion-title: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief"><p class="paragraph">The localized title for the suggestion.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="type" data-filterable-set=":modules:dokkaHtml/release" data-name="-435509574%2FProperties%2F1617540583" id="-435509574%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggestion-type</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggestion-type: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggestion-type</div><div class="brief"><p class="paragraph">Type of the suggestion.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="getHighlights" data-filterable-set=":modules:dokkaHtml/release" data-name="-126017519%2FFunctions%2F1617540583" id="-126017519%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggestion-get-highlights</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggestion-get-highlights(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a>&lt;@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html">JvmSuppressWildcards</a> /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-highlight-type, <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-index-range&gt;&gt;</div><div class="brief"><p class="paragraph">The text slices matching the input query.</p></div></div></div>
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
