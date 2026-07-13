---
title: "W3WSearchCallback typedef - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-w3wsearchcallback"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">W3WSearchCallback</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">W3WSearchCallback</span> = <span class="returntype">void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-searchError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-w3wsearcherror">W3WSearchError</a>?</span> <span class="parameter-name">searchError</span>, </span><span id="sdk-for-flutter-navigate-param-square" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-w3wsquare-class">W3WSquare</a>?</span> <span class="parameter-name">square</span></span>)</span></span>

</div>

<div class="section desc markdown">

The method that will be called on the main thread when a search operation in `W3WSearchEngine` has been completed.

- `searchError` The w3w search error.

- `square` The w3w square.

</div>

## Implementation

``` dart
typedef W3WSearchCallback = void Function(W3WSearchError? searchError, W3WSquare? square);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

