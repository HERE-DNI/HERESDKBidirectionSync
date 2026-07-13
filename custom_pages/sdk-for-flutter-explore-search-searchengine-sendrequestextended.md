---
title: "sendRequestExtended method - SearchEngine class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-searchengine-sendrequestextended"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/SearchEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">sendRequestExtended</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">sendRequestExtended</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-sendRequestExtended-param-href" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">href</span>, </span>
2.  <span id="sdk-for-flutter-explore-sendRequestExtended-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchcallbackextended">SearchCallbackExtended</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Performs an asynchronous request by using the given href.

The href value can be obtained from <a href="sdk-for-flutter-explore-search-suggestion-class">Suggestion</a> objects, which are the result of successful call to <a href="sdk-for-flutter-explore-search-searchengine-suggestextended">SearchEngine.suggestExtended</a>. Currently supports only /v1/discover path. Provides candidate places sorted by relevance.

- `href` The direct link.

- `callback` Callback which receives result on the main thread.

Returns <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate execution of the task.

</div>

## Implementation

``` dart
TaskHandle sendRequestExtended(String href, SearchCallbackExtended callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

