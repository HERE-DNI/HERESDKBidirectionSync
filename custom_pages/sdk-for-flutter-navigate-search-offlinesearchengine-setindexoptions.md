---
title: "setIndexOptions method - OfflineSearchEngine class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-offlinesearchengine-setindexoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setIndexOptions.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/OfflineSearchEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setIndexOptions</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-search-offlinesearchindexerror">OfflineSearchIndexError</a>?</span> <span class="name">setIndexOptions</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setIndexOptions-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span>, </span>
2.  <span id="sdk-for-flutter-navigate-setIndexOptions-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-offlinesearchindexoptions-class">OfflineSearchIndexOptions</a></span> <span class="parameter-name">options</span>, </span>
3.  <span id="sdk-for-flutter-navigate-setIndexOptions-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-offlinesearchindexlistener-class">OfflineSearchIndexListener</a></span> <span class="parameter-name">listener</span></span>

)

</div>

<div class="section desc markdown">

Enables or disables indexing.

When indexing is enabled, HERE SDK will create a detailed index over persistent map data and update it as needed. A detailed index enables finding data faster and over entire persistent map. Creating an index takes time, but usually no more than a few seconds up to a couple of minutes, depending on persistent map size. As the feature is improved, the indexing time will improve. Also please note that this is a heavy processing task. The stored index increases the space taken by offline maps by around 2-5%. This may also improve in future versions.

Indexing is disabled by default. If you want it enabled, make sure to call setIndexOptions with `OfflineSearchIndex.Options.enabled` as `true` before any operations in `MapDownloader` or `MapUpdater` that modify the persistent map. Calling setIndexOptions may also create or remove map index to match the previously installed map regions. If the matching index for installed map regions is found, then indexing is skipped. While a new index is being created, `OfflineSearchEngine` functionality can still be used. However, without a valid index in place yet, it operates as though indexing is disabled. If `SDKNativeEngine` is disposed during indexing (for example, by closing the app), the indexing is cancelled. Recreating `SDKNativeEngine` and enabling indexing will ensure that index is created.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

- `sdkEngine` Indexing is enabled and disabled per SDKNativeEngine instance. The index is created inside the related <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a>.

- `options` Sets indexing options.

- `listener` The listener that will receive updates about indexing process. When `OfflineSearchIndex.Options.enabled` is true, SDK would store listener and the listener will receive updates about indexing progress every time it is performed. When `OfflineSearchIndex.Options.enabled` is false, SDK would report indexing removal progress to the listener one last time and remove storage of listener.

Returns <a href="sdk-for-flutter-navigate-search-offlinesearchindexerror">OfflineSearchIndexError?</a>. An error in case there was one.

It's `null` if the indexing listener could be configured successfully.

</div>

## Implementation

``` dart
static OfflineSearchIndexError? setIndexOptions(SDKNativeEngine sdkEngine, OfflineSearchIndexOptions options, OfflineSearchIndexListener listener) => $prototype.setIndexOptions(sdkEngine, options, listener);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
