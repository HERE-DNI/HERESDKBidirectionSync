---
title: "SuggestCallback typedef - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-suggestcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SuggestCallback.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">SuggestCallback</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">SuggestCallback</span> = <span class="returntype">void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-searchError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a>?</span> <span class="parameter-name">searchError</span>, </span><span id="sdk-for-flutter-navigate-param-suggestions" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-suggestion-class">Suggestion</a></span>\></span>?</span> <span class="parameter-name">suggestions</span></span>)</span></span>

</div>

<div class="section desc markdown">

The method will be called on the main thread when a suggest call has been completed.

The first argument indicates an error in case of a failure. The second argument contains the results. Both arguments cannot be `null` at the same time - or not `null` at the same time.

- `searchError` An error enum indicating what went wrong. It is `null` for an operation that succeeds.

- `suggestions` The list of suggestion results. It is `null` in case of an error.

</div>

## Implementation

``` dart
typedef SuggestCallback = void Function(SearchError? searchError, List<Suggestion>? suggestions);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
