---
title: "SearchCallback typedef - search library - Dart API"
slug: "sdk-for-flutter-explore-search-searchcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SearchCallback.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">SearchCallback</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">SearchCallback</span> = <span class="returntype">void Function<span class="signature">(<span id="sdk-for-flutter-explore-param-searchError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searcherror">SearchError</a>?</span> <span class="parameter-name">searchError</span>, </span><span id="sdk-for-flutter-explore-param-places" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-place-class">Place</a></span>\></span>?</span> <span class="parameter-name">places</span></span>)</span></span>

</div>

<div class="section desc markdown">

The method will be called on the main thread when a search call has been completed.

The first argument indicates an error in case of a failure. The second argument contains the results. Both arguments cannot be `null` at the same time - or not `null` at the same time.

- `searchError` An error enum indicating what went wrong. It is `null` for an operation that succeeds.

- `places` The list of search results. It is `null` in case of an error.

</div>

## Implementation

``` dart
typedef SearchCallback = void Function(SearchError? searchError, List<Place>? places);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
