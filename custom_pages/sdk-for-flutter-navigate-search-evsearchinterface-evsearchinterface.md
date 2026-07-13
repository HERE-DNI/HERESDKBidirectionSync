---
title: "EVSearchInterface constructor - EVSearchInterface - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-evsearchinterface-evsearchinterface"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/EVSearchInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">EVSearchInterface</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">EVSearchInterface</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-searchLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="parameter-name">searchLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-evsearchcallback">EVSearchCallback</a></span> <span class="parameter-name"></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

Provides the abstract class for the `EVSearchEngine`.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
factory EVSearchInterface(
  TaskHandle Function(List<String>, EVSearchCallback) searchLambda,

) => EVSearchInterface$Lambdas(
  searchLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

