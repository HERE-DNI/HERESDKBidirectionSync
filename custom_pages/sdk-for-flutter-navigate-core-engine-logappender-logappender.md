---
title: "LogAppender constructor - LogAppender - core.engine library - Dart API"
slug: "sdk-for-flutter-navigate-core-engine-logappender-logappender"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/LogAppender-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">LogAppender</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">LogAppender</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-logLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">logLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-loglevel">LogLevel</a></span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">String</span></span>

    )</span>

)

</div>

<div class="section desc markdown">

An interface to implement a listener to receive log messages.

</div>

## Implementation

``` dart
factory LogAppender(
  void Function(LogLevel, String) logLambda,

) => LogAppender$Lambdas(
  logLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

