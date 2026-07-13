---
title: "setCustomOption method - SearchEngine class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-searchengine-setcustomoption"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/SearchEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setCustomOption</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a>?</span> <span class="name">setCustomOption</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setCustomOption-param-name" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">name</span>, </span>
2.  <span id="sdk-for-flutter-navigate-setCustomOption-param-value" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">value</span></span>

)

</div>

<div class="section desc markdown">

Sets a custom option for search backend queries.

This allows more control over the behavior of the search algorithm. Name has the format \<endpoint_name\>.\<option_name\>, for example "discover.show". Values can be combined for the same name by using a comma, for example "truck,fuel". The custom option is applied only for the endpoint that is specified as prefix in `name`. Some of the supported name/value options are:

- name = "revgeocode.with", value = "unnamedStreets" enables the retrieval of access points on unnamed streets.

- name = "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show", value = "truck" enables retreival of truck amenities. **Note:** Only participants of the closed-alpha group can get access from HERE to use this feature, otherwise, a <a href="sdk-for-flutter-navigate-search-searcherror">SearchError.forbidden</a> will be propagated in callbacks.

- name = "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show", value = "fuel" enables retreival of fuel station details. **Note:** Only participants of the closed-alpha group can get access from HERE to use this feature, otherwise, a <a href="sdk-for-flutter-navigate-search-searcherror">SearchError.forbidden</a> will be propagated in callbacks.

- name = "lookup.show" or "discover.show" or "browse.show", value = "ev" enables retreival of EV charging station details.

- name = "lookup.show" or "discover.show" or "browse.show", value = "eMobilityServiceProviders" enables retreival of e-Mobility Service Providers details.

- name = "lookup.show" or "discover.show" or "browse.show", value = "tripadvisor" adds images, ratings, and editorials from Tripadvisor (TM). **Note:** Only clients with a license with TripAdvisor for rich content will actually get it. If this licence is missing, TripAdvisor rich content will be missing, with no error reported. This content is only added to top 10 search results. If more results are returned, they will be missing rich TripAdvisor content.

- name = "lookup.datasets" or "discover.datasets" or "browse.datasets" or "autosuggest.datasets", value = \<your_dataset_hrn\> enables ingesting and searching of private POIs. **Note:** Only participants of the search customization can get access from HERE to use this feature, otherwise, a <a href="sdk-for-flutter-navigate-search-searcherror">SearchError.invalidCustomOptionFormat</a> will be propagated in callbacks.

- name = "discover.ranking" or "browse.ranking", value = "excursionDistance" enables balanced distribution of results for search in `GeoCorridor`. Constraint: using this parameter when searching an area that is not a `GeoCorridor` generates an error <a href="sdk-for-flutter-navigate-search-searcherror">SearchError.badRequest</a>. **Note:** It is recommended to use <a href="sdk-for-flutter-navigate-search-searchoptions-distributedresults">SearchOptions.distributedResults</a> instead. For a complete list of available endpoints, parameter names and their valid values, refer to <a href="https://www.here.com/docs/bundle/batch-api-developer-guide/page/topics/constructing-request.html">HERE Geocoding & Search API v7</a>. **Note:** It's easy to set a wrong option that makes queries invalid, so make sure you read and understand the backend documentation.

- `name` Option name in the format \<endpoint_name\>.\<option_name\>, for example "discover.show".

- `value` Option value.

Returns <a href="sdk-for-flutter-navigate-search-searcherror">SearchError?</a>. Error in case when setting the option fails.

</div>

## Implementation

``` dart
SearchError? setCustomOption(String name, String value);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

