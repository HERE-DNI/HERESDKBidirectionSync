---
title: "sendRequest method - SearchEngine class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-searchengine-sendrequest"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/SearchEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">sendRequest</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">sendRequest</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-sendRequest-param-href" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">href</span>, </span>
2.  <span id="sdk-for-flutter-navigate-sendRequest-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-searchcallback">SearchCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Performs an asynchronous request by using the given href.

The href value can be obtained from <a href="sdk-for-flutter-navigate-search-suggestion-class">Suggestion</a> objects, which are the result of successful call to <a href="sdk-for-flutter-navigate-search-searchengine-suggestextended">SearchEngine.suggestExtended</a>. Currently supports only /v1/discover path. Provides candidate places sorted by relevance.

- `href` The direct link.

- `callback` Callback which receives result on the main thread.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate execution of the task.

</div>

## Implementation

``` dart
TaskHandle sendRequest(String href, SearchCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

