---
title: "EVSearchCallback typedef - search library - Dart API"
slug: "sdk-for-flutter-explore-search-evsearchcallback"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">EVSearchCallback</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">EVSearchCallback</span> = <span class="returntype">void Function<span class="signature">(<span id="sdk-for-flutter-explore-param-error" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-evsearcherror">EVSearchError</a>?</span> <span class="parameter-name">error</span>, </span><span id="sdk-for-flutter-explore-param-chargingLocations" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-evcharginglocation-class">EVChargingLocation</a></span>\></span>?</span> <span class="parameter-name">chargingLocations</span></span>)</span></span>

</div>

<div class="section desc markdown">

The method that will be called on the main thread when a search operation in `EVSearchEngine` has been completed.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

- `error` The ev search error.

- `chargingLocations` The ev charging locations.

</div>

## Implementation

``` dart
typedef EVSearchCallback = void Function(EVSearchError? error, List<EVChargingLocation>? chargingLocations);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

