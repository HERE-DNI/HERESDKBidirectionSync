---
title: "searchByText method - SearchInterface class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-searchinterface-searchbytext"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/SearchInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">searchByText</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">searchByText</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-searchByText-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-textquery-class">TextQuery</a></span> <span class="parameter-name">query</span>, </span>
2.  <span id="sdk-for-flutter-explore-searchByText-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span>
3.  <span id="sdk-for-flutter-explore-searchByText-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchcallback">SearchCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Performs an asynchronous text query search for <a href="sdk-for-flutter-explore-search-place-class">Place</a> instances within a given <a href="sdk-for-flutter-explore-search-textqueryarea-class">TextQueryArea</a>.

The returned places are sorted by relevance.

- `query` Desired free-form text query to search.

- `options` Search options.

- `callback` Callback which receives the result on the main thread.

Returns <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle searchByText(TextQuery query, SearchOptions options, SearchCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

