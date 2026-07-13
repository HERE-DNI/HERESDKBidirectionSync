---
title: "SearchCallbackExtended typedef - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-searchcallbackextended"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">SearchCallbackExtended</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">SearchCallbackExtended</span> = <span class="returntype">void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-searchError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a>?</span> <span class="parameter-name">searchError</span>, </span><span id="sdk-for-flutter-navigate-param-places" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-place-class">Place</a></span>\></span>?</span> <span class="parameter-name">places</span>, </span><span id="sdk-for-flutter-navigate-param-responseDetails" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-responsedetails-class">ResponseDetails</a>?</span> <span class="parameter-name">responseDetails</span></span>)</span></span>

</div>

<div class="section desc markdown">

The method will be called on the main thread when a search call has been completed.

The first argument indicates an error in case of a failure. The second argument contains the results. Both arguments cannot be `null` at the same time - or not `null` at the same time.

- `searchError` An error enum indicating what went wrong. It is `null` for an operation that succeeds.

- `places` The list of search results. It is `null` in case of an error.

- `responseDetails` Additional information provided with response. It is `null` in case of an error.

</div>

## Implementation

``` dart
typedef SearchCallbackExtended = void Function(SearchError? searchError, List<Place>? places, ResponseDetails? responseDetails);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

