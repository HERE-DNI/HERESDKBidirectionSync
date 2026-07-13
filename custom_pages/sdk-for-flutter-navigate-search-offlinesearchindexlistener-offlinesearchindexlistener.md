---
title: "OfflineSearchIndexListener constructor - OfflineSearchIndexListener - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-offlinesearchindexlistener-offlinesearchindexlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- OfflineSearchIndexListener.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/OfflineSearchIndexListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">OfflineSearchIndexListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">OfflineSearchIndexListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onStartedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onStartedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-offlinesearchindexoperation">OfflineSearchIndexOperation</a></span></span>

    ), </span>
2.  <span id="sdk-for-flutter-navigate-param-onProgressLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onProgressLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">int</span></span>

    ), </span>
3.  <span id="sdk-for-flutter-navigate-param-onCompleteLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onCompleteLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-offlinesearchindexerror">OfflineSearchIndexError</a>?</span></span>

    )</span>

)

</div>

<div class="section desc markdown">

Abstract class to get updates about progress of creating persistent map index.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
factory OfflineSearchIndexListener(
  void Function(OfflineSearchIndexOperation) onStartedLambda,
  void Function(int) onProgressLambda,
  void Function(OfflineSearchIndexError?) onCompleteLambda,

) => OfflineSearchIndexListener$Lambdas(
  onStartedLambda,
  onProgressLambda,
  onCompleteLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
