---
title: "Untitled"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-set-custom-option"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- set-custom-option.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="member" id="content" pageids="API Reference::com.here.sdk.search/SearchEngine/setCustomOption/#kotlin.String#kotlin.String/PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine/setCustomOption</div>
<div class="cover">
<h1 class="cover">set<wbr/>Custom<wbr/>Option</h1>
</div>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-set-custom-option(name: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, value: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-error?</div><p class="paragraph">Sets a custom option for search backend queries. This allows more control over the behavior of the search algorithm. Name has the format <endpoint_name>.<option_name>, for example "discover.show". Values can be combined for the same name by using a comma, for example "truck,fuel". The custom option is applied only for the endpoint that is specified as prefix in <code class="lang-kotlin">name</code>. Some of the supported name/value options are:</option_name></endpoint_name></p><ul><li><p class="paragraph">name = "revgeocode.with", value = "unnamedStreets" enables the retrieval of access points on unnamed streets.</p></li><li><p class="paragraph">name = "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show", value = "truck" enables retreival of truck amenities. <strong>Note:</strong> Only participants of the closed-alpha group can get access from HERE to use this feature, otherwise, a /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-error-f-o-r-b-i-d-d-e-n will be propagated in callbacks.</p></li><li><p class="paragraph">name = "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show", value = "fuel" enables retreival of fuel station details. <strong>Note:</strong> Only participants of the closed-alpha group can get access from HERE to use this feature, otherwise, a /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-error-f-o-r-b-i-d-d-e-n will be propagated in callbacks.</p></li><li><p class="paragraph">name = "lookup.show" or "discover.show" or "browse.show", value = "ev" enables retreival of EV charging station details.</p></li><li><p class="paragraph">name = "lookup.show" or "discover.show" or "browse.show", value = "eMobilityServiceProviders" enables retreival of e-Mobility Service Providers details.</p></li><li><p class="paragraph">name = "lookup.show" or "discover.show" or "browse.show", value = "tripadvisor" adds images, ratings, and editorials from Tripadvisor (TM). <strong>Note:</strong> Only clients with a license with TripAdvisor for rich content will actually get it. If this licence is missing, TripAdvisor rich content will be missing, with no error reported. This content is only added to top 10 search results. If more results are returned, they will be missing rich TripAdvisor content.</p></li><li><p class="paragraph">name = "lookup.datasets" or "discover.datasets" or "browse.datasets" or "autosuggest.datasets", value = <your_dataset_hrn> enables ingesting and searching of private POIs. <strong>Note:</strong> Only participants of the search customization can get access from HERE to use this feature, otherwise, a /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-error-i-n-v-a-l-i-d-c-u-s-t-o-m-o-p-t-i-o-n-f-o-r-m-a-t will be propagated in callbacks.</your_dataset_hrn></p></li><li><p class="paragraph">name = "discover.ranking" or "browse.ranking", value = "excursionDistance" enables balanced distribution of results for search in <code class="lang-kotlin">GeoCorridor</code>. Constraint: using this parameter when searching an area that is not a <code class="lang-kotlin">GeoCorridor</code> generates an error /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-error-b-a-d-r-e-q-u-e-s-t. <strong>Note:</strong> It is recommended to use /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-options-distributed-results instead. For a complete list of available endpoints, parameter names and their valid values, refer to <a href="https://www.here.com/docs/bundle/batch-api-developer-guide/page/topics/constructing-request.html">HERE Geocoding &amp; Search API v7</a>. <strong>Note:</strong> It's easy to set a wrong option that makes queries invalid, so make sure you read and understand the backend documentation.</p></li></ul><h4 class="">Return</h4><p class="paragraph">Error in case when setting the option fails.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>name</u></div></div><div><div class="title"><p class="paragraph">Option name in the format <endpoint_name>.<option_name>, for example "discover.show".</option_name></endpoint_name></p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>value</u></div></div><div><div class="title"><p class="paragraph">Option value.</p></div></div></div></div></div></div></div>
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
