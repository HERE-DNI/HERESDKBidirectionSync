---
title: "PlaceIdSearchCallback typedef - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-placeidsearchcallback"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">PlaceIdSearchCallback</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">PlaceIdSearchCallback</span> = <span class="returntype">void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-searchError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a>?</span> <span class="parameter-name">searchError</span>, </span><span id="sdk-for-flutter-navigate-param-place" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-place-class">Place</a>?</span> <span class="parameter-name">place</span></span>)</span></span>

</div>

<div class="section desc markdown">

The method will be called on the main thread when a search by id call has been completed.

- `searchError` The search error.

- `place` The place.

</div>

## Implementation

``` dart
typedef PlaceIdSearchCallback = void Function(SearchError? searchError, Place? place);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

