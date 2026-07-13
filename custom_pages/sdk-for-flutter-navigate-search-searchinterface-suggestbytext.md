---
title: "suggestByText method - SearchInterface class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-searchinterface-suggestbytext"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- suggestByText.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/SearchInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">suggestByText</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">suggestByText</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-suggestByText-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-textquery-class">TextQuery</a></span> <span class="parameter-name">query</span>, </span>
2.  <span id="sdk-for-flutter-navigate-suggestByText-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span>
3.  <span id="sdk-for-flutter-navigate-suggestByText-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-suggestcallback">SuggestCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Performs an asynchronous request to suggest places for text queries and returns suggestions sorted by relevance.

Note that while `OfflineSearchEngine` includes as many details as are available, `SearchEngine` includes only the information that is relevant for autosuggest use cases. Complete details can be obtained by searching with <a href="sdk-for-flutter-navigate-search-placeidquery-class">PlaceIdQuery</a>.

- `query` Desired text query to search.

- `options` Search options.

- `callback` Callback which receives the result on the main thread.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle suggestByText(TextQuery query, SearchOptions options, SuggestCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
