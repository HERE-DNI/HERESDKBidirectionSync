---
title: "searchByWords method - W3WSearchEngine class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-w3wsearchengine-searchbywords"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- searchByWords.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/W3WSearchEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">searchByWords</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">searchByWords</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-searchByWords-param-words" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">words</span>, </span>
2.  <span id="sdk-for-flutter-navigate-searchByWords-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-w3wsearchcallback">W3WSearchCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Performs an asynchronous request to search for a <a href="sdk-for-flutter-navigate-search-w3wsquare-class">W3WSquare</a> that corresponds to the given 3 words.

- `words` A 3 word address as a string. It must be three words separated with dots or a japanese middle dot character (・). Words separated by spaces will be rejected. Optionally, the 3 word address can be prefixed with ///.

- `callback` Callback which receives the result on the main thread.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that can be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle searchByWords(String words, W3WSearchCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
