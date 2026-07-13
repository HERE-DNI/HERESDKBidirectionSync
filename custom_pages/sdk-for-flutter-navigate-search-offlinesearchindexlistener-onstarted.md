---
title: "onStarted method - OfflineSearchIndexListener class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-offlinesearchindexlistener-onstarted"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/OfflineSearchIndexListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">onStarted</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">onStarted</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-onStarted-param-operation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-offlinesearchindexoperation">OfflineSearchIndexOperation</a></span> <span class="parameter-name">operation</span></span>

)

</div>

<div class="section desc markdown">

Called each time that the indexing has started.

It is triggered by changes to persistent map or by calling `OfflineSearchEngine.setIndexOptions`. If a valid index was previously created for the installed regions, no additional indexing is performed, so no notifications are sent. In this context, a valid index is the one that contains data for the exact versions of the installed map regions. When any of them is updated or new regions are downloaded or deleted, the index becomes invalid and is automatically rebuilt, as long as indexing has been enabled previously. Invoked on the main thread.

- `operation` Shows whether the index is being created or removed.

</div>

## Implementation

``` dart
void onStarted(OfflineSearchIndexOperation operation);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

