---
title: "searchByAddressElements method - OfflineSearchEngine class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-offlinesearchengine-searchbyaddresselements"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- searchByAddressElements.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/OfflineSearchEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">searchByAddressElements</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">searchByAddressElements</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-searchByAddressElements-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-structuredquery-class">StructuredQuery</a></span> <span class="parameter-name">query</span>, </span>
2.  <span id="sdk-for-flutter-navigate-searchByAddressElements-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span>
3.  <span id="sdk-for-flutter-navigate-searchByAddressElements-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-searchcallback">SearchCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Performs an asynchronous request to search for places.

The user submits a <a href="sdk-for-flutter-navigate-search-structuredquery-class">StructuredQuery</a> that returns places adhering to the constraints provided in <a href="sdk-for-flutter-navigate-search-structuredquery-class">StructuredQuery</a>. For example, when user wants results of type street for a text query `Invalidenstraße` in `Berlin`, it can be searched by preparing <a href="sdk-for-flutter-navigate-search-structuredquery-class">StructuredQuery</a> providing <a href="sdk-for-flutter-navigate-search-structuredquery-query">StructuredQuery.query</a> as `Invalidenstraße`, <a href="sdk-for-flutter-navigate-search-structuredquery-areacenter">StructuredQuery.areaCenter</a>, <a href="sdk-for-flutter-navigate-search-structuredqueryaddresselements-country">StructuredQueryAddressElements.country</a> as `Germany`, <a href="sdk-for-flutter-navigate-search-structuredqueryaddresselements-city">StructuredQueryAddressElements.city</a> as `Berlin` and <a href="sdk-for-flutter-navigate-search-structuredqueryresulttype">StructuredQueryResultType</a> as `STREET`. The results will be presented only from the given geographical area.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

- `query` Desired structured query to search.

- `options` Search options.

- `callback` Callback which receives the result on the main thread.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle searchByAddressElements(StructuredQuery query, SearchOptions options, SearchCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
