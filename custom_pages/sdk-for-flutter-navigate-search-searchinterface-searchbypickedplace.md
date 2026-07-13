---
title: "searchByPickedPlace method - SearchInterface class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-searchinterface-searchbypickedplace"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- searchByPickedPlace.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/SearchInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">searchByPickedPlace</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">searchByPickedPlace</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-searchByPickedPlace-param-pickedPlace" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-pickedplace-class">PickedPlace</a></span> <span class="parameter-name">pickedPlace</span>, </span>
2.  <span id="sdk-for-flutter-navigate-searchByPickedPlace-param-languageCode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-languagecode">LanguageCode</a>?</span> <span class="parameter-name">languageCode</span>, </span>
3.  <span id="sdk-for-flutter-navigate-searchByPickedPlace-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-placeidsearchcallback">PlaceIdSearchCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Performs an asynchronous search for a <a href="sdk-for-flutter-navigate-search-place-class">Place</a> based on the content found in <a href="sdk-for-flutter-navigate-core-pickedplace-class">PickedPlace</a>.

If <a href="sdk-for-flutter-navigate-core-pickedplace-class">PickedPlace</a> data is obtained from the offline map, it may happen that the newer version that is used by the online service represented by `SearchEngine` no longer contains the related POI. In that case, <a href="sdk-for-flutter-navigate-search-searcherror">SearchError.noResultsFound</a> error is reported. When that happens, you may try to obtain the POI from the offline map by calling `OfflineSearchEngine.searchByPickedPlace`, only available for the Navigate license.

- `pickedPlace` The content picked from map.

- `languageCode` The preferred language for the search result. When unset or unsupported language is chosen, result will be returned in the local language.

- `callback` Callback which receives the result on the main thread.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle searchByPickedPlace(PickedPlace pickedPlace, LanguageCode? languageCode, PlaceIdSearchCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
